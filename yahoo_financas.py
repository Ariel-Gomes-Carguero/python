import requests
from bs4 import BeautifulSoup

page = "https://br.financas.yahoo.com/quote/VVAR3.SA"
valor = []
title = []

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print("Erro ao fazer requisição")
    except Exception as error:
        print("Erro ao fazer requisição")
        print(error)


def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except Exception as error:
        print("Erro ao fazer o parsing HTML")
        print(error)

def tituloacao(soup):
    titulo = soup.find_all('h1', class_="D(ib) Fz(16px) Lh(18px)")
    for title in titulo:
        title = (title.text.strip())
    return title


def valoracao(soup):
    valores = soup.find('div', class_="My(6px) Pos(r) smartphone_Mt(6px)")
    for valor in valores:
        valor = (valor.text.strip())
    return valor

def apresenta(title,acao):
    print("Ação: {}".format(title))
    print("Valor Atualizado: {}".format(acao[0:4]))
    return


if __name__ == "__main__":
    resposta_yahoo = requisicao(page)
    if resposta_yahoo:
        soup_busca = parsing(resposta_yahoo)
        if soup_busca:
            title = tituloacao(soup_busca)
            acao =  valoracao(soup_busca)
            apresenta(title,acao)


