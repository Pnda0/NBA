import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import ShotChartDetail
import matplotlib.pyplot as plt
import seaborn as sns 


jogador = "Luka Doncic"
temporada = "2024-25" 


def fetch_and_plot_shot_chart(player_name, season):
    """
    Busca dados de arremessos de um jogador para uma temporada e plota um gráfico básico.
    """
    print(f"Buscando shot chart para: {player_name}, Temporada: {season}...\n")

    # 1. Encontrar o ID do jogador
    try:
        player_list = players.find_players_by_full_name(player_name)
    except Exception as e:
        print(f"Erro ao tentar encontrar jogadores: {e}")
        return

    if not player_list:
        print(f"Jogador '{player_name}' não encontrado.")
        return

    player_id = player_list[0]['id']
    player_actual_name = player_list[0]['full_name']
    print(f"ID do jogador {player_actual_name}: {player_id}\n")

    team_id_for_shots = 0 

    try:
        shot_chart_endpoint = ShotChartDetail(
            team_id=team_id_for_shots,
            player_id=player_id,
            season_nullable=season,
            context_measure_simple='FGA'
        )
        shot_df = shot_chart_endpoint.get_data_frames()[0]
    except IndexError:
        print(f"Não foi possível obter os DataFrames de ShotChartDetail para {player_actual_name} na temporada {season}.")
        return
    except Exception as e:
        print(f"Erro ao buscar ShotChartDetail: {e}")
        return

    if shot_df.empty:
        print(f"Nenhum dado de arremesso encontrado para {player_actual_name} na temporada {season}.")
        return

    print(f"--- Dados de Arremessos para {player_actual_name} ({season}) ---")
    print(f"Total de arremessos tentados registrados: {len(shot_df)}")
    print(shot_df[['ACTION_TYPE', 'SHOT_TYPE', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_DISTANCE', 'LOC_X', 'LOC_Y', 'SHOT_MADE_FLAG']].head())

    plt.figure(figsize=(12, 11)) 
    
    sns.scatterplot(
        x='LOC_X',
        y='LOC_Y',
        hue='SHOT_MADE_FLAG',
        data=shot_df,
        palette={1: 'green', 0: 'red'}, 
        alpha=0.7,
        legend='full'
    )
    
    plt.title(f'Shot Chart de {player_actual_name} - Temporada {season}')
    plt.xlabel('LOC_X (Distância horizontal do centro do aro)')
    plt.ylabel('LOC_Y (Distância vertical do aro)')
    
    plt.xlim(-250, 250)
    plt.ylim(-47.5, 470) 
    plt.gca().set_aspect('equal', adjustable='box') 
    plt.grid(False) 

    # Adicionando uma linha central e o arco de 3 pontos (simplificado)
    plt.scatter(0, 0, s=100, c='orange', marker='o', edgecolors='black', zorder=5) 
    three_point_arc = plt.Circle((0, 0), 237.5, color='blue', fill=False, linewidth=1.5, linestyle='--') # Raio de 23.75 pés
    plt.gca().add_patch(three_point_arc)

    plt.plot([-220, -220], [-47.5, 80], color='blue', linewidth=1.5, linestyle='--') 
    plt.plot([220, 220], [-47.5, 80], color='blue', linewidth=1.5, linestyle='--')   

    print("\nVisualização básica do shot chart gerada. Para um mapa de calor ou um desenho preciso da quadra,")
    plt.show()

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    fetch_and_plot_shot_chart(jogador, temporada)
