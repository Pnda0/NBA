# get_team_details.py
import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import TeamDetails


time = "Golden State Warriors"  


def fetch_team_details(team_name_query):
    """
    Busca e exibe informações detalhadas de um time da NBA.
    """
    print(f"Buscando detalhes para o time: {team_name_query}...\n")

    # 1. Encontrar o ID do time
    try:
        team_list = teams.find_teams_by_full_name(team_name_query)
        if not team_list:
            team_list = teams.find_teams_by_nickname(team_name_query)
        if not team_list:
            team_list = teams.find_teams_by_city(team_name_query)
        if not team_list:
            team_list = teams.find_teams_by_abbreviation(team_name_query.upper())

    except Exception as e:
        print(f"Erro ao tentar encontrar times: {e}")
        return

    if not team_list:
        print(f"Time '{team_name_query}' não encontrado. Verifique o nome e tente novamente.")
        return

    team_id = team_list[0]['id']
    actual_team_name = team_list[0]['full_name'] 
    print(f"ID do time {actual_team_name}: {team_id}\n")

    # 2. Fazer a requisição dos detalhes do time
    try:
        team_details_endpoint = TeamDetails(team_id=team_id)
    except Exception as e:
        print(f"Erro ao buscar TeamDetails para team_id {team_id}: {e}")
        return
    
    try:
        team_info_df = team_details_endpoint.get_data_frames()[0]
    except IndexError:
        print(f"Não foi possível obter os DataFrames de TeamDetails para {actual_team_name}.")
        return
    except Exception as e:
        print(f"Erro ao processar DataFrames de TeamDetails: {e}")
        return

    if team_info_df.empty:
        print(f"Nenhuma informação detalhada encontrada para {actual_team_name} (ID: {team_id}).")
        return

    team_data = team_info_df.iloc[0].to_dict()

    print(f"--- Detalhes do Time: {actual_team_name} ---")
    print(f"ID do Time: {team_data.get('TEAM_ID', 'N/A')}")
    print(f"Cidade: {team_data.get('CITY', 'N/A')}")
    print(f"Nome: {team_data.get('NICKNAME', 'N/A')}") # 'NICKNAME' aqui é o nome do time (ex: Celtics)
    print(f"Abreviação: {team_data.get('ABBREVIATION', 'N/A')}")
    print(f"Conferência: {team_data.get('CONFERENCE', 'N/A')}")
    print(f"Divisão: {team_data.get('DIVISION', 'N/A')}")
    print(f"Ano de Fundação: {team_data.get('YEARFOUNDED', 'N/A')}")

    try:
        team_background_df = team_details_endpoint.get_data_frames()[2]
        if not team_background_df.empty and 'HEADCOACH' in team_background_df.columns:
            print(f"Técnico Principal (Head Coach): {team_background_df.iloc[0].get('HEADCOACH', 'N/A')}")
        else:
            print("Informação do técnico não encontrada diretamente em TeamDetails.Background.")
    except IndexError:
        print("DataFrame de Background não encontrado em TeamDetails.")
    except Exception as e:
        print(f"Erro ao tentar buscar técnico: {e}")


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    fetch_team_details(time)
