print('---PROGRAMA QUE INSERE 5 PORCENTO DE DESCONTO EM UM PRODUTO---')

precoProduto = float(input('Digite o preço do produto desejado: '))

desconto = precoProduto*5/100

print('O valor com 5% de desconto ficou em: R${:.2f}'.format(precoProduto-desconto))
