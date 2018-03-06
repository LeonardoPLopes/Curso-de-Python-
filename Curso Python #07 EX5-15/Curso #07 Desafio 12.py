#Mostre o preço do Produto e mostre com desconto de 5%

preço=float(input("Digite o valor do produto: "))

desconto = preço-(preço*(5/100))

print("O valor do produto com 5% de desconto é de: {}".format(desconto))
