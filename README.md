### 🍿🍿🍿 Popcorn Show CLI 🍿🍿🍿

CLI com o objetivo de obter informações sobre filmes/séries e pessoas envoldidas na produção via terminal.
Apresentando as informações mais relevantes diretamente no seu terminal.

- nome
- ==link para streming==
- datas
- elenco/produção
- trailer
- notas do IMDB
- resumo da obra

possibilidade de navegar entre pessoas e obras

## Instalação

```` bash
pip install popcornshow
````
## Prints

**Busca** 
![](docs/assets/cli_search.png)

**Filmes**
![](docs/assets/show_movie.png)  

**Séries**
![](docs/assets/show_serie.png)  

**Pessoa**
![](docs/assets/person.png)

## Comandos para usar

* `popcornshow [nome do filme ou serie]` - Busca por uma lista que corresponde a texto enviada.
* `popcornshow --year -y [2000]` - Busca por uma midia com esse ano de lançamento.
* `popcornshow --type -t [m] [s]` - Busca por apenas o tipo escolhido. Filme ou Série.
* `popcornshow  -l --luck` - Retorna/escolhe a primeira opção retornada pela busca.
* `popcornshow -h` - Mostra a tela de Ajuda padrão.

* em cada tela, pode haver uma opção de escolha para detalhes

![](docs/assets/help.png)

## Sobre

Aplicação feita 100% em python

Informações obtidas do site [RealGood](https://reelgood.com/)
### Desenvolvido por [Icaro Nunes](https://www.github.com/icaronunes)  

<img src=docs/assets/android.png width=120px />Há uma versão mais completa para Android: [play.google.com/popcornshow](https://play.google.com/store/apps/details?id=br.com.icaro.filme) ![alt text](docs/assets/popcorn.png)
