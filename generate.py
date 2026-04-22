# Esse bloco cria um arquivo chamado "alunos.csv" na sua pasta
# É só para termos um arquivo para praticar — no dia a dia você receberia esse arquivo pronto

conteudo = """nome,nota_1,nota_2,nota_3,cidade
Ana,8.5,7.0,9.0,São Paulo
Bruno,6.0,5.5,7.5,Rio de Janeiro
Carla,9.0,9.5,8.0,Curitiba
Daniel,4.0,6.0,5.0,Belo Horizonte
Elena,7.5,8.0,9.5,São Paulo
Felipe,5.0,4.5,6.5,Porto Alegre
"""

# Abrimos o arquivo no modo de escrita ("w") e salvamos o conteúdo
with open("alunos.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo)

print("Arquivo alunos.csv criado com sucesso!")