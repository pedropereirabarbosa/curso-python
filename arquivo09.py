# arquivo = open("python.txt", "w")
# arquivo.write("Curso de Python\n")
# arquivo.write("Aprendendo a manipular arquivos com python...")
# arquivo.close()

pegar = open("python.txt", "r")
conteudo = pegar.read()
print(conteudo)

for i in conteudo:
    print(i)