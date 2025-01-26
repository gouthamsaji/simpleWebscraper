import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

#sending request to fetch html content of the webpage
response = requests.get(url)

if response.status_code == 200:
    html_content = response.content

#parsing html content
soup = BeautifulSoup(html_content,'html.parser')

#finding all headlines
headlines = soup.find_all('h2')
print('BBC News headlines : \n')

#printing first 10 headlines
for i,headline in enumerate(headlines[:10],1):
    print(f"{i}. {headline.text.strip()}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")