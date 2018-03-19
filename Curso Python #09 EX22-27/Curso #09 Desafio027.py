nome=input("Digie o seu nome: ").strip()

lista=nome.split()

print("Muito Prazer em te conhecer!!!")
print("Primeiro: {}".format(lista[0]))
print("Ultimo: {}".format(lista[len(lista)-1]))
