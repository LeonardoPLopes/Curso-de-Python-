import random

alu1=input("Primeiro Aluno: ")
alu2=input("Segundo Aluno: ")
alu3=input("Terceiro Aluno: ")
alu4=input("Quarto Aluno: ")

lista=[alu1,alu2,alu3,alu4]

escolher=random.choice(lista)
random.shuffle(lista)
#random.choice ela faz voce escolher
#random.shuffle faz voce apenas embbaralhar

print("Os Alunos que irão apresentar são: {}".format(escolher))
print("Os Alunos que irão apresentar são: {}".format(lista))

