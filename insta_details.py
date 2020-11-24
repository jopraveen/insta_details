#make sure you installed bs4 module if not intsall it using pip
from bs4 import BeautifulSoup as bs
import requests

URL = "https://www.instagram.com/{}/"

# function for getting details

def parse_data(s):
    data = {}
    s = s.split("-")[0]
    s = s.split(" ")
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    return data

def scrape_data(username):
    r = requests.get(URL.format(username))
    s = bs(r.text,'html.parser')
    meta = s.find("meta", property="og:description")
    return parse_data(meta.attrs['content'])

if __name__ == "__main__":
    username = input("Enter Insta ID: ")
    data = scrape_data(username)
    print()
    print("The details of",username, "is:")
    print()
    print(data)
    print()
    print("Thank you, Follow Jopraveen for more Awesome stuffs :D")
