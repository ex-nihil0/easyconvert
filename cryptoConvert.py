#v.1.2

import requests
import time

def price(symbol, comparison_symbols=['USD'], exchange=''): # ex: price('coin', ['BTC','USD']) returns {u'USD': VALUE, u'BTC': VALUE}
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'.format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data

def chop(IN = None): # subfunction for parse(): gets the position of the first letter and the semicolon splitter
    letterPos = 0
    semiPos = 0
    for e in IN:
        if e not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            letterPos += 1
        else:
            break
    for e in IN:
        if e not in [':']:
            semiPos += 1
        else:
            break
    return letterPos, semiPos

def parse(): # parses user input into standarized format/ex. '4eth:btc' to ['4', 'eth', 'btc']
    val = uInput
    markers = chop(val)
    multiplier = val[:markers[0]]
    if multiplier == '':
        multiplier = '1'
    coin = val[markers[0]:markers[1]]
    coin = coin.upper()
    baseCoin = val[markers[1]+1:]
    baseCoin = baseCoin.upper()
    pInput = [multiplier, coin, baseCoin]
    return pInput

def toUSD(prices = None): # converts prices to USD value
    if 'USD' in prices:
        res = prices['USD']
    elif 'BTC' in prices: # convert BTC price to USD
        BTCprice = prices['BTC']
        BTCUSD = price('BTC',['USD'])
        res = int(BTCprice * BTCUSD['USD'])
        res = round(res,2)
    else:
        res = 'There are no BTC or USD prices for this coin.'
    return res # USD price

# start coinConvert (need to package as a function)

print('\ncalling API...', end='') # check for API success
while True:
    try:
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=0')
        r = r.json()
        r2 = requests.get('https://api.coinmarketcap.com/v1/global/')
        r2 = r2.json()
        break
    except:
        print('Error: exceeded API call limit')
        print('Please wait...')
        sec = 120
        while sec > 0:
            print('{} seconds left...'.format(sec))
            sec -= 1
            time.sleep(1)
        print('retrying API call...')
        continue
time.sleep(.5) # flair
print('success!')
time.sleep(.25) # flair

firstTime = True # check whether user would like to convert (or convert again) / contextual print statments / enable quit
while True: 
    if firstTime == True:
        pass
    else:
        while True:
            response = input("\nConvert again? Y/N ")
            response = response.lower()
            if response not in ["y","n"]:
                print("Please just enter Y/N. I'm not that sophisticated!")
                continue
            elif response != 'y':
                print("See ya!")
                quit()
            elif response == 'thanks' or response == 'ty':
                print('No problem. See ya!')
                quit()
            else:
                break
    firstTime = False 

    uInput = input('\nPlease input your conversion: ') # miniparse
    uInput = uInput.replace(' to ',':')
    uInput = uInput.replace(' ','')

    pInput = parse() # pInput <- [multiplier,coin,baseCoin]
    multi = pInput[0]
    coin = pInput[1]
    baseCoin = pInput[2]

    coinPrice = price(coin, ['BTC', 'USD']) # coinPrice <- {u'USD': VALUE, u'BTC': VALUE}
    coinPrice_USD = toUSD(prices = coinPrice) # converts price to USD
    basecoinPrice = price(baseCoin, ['BTC', 'USD'])
    baseCoinPrice_USD = toUSD(prices = basecoinPrice)

    try: # check for input error
        USDprice = round((coinPrice_USD * float(multi)),2) #  USD price * multi 
        conversion = (coinPrice_USD * float(multi)/baseCoinPrice_USD)
    except TypeError:
        print ("Hmm...I can't understand that. Did you format your input correctly?")
        continue

    conversion = round(conversion,8)
    totalCap = r2['total_market_cap_usd']

    cap = [item['market_cap_usd'] for item in r if item['symbol'] == coin]
    cap = float(cap[0])
    coinCap = cap # coinCap <- coin marketcap in USD
    
    cap = [item['market_cap_usd'] for item in r if item['symbol'] == baseCoin]
    cap = float(cap[0])
    baseCoinCap = cap # baseCoinCap <- baseCoin marketcap in USD
    print('\n{} {} = {} {} ({} USD)'.format(multi,coin,conversion,baseCoin,USDprice)) # print result line 1

# sift through logic and print applicable 'marketcap' string (result line 2)
    mcCompare_pct = int(round((coinCap/baseCoinCap)*100))
    mcTotalCompare_pct = int(round((coinCap/totalCap)*100))
    if coinCap<baseCoinCap:
        if mcCompare_pct >= 1:
            if mcTotalCompare_pct >= 1:
                print("{}'s marketcap is ~{}% of {}'s marketcap (~{}% of the total marketcap)"
                .format(coin,mcCompare_pct,baseCoin,mcTotalCompare_pct))
            else:
                print("{}'s marketcap is ~{}% of {}'s marketcap (less than 1% of the total marketcap)"
                .format(coin,mcCompare_pct,baseCoin))
        else:
            if mcTotalCompare_pct >= 1:
                print("{}'s marketcap is less than 1% of {}'s marketcap (~{}% of the total marketcap)"
                .format(coin,baseCoin,mcTotalCompare_pct))
            else:
                print("{}'s marketcap is less than 1% of {}'s marketcap (less than 1% of the total marketcap)"
                .format(coin,baseCoin))
    else:
        if mcTotalCompare_pct >= 1:
            print("{}'s marketcap is ~{}% of the total marketcap.".format(coin,mcTotalCompare_pct))
        else:
            print("{}'s marketcap is less than 1% of the total marketcap.".format(coin))

# get fantasyPrice and print result line 3
    ratio = baseCoinCap/coinCap 
    fantasyCap = coinCap * ratio 
    circulatingSupply = [item['total_supply'] for item in r if item['symbol'] == coin]
    circulatingSupply = float(circulatingSupply[0])
    fantasyPrice = fantasyCap/circulatingSupply
    fantasyPrice = round(fantasyPrice,2)
    print("If {}'s marketcap was equal to {}'s, the price of {} would be ${}".format(coin,baseCoin,coin,fantasyPrice))