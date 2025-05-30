# Análises de Estatísticas da NBA com Python e nba_api

Este repositório contém scripts Python para buscar, analisar e visualizar estatísticas de jogadores e times da NBA, utilizando a biblioteca `nba_api`. O objetivo é demonstrar como extrair dados ricos da NBA e realizar análises comuns no basquete em PT-BR.

## 🎯 Motivação 

Este projeto foi desenvolvido como parte do meu portfólio de Análise de Dados/BI, com o intuito de praticar a coleta de dados via API, manipulação de dados com Pandas e criação de visualizações.

## ✨ Funcionalidades / Análises Implementadas

Liste as principais análises que seus scripts realizam. Isso ajuda o usuário a entender rapidamente o que ele pode encontrar aqui.
* Análise de desempenho de jogadores ao longo do tempo.
* Comparação de eficiência de diferentes quintetos (lineups).
* Geração e análise de "shot charts" para visualizar zonas de arremesso.
* Cálculo de correlação entre diferentes estatísticas de time e vitórias.

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

Todos os scripts Python estão localizados na pasta `scripts/src/`. Para executá-los, navegue até a raiz do projeto no seu terminal.

Abaixo, detalhes sobre cada script:

1. Informações do Jogador

    Nome do Script: scripts/src/getPlayerInfo.py
    O que ele faz: Busca e exibe informações detalhadas de um jogador da NBA, como time, posição, altura, peso, data de nascimento, universidade, etc.
    Como configurar: Abra o script e altere a variável NOME_JOGADOR_ALVO no topo do arquivo para o nome do jogador desejado. 

    # Exemplo no topo do getPlayerInfo.py
    jogador = "Nikola Jokic"

    Como executar: 

    ```python scripts/src/getPlayerInfo.py```

2. Estatísticas da Carreira do Jogador

    Nome do Script: scripts/src/getPlayerCareerStats.py
    O que ele faz: Mostra as estatísticas de um jogador temporada por temporada, com opções para ver dados por jogo, totais, por 36 minutos, e para temporada regular ou playoffs.
    Como configurar: Abra o script e altere as variáveis jogador e PER_MODE (ex: "PerGame", "Totals") no topo do arquivo. 

    # Exemplo no topo do getPlayerCareerStats.py
    jogador = "Luka Doncic"
    per_mode = "PerGame"

    Como executar:

    ```python scripts/src/getPlayerCareerStats.py```

3. Mapa de Arremessos do Jogador

    Nome do Script: scripts/src/getPlayerShotChart.py
    O que ele faz: Coleta dados detalhados dos arremessos (localização, acerto/erro) de um jogador para uma temporada específica e gera uma visualização básica desses arremessos.
    Como configurar: Abra o script e altere as variáveis jogador e temporada no topo do arquivo. 

    # Exemplo no topo do getPlayerShotChart.py
    jogador = "Jayson Tatum"
    temporada = "2024-25" # Formato AAAA-AA

    Como executar:

    ```python scripts/src/getPlayerShotChart.py```

E aí, jogador! Que demais que você já organizou os scripts na pasta scripts/src/! Essa estrutura é ótima. Seu README já tem uma base excelente, vamos agora dar um "upgrade" nele para refletir os scripts que você criou e deixar tudo bem claro para quem visitar seu repositório.

Vou focar em como podemos preencher as seções "✨ Funcionalidades / Análises Implementadas" e, principalmente, "🚀 Como Usar / Exemplos de Requisições" com base nos seus scripts.

Assumindo os seguintes nomes para seus arquivos (corrigindo pequenos errinhos de digitação que podem ter ocorrido):

    getLeagueLeaders.py
    getLeagueStandings.py
    getPlayerCareerStats.py
    getPlayerInfo.py
    getPlayerShotChart.py
    getTeamDetails.py
    getTeamRosterSeason.py

Melhorias para o seu README.md

Aqui estão as sugestões para cada seção:
✨ Funcionalidades / Análises Implementadas

Você pode listar de forma mais direta o que cada script principal faz. Substitua o texto genérico por algo assim:
Markdown

## ✨ Funcionalidades / Análises Implementadas

Este repositório oferece os seguintes scripts para análise de dados da NBA:

* **Informações de Jogadores (`getPlayerInfo.py`):** Busca e exibe detalhes biográficos e de carreira de um jogador específico.
* **Estatísticas da Carreira de Jogadores (`getPlayerCareerStats.py`):** Mostra as estatísticas de um jogador temporada por temporada (regular e playoffs).
* **Mapa de Arremessos de Jogadores (`getPlayerShotChart.py`):** Coleta dados de arremessos de um jogador para uma temporada e permite a visualização básica de suas posições de arremesso.
* **Detalhes de Times (`getTeamDetails.py`):** Apresenta informações gerais sobre uma equipe da NBA, como conferência, divisão e ano de fundação.
* **Elenco de Times por Temporada (`getTeamRosterSeason.py`):** Lista os jogadores e a comissão técnica de um time para uma temporada específica.
* **Classificação da Liga (`getLeagueStandings.py`):** Exibe a classificação da NBA (Leste e Oeste) para uma determinada temporada.
* **Líderes de Estatísticas da Liga (`getLeagueLeaders.py`):** Mostra os jogadores líderes em diversas categorias estatísticas (pontos, rebotes, assistências, etc.).

(As descrições das funcionalidades que você tinha antes como "Análise de desempenho...", "Comparação de eficiência...", etc., são ótimas para descrever o tipo de análise que PODE ser feita com os dados extraídos. Você pode mantê-las ou integrá-las aqui, se achar que complementa.)
⚙️ Configuração e Instalação

A sua seção atual está muito boa! Apenas uma pequena sugestão no comando cd:
Markdown

2.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO 
    ```
    (Substitua `SEU_USUARIO/SEU_REPOSITORIO` pelo link real do seu repo. O seu exemplo `Pnda0/NBA` já está correto se for esse mesmo).

O restante desta seção está perfeito.
🚀 Como Usar / Exemplos de Requisições

Esta é a seção mais importante para detalhar. Primeiro, uma nota geral sobre a localização dos scripts:
Markdown

## 🚀 Como Usar / Exemplos de Requisições

Todos os scripts Python estão localizados na pasta `scripts/src/`. Para executá-los, navegue até a raiz do projeto no seu terminal.

Abaixo, detalhes sobre cada script:

Agora, para cada um dos seus scripts:

1. Informações do Jogador

    Nome do Script: scripts/src/getPlayerInfo.py
    O que ele faz: Busca e exibe informações detalhadas de um jogador da NBA, como time, posição, altura, peso, data de nascimento, universidade, etc.
    Como configurar: Abra o script e altere a variável NOME_JOGADOR_ALVO no topo do arquivo para o nome do jogador desejado.
    Python

# Exemplo no topo do getPlayerInfo.py
NOME_JOGADOR_ALVO = "Nikola Jokic"

Como executar:
Bash

    python scripts/src/getPlayerInfo.py

2. Estatísticas da Carreira do Jogador

    Nome do Script: scripts/src/getPlayerCareerStats.py
    O que ele faz: Mostra as estatísticas de um jogador temporada por temporada, com opções para ver dados por jogo, totais, por 36 minutos, e para temporada regular ou playoffs.
    Como configurar: Abra o script e altere as variáveis NOME_JOGADOR_ALVO e PER_MODE (ex: "PerGame", "Totals") no topo do arquivo.
    Python

# Exemplo no topo do getPlayerCareerStats.py
NOME_JOGADOR_ALVO = "Luka Doncic"
PER_MODE = "PerGame" 

Como executar:
Bash

    python scripts/src/getPlayerCareerStats.py

(Seu exemplo de código da requisição para este já está bom no seu README atual, pode mantê-lo ou adaptar!)

3. Mapa de Arremessos do Jogador

    Nome do Script: scripts/src/getPlayerShotChart.py
    O que ele faz: Coleta dados detalhados dos arremessos (localização, acerto/erro) de um jogador para uma temporada específica e gera uma visualização básica desses arremessos.
    Como configurar: Abra o script e altere as variáveis NOME_JOGADOR_ALVO e TEMPORADA_ALVO no topo do arquivo.
    Python

    # Exemplo no topo do getPlayerShotChart.py
    jogador = "Jayson Tatum"
    temporada = "2024-25" # Formato AAAA-AA

    Como executar:

        python scripts/src/getPlayerShotChart.py

4. Detalhes do Time

    Nome do Script: scripts/src/getTeamDetails.py
    O que ele faz: Apresenta informações gerais sobre uma equipe da NBA, como cidade, conferência, divisão, e ano de fundação.
    Como configurar: Abra o script e altere a variável NOME_TIME_ALVO no topo do arquivo. 

E aí, jogador! Que demais que você já organizou os scripts na pasta scripts/src/! Essa estrutura é ótima. Seu README já tem uma base excelente, vamos agora dar um "upgrade" nele para refletir os scripts que você criou e deixar tudo bem claro para quem visitar seu repositório.

Vou focar em como podemos preencher as seções "✨ Funcionalidades / Análises Implementadas" e, principalmente, "🚀 Como Usar / Exemplos de Requisições" com base nos seus scripts.

Assumindo os seguintes nomes para seus arquivos (corrigindo pequenos errinhos de digitação que podem ter ocorrido):

    getLeagueLeaders.py
    getLeagueStandings.py
    getPlayerCareerStats.py
    getPlayerInfo.py
    getPlayerShotChart.py
    getTeamDetails.py
    getTeamRosterSeason.py

Melhorias para o seu README.md

Aqui estão as sugestões para cada seção:
✨ Funcionalidades / Análises Implementadas

Você pode listar de forma mais direta o que cada script principal faz. Substitua o texto genérico por algo assim:
Markdown

## ✨ Funcionalidades / Análises Implementadas

Este repositório oferece os seguintes scripts para análise de dados da NBA:

* **Informações de Jogadores (`getPlayerInfo.py`):** Busca e exibe detalhes biográficos e de carreira de um jogador específico.
* **Estatísticas da Carreira de Jogadores (`getPlayerCareerStats.py`):** Mostra as estatísticas de um jogador temporada por temporada (regular e playoffs).
* **Mapa de Arremessos de Jogadores (`getPlayerShotChart.py`):** Coleta dados de arremessos de um jogador para uma temporada e permite a visualização básica de suas posições de arremesso.
* **Detalhes de Times (`getTeamDetails.py`):** Apresenta informações gerais sobre uma equipe da NBA, como conferência, divisão e ano de fundação.
* **Elenco de Times por Temporada (`getTeamRosterSeason.py`):** Lista os jogadores e a comissão técnica de um time para uma temporada específica.
* **Classificação da Liga (`getLeagueStandings.py`):** Exibe a classificação da NBA (Leste e Oeste) para uma determinada temporada.
* **Líderes de Estatísticas da Liga (`getLeagueLeaders.py`):** Mostra os jogadores líderes em diversas categorias estatísticas (pontos, rebotes, assistências, etc.).

(As descrições das funcionalidades que você tinha antes como "Análise de desempenho...", "Comparação de eficiência...", etc., são ótimas para descrever o tipo de análise que PODE ser feita com os dados extraídos. Você pode mantê-las ou integrá-las aqui, se achar que complementa.)
⚙️ Configuração e Instalação

A sua seção atual está muito boa! Apenas uma pequena sugestão no comando cd:
Markdown

2.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO 
    ```
    (Substitua `SEU_USUARIO/SEU_REPOSITORIO` pelo link real do seu repo. O seu exemplo `Pnda0/NBA` já está correto se for esse mesmo).

O restante desta seção está perfeito.
🚀 Como Usar / Exemplos de Requisições

Esta é a seção mais importante para detalhar. Primeiro, uma nota geral sobre a localização dos scripts:
Markdown

## 🚀 Como Usar / Exemplos de Requisições

Todos os scripts Python estão localizados na pasta `scripts/src/`. Para executá-los, navegue até a raiz do projeto no seu terminal.

Abaixo, detalhes sobre cada script:

Agora, para cada um dos seus scripts:

1. Informações do Jogador

    Nome do Script: scripts/src/getPlayerInfo.py
    O que ele faz: Busca e exibe informações detalhadas de um jogador da NBA, como time, posição, altura, peso, data de nascimento, universidade, etc.
    Como configurar: Abra o script e altere a variável NOME_JOGADOR_ALVO no topo do arquivo para o nome do jogador desejado.
    Python

    # Exemplo no topo do getPlayerInfo.py
    jogador = "Nikola Jokic"

    Como executar:

        python scripts/src/getPlayerInfo.py

2. Estatísticas da Carreira do Jogador

    Nome do Script: scripts/src/getPlayerCareerStats.py
    O que ele faz: Mostra as estatísticas de um jogador temporada por temporada, com opções para ver dados por jogo, totais, por 36 minutos, e para temporada regular ou playoffs.
    Como configurar: Abra o script e altere as variáveis NOME_JOGADOR_ALVO e PER_MODE (ex: "PerGame", "Totals") no topo do arquivo.
    Python

    # Exemplo no topo do getPlayerCareerStats.py
    jogador = "Luka Doncic"
    permode = "PerGame" 

    Como executar:
    
        python scripts/src/getPlayerCareerStats.py

    (Seu exemplo de código da requisição para este já está bom no seu README atual, pode mantê-lo ou adaptar!)

3. Mapa de Arremessos do Jogador

    Nome do Script: scripts/src/getPlayerShotChart.py
    O que ele faz: Coleta dados detalhados dos arremessos (localização, acerto/erro) de um jogador para uma temporada específica e gera uma visualização básica desses arremessos.
    Como configurar: Abra o script e altere as variáveis NOME_JOGADOR_ALVO e TEMPORADA_ALVO no topo do arquivo.
    Python

    # Exemplo no topo do getPlayerShotChart.py
    NOME_JOGADOR_ALVO = "Jayson Tatum"
    TEMPORADA_ALVO = "2024-25" # Formato AAAA-AA

    Como executar:

    python scripts/src/getPlayerShotChart.py

4. Detalhes do Time

    Nome do Script: scripts/src/getTeamDetails.py
    O que ele faz: Apresenta informações gerais sobre uma equipe da NBA, como cidade, conferência, divisão, e ano de fundação.
    Como configurar: Abra o script e altere a variável NOME_TIME_ALVO no topo do arquivo. 
    
    # Exemplo no topo do getTeamDetails.py
    time = "Milwaukee Bucks"

##📊 Exemplos de Saída / Visualizações (Opcional, mas muito bom!)

Se seus scripts geram gráficos ou tabelas interessantes, inclua imagens deles no README (você pode colocar as imagens numa pasta `img/` ou `assets/` e linkar no Markdown). Se for texto, pode colar um trecho da saída.

Ex:
*Figura 1: Gráfico de Pontos por Temporada de LeBron James.*
`![Descrição da Imagem](img/lebron_pts_temporada.png)`

## 📜 Licença


