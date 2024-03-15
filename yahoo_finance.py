import requests
#Yahoo finance provide free,open API
address="https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"
# period1=0 & period2=1549258857 (second)
response= requests.get(address,headers={'User-agent':''})
print(response.text)