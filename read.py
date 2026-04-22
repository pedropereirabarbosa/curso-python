import pandas as pd

df = pd.read_csv("alunos.csv")

# print(df.shape) # qtde de linhas e colunas
# print(df.columns) # lista as colunas
# print(df.dtypes) # mostra o tipo de dado de cada coluna
# print(df.head()) # as 5 primeiras linhas
# print(df.head(2)) # mostra somente as duas primeiras
# print(df.tail()) # mostra as ultimas linhas
# print(df.tail(3)) # mostra as 3 ultimas linhas
# print(df.info()) # resumo geral da tabela
# print(df.describe()) # calculos estatisticos (media)

nomes = df["nome"] # selecionar UMA coluna em serie "lista"
print(nomes)

notas = df[["nome", "nota_1", "nota_2"]]
print(notas)

df["media"] = (df["nota_1"] + df["nota_2"] + df["nota_3"]) / 3

print(df["media"])

df["media"] = df["media"].round(1)

print(df["nome ", "nota_1", "nota_2", "nota_3", "media"])