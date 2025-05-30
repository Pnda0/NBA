# get_player_career_stats.py
from pprint import pprint
import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import PlayerCareerStats


nomeJogador = "Stephen Curry"

PER_MODE = "PerGame" 

def fetch_player_career_stats(player_name, per_mode="PerGame"):
    """
    Busca e exibe as estatísticas da carreira de um jogador da NBA,
    temporada por temporada.
    """
    pprint(f"Buscando estatísticas da carreira para: {player_name} (Modo: {per_mode})...\n")

    try:
        player_list = players.find_players_by_full_name(player_name)
    except Exception as e:
        print(f"Erro ao tentar encontrar jogadores: {e}")
        print("Verifique sua conexão com a internet ou se o nome do jogador está correto.")
        return

    if not player_list:
        print(f"Jogador '{player_name}' não encontrado. Verifique o nome e tente novamente.")
        return

    player_id = player_list[0]['id']
    player_actual_name = player_list[0]['full_name']
    pprint(f"ID do jogador {player_actual_name}: {player_id}\n")

    try:
        career_stats_endpoint = PlayerCareerStats(player_id=player_id, per_mode36=per_mode)
    except Exception as e:
        print(f"Erro ao buscar PlayerCareerStats para player_id {player_id}: {e}")
        return

    try:
        career_df_regular_season = career_stats_endpoint.get_data_frames()[0]
        
    except IndexError:
        print(f"Não foi possível obter os DataFrames de PlayerCareerStats para {player_actual_name}.")
        return
    except Exception as e:
        print(f"Erro ao processar DataFrames de PlayerCareerStats: {e}")
        return

    if career_df_regular_season.empty:
        print(f"Nenhuma estatística de temporada regular encontrada para {player_actual_name} (ID: {player_id}).")
        return

    pprint(f"--- Estatísticas da Carreira (Temporada Regular - {per_mode}) para {player_actual_name} ---")
    
    colunas_para_mostrar = [
        'SEASON_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN',
        'FGM', 'FGA', 'FG_PCT',
        'FG3M', 'FG3A', 'FG3_PCT',
        'FTM', 'FTA', 'FT_PCT',
        'OREB', 'DREB', 'REB',
        'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'
    ]
    
    colunas_existentes = [col for col in colunas_para_mostrar if col in career_df_regular_season.columns]
    
    return (career_df_regular_season[colunas_existentes])


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None) 
    pd.set_option('display.width', 1000) 
    
    df = fetch_player_career_stats(nomeJogador, per_mode=PER_MODE)
    print(df)