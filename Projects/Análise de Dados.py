#ESSE CÓDIGO IRÁ ANALISAR E CONSERTAR UMA BASE DE DADOS DE UMA PLANILHA EXCEL

import pandas as pd
import plotly as pt
import openpyxl as op
import plotly_express as px
import matplotlib.pyplot as plt

#TRATAMENTO DOS DADOS
tabela = pd.read_csv(r'C:/Users/PC/Desktop/Estudo e Escola/Programmer Projects/Python (Pycharm)/Projects/tabela_de_dados.csv')
tabela = tabela.drop('Codigo', axis = 1)
tabela = tabela.dropna(how='any', axis = 0)
#VISUALIZAÇÃO DO GRÁFICO DA TABELA
grafico = px.histogram(tabela, x='Genero', y='Casado')
grafico.show()