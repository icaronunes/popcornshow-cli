import requests
from api.models.Result import Result

paramsDefault = {'page': '1', 'pageSize': '10',
                 'region': 'us', 'take': '50', 'terms': ''}


def search(query: str) -> Result:
    paramsDefault['terms'] = query
    result = requests.get(
        "https://api.reelgood.com/v3.0/content/search/content", params=paramsDefault)
    if result.status_code == requests.codes.ok:
        return Result(value=result.text)    
    else:        
        return Result(error=Exception(result.content))


def getMovieApi(id: str) -> Result:
    result = requests.get(
        f"https://api.reelgood.com/v3.0/content/movie/{id}")
    if result.status_code == requests.codes.ok:
        return Result(value=result.text)
    else:
        return Result(error=Exception(result.content))
