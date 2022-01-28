#IRÁ COLETAR DADOS ATUAIS SOBRE O EURO, OURO E O DOLAR, ATUALIZAR A PLANILHA E ENVIAR APRA SI MESMO NO EMAIL

from selenium import webdriver
import pyautogui as py
import time as tm
from selenium.webdriver.common.keys import Keys
import pandas as pd

#ABRIR GOOGLE
navegador = webdriver.Chrome('chromedriver.exe')
#NAVEGAR EM GUIAS E COLETAR OS DADOS
navegador.get("https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&oq=cotacao+d&aqs=chrome.1.69i57j0i512l2j0i3j0i512l6.3575j1j7&sourceid=chrome&ie=UTF-8")
dollar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
navegador.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+euro&oq=cota%C3%A7%C3%A3o+euro&aqs=chrome..69i57j0i433i512l3j0i512l6.2496j1j7&sourceid=chrome&ie=UTF-8')
euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
navegador.get('https://www.melhorcambio.com/ouro-hoje')
ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')
#ALTERAÇÕES E LEITURA DA TABELA
tabela = pd.read_excel(r'C:\Users\PC\Desktop\Estudo e Escola\Programmer Projects\Python (Pycharm)\Projects\Produtos.xlsx')
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(dollar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(ouro)

tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

tabela.to_excel('Produtos Novo.xlsx', index=False)
