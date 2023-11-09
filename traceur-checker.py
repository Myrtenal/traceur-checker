import requests

def checkTraceur(robloxid):
    response = requests.get(f'https://groups.roblox.com/v2/users/{robloxid}/groups/roles')
    for group in response.json()['data']:
        if group['group']['id'] == 3468086:
            if group['role']['id'] == 102688639:
                return True
    return False

print(checkTraceur(20706760))