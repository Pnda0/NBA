🏀 Análises de Estatísticas da NBA com Python e nba_api

Este repositório contém scripts em Python para buscar, analisar e visualizar estatísticas de jogadores e times da NBA usando a biblioteca `nba_api`. 
O objetivo é demonstrar como extrair dados valiosos da NBA e realizar análises comuns no universo do basquete, tudo em português.

🎯 Motivação

Este projeto faz parte do meu portfólio de Análise de Dados/BI e foi criado com os seguintes objetivos:

* Praticar a coleta de dados via API (`nba_api`).
* Aprimorar a manipulação de dados com a biblioteca Pandas.
* Desenvolver visualizações de dados informativas com Matplotlib e Seaborn.
* Compartilhar um recurso prático para outros entusiastas de basquete e análise de dados.

✨ Funcionalidades

Os seguintes scripts estão disponíveis para realizar diversas análises de dados da NBA:

* `getPlayerInfo.py`: Busca informações biográficas e de carreira de um jogador específico.
* `getPlayerCareerStats.py`: Coleta estatísticas por temporada de um jogador (temporada regular e playoffs).
* `getPlayerShotChart.py`: Gera o mapa de arremessos de um jogador para uma determinada temporada.
* `getTeamDetails.py`: Obtém detalhes gerais sobre uma equipe da NBA.
* `getTeamRosterSeason.py`: Lista o elenco e a comissão técnica de um time em uma temporada específica.
* `getLeagueStandings.py`: Apresenta a classificação da NBA por conferência.
* `getLeagueLeaders.py`: Mostra os líderes de estatísticas em diversas categorias (pontos, rebotes, assistências, etc.).

📊 Glossário de Estatísticas da NBA

| Abreviação | Significado                                           |
| :--------- | :---------------------------------------------------- |
| **GP** | Games Played (Jogos Disputados)                       |
| **GS** | Games Started (Jogos como Titular)                    |
| **MIN** | Minutes Played (Minutos Jogados)                      |
| **FGM** | Field Goals Made (Cestas de Campo Convertidas)        |
| **FGA** | Field Goals Attempted (Cestas de Campo Tentadas)      |
| **FG_PCT** | Field Goal Percentage (Percentual de Cestas de Campo) |
| **FG3M** | 3-Point Field Goals Made (Cestas de 3 Pontos Convertidas) |
| **FG3A** | 3-Point Field Goals Attempted (Cestas de 3 Pontos Tentadas) |
| **FG3_PCT**| 3-Point Field Goal Percentage (Percentual de Cestas de 3 Pontos) |
| **FTM** | Free Throws Made (Lances Livres Convertidos)          |
| **FTA** | Free Throws Attempted (Lances Livres Tentados)        |
| **FT_PCT** | Free Throw Percentage (Percentual de Lances Livres)   |
| **OREB** | Offensive Rebounds (Rebotes Ofensivos)                |
| **DREB** | Defensive Rebounds (Rebotes Defensivos)               |
| **REB** | Total Rebounds (Total de Rebotes)                     |
| **AST** | Assists (Assistências)                                |
| **STL** | Steals (Roubos de Bola)                               |
| **BLK** | Blocks (Tocos)                                        |
| **TOV** | Turnovers (Perdas de Bola)                            |
| **PF** | Personal Fouls (Faltas Pessoais)                      |
| **PTS** | Points (Pontos)                                       |



📂 Estrutura do Projeto

├── scripts/
│ └── src/ # Contém todos os scripts Python executáveis
├── requirements.txt # Lista de dependências do projeto
└── README.md # Este arquivo


🛠️ Tecnologias Utilizadas

* Python 3.x
* `nba_api`
* `pandas`
* `matplotlib`
* `seaborn`

⚙️ Instalação

Siga os passos abaixo para configurar o ambiente e executar os scripts.

**1. Pré-requisitos**

    * Python 3.8 ou superior instalado.
    * Git instalado.
    * Recomendado: Familiaridade com ambientes virtuais Python (`venv` ou `conda`).

**2. Clone o Repositório**

    ```bash
    git clone [https://github.com/Pnda0/NBA.git](https://github.com/Pnda0/NBA.git)

    cd NBA
    ```

Instale as Dependencias

Instale todas as bibliotecas necessárias listadas no arquivo requirements.txt:

pip ```install -r requirements.txt```


🚀 Como Usar

Recomendo um ambiente virtual com o *venv*
Todos os scripts estão na pasta scripts/src/. Navegue até a raiz do projeto e execute:

📌 Exemplos:
1. Informações do Jogador

    jogador = "Nikola Jokic"

    ```python scripts/src/getPlayerInfo.py```

2. Estatísticas da Carreira

    jogador = "Luka Doncic"
    per_mode = "PerGame"

    ```python scripts/src/getPlayerCareerStats.py```

3. Mapa de Arremessos

    jogador = "Jayson Tatum"
    temporada = "2024-25"

    ```python scripts/src/getPlayerShotChart.py```

4. Detalhes do Time

    time = "Milwaukee Bucks"

    ```python scripts/src/getTeamDetails.py```

5. Elenco do Time por Temporada

    time = "Golden State Warriors"
    temporada = "2024-25"

    ```python scripts/src/getTeamRosterSeason.py```

6. Classificação da Liga

    temporada = 2024  # ou None para a atual

    ```python scripts/src/getLeagueStandings.py```

7. Líderes de Estatísticas

    categoriaEstatistica = 'AST'
    temporada = "2024-25"
    tipoTemporada = "Regular Season"
    modoEstatistica = "PerGame"
    numLideres = 5

    ```python scripts/src/getLeagueLeaders.py```

📊 Exemplo de Saída

--- Top 3 Líderes em PTS (2023-24, Regular Season, PerGame) ---
   RANK            PLAYER TEAM_ABBREVIATION   PTS  GP   MIN
0     1     Luka Doncic               DAL  33.9  70  37.5
1     2  Shai Gilgeous-Alexander      OKC  30.1  75  34.0
2     3   Giannis Antetokounmpo       MIL  30.4  73  35.2

📄 Licença

MIT License

Copyright (c) 2025 Alan Ribeiro de Carvalho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

