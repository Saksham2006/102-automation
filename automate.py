import requests
from bs4 import BeautifulSoup

print(f'What day of the week is it?\n\n')
response = requests.get("https://whatweekisit.com/")                                                     
status_1 = response.status_code
if status_1 == 200:
    soup = BeautifulSoup(response.content, "html.parser")  
    soup.find_all("p")
    table = soup.find("table")
    table_content = table.find_all("td")
    for tag in table_content:
        print(tag.get_text())
else:
    print('Error, unable to fetch results. Try again later.')