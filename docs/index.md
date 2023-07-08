# Bem-Vindo ao PopCorn Show Cli
:corn: :corn: :corn: :corn: :corn: :corn: :corn: :corn: :corn: :corn:
## A versão Android visite: [play.google.com/popcornshow](https://play.google.com/store/apps/details?id=br.com.icaro.filme) ![alt text](assets/popcorn.png)



## Instalação
``` bash
 git clone https://github.com/icaronunes/popcornshow-cli
 cd popcornshow-cli
 pip install -r requirements.txt
 python cli.py ['comando']
```

## Comandos

* `cli [nome do filme ou serie]` - Busca por uma lista que corresponde a texto enviada.
* `cli --year -y [2000]` - Busca por uma midia com esse ano de lançamento.
* `cli --type -t [m] [s]` - Busca por apenas o tipo escolhido. Filme ou Série.
* `cli  -l --luck` - Retorna/escolhe a primeira opção retornada pela busca.
* `cli -h` - Mostra a tela de Ajuda padrão.
* em cada tela, pode haver uma opção de escolha para detalhes

## Exemplos

```bash 
python cli.py 'lost'
python cli.py 'lost' --year 2004
python cli.py 'lost' -type s    
python cli.py 'lost' --luck
```

# Informações retornadas
- Titulo
- Nota IMDB
- Pessoas do Filme/Série
- Detalhes sobre atores
- Descrição
- Lançamento
- Classificação
- Trailers
- Onde assistir

# Telas
### Busca 
![](assets/cli_search.png)

### Filmes
![](assets/show_movie.png)  
  
### Séries
![](assets/show_serie.png)  

### Pessoa
![](assets/person.png)