import requests


url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3sq6ckkmf&latitude=31.235742&limit=24&longitude=121.479797&offset=48&terminal=web'
cookie = {
    'SID': 'q2QQidueQFMrElACFG5pLcr0pjw0HdwgkWng',
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.98 Safari/537.36',
    'Referer': 'https://www.ele.me/place/wtw3sq6ckkmf?latitude=31.235742&longitude=121.479797',
}
response = requests.get(url, headers=header, cookies=cookie)
print(response.json())
