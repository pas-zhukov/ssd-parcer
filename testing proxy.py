import requests


proxxies = {"http": "socks5://localhost:9050", "https": "socks5://localhost:9050"}
html = requests.get('https://icanhazip.com', proxies=proxxies) 
print(html)
    
print("Страница запроса с IP:", html.text.strip())