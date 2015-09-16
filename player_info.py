import requests, json

def get_value(listOfDicts, key):
    for subVal in listOfDicts:
        if key in subVal:
            return subVal[key]

def playerid_list():
	endpoint = "http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=1&LeagueID=00&Season=2014-15"
	players = json.loads(requests.get(endpoint).text)
	results =players['resultSets']
	player_list = get_value(results, 'rowSet')
	for i in range(len(player_list)):
		playerids.append(player_list[i][0])
		

	
	
def player_bio(id):
	playerlink= "http://stats.nba.com/stats/commonplayerinfo?PlayerID=%s" % id
	playerbio= json.loads(requests.get(playerlink).text)
	info = playerbio['resultSets']
	player_info = get_value(info, 'rowSet')
	return player_info
	
players_bios=[]


def __init__(self): 
	playerids=[]
	players_bios=[]
playerid_list()
for i in playerids:
player_info = player_bio(i)
playerid= player_info[0]
first_name = player_info[1]
last_name = player_info[2]
birthdate = player_info[6]
season_exp = player_info[12]
current_team = player_info[16]
position = player_info[14]
height = player_info[10]
from_year = player_info[22]
to_year = player_info[23]
info=(playerid, first_name, last_name, birthdate, season_exp, current_team, 
position, height, from_year, to_year) 
players_bios.append(info)
    

	# (player_info[0], player_info[1], player_info[2], player_info[6],
# 	player_info[12], player_info[16], player_info[14], player_info[10], 
# 	player_info[22], player_info[23])
# 	
# 	
# 	
	playerid= player_info[i][0]
	first_name = player_info[i][1]
	last_name = player_info[i][2]
	birthdate = player_info[i][6]
	season_exp = player_info[i][12]
	current_team = player_info[i][16]
	position = player_info[i][14]
	height = player_info[i][10]
	from_year = player_info[i][22]
	to_year = player_info[i][23]
	 
	query = """
        INSERT INTO basic_python_database
        ('playerID', 'first_name', 'last_name', 'birthdate' , 'season_exp', 'current_team',/
        'position', 'height', 'from_year', 'to_year')

        VALUES
        ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' '%s')
        """ , (	playerid, first_name, last_name, birthdate, season_exp, current_team, 
        	position, height, from_year, to_year) 
