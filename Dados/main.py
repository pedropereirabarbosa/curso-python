import pandas as pd
import matplotlib.pyplot as plt

print("bibliotecas instaladas")

df = pd.read_csv("alunos.csv")
print(df)

print(df["cidade"])

df["media"] = (df["nota_1"] + df["nota_2"] + df["nota_3"]) / 3

df["media"] = df["media"].round(1)

print(df[["nome", "nota_1", "nota_2", "nota_3", "media"]])

# df["situacao"] = df["media"].apply(
#     lambda media: "Aprovado" if media >= 6 else "Reprovado"
# )

# print(df[["nome" , "situacao"]])

# aprovados_com_distincao = df[df["media"] >=7]
# print(aprovados_com_distincao)

# alunos_sp = df[df["cidade"] == "São Paulo"]
# print(alunos_sp)

filtro = df[(df["media"] >= 7) & (df["cidade"] == "São Paulo")]
print(filtro)

df_ordenado = df.sort_values("media")
print(df_ordenado[["nome", "media"]])

df_ordenado = df.sort_values("media", ascending=False)
print(df_ordenado[["nome", "media"]])

print(df["media"].sum) # soma

fig, ax = plt.subplots(figsize=(8,5))
ax.bar(df["nome"], df["media"], color="steelblue")
ax.set_title("Média Final dos Alunos", fontsize=14)
ax.set_xlabel("Alunos")
ax.set_ylabel("Alunos")
plt.tight_layout()

plt.show()