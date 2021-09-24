
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

import requests

from bs4 import BeautifulSoup

source = requests.get(wiki).text

soup = BeautifulSoup(source, "lxml")

right_table = soup.find('table', class_ = 'wikitable')

A = []
B = []
C = []
D = []
E = []
F = []

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    
    #if it is first row, th(count) = 7, td(count) = 0
    #for rest of rows, th(count) = 1, td(count) = 6
    
    if len(cells) == 6:
        A.append(cells[1].text.strip())
        B.append(states[0].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        
        
import pandas as pd


df = pd.DataFrame()

df['State_UT'] = B
df['Admin_Cap'] = A
df['Legis_Cap'] = C
df['Judi_Cap'] = D
df['Year'] = E
df['Formar_Cap'] = F
        
df.to_csv('states.csv', index = False)



df1 = pd.DataFrame(zip(A,B,C,D,E,F), columns = ['States','B','C','D','E','F'])
        
        
    
    
    