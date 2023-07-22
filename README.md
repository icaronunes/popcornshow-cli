### 🍿🍿🍿 Popcorn Show CLI 🍿🍿🍿

[![Documentation Status](https://readthedocs.org/projects/popcornshow-cli/badge/?version=latest)](https://popcornshow-cli.readthedocs.io/en/latest/?badge=latest)
[![CI](https://github.com/icaronunes/popcornshow-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/icaronunes/popcornshow-cli/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/icaronunes/popcornshow-cli/branch/master/graph/badge.svg?token=OL7MWQKQKR)](https://codecov.io/gh/icaronunes/popcornshow-cli)

CLI with the objective of obtaining information about movies/series and people involved in production via the terminal.
Presenting the most relevant information directly on your terminal.

- Title
- Streaming link
- Dates
- Cast/Crew
- Trailer
- IMDB ratings
- Summary

Ability to navigate between people and works.

## Installation

```bash
pip install popcornshow
```

**Search** 
![](https://popcornshow-cli.readthedocs.io/en/latest/assets/cli_search.png)

**Movies**
![](https://popcornshow-cli.readthedocs.io/en/latest/assets/show_movie.png)  

**Shows**
![](https://popcornshow-cli.readthedocs.io/en/latest/assets/show_serie.png)  

**Person**
ci![](https://popcornshow-cli.readthedocs.io/en/latest/assets/person.png)

## Commands to use

* popcornshow [movie or series name] - Search for a list that matches the given text.

* popcornshow --year -y [2000] - Search for media released in a specific year.

* popcornshow --type -t [m] [s] - Search for media of a specific type. Movie or Series.

* popcornshow -l --luck - Return/choose the first option returned by the search.

* popcornshow -h - Show the default Help screen.

#### on each screen, there might be a navigation option


## About
Documentation on [ReadTheDocs](https://popcornshow-cli.readthedocs.io/en/latest/?)

Application made 100% in Python

Information obtained from [RealGood](https://reelgood.com/)

<img src=https://popcornshow-cli.readthedocs.io/en/latest/assets/android.svg width=50px />There is a more comprehensive version for Android: [play.google.com/popcornshow](https://play.google.com/store/apps/details?id=br.com.icaro.filme) ![alt text](https://popcornshow-cli.readthedocs.io/en/latest/assets/popcorn.png)