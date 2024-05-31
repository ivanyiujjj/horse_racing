# scrapper.py
import requests
import pandas as pd

print("HKJC Horse Scraping Sample Program")


# 設立Table將API得到的數據轉換
df = pd.DataFrame(columns=['Key', 'Value'])

# 設置API接口的URL和相關參數
# 發送GET請求獲取賽馬資訊
odds = requests.get('https://bet.hkjc.com/racing/getJSON.aspx?type=winplaodds&date=2024-06-01&venue=S2&start=1&end=1')

# 解析JSON格式的資料
data = odds.json()


table = []
# 獲取相關的賽馬資訊
print(data)

print("賠率表格-快速換算")
for i in data['OUT'].split('#'):
    for o in i.split(';'):
        if '=' in o:
            data = o.split('=')
            print(f'{data[0]} --> {data[1]}')
            key = data[0]
            value = data[1]
            df = df.append({'Key': key, 'Value': value}, ignore_index=True)
        else:
            if o == 'PLA': 
                print('位置賠率')
                df = df.append({'Key': '位置賠率', 'Value': ''}, ignore_index=True)
            else:
                print(o)
                df = df.append({'Key': o, 'Value': ''}, ignore_index=True)


print(df)

df.to_excel('output.xlsx', index=False)
