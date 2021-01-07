import requests
import sys
from colorama import Fore, Back, Style

# Gameboy: 29PPU88JC
# Bazsi: 2V8QR8QVP
# Tomek: PCQCV92VY
# PingpongFighter: 2GGGLVGL8

headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImU5YWE0MWE1LWM2MzctNGQ1ZC1iYWY3LWE2ZDY2MGVlNmI3OCIsImlhdCI6MTYwOTgwMDY4OSwic3ViIjoiZGV2ZWxvcGVyLzIxZTQwNDlmLWY4YzctZGI1Ny05MjM1LTY4NWM0ZmJjMTc5ZiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY5LjY5LjY5LjcwIiwiMTc4LjQ4Ljg0LjQyIl0sInR5cGUiOiJjbGllbnQifV19.9dUiGCHmU0JRLC8HbkrzoCVNp4NCpNja65nbaUtKVgR9xzuiLvoeCppiXAnp_onnRCCkHHgEhhs6C32lP-kiCw',
    'Accept': 'application/json'
}


b = Fore.LIGHTBLACK_EX + Style.BRIGHT   # b
y = Fore.LIGHTYELLOW_EX + Style.BRIGHT  # yellow
r = Fore.LIGHTRED_EX + Style.BRIGHT     # red
w = Fore.WHITE + Style.BRIGHT           # white
m = Fore.MAGENTA + Style.BRIGHT         # magenta
c = Fore.CYAN + Style.BRIGHT            #cyan
g = Fore.GREEN                          #green

player_id = '2GGGLVGL8'     # my id
command_list ={
    'getme': 'shows information about you',
    'getplayer "ID"': 'show information about a specific clasher',
    'myclan': 'lists the members of your clan BUGGY!!!',
    'getclan "ID"': 'lists the members of a specific clan BUGGY!!!',
    'exit': 'travels you back into linux terminal',
    
}

def main():
    def query():
        global player_id
        command = input(Fore.GREEN + Style.BRIGHT + 'coc_stats: ' + Fore.RESET)
        if command == 'getme':
            player_id = '2GGGLVGL8'  # my id
            getplayer()
            query()

        if command == 'myclan':
            getclan()
            query()     ##TODO: not elegant

        if ' ' and 'getplayer' in command:      ##TODO: add clan name, level, town hall level
            temp = command.split()
            player_id = temp[1]
            getplayer()
            query()

        if command == 'exit': sys.exit()
        if command == '': query()

        else:
            print(Fore.RED + Style.BRIGHT + r"this command doesn't exist")
            query()

    print(Fore.YELLOW + Style.BRIGHT + rf"""
                 {b}/ \
                 |||{y}
       ___       {b}|||{y}
      /___\      {b}|||{y}
     (|{w}0 0{y}|)   {b}\_|||_/{y}
   __/[\{r}U{y}/]\____/vvv
  / \  |~|   / _|_P|
  | /\  ~   /_/  {b}[X]{y}
  |_| (____)        
  \_]/______\  {c}Clash of Clans stats tool{y}
     _\_||_/_         {c}by @ladiboti{y}
    (_,_||_,_)            {m}ALPHA
{g}██████████████████████████████████████████
    """)    ##TODO: add an archer too
    query()


def getplayer():
    response = requests.get(f'https://api.clashofclans.com/v1/players/%23{player_id}', headers=headers)
    #https: // api.clashofclans.com / v1 / players / % 232GGGLVGL8
    user = response.json()
    print(fr"{w}Name: {m}{str(user['name'])}")  ##TODO: do it in 1 print
    print(fr"{w}Level: {m}{str(user['expLevel'])}")
    print(fr"{w}Town Hall level: {m}{str(user['townHallLevel'])}")
    print(fr"{w}Current trophies: {m}{str(user['trophies'])}")
    print(fr"{w}All time best: {m}{str(user['bestTrophies'])}")
    print(fr"{w}Successful attacks: {m}{str(user['attackWins'])}")
    print(fr"{w}Clan war stars: {m}{str(user['warStars'])}")
    print(fr"{w}Donations given: {m}{str(user['donations'])} {w}recieved: {m}{str(user['donationsReceived'])}")


def getclan():
    response = requests.get('https://api.clashofclans.com/v1/clans/%23JC2QC8RP/members', headers=headers)
    clan = response.json()
    line = ''
    count = 0
    out = []

    for key in clan:line = line + str(clan[key])

    members = line.split()
    for i in range(len(members)):   ##TODO: only shows the firsts part of the nicknames!!!!!!!!!
        members[i] = members[i].replace(r"'", "")
        if 'expLevel' in members[i]:
            out.append(members[i + 1])
        if 'name' in members[i]:
            if count % 2 == 0:
                #print(members[i + 1])
                out.append(members[i + 1])
            count += 1
        if 'trophies' in members[i]:
            out.append(members[i + 1])

    i = 0
    c = 1
    while i < len(out):
        print(f"{c}. ({out[i + 1][0:-1]}) {out[i][1:-2]} {out[i + 2][0:-1]}")   ##TODO: make a fancy table, add th level, role, sent and recieved donations
        i += 3
        c += 1


main()
##TODO: help: list all existing commands, getplayer: show player by id, getclan2: get clan members by clan id, ALLIGN THE MEMBERS AS FANCY AS POSSIBLE, allow uppercase too
##TODO: CONFIG:TXT!!!!!!!!!!!!!!!!!!

#ask = input("asd")
#temp = ask.split()
#print(temp[1])
