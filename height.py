from bs4 import BeautifulSoup

import requests

year = raw_input("Enter a NBA season. Note that inputing 1999 would yield the 1998-1999 season:")

r  = requests.get("http://www.basketball-reference.com/leagues/NBA_" +year+"_totals.html")

data = r.text

soup = BeautifulSoup(data)
prev = ""
top5 = [["", 0],["", 0], ["", 0], ["", 0], ["", 0]]
for link in soup.findAll('table')[0].findAll('a'):
    url = link.get('href')
    if (url.startswith("/players")):
    	address = url;
    	if prev != address:
            url = "http://www.basketball-reference.com"+url
            soup2 = BeautifulSoup(requests.get("http://www.basketball-reference.com/players/g/garripa01.html").text)
            text = soup2.find("h1")
            height = soup2.findAll("p")[3]
            Height = unicode(height)
            m = re.search('Height:(.+?)Weight:', Height)
            if m:
                Height = m.group(1)
            m = re.search('</span>(.+?)<span', Height)
            if m:
                Height = m.group(1)
            Height = Height[:-3]
            Height = Height[1:]
            if (len(Height) == 4):
                Feet = Height [:-3]
                Inches = Height [2:]
            else:
                Feet = Height [:-2]
                Inches = Height [2:]
            Total = int(Feet)*12 + int(Inches)
            print(text)
            print(Total)
        prev = address

