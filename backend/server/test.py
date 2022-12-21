from steam.client import SteamClient
from steam.enums import EResult

client = SteamClient()

result = client.cli_login()

if result != EResult.OK:
    print("Failed to login: %s" % repr(result))
    raise SystemExit

print("-"*20)
print("Logged on as:", client.user.name)
print("Community profile:", client.steam_id.community_url)
print("Last logon:", client.user.last_logon)
print("Last logoff:", client.user.last_logoff)
print("Current Games Played", client.user.get_ps('game_played_app_id'))
client.logout()
