# pip install requests

# pip install bs4

import requests

from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# html da noticia
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# titulo da noticia
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
print('\nTitulo - ',titulo.text ,'\n')

# resumo da noticia
resumo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
print('\nResumo: ',resumo.text,'\n')

# texto relacionado
textoRelacionado = noticia.find('a', attrs={'class': 'bstn-relatedtext'})
print('Texto relacionado: ', textoRelacionado.text,'\n')