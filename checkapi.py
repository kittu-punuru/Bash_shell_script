#!/usr/bin/env python
import requests

try:
    r = requests.head("https://dev.chaikinanalytics.com/CPTRestSecure/app/pgr/getPGRValues?uid=9580&tickers=AAPL,GOOG,BCA&token=4XC534118T00FR73S127L77QWU65GA1H")
    
    print(r.status_code)
   
except requests.ConnectionError:
    print("failed to connect")
