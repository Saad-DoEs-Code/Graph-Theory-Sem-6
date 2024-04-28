import requests

proxies={
    "http":"https://proxylist.geonode.com/api/proxy-list?protocols=http&speed=fast&google=false&limit=500&page=1&sort_by=lastChecked&sort_type=desc"
}

requests = requests.get("https://www.dawn.com/", proxies=proxies)

print(requests.json())