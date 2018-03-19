#essa frase só vai do 0 ao 20
frase='Curso em Video Python' 

print(frase) # frase normal
print(frase[9]) # mostra a posição 9
print(frase[9:15]) # Mostra do 9 ao 15
print(frase[9:21]) # Mostra do 9 ao 21
print(frase[9:21:2]) # Mostra do 9 ao 21 Pulando de 2 em 2
print(frase[:5]) # Do começo até a posição 5
print(frase[15:]) # Mostra do 15 até o final
print(frase[9::3]) #Vai do 9 até o final pulando de 3 em 3
print(len(frase)) # Mostra o quanto de caracteres
print(frase.count('o')) #Conta quantos 'o' possuem
print(frase.count('o',0,13)) #Conta quantos 'o' do 0 ate o 13 os  
print(frase.find('deo')) #Quantas vezes encontrou o 'deo' e mostra a posição
print(frase.find('Android')) #Não existe o Android na frase, então ele retorna o valor -1
print('Curso' in frase) #Ele pergunta se tem 'Curso' na frase ai retorna true ou false
print(frase.replace('Python','Android')) #Muda o python para Android
print(frase.upper()) # Tudo vai ficar maiusculo
print(frase.lower()) # Tudo para minusculas
print(frase.capitalize()) # Tudo para minusculo e depois colocar só a primeira para maiuscula
print(frase.title()) # Ele analisa a frase, faz uma quebra e coloca em maiusculo só a primeira letra da frase

frasee='   Aprenda Python  '
print(frasee.strip()) # Ele remove os primeiros e ultimos espaços inuteis
print(frasee.rstrip()) # Ele só remove os espaços do lado direito r=rigth
print(frasee.lstrip()) # Remove os espaços da direita

print(frase.split()) #Ele quebra tudo e coloca toda frase em uma lista
d=frase.split()
print('-'.join(d))#Junta todos os elementos de frase e coloca um tracinho

print('')
print('''Caso voce precide fazer um print de uma frase enorme e que
ela esteja tambem em outras linhas é simples
voce pode colocar apenas tres aspas no começo e no final que
da tudo certo!!!''')
print('')
print(frase.upper().count('O')) #Aqui esta combinando o upper com a contagem de 'o' maiusculo



