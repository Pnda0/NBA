import pandas as pd
from nba_api.stats.endpoints import LeagueStandingsV3 
from datetime import datetime


temporada = None 

def fetch_league_standings(season_year_start=None):
    """
    Busca e exibe a classificação da NBA por conferência para uma temporada.
    """
    if season_year_start is None:

        today = datetime.today()
        current_year = today.year
        if today.month < 10: 
            season_year_start = current_year - 1
        else:
            season_year_start = current_year
        print(f"Buscando classificação para a temporada atual inferida: {season_year_start}-{str(season_year_start+1)[-2:]}...\n")
    else:
        print(f"Buscando classificação para a temporada: {season_year_start}-{str(season_year_start+1)[-2:]}...\n")

    try:
        standings_endpoint = LeagueStandingsV3(season=str(season_year_start))
    except Exception as e:
        print(f"Erro ao buscar LeagueStandingsV3 para a temporada iniciada em {season_year_start}: {e}")
        return

    try:
        standings_df = standings_endpoint.get_data_frames()[0]
    except IndexError:
        print(f"Não foi possível obter os DataFrames de LeagueStandingsV3 para a temporada iniciada em {season_year_start}.")
        return
    except Exception as e:
        print(f"Erro ao processar DataFrames de LeagueStandingsV3: {e}")
        return

    if standings_df.empty:
        print(f"Nenhuma classificação encontrada para a temporada iniciada em {season_year_start}.")
        return

    print("--- Classificação da NBA ---")
    
    colunas_relevantes_v3 = [
        'TeamCity', 'TeamName', 'Conference', 'PlayoffRank', 
        'WINS', 'LOSSES', 'WinPCT', 'ConferenceGamesBack', 'Streak',
        'ClinchIndicator' 
    ]
    
    colunas_para_mostrar = [col for col in colunas_relevantes_v3 if col in standings_df.columns]
    
    rename_map = {
        'TeamCity': 'Cidade', 'TeamName': 'Time', 'Conference': 'Conf',
        'PlayoffRank': 'Rank Conf', 'WINS': 'V', 'LOSSES': 'D', 'WinPCT': '%V',
        'ConferenceGamesBack': 'GB Conf', 'Streak': 'Seq', 'ClinchIndicator': 'Clinch'
    }
    standings_df_renamed = standings_df[colunas_para_mostrar].rename(columns=rename_map)

    east_standings = standings_df_renamed[standings_df_renamed['Conf'] == 'East'].sort_values(by='Rank Conf')
    west_standings = standings_df_renamed[standings_df_renamed['Conf'] == 'West'].sort_values(by='Rank Conf')

    print("\n--- Conferência Leste ---")
    print(east_standings)

    print("\n--- Conferência Oeste ---")
    print(west_standings)

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_rows', 50) 
    fetch_league_standings(temporada)
