import requests
from bs4 import BeautifulSoup
import re
import time

teamRoster = {}
NBA = ["https://www.espn.com/nba/team/roster/_/name/bos/boston-celtics","https://www.espn.com/nba/team/roster/_/name/bkn/brooklyn-nets","https://www.espn.com/nba/team/roster/_/name/ny/new-york-knicks","https://www.espn.com/nba/team/roster/_/name/phi/philadelphia-76ers","https://www.espn.com/nba/team/roster/_/name/tor/toronto-raptors","https://www.espn.com/nba/team/roster/_/name/chi/chicago-bulls","https://www.espn.com/nba/team/roster/_/name/cle/cleveland-cavaliers","https://www.espn.com/nba/team/roster/_/name/det/detroit-pistons","https://www.espn.com/nba/team/roster/_/name/ind/indiana-pacers","https://www.espn.com/nba/team/roster/_/name/mil/milwaukee-bucks","https://www.espn.com/nba/team/roster/_/name/den/denver-nuggets","https://www.espn.com/nba/team/roster/_/name/min/minnesota-timberwolves","https://www.espn.com/nba/team/roster/_/name/okc/oklahoma-city-thunder","https://www.espn.com/nba/team/roster/_/name/por/portland-trail-blazers","https://www.espn.com/nba/team/roster/_/name/utah/utah-jazz","https://www.espn.com/nba/team/roster/_/name/gs/golden-state-warriors","https://www.espn.com/nba/team/roster/_/name/lac/la-clippers","https://www.espn.com/nba/team/roster/_/name/lal/los-angeles-lakers","https://www.espn.com/nba/team/roster/_/name/phx/phoenix-suns","https://www.espn.com/nba/team/roster/_/name/sac/sacramento-kings","https://www.espn.com/nba/team/roster/_/name/atl/atlanta-hawks","https://www.espn.com/nba/team/roster/_/name/cha/charlotte-hornets","https://www.espn.com/nba/team/roster/_/name/mia/miami-heat","https://www.espn.com/nba/team/roster/_/name/orl/orlando-magic","https://www.espn.com/nba/team/roster/_/name/wsh/washington-wizards","https://www.espn.com/nba/team/roster/_/name/dal/dallas-mavericks","https://www.espn.com/nba/team/roster/_/name/hou/houston-rockets","https://www.espn.com/nba/team/roster/_/name/mem/memphis-grizzlies","https://www.espn.com/nba/team/roster/_/name/no/new-orleans-pelicans","https://www.espn.com/nba/team/roster/_/name/sa/san-antonio-spurs"]
for x in NBA:  
    page = requests.get(x)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="espnfitt")
    job_elements = results.find("tbody", class_="Table__TBODY")
    teamRoster[x] = {_.get("href") for _ in job_elements.find_all("a",class_="AnchorLink")}

NBATeams = {}
for i,j in teamRoster.items():
    teamName = i.split("/")[8]
    NBATeams[teamName] = {}
    for x in j:
        playerName,playerID = x.split("/")[8], x.split("/")[7]
        NBATeams[teamName][playerName] = playerID

print(NBATeams)