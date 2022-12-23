import requests
import json
import time
import threading

lock = threading.Lock()

steam_id = 76561198871279330
api_key = "69165F7C2940B1D23B6A67783A944BAB"

time_counter = 0

def game_poller():
    response_data = json.loads(requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=69165F7C2940B1D23B6A67783A944BAB&steamids=76561198871279330").text)
    if 'gameextrainfo' in response_data['response']['players'][0]:
        return True
    return False

def counter():
    global time_counter
    start = time.time()
    while True:
        if game_poller() == True:
            lock.acquire()
            time_counter = int(time.time() - start)
            lock.release()
            time.sleep(1)
            continue
        else:
            break

def printer():
    global time_counter
    while True:
        lock.acquire()
        print(time_counter)
        lock.release()
        time.sleep(1)

def main():
    t1 = threading.Thread(target=counter)
    t2 = threading.Thread(target=printer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()




if __name__ == '__main__':
    main()



