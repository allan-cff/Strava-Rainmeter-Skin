import requests
import datetime

tokens = open("tokens.txt", "r")
ATHLETE = tokens.readline().rstrip()
ID = tokens.readline().rstrip()
SECRET = tokens.readline().rstrip()
ACCESS_TOKEN = tokens.readline().rstrip()
REFRESH_TOKEN = tokens.readline().rstrip()
tokens.close()

request = "https://www.strava.com/oauth/token?client_id="+ID+"&client_secret="+SECRET+"&grant_type=refresh_token&refresh_token="+REFRESH_TOKEN

r = requests.post(request)

ACCESS_TOKEN = r.json()['access_token']
REFRESH_TOKEN = r.json()['refresh_token']

tokens = open("tokens.txt", "w")
tokens.write(ATHLETE + "\n" + ID + "\n" + SECRET + "\n" + ACCESS_TOKEN + "\n" + REFRESH_TOKEN)
tokens.close()

request = "https://www.strava.com/api/v3/athlete/activities?access_token=" + ACCESS_TOKEN
r = requests.get(request)
lastActivity = []
lastActivity.append(r.json()[0]['name'])
lastActivity.append(r.json()[0]['distance'])
lastActivity.append(datetime.timedelta(seconds=int(r.json()[0]['moving_time'])))

request = "https://www.strava.com/api/v3/athletes/" + ATHLETE + "/koms?access_token=" + ACCESS_TOKEN
r = requests.get(request)
Koms = len(r.json())

request = "https://www.strava.com/api/v3/athletes/" + ATHLETE + "/stats?access_token=" + ACCESS_TOKEN
r = requests.get(request)
YearCount = r.json()["ytd_ride_totals"]["count"]
YearDistance = r.json()["ytd_ride_totals"]["distance"]

displaytxt = "Last activity : " + str(lastActivity[0]) + ", " + str(lastActivity[1]) + "km, " + str(lastActivity[2]) + "\nTotal of the year : " + str(YearDistance) + "km, " + str(YearCount) + " activities\nKOMs : " + str(Koms)
print(displaytxt)
