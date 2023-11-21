import requests

URL = "https://www.hltv.org/fantasy/408/leagues/160778/join/json" #JSON sent on get request when joining a specific fantasy event
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    player_names = [player["playerData"]["name"] for team in data["moneyDraftData"]["teams"] for player in team["players"]]
    players_cost = [player["cost"] for team in data["moneyDraftData"]["teams"] for player in team["players"]]
    player_pic_links = [player["playerData"]["picture"] for team in data["moneyDraftData"]["teams"] for player in team["players"]]
    player_stats = [player["playerData"]["stats"] for team in data["moneyDraftData"]["teams"] for player in team["players"]]
    player_data = list(zip(player_names, players_cost, player_pic_links, player_stats))
    print(player_data)