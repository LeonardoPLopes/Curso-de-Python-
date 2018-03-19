frase=input("Digite uma frase: ").upper()

print("A letra 'A' aparece : {}".format(frase.count('A')))
print("A letra 'A' aparece na posicao {} pela primeira vez".format(frase.find('A')+1))
print("A letra 'A' aparece na posicao {} pela primeira vez".format(frase.rfind('A')+1))


