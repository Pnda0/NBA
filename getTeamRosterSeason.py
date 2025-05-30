import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import CommonTeamRoster


time = "Golden State Warriors"
temporada = "2024-25" 

def fetch_team_roster(team_name_query, season):
    """
    Busca e exibe o elenco de um time da NBA para uma temporada específica.
    """
    print(f"Buscando elenco para: {team_name_query}, Temporada: {season}...\n")

    try:
        team_list = teams.find_teams_by_full_name(team_name_query)
        if not team_list: team_list = teams.find_teams_by_nickname(team_name_query)
        if not team_list: team_list = teams.find_teams_by_city(team_name_query)
        if not team_list: team_list = teams.find_teams_by_abbreviation(team_name_query.upper())
    except Exception as e:
        print(f"Erro ao tentar encontrar times: {e}")
        return

    if not team_list:
        print(f"Time '{team_name_query}' não encontrado. Verifique o nome e tente novamente.")
        return

    team_id = team_list[0]['id']
    actual_team_name = team_list[0]['full_name']
    print(f"ID do time {actual_team_name}: {team_id}\n")

    try:
        team_roster_endpoint = CommonTeamRoster(team_id=team_id, season=season)
    except Exception as e:
        print(f"Erro ao buscar CommonTeamRoster para team_id {team_id}, temporada {season}: {e}")
        return

    try:
        roster_df = team_roster_endpoint.get_data_frames()[0]
        coaches_df = team_roster_endpoint.get_data_frames()[1]
    except IndexError:
        print(f"Não foi possível obter os DataFrames de CommonTeamRoster para {actual_team_name}, temporada {season}.")
        return
    except Exception as e:
        print(f"Erro ao processar DataFrames de CommonTeamRoster: {e}")
        return

    if roster_df.empty:
        print(f"Nenhum jogador encontrado no elenco de {actual_team_name} para a temporada {season}.")
    else:
        print(f"--- Elenco de Jogadores: {actual_team_name} ({season}) ---")
        colunas_jogadores = ['PLAYER', 'NUM', 'POSITION', 'HEIGHT', 'WEIGHT', 'BIRTH_DATE', 'AGE', 'EXP', 'SCHOOL']
        print(roster_df[colunas_jogadores])

    if coaches_df.empty:
        print(f"\nNenhuma informação de técnicos encontrada para {actual_team_name} na temporada {season}.")
    else:
        print(f"\n--- Comissão Técnica: {actual_team_name} ({season}) ---")
        colunas_tecnicos = ['COACH_NAME', 'COACH_TYPE', 'COACH_ID'] 
        print(coaches_df[[col for col in colunas_tecnicos if col in coaches_df.columns]])


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000) 
    fetch_team_roster(time, temporada)
