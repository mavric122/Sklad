import requests

search = 'oppo%20a96'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.3.838 Yowser/2.5 Safari/537.36"
}
params = {
    # "sort": "popular",
    "search": search
}

r = requests.get('https://www.wildberries.ru/catalog/0/search.aspx',
                 headers=headers, params=params)
r.encoding = 'utf-8'

print(r.status_code)
# print(r.content)
print(r.headers)
print(r.text)
