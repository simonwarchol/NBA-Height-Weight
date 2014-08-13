from bs4 import BeautifulSoup
import re
import requests
import unicodedata


top5 = [["", 0],["", 0], ["", 0], ["", 0], ["", 0]]

soup2 = BeautifulSoup(requests.get("http://www.basketball-reference.com/players/g/garripa01.html").text)
text = soup2.find("h1")
next = 0
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
    print("Feet:"+Feet)
    print("Inches:"+Inches)
else:
    Feet = Height [:-2]
    Inches = Height [2:]
    print("Feet:"+Feet)
    print("Inches:"+Inches)
Total = int(Feet)*12 + int(Inches)
print(Total)