import json
import pandas as pd

with open("materias.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
    lst = list(dados)

materias = [n for n in lst if n['situacao'] == "Aprovado"]
df = pd.DataFrame(materias)

fil = filter((lambda x: x['situacao'] == "Aprovado"), lst)
for i in fil: print(i)

# df.to_csv("materias Aprovado.csv")
# for i in materias: print(i)
