import requests

requisicao=requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
requisicao_json=requisicao.json()

#print(requisicao_json)

cotacao_dolar = requisicao_json["USDBRL"]["bid"]
cotacao_euro = requisicao_json["EURBRL"]["bid"]
cotacao_bitcoin = requisicao_json["BTCBRL"]["bid"]

print(f"cotação atual do dollar é: {cotacao_dolar}")
print(f"cotação atual do euro é: {cotacao_euro}")
print(f"cotação atual do bitcoin é: {cotacao_bitcoin}")

real=float(input("\n QUANTOS REAIS DESEJA CONVERTER? \n"))
moeda=input("QUAL MOEDA? (DOLLAR, EURO OU BITCOIN) \n")

if moeda == "DOLLAR":
  dolar=float(real)/float(cotacao_dolar)
  print(f"R${real} = USD {dolar:.2f}")
elif moeda == "EURO":
  euro=float(real)/float(cotacao_dolar)
  print(f"R${real} = EUR {euro:.2f}")
elif moeda == "BITCOIN":
  bitcoin=float(real)/float(cotacao_dolar)
  print(f"R${real} = BTC {bitcoin:.2f}")
else:
  print("moeda inválida")