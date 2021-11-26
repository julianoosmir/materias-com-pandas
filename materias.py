import json
import pandas as pd


with open("materias.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
    lst = list(dados)
   
materias = [n for n in lst if  n['situacao'] == "A cursar"] 
df = pd.DataFrame(materias)

df.to_csv("materias a cursar.csv")
for i in materias: print(i) 