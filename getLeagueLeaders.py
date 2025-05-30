import pandas as pd
from nba_api.stats.endpoints import LeagueLeaders
from nba_api.stats.library.parameters import SeasonAll 


CATEGORIA_ESTATISTICA = 'PTS' 
TEMPORADA_ALVO = "2024-25" 
TIPO_TEMPORADA = "Regular Season" 
MODO_ESTATISTICA = "PerGame"      
NUM_LIDERES = 10                  

def fetch_league_leaders(stat_category, season, season_type="Regular Season", per_mode="PerGame", top_n=10):
    """
    Busca e exibe os líderes de uma categoria estatística da NBA para uma temporada.
    """
    print(f"Buscando líderes em '{stat_category}' para a temporada {season} ({season_type}, Modo: {per_mode})...\n")

    try:
        leaders_endpoint = LeagueLeaders(
            league_id='00', 
            per_mode_simple=per_mode,
            stat_category_abbreviation=stat_category,
            season=season,
            season_type_all_star=season_type 
        )
    except Exception as e:
        print(f"Erro ao buscar LeagueLeaders para {stat_category}, temporada {season}: {e}")
        return

    try:
        leaders_df = leaders_endpoint.get_data_frames()[0]
    except IndexError:
        print(f"Não foi possível obter os DataFrames de LeagueLeaders para {stat_category}, temporada {season}.")
        return
    except Exception as e:
        print(f"Erro ao processar DataFrames de LeagueLeaders: {e}")
        return

    if leaders_df.empty:
        print(f"Nenhum líder encontrado para '{stat_category}' na temporada {season} ({season_type}).")
        return

    print(f"--- Top {top_n} Líderes em {stat_category} ({season}, {season_type}, {per_mode}) ---")
    
    colunas_relevantes = ['RANK', 'PLAYER', 'TEAM_ABBREVIATION', stat_category, 'GP', 'MIN']
    
    colunas_para_mostrar = [col for col in colunas_relevantes if col in leaders_df.columns]
    
    print(leaders_df[colunas_para_mostrar].head(top_n))

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    fetch_league_leaders(
        CATEGORIA_ESTATISTICA,
        TEMPORADA_ALVO,
        TIPO_TEMPORADA,
        MODO_ESTATISTICA,
        NUM_LIDERES
    )
