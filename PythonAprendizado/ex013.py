print('---PROGRAMA QUE INSERE 15 PORCENTO DE AUMENTO NO SALÁRIO---')

nome = str(input('Digite o seu nome: '))
salario = float(input('Digite o valor do seu salário: '))
nota = float(input('Digite sua avaliação semestral de 0 a 10: '))

if nota <= 7.99:
    print('Olá {}, infelizmente você não recebeu o reajuste por conta da nota {}'
          ' no semestre, portanto, seu salário continua em R${}'
          .format(nome, nota, salario)
    )
else:
    reajuste = salario*15/100
    novoSalario = salario+reajuste
    print('Olá {}, parabéns! Você recebeu um reajuste de 15% no salário de R${}\n'
          'graças a nota {} no semestre e agora vai passar à receber R${}'
          .format(nome, salario, nota, novoSalario)
    )

