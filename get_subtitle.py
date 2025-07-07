import requests
from bs4 import BeautifulSoup

def search_subtitle(movie_name):
    url = f'https://subtitlecat.com/index.php?search={movie_name.replace(" ", "+")}'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching data from {url}")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #get div with class subtitles
    tr = ((soup.find('div', class_='subtitles')).find('table', class_='table sub-table')).find('tbody').find_all('tr')

    results = []

    for row in tr:
        tds = row.find_all('td')

        title = tds[0].find('a').text.strip()
        rurl = 'https://subtitlecat.com/'+tds[0].find('a')['href']
        nr_of_downloads = tds[2].text.strip()
        nr_of_languages = tds[3].text.strip()

        result = (title, rurl, nr_of_downloads, nr_of_languages)
        results.append(result)
    
    if not results:
        print("No subtitles found.")
        return []   
    print(f"Found {len(results)} subtitles for '{movie_name}':")
    return results

def get_subtitle(url):
    pass