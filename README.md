
## easyconvert - Crypto conversions on the fly!

#### About
Easyconvert is tool to simplify cryptocurrency conversions. 

If you'd like to report a bug, suggest something you'd like to see, or just say hello, please email me. Thanks!

#### Using easyconvert
Using easyconvert is, well, easy! When asked for input, just type your request in plain english. Don't worry about capitalization or spaces. Easyconvert will return the conversion rate in the specified currency and USD and some marketcap comparison data. Easyconvert can also return some other useful figures, so check out the additional features!   
**Easyconvert calls several APIs, so avoid restarting the program more than 5 times in a minute.**  

### - Formatting and i/o examples
Here are some common examples of accepted inputs:

Input: `eth to btc`  OR  `eth:btc`

Output:

```
1 ETH = 0.09869766 BTC (616.89 USD)
ETH's marketcap is $60,753,266,111: 
   ~57% of BTC's marketcap 
   ~21% of the total marketcap
If ETH's marketcap was equal to BTC's, the price of ETH would be $1089.87
```

Input: `2 btc to eth`  OR  `2btc:eth`

Output:

```
2 BTC = 20.2805621 ETH (12483.7 USD)
BTC's marketcap is $106,195,019,112: 
   ~36% of the total marketcap
If BTC's marketcap was equal to ETH's, the price of BTC would be $3605.82
```

Input: `20 omg to eth`  OR  `20omg:eth`

Output:

```
20 OMG = 0.25893336 ETH (159.2 USD)
OMG's marketcap is $830,491,675: 
   ~1% of ETH's marketcap 
   less than 1% of the total marketcap
If OMG's marketcap was equal to ETH's, the price of OMG would be $433.19
```

Input: `3000 xrp to req`  OR  `3000xrp:req`

Output:

```
3000 XRP = 10522.97220647 REQ (1855.2 USD)
XRP's marketcap is $24,509,958,422: 
   ~8% of the total marketcap.
If XRP's marketcap was equal to REQ's, the price of XRP would be $0.0
```

### - Additional features 
Use easyconvert to see a coin's price **given a hypothetical marketcap**. 
Just add a question mark to the end of the string, followed by a number (the hypothetical marketcap). 

Examples:

Input: `eth to btc ? 150 000 000 000`  OR  `eth:btc?150000000000`

Output:

```
1 ETH = 0.09794369 BTC (610.96 USD)
ETH's marketcap is $60,753,266,111: 
   ~57% of BTC's marketcap 
   ~21% of the total marketcap
If ETH's marketcap was equal to BTC's, the price of ETH would be $1089.87
If ETH's marketcap was $150,000,000,000, the price of ETH would be $1539.44
```

Input : `2 btc to eth ? 50 000 000 000`  OR  `2btc:eth?50000000000`


Output 2:

```
2 BTC = 20.40648012 ETH (12470.4 USD)
BTC's marketcap is $106,195,019,112: 
   ~36% of the total marketcap.
If BTC's marketcap was equal to ETH's, the price of BTC would be $3605.82
If BTC's marketcap was $50,000,000,000, the price of BTC would be $2967.6
```

Try it out!

