🏀 Análises de Estatísticas da NBA com Python e nba_api

Este repositório contém scripts em Python para buscar, analisar e visualizar estatísticas de jogadores e times da NBA usando a biblioteca nba_api. O objetivo é demonstrar como extrair dados ricos da NBA e realizar análises comuns no basquete, tudo em português.
🎯 Motivação

Este projeto faz parte do meu portfólio de Análise de Dados/BI. Ele foi criado para praticar:

    Coleta de dados via API

    Manipulação com Pandas

    Visualização com Matplotlib/Seaborn

✨ Funcionalidades

Scripts disponíveis para análise de dados da NBA:

- getPlayerInfo.py	Informações biográficas e de carreira de um jogador
- getPlayerCareerStats.py	Estatísticas por temporada (temporada regular e playoffs)
- getPlayerShotChart.py	Mapa de arremessos de um jogador
- getTeamDetails.py	Detalhes gerais de uma equipe da NBA
- getTeamRosterSeason.py	Elenco e comissão técnica de um time por temporada
- getLeagueStandings.py	Classificação da NBA por conferência
- getLeagueLeaders.py	Líderes de estatísticas por categoria (pontos, rebotes, etc.)

🛠️ Tecnologias Utilizadas

    Python 3.x

    nba_api

    pandas

    matplotlib, seaborn

⚙️ Instalação
1. Pré-requisitos

    Python 3.8+

    Git instalado

2. Clone o repositório

git clone https://github.com/Pnda0/NBA.git
cd NBA

3. Instale as dependências

pip install -r requirements.txt

🚀 Como Usar

Todos os scripts estão na pasta scripts/src/. Navegue até a raiz do projeto e execute:
📌 Exemplos:
1. Informações do Jogador

# No topo de getPlayerInfo.py
jogador = "Nikola Jokic"

python scripts/src/getPlayerInfo.py

2. Estatísticas da Carreira

jogador = "Luka Doncic"
per_mode = "PerGame"

python scripts/src/getPlayerCareerStats.py

3. Mapa de Arremessos

jogador = "Jayson Tatum"
temporada = "2024-25"

python scripts/src/getPlayerShotChart.py

4. Detalhes do Time

time = "Milwaukee Bucks"

python scripts/src/getTeamDetails.py

5. Elenco do Time por Temporada

time = "Golden State Warriors"
temporada = "2024-25"

python scripts/src/getTeamRosterSeason.py

6. Classificação da Liga

temporada = 2024  # ou None para a atual

python scripts/src/getLeagueStandings.py

7. Líderes de Estatísticas

categoriaEstatistica = 'AST'
temporada = "2024-25"
tipoTemporada = "Regular Season"
modoEstatistica = "PerGame"
numLideres = 5

python scripts/src/getLeagueLeaders.py

📊 Exemplo de Saída

--- Top 3 Líderes em PTS (2023-24, Regular Season, PerGame) ---
   RANK            PLAYER TEAM_ABBREVIATION   PTS  GP   MIN
0     1     Luka Doncic               DAL  33.9  70  37.5
1     2  Shai Gilgeous-Alexander      OKC  30.1  75  34.0
2     3   Giannis Antetokounmpo       MIL  30.4  73  35.2

📄 Licença

```MIT License

Copyright (c) 2025 Alan Ribeiro/ 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. ```

