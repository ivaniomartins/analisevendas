import pandas as pd

#ler todos os arquivos de vendas
meses = ['janeiro', 'fevereiro','março', 'abril','mario','junho' ]


#lendo cada arquivo e verificando quem bateu a meta
for mes in meses:
    tabela_vendas = pd.read_excel(mes + '.xlsx')
    if (tabela_vendas['Vendas'] >55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] >55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        