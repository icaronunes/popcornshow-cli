:corn: :corn: :corn: :corn: :corn: :corn: :corn: :corn: :corn: :corn:
## <img src=./../assets/android.svg width=40px /> Versão Android visite: [play.google.com/popcornshow](https://play.google.com/store/apps/details?id=br.com.icaro.filme) ![alt text](assets/popcorn.png)


````bash
git clone https://github.com/icaronunes/popcornshow-cli.git
cd 'popcornshow cli'

poetry install
````

## Comandos para usar

* `popcornshow [nome do filme ou serie]` - Busca por uma lista que corresponde a texto enviada.
* `popcornshow --year -y [2000]` - Busca por uma midia com esse ano de lançamento.
* `popcornshow --type -t [m] [s]` - Busca por apenas o tipo escolhido. Filme ou Série.
* `popcornshow  -l --luck` - Retorna/escolhe a primeira opção retornada pela busca.
* `popcornshow -h` - Mostra a tela de Ajuda padrão.

* em cada tela, pode haver uma opção de escolha para detalhes

## Tasks do poetry

### Lint
``` bash
poetry run task lint
```

#### Teste
```bash
poetry run task test
```

#### Docs - readthedocs.io
``` bash
poetry run task 
```

#### CI - GitHub Action
[CI](https://github.com/icaronunes/popcornshow-cli/actions) rodando nas seguintes ordem:

* checagem com python black usando length de 88
* isort
* testes com pytest na pasta ./popcorn e ./tests
* caso passe todas a etapa anteriores e enviado um relatorio para [codecov](https://app.codecov.io/gh/icaronunes/popcornshow-cli)
    
Qualquer erro para a pipeline


#### Estrutura padrão das pastas

```bash
├───popcorn
├───api
│   ├───models
│   │   
│    PersonApi.py
│   │Result.py
│   │SearchApi.py
│   ├───models
│          ├───tables
│          .....>>>>
│    cli.py
│    config.py
│    controller.py
│    dto.py
│    utils.py
│    __init__.py
├───tests
│   test_cli.py
│   test_controller.py
│   test_utils.py
│   __init__.py
├───docs
│   │   develops.md
│   │   index.md
│   │
│   └───assets
│           android.svg
│           cli_search.png
│           favico.ico
│           help.png
│           person.png
│           popcorn.png
│           show_movie.png
│           show_serie.png
│
 .coverage
 .gitignore
 coverage.xml
 LICENSE
 mkdocs.yml
 poetry.lock
 pyproject.toml
 pyvenv.cfg
 README.md

END
```  
