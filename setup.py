import requests

ATHLETE = input("Enter your Strava athlete number : ").rstrip()
ID = input("Enter Strava api Client id : ").rstrip()
SECRET = input("Enter Strava api Client secret : ").rstrip()
print("Copy/Paste this link : http://www.strava.com/oauth/authorize?client_id=" + str(ID) + "&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all")
CODE = input("Enter authorization code : ").rstrip()

request = "https://www.strava.com/oauth/token?client_id=" + str(ID) + "&client_secret=" + str(SECRET) + "&code=" + str(CODE) + "&grant_type=authorization_code"
r = requests.post(request)

try:
    ACCESS_TOKEN = r.json()['access_token']
    REFRESH_TOKEN = r.json()['refresh_token']

    tokens = open("tokens.txt", "w")
    tokens.write(ATHLETE + "\n" + ID + "\n" + SECRET + "\n" + ACCESS_TOKEN + "\n" + REFRESH_TOKEN)
    tokens.close()
    print("Setup complete !")
except :
    print("There was an error, please try again")