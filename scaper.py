import requests
from bs4 import BeautifulSoup
from database import *

def buscaMagnet(a):
    torrentPage = requests.get(a.get('https://lapumia.org/uncharted-fora-do-mapa-torrent-2022-legendado-camrip-720p-download/'))
    print(torrentPage)

def buscaTorrent():
    pagina = 1
    buscando = True
    while buscando:
        try:
            res = requests.get('https://lapumia.org/page/' + str(pagina) + '/')
        except:
            buscando = False
            break
        html_page = res.text
        soup = BeautifulSoup(html_page, 'html.parser')
        soup.prettify()
        section = soup.find('section')
        for div_posts in section.find_all('div', class_='posts'):
            # print(div_posts.text)
            for div_post in div_posts.find_all('div', class_='post'):
                for div_title in div_post.find_all('div', class_='title'):
                    # print(div_title.text)
                    for a in div_title.find_all('a'):
                        insereMedia(a.get('href'), 4 , a.get('title'))
                        # buscaMagnet(a)
        pagina = pagina + 1
    finalizaConexao()

buscaTorrent()





# for link in table:
#     print(link.get('href'))

# table = soup.findAll('div')
# print(posts)
# torrentPage = requests.get(a.get('https://lapumia.org/uncharted-fora-do-mapa-torrent-2022-legendado-camrip-720p-download/'))