import requests
import json
import pandas as pd
import numpy as np
#Yahoo finance provide free,open API
address="https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"
# period1=0 & period2=1549258857 (second)
response= requests.get(address,headers={'User-agent':''})
data=json.loads(response.text) #json.loads() can convert json string to python dictionary
#print(data)
df= pd.DataFrame(data["chart"]["result"][0]["indicators"]["quote"][0],index=pd.to_datetime(np.array(data["chart"]["result"][0]["timestamp"])*10**9)) #convert second to nanosecond
print(df.head(20))