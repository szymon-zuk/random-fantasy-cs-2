import requests
import random

URL = "https://www.hltv.org/fantasy/408/leagues/160778/join/json"  # JSON sent on get request when joining a specific fantasy event
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    player_names = [
        player["playerData"]["name"]
        for team in data["moneyDraftData"]["teams"]
        for player in team["players"]
    ]
    players_cost = [
        player["cost"]
        for team in data["moneyDraftData"]["teams"]
        for player in team["players"]
    ]
    player_pic_links = [
        player["playerData"]["picture"]
        for team in data["moneyDraftData"]["teams"]
        for player in team["players"]
    ]
    player_stats = [
        player["playerData"]["stats"]
        for team in data["moneyDraftData"]["teams"]
        for player in team["players"]
    ]
    player_data = list(zip(player_names, players_cost, player_pic_links, player_stats))


def generate_random_team(player_data=player_data, max_cost=1000000):
    available_players = sorted(player_data, key=lambda x: int(x[1]))
    generated_players = []

    while len(generated_players) != 5:
        random_player = random.choice(available_players)
        if (
            sum(player[1] for player in generated_players) + random_player[1]
            <= max_cost
        ):
            generated_players.append(random_player)
            available_players.remove(random_player)

    return generated_players
