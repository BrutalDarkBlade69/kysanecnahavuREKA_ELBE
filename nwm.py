import requests
from bs4 import BeautifulSoup

url = "https://hydro.chmi.cz/hppsoldv/popup_hpps_prfdyn.php?seq=307081"

response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, "html.parser")

    elements = soup.find_all(class_="tborder center_text")

    for element in elements:
       
        text = element.get_text(strip=True)
       
        print(text)
        
else:
    print("Chyba: Nepodařilo se načíst data ze stránky.")


