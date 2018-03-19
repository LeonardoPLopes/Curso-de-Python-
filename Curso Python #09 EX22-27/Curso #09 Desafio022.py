nome=input("Digite o Seu Nome Completo: ").strip() # funciona fazendo ja o strip no input

print("Todas maiusculas: {}".format(nome.upper()))
print("Todas Minusculas: {}".format(nome.lower()))
print("Letras ao todo sem considerar o espaço é: {}".format(len(nome) - nome.count(' ')))
lista=nome.split()
print("Quantas letras tem o primeiro nome: {}".format(len(lista[0])))
#ouuu
print("Quantas letras tem o primeiro nome: {}".format(nome.find(' ')))
