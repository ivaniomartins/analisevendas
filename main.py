import pandas as pd
from twilio.rest import Client

#ler todos os arquivos de vendas
meses = ['janeiro', 'fevereiro','março', 'abril','maio','junho']

# Your Account SID from twilio.com/console
account_sid = "AC1c31abffc2ab99c7fabb08a7d6886ac7"
#"AC1c31abffc2ab99c7fabb08a7d6886ac7"
# Your Auth Token from twilio.com/console
auth_token = "5f3f81857a4e1a74d7868dc54c595fe3" #"your_auth_token"
client = Client(account_sid, auth_token)


#lendo cada arquivo e verificando quem bateu a meta
for mes in meses:
    tabela_vendas = pd.read_excel(mes + '.xlsx')
    if (tabela_vendas['Vendas'] >55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] >55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]


        message = client.messages.create(
            to="+5581993753853",
            from_="+19543680589",
            body=f'Em {mes}, a meta  foi alcançada pelo vendedor {vendedor}, no valor de R${vendas}')

        print(message.sid)