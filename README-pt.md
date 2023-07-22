### 🍿🍿🍿 Popcorn Show CLI 🍿🍿🍿

[![Documentation Status](https://readthedocs.org/projects/popcornshow-cli/badge/?version=latest)](https://popcornshow-cli.readthedocs.io/en/latest/?badge=latest)
[![CI](https://github.com/icaronunes/popcornshow-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/icaronunes/popcornshow-cli/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/icaronunes/popcornshow-cli/branch/master/graph/badge.svg?token=OL7MWQKQKR)](https://codecov.io/gh/icaronunes/popcornshow-cli)

CLI com o objetivo de obter informações sobre filmes/séries e pessoas envolvidas na produção via terminal.
Apresentando as informações mais relevantes diretamente no seu terminal.

- nome
- link para streming
- datas
- elenco/produção
- trailer
- notas do IMDB
- sinopse

possibilidade de navegar entre pessoas e obras

## Instalação

```` bash
pip install popcornshow
````
## Prints

**Busca** 
![](https://popcornshow-cli.readthedocs.io/en/latest/assets/cli_search.png)

**Filmes**
![](https://popcornshow-cli.readthedocs.io/en/latest/assets/show_movie.png)  

**Séries**
![](https://popcornshow-cli.readthedocs.io/en/latest/assets/show_serie.png)  

**Pessoa**
ci![](https://popcornshow-cli.readthedocs.io/en/latest/assets/person.png)

## Comandos para usar

* `popcornshow [nome do filme ou serie]` - Busca por uma lista que corresponde a texto enviada.
* `popcornshow --year -y [2000]` - Busca por uma midia com esse ano de lançamento.
* `popcornshow --type -t [m] [s]` - Busca por apenas o tipo escolhido. Filme ou Série.
* `popcornshow  -l --luck` - Retorna/escolhe a primeira opção retornada pela busca.
* `popcornshow -h` - Mostra a tela de Ajuda padrão.

* em cada tela, pode haver uma opção de navegação

![](docs/assets/help.png)

## Sobre
Documentação do [ReadTheDocs](https://popcornshow-cli.readthedocs.io/en/latest/?)


Aplicação feita 100% em python

Informações obtidas do site [RealGood](https://reelgood.com/)

<img src=https://popcornshow-cli.readthedocs.io/en/latest/assets/android.svg width=50px />Há uma versão mais completa para Android: [play.google.com/popcornshow](https://play.google.com/store/apps/details?id=br.com.icaro.filme) ![alt text](https://popcornshow-cli.readthedocs.io/en/latest/assets/popcorn.png)
