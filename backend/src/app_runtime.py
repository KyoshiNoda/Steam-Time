import requests
import json
import time
import threading
from secret_settings import API_KEY, STEAM_ID

lock = threading.Lock()


time_counter = 0

def game_poller():
    response_data = json.loads(requests.get(f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_KEY}&steamids={STEAM_ID}').text)
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



