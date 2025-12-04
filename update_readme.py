import requests
from bs4 import BeautifulSoup
import re

# configuration
token_file = '.config/aocd/token'
readme_file = './README.md'

# get number of stars for all years
def get_number_of_stars() -> int:
    """
    Retrieves the number of stars from the Advent of Code leaderboard API.
    Returns:
        int: The number of stars the user has earned.
    """

    # read access token
    try:
        with open(token_file, "r") as file:
            token = file.read().splitlines()[0]
    except FileNotFoundError:
        print(f"Token file not found: {token_file}")
        exit(1)

    cookie = {'session': token}
    event_page = f'https://adventofcode.com/events'

    # request leaderboard data
    r = requests.get(event_page, cookies=cookie, timeout=60)
    if r.status_code != 200:
        print(f'Event page returned status code {r.status_code}:{r.text}')
        exit(1)
    
    # extract stars information from event page
    html = BeautifulSoup(r.text, "html.parser")
    events = html.find_all("div", attrs={"class": "eventlist-event"})
    stars = {int(x.find("a").text[1:-1]): int((x.find("span").text.replace("*", "")) if x.find("span") is not None else 0) for x in events}

    # return stars
    return stars

if __name__ == "__main__":
    stars = get_number_of_stars()

    # open readme file
    try:
        f = open(readme_file, mode='r+', encoding='utf-8')
        txt = f.read()
        f.seek(0)
    except FileNotFoundError:
        print(f"Readme file not found: {readme_file}")
        exit(1)

    # get number of stars for each year
    stars = get_number_of_stars()

    # update readme content
    for year in stars:
        stars_regex = r'(?<=https:\/\/img\.shields\.io\/badge\/' + re.escape(str(year)) + r'%20⭐-)[0-9]+(?=-yellow)'
        txt = re.sub(stars_regex, f"{stars[year]:02}", txt)

    # write updated content back to readme file
    f.write(txt)
    f.truncate()