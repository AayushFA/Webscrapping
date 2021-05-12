from bs4 import BeautifulSoup
import requests

with open('simple.html') as fd:
    soupy=BeautifulSoup(fd,'lxml')
    
#print(soupy.prettify())    
#print(soupy.title.text)
            
                       
            
source= requests.get('https://coreyms.com/').text
soup=BeautifulSoup(source,'lxml')
#print(soup.prettify())
artival=soup.find('article')
#print(artival.prettify())

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()