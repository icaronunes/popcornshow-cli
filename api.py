import requests

paramsDefault = {'page': '1', 'pageSize': '50',
                 'region': 'us', 'take': '50', 'terms': ''}

def search(query: str) -> str:
    paramsDefault['terms'] = query
    result = requests.get(
        "https://api.reelgood.com/v3.0/content/search/content", params=paramsDefault)
    print(result.url)
    print(result.status_code == requests.codes.ok)
    if result.status_code == requests.codes.ok:
        return result.text
    else:
        print("Error")
        return "{'error':'faiou' }"
