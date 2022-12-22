import requests
import json
import time

steam_id = 76561198871279330
api_key = "69165F7C2940B1D23B6A67783A944BAB"

game_tracker = {}

def game_poller():
    global game_tracker

    while True:
        response_data = json.loads(requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=69165F7C2940B1D23B6A67783A944BAB&steamids=76561198871279330").text)
        if 'gameextrainfo' in response_data['response']['players'][0]:
            game_name = response_data['response']['players'][0]['gameextrainfo']
            if game_name not in game_tracker:
                game_tracker[game_name] = {"runtime": 0, "gameid": response_data['response']['players'][0]['gameid']}
            else:
                game_tracker[game_name]["runtime"] += 1
        else:
            print("Sleep 10 seconds")
            time.sleep(10)
            print("Wake up")
            continue
        time.sleep(1)
        print(game_tracker)



def main():
    game_poller()

if __name__ == '__main__':
    main()



