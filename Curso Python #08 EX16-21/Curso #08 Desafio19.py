from random import choice

pri=input("Digite o nome do primeiro participante: ")
segu=input("Digite o nome do segundo participante: ")
terc=input("Digite o nome do terceiro participante: ")
quarto=input("Digite o nome do quarto participante: ")

print("O aluno sortudo foi: {}, Parabens!!".format(choice(pri,segu,terc,quarto)))
