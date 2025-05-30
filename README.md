# Análises de Estatísticas da NBA com Python e nba_api

Este repositório contém scripts Python para buscar, analisar e visualizar estatísticas de jogadores e times da NBA, utilizando a biblioteca `nba_api`. O objetivo é demonstrar como extrair dados ricos da NBA e realizar análises comuns no basquete em PT-BR.

## 🎯 Motivação 

Este projeto foi desenvolvido como parte do meu portfólio de Análise de Dados/BI, com o intuito de praticar a coleta de dados via API, manipulação de dados com Pandas e criação de visualizações.

## ✨ Funcionalidades / Análises Implementadas

Este repositório oferece os seguintes scripts para análise de dados da NBA:

* **Informações de Jogadores (`getPlayerInfo.py`):** Busca e exibe detalhes biográficos e de carreira de um jogador específico.
* **Estatísticas da Carreira de Jogadores (`getPlayerCareerStats.py`):** Mostra as estatísticas de um jogador temporada por temporada (regular e playoffs).
* **Mapa de Arremessos de Jogadores (`getPlayerShotChart.py`):** Coleta dados de arremessos de um jogador para uma temporada e permite a visualização básica de suas posições de arremesso.
* **Detalhes de Times (`getTeamDetails.py`):** Apresenta informações gerais sobre uma equipe da NBA, como conferência, divisão e ano de fundação.
* **Elenco de Times por Temporada (`getTeamRosterSeason.py`):** Lista os jogadores e a comissão técnica de um time para uma temporada específica.
* **Classificação da Liga (`getLeagueStandings.py`):** Exibe a classificação da NBA (Leste e Oeste) para uma determinada temporada.
* **Líderes de Estatísticas da Liga (`getLeagueLeaders.py`):** Mostra os jogadores líderes em diversas categorias estatísticas (pontos, rebotes, assistências, etc.).

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* nba_api (para acesso aos dados da NBA)
* Pandas (para manipulação de dados)
* Matplotlib / Seaborn (para visualização de dados)

## ⚙️ Configuração e Instalação

Instruções claras para que outra pessoa possa rodar seu projeto.

1.  **Pré-requisitos:**
    * Python 3.8 ou superior instalado.
    * Git instalado (para clonar o repositório).

2.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Pnda0/NBA.git
    cd NBA
    ```

3.  **Instale as dependências:**
    Crie um arquivo `requirements.txt` no seu projeto. Você pode gerar ele no seu ambiente com:
    ```bash
    pip freeze > requirements.txt
    ```
    Depois, no README, instrua para instalar com:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Como Usar / Exemplos de Requisições

Esta é a parte crucial para "ensinar a fazer as requisições".

Explique a estrutura das pastas (se houver) e como executar os scripts. Para cada tipo de análise/script principal, forneça:

* **Nome do Script:** Ex: `analise_desempenho_jogador.py`
* **O que ele faz:** Ex: "Este script busca as estatísticas de carreira de um jogador e plota seu desempenho em pontos, rebotes e assistências ao longo das temporadas."
* **Como configurar (se necessário):** Ex: "Abra o script e altere a variável `jogador` para o jogador que deseja analisar."
* **Como executar:** Ex: `python analise_desempenho_jogador.py`
* **Exemplo de Código da Requisição (direto no README ou bem comentado no script):**

    **Exemplo para Desempenho do Jogador:**
    ```python
    # Dentro de analise_desempenho_jogador.py (ou um trecho no README)

    from nba_api.stats.static import players
    from nba_api.stats.endpoints import PlayerCareerStats
    import pandas as pd

    # 1. Encontrar o ID do jogador
    player_name_alvo = "LeBron James" # Fácil de alterar!
    player_info = players.find_players_by_full_name(player_name_alvo)
    if not player_info:
        print(f"Jogador '{player_name_alvo}' não encontrado.")
        exit()
    player_id = player_info[0]['id']

    # 2. Fazer a requisição das estatísticas da carreira
    career = PlayerCareerStats(player_id=player_id)
    career_df = career.get_data_frames()[0]

    print(f"Estatísticas de {player_name_alvo} por temporada:")
    print(career_df[['SEASON_ID', 'TEAM_ABBREVIATION', 'PTS', 'REB', 'AST']].head())

    # (Restante do código para plotar, etc.)
    ```
    **Dica:** Explique parâmetros chave como `player_id`, `team_id`, `season` e como o usuário pode obter esses IDs (ex: usando `players.find_players_by_full_name()` ou `teams.find_teams_by_full_name()`).

##📊 Exemplos de Saída / Visualizações (Opcional, mas muito bom!)

Se seus scripts geram gráficos ou tabelas interessantes, inclua imagens deles no README (você pode colocar as imagens numa pasta `img/` ou `assets/` e linkar no Markdown). Se for texto, pode colar um trecho da saída.

Ex:
*Figura 1: Gráfico de Pontos por Temporada de LeBron James.*
`![Descrição da Imagem](img/lebron_pts_temporada.png)`

## 📜 Licença


