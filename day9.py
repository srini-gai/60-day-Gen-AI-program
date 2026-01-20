'''import requests
import time
import webbrowser

# Pause for 1 second
time.sleep(1)
# Open Google in the browser
webbrowser.open("www.bbc.com")'''

# Use requests to fetch the page
#output =requests.get("https://www.google.com")
#print(output)


# To do : 2 modules /packages install and run 


import requests

from bs4 import BeautifulSoup
import webbrowser


webbrowser.open("www.bbc.com")
# Fetch Google homepage
response = requests.get("https://www.bbc.com")

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract headlines
headlines = soup.find_all(["h2","h3"])  # many news sites use <h3> for headlines

print("=== Latest Headlines ===")
for h in headlines[:10]:  # limit to first 10
    print("-", h.get_text(strip=True))




