import requests
from api.models.Result import Result

paramsDefault = {'page': '1', 'pageSize': '10',
                 'region': 'us', 'take': '10', 'terms': ''}


def search(query: str) -> Result:
    """
    Busca por mídias com valores igual a 'query', retornando um json 
    Parameters:
        query: texto nome do filme ou serie        
    Returns:
        Retorna um object Result onde se tem objetos internos, como value contento o json do resultado
    Exemplos:
        >>> search('the matrix') -> Result

            "items": [{
                    "id": "2c947f66-ba1e-4747-91a3-ab1432f6bb96",
                    "slug": "the-lord-of-the-rings-the-return-of-the-king-2003",
                    "content_type": "m",
                    "title": "The Lord of the Rings: The Return of the King",
                    "overview": null,
                    "availability_pros": null,
                    "imdb_rating": 9,
                    "rt_critics_rating": null,
                    "rg_content_score": null,
                    "has_poster": true,
                    "poster_blur": null,
                    "has_backdrop": true,
                    "backdrop_blur": null,
                    "released_on": "2003-12-17T00:00:00Z",
                    "classification": "13+",
                    "sources": [
                        "hbo_max"
                    ],
                    "genres": [],
                    "on_services": false,
                    "on_free": false,
                    "on_rent_purchase": true,
                    "user_rating": null,
                    "tracking": false,
                    "watchlisted": false,
                    "seen": false,
                    "season_count": 0,
                    "featured_services": [],
                    "episode_source_count": 0
                    },
                    ...
                ]

        >>> search('um texto sem correspondência') -> Result

            {
               "items": [],
               "page": 1,
               "pages": 0,
               "page_size": 10
            }
    """
    paramsDefault['terms'] = query
    result = requests.get(
        "https://api.reelgood.com/v3.0/content/search/content", params=paramsDefault)
    if result.status_code == requests.codes.ok:
        return Result(value=result.text)
    else:
        return Result(error=Exception(result.content))


def getMovieApi(id: str) -> Result:
    """
    Busca por informações da filme, retornando um json
    Parameters:
        id: texto com ID completo de um filme
    Returns:
        Retorna um object Result onde se tem objetos internos, como value contento o json do resultado
    Exemplos:
        >>> getMovieApi('the matrix') -> Result

            {
                "metadata": {
                    "ad_data": null
                },
                "id": "6eb67f3f-113d-47e6-8776-406dda49f7ca",
                "slug": "the-matrix-1999",
                "title": "The Matrix",
                "overview": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.",
                "tagline": "Welcome to the Real World.",
                "reelgood_synopsis": "The Matrix featuring Keanu Reeves and Laurence Fishburne is streaming on HBO MAX, streaming with subscription on fuboTV, streaming via tv everywhere with Syfy, and 8 others. It's an Action & Adventure and Science Fiction movie with a high IMDb audience rating of 8.7 (1,942,671 votes).",
                "classification": "18+",
                "runtime": 136,
                "released_on": "1999-03-31T00:00:00Z",
                "trailer": {
                    "site": "youtube",
                    "key": "nUEQNVV3Gfs",
                    "url": null
                },
                ...    
            }
        >>> search('um texto sem correspondência')

            {
                "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
                "title": "Not Found",
                "status": 404,
                "traceId": "00-879fe78e889ae66bb06aa8ae86c6ac11-9a132b9f1975f20e-00"
            }
    """
    result = requests.get(
        f"https://api.reelgood.com/v3.0/content/movie/{id}")
    if result.status_code == requests.codes.ok:
        return Result(value=result.text)
    else:
        return Result(error=Exception(result.content))


def getTvShowApi(id: str) -> Result:
    """
    Busca por informações da série, retornando um json
    Parameters:
        id: texto com ID completo de um Série
    Returns:
        Retorna um object Result onde se tem objetos internos, como value contento o json do resultado
    Exemplos:
        >>> getTvShowApi('the matrix') -> Result

            {
                "metadata": {
                    "ad_data": null
                },
                "id": "a9f4f694-09b0-47c0-be5e-6a8b0032a08e",
                "slug": "lost-2004",
                "title": "Lost",
                "overview": "The survivors of a plane crash are forced to work together in order to survive on a seemingly deserted tropical island.",
                "reelgood_synopsis": "Lost featuring Naveen Andrews and Matthew Fox has one or more episodes streaming with subscription on Hulu, free on Freevee (Via Prime Video), available for purchase on Google Play, and 2 others. It's an action & adventure and drama show with 124 episodes over 6 seasons. Lost is no longer running and has no plans to air new episodes or seasons. It has a high IMDb audience rating of 8.3 (563,917 votes) and was well received by critics.",
                "trailer": {
                    "site": "youtube",
                    "key": "KTu8iDynwNc",
                    "url": null
                },
                "trailers": [
                    {
                        "site": "youtube",
                        "key": "KTu8iDynwNc",
                        "url": null
                    }
                ],
                "imdb_rating": 8.3,
                "rt_critics_rating": null,
                "rt_audience_rating": 91,
                "has_poster": true,
                "has_backdrop": true,
                "season_count": 6,
                "classification": "16+",
                "last_modified_at": "2023-03-16T00:00:00",
                ...
            }    
        >>> getTvShowApi('um texto sem correspondência')

            {
                "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
                "title": "Not Found",
                "status": 404,
                "traceId": "00-cfa2d680394c5d6dcba63ceda93993eb-b2dc38cd80923d52-00"
            }
    """
    result = requests.get(
        f"https://api.reelgood.com/v3.0/content/show/{id}")
    if result.status_code == requests.codes.ok:
        return Result(value=result.text)
    else:
        return Result(error=Exception(result.content))
