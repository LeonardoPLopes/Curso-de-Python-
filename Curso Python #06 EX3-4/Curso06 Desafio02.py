#Esse programa ele mostra o tipo primitivo e tambem mostra outras informações alem!

x=input("Digite algo em seu teclado: ")
print("O tipo Primitivo é: ",type(x))
print("É uma letra: ",x.isalpha())
print("É um numero: ",x.isnumeric())
print("É uma letra ou numero: ",x.isalnum())
print("Possui uma letra maiuscula: ",x.isupper())

