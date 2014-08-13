from bs4 import BeautifulSoup
import re
import unicodedata
import requests


#Change this year to change the year for the data
year = "2006";
r  = requests.get("http://www.basketball-reference.com/leagues/NBA_" +year+"_totals.html")

data = r.text

soup = BeautifulSoup(data)
prev = ""
where = 0
heightlist = []
print("\"Name\", Height (Inches), Height(Feet-Inches), Weight")
for link in soup.findAll('table')[0].findAll('a'):
    url = link.get('href')
    if (url.startswith("/players")):
    	address = url;
    	if prev != address:
            url = "http://www.basketball-reference.com"+url
            soup2 = BeautifulSoup(requests.get(url).text)
            name = soup2.find("h1")
            name = unicode(name)
            name = name[4:]
            name = name[:-5]
            height = soup2.findAll("p")[3]
            Height = unicode(height)
            Weight = Height
            m = re.search('Height:(.+?)Weight:', Height)
            if m:
                Height = m.group(1)
            m = re.search('</span>(.+?)<span', Height)
            if m:
                Height = m.group(1)
            #players with pronounciations of their names
            #require a sepcial case
            if(len(Height)>8):
                height = soup2.findAll("p")[4]
                Height = unicode(height)
                Weight = Height
                m = re.search('Height:(.+?)Weight:', Height)
                if m:
                    Height = m.group(1)
                m = re.search('</span>(.+?)<span', Height)
                Height = Height[:-24]
                Height = Height[7:]
            m = re.search('Weight:(.+?)Age:', Weight)
            if m:
                Weight = m.group(1)
            m = re.search('Weight:</span> (.+?) lbs', Weight)
            if m:
                Weight = m.group(1)
            Height = Height[:-3]
            Height = Height[1:]
            if (len(Height) == 4):
                Feet = Height [:-3]
                Inches = Height [2:]
            else:
                Feet = Height [:-2]
                Inches = Height [2:]
            Total = int(Feet)*12 + int(Inches)
            Height.decode('ascii','ignore')
            StringHeight = str(Feet)+"-"+str(Inches)
            print "\"%s\", %d, %s, %d"% (name, Total, StringHeight, int(Weight))
            #see where this player ranks that season
            heightlist.append((name, Total))
    prev = address
# print("Done Reading Data In")
# heightlist.sort(key=lambda tup: tup[1], reverse=True)
# print "Tallest Player in the %d-%d NBA Season was %s with a height of %d'%d" 
# print(heightlist[0][0])
# print("With Height of")
# print(heightlist[0][1])


