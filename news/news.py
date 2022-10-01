# pip install requests
# pip install bs4

import requests

from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# html da noticia
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#titulo
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

print('\nTitulo: ',titulo.text ,'\n')

#subtitulo
textoRelacionado = noticia.find('a', attrs={'class': 'bstn-relatedtext'})

print('Texto relacionado: ', textoRelacionado.text,'\n')