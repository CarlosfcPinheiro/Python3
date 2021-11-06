#esse programa irá entrar no email, e enviar um email para si com certos valores de uma tabela.

import pyautogui as py
import pandas as pd
import time as t
import pyperclip as pc
import openpyxl as op

py.PAUSE = 3
#LEITURA DO PANDAS DA PLANILHA
tabela = pd.read_excel(r'C:/Users/PC/Desktop/Estudo e Escola/Programmer Projects/Python (Pycharm)/Projects/dia anterior.xlsx')
vendas = tabela['vendas ontem'].sum()
#ABRIR O INICIAR
py.click(x=5, y=752, button='left')
#ABRIR O GOOGLE E A GUIA
py.click(x=148, y=212, button='left')
py.click(x=671, y=414, button='left')
py.hotkey('ctrl', 't')
#ENTRAR NO GMAIL E ENVIAR O EMAIL
py.write('https://www.google.com/gmail/')
py.press('enter')
py.sleep(20)
py.click(x=96, y=179, button='left')
py.click(x=871, y=315, button='left')
t.sleep(10)
pc.copy('pg077685@gmail.com')
py.hotkey('ctrl', 'v')
py.click(x=836, y=344, button='left')
pc.copy('Envio teste de informação diária.')
py.hotkey('ctrl', 'v')
py.click(x=832, y=393, button='left')
pc.copy("""
Prezado gerente.
Nosso relatório de vendas de ontem foi de:
{} vendas no total.


""".format(vendas))
py.hotkey('ctrl', 'v')
py.click(x=852, y=699, button='left')








