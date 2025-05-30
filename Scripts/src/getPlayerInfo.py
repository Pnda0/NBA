import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import CommonPlayerInfo
import json 

jogador = "Stephen Curry"

def fetch_player_info(player_name):
    """
    Busca e exibe informações detalhadas de um jogador da NBA.
    """
    print(f"Buscando informações para: {player_name}...\n")

    # 1. Encontrar o ID do jogador
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
    print(f"ID do jogador {player_actual_name}: {player_id}\n")

    # 2. Fazer a requisição das informações comuns do jogador
    try:
        player_info_endpoint = CommonPlayerInfo(player_id=player_id)
    except Exception as e:
        print(f"Erro ao buscar CommonPlayerInfo para player_id {player_id}: {e}")
        return
    
    try:
        player_main_info_df = player_info_endpoint.get_data_frames()[0]
    except IndexError:
        print(f"Não foi possível obter os DataFrames de CommonPlayerInfo para {player_actual_name}.")
        return
    except Exception as e:
        print(f"Erro ao processar DataFrames de CommonPlayerInfo: {e}")
        return

    if player_main_info_df.empty:
        print(f"Nenhuma informação principal encontrada para {player_actual_name} (ID: {player_id}).")
        return

    player_details = player_main_info_df.iloc[0].to_dict()

    print("--- Detalhes do Jogador ---")    
    # Selecionando e exibindo informações mais relevantes e formatadas
    print(f"Nome Completo: {player_details.get('DISPLAY_FIRST_LAST', 'N/A')}")
    print(f"Time Atual: {player_details.get('TEAM_CITY', '')} {player_details.get('TEAM_NAME', '')} ({player_details.get('TEAM_ABBREVIATION', 'N/A')})")
    print(f"Camisa: #{player_details.get('JERSEY', 'N/A')}")
    print(f"Posição: {player_details.get('POSITION', 'N/A')}")
    print(f"Altura: {player_details.get('HEIGHT', 'N/A')}")
    print(f"Peso: {player_details.get('WEIGHT', 'N/A')} lbs")
    print(f"Data de Nascimento: {player_details.get('BIRTHDATE', 'N/A').split('T')[0] if player_details.get('BIRTHDATE') else 'N/A'}") 
    print(f"Idade: {player_details.get('AGE', 'N/A')}") 
    print(f"Universidade: {player_details.get('SCHOOL', 'N/A')}")
    print(f"País: {player_details.get('COUNTRY', 'N/A')}")
    print(f"Anos de Draft: {player_details.get('DRAFT_YEAR', 'N/A')}, Round: {player_details.get('DRAFT_ROUND', 'N/A')}, Pick: {player_details.get('DRAFT_NUMBER', 'N/A')}")
    print(f"Anos de Experiência na NBA: {player_details.get('SEASON_EXP', 'N/A')}")
    print(f"Status (PT_BUTTON_TEXT): {player_details.get('PT_BUTTON_TEXT', 'N/A')}") 

if __name__ == "__main__":
    fetch_player_info(jogador)
