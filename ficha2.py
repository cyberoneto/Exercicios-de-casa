# Desenvolva um programa que solicite que um usuário informe o número de votos brancos, nulos e válidos de uma eleição e exiba
#  o percentual que cada um representa em relação ao total de eleitores.

# 2. Escreva um programa que verifica se uma pessoa é maior de idade (18 anos ou mais). E imprima se ela é ou não maior de idade.
# ==base==
#  PEDIR IDADE
# VERIFICA SE É MAIOR DE IDADE
# DIZER SE É MAIOR OU NAO

# ==ENTRADA DE DADOS==

# idade = int ( input (' Informe a sua idade:'))

# # ==PROCESSAMENTO DE DADOS==
# if idade >= 18:
#     print ('Você é maior de Idade')
# else: 
#     print (' Você é menor de idade')
# # ==SAIDA DE DADOS==


# 3. Escreva um programa que verifique se um número é par ou ímpar. E imprima essa informação.

# # ==BASE==
# # INSERIR NUMERO
# # PRINTAR SE É PAR OU IMPAR


# # ==ENTRADA DE DADOS==

# numero = float (input ('Digite um numero: '))
 
# # ==PROCESSAMENTO==
# if numero %2 == 0:
#     print ('O numero é par')

# else:
#     print ('O numero é impar.')


# 4. Escreva um programa que peça o salário de 2 pessoas e informe qual dos dois é o maior.

# # ==BASE==
# ESCREVER DOIS SALARIOS
# DIZER QUAL FOI O MAIOR

# ==ENTRADA DE DADOS==
salario1 =  float (input ('Digite um Salário da primeira pessoa:' ))
salario2 = float (input (' Digite o salario da outra pessoa:'))

# ==PROCESSAMENTO==
if salario1 > salario2:
    print ('O maior salario foi: {salario1}')
elif salario2 < salario2 :
    print ('O salario {salario2} é maior.')
else:
    print (' Os salarios sao iguais')

# ==SAIDA DE DADOS==
# 5. Escreva um programa que verifica se uma palavra inserida pelo usuário é "Python". E imprima se é ou não.
# 6. Escreva um programa que verifica se um número é positivo, negativo ou zero.
# 7. Escreva um programa que encontra o maior de três números.

# ==BASE==
# SOLICITAR 3 NUMEROS
# PRINTAR O MAIOR
 

# # ==ENTRADA DE DADOS==
# numero1 = float (input ( 'Digite um Numero:'))
# numero2=float (input('Digite outro numero:'))
# numero3= float (input( 'Digite o terceiro numero:'))

# # ==PROCESSAMENTO==
# if numero1 > numero2 and numero2 > numero3:
#     print (f'( O maior numero é: {numero1})')

# elif numero2 > numero3 and numero2 > numero1:
#     print (f'O maior numero foi {numero2} ')

# elif numero3 > numero1 and numero3 > numero2:
#     print (f'O numero maior foi o {numero3}')
# else:
#     print (' Algum numero repetido')



# 8. Escreva um programa que verifica se um número é divisível por 5.


# 9. Escreva um programa que solicita a nota 3 provas, faz a média e informa se o aluno foi aprovado (nota maior ou igual a 7).
# 10. Escreva um programa que verifica se um número é divisível por 3 e por 5.
# 11. Desenvolva um programa que determine o módulo de um número inteiro (se o número for negativo ele deve ser transformado em positivo).
# 12. Escreva um programa que peça a velocidade do motorista e a velocidade máxima em uma determinada avenida, e calcule a multa (se houver), sabendo que
# são pagos:
# a) 50 reais se o motorista ultrapassar em até 10km/h a velocidade permitida (ex.: velocidade máxima: 50km/h; motorista a 60km/h ou a56km/h);

# b) 100 reais, se o motorista ultrapassar de 11 a 30 km/h a velocidade permitida.
# c) 200 reais, se estiver acima de 31km/h da velocidade permitida.
# 13. Em uma determinada faculdade, dado que um estudante não atingiu a média 7,0, este precisará fazer uma prova final. A nota mínima na avaliação final para que este estudante seja aprovado é dada pela seguinte fórmula: NF = (50 - Média x 6) ÷ 4. Assim, com base nessa informação desenvolva um programa que solicite três notas e caso esteja abaixo da média, calcule qual a nota mínima que o estudante precisa tirar na avaliação final para passar.
# 14. Um hotel cobra R$ 50,00 por diária acrescida de uma taxa de serviços. A taxa de serviços é de:
# R$ 4,00 por diária, se o número de diárias for menor que 5;
# R$ 3,60 por diária, caso contrário. De posse destas informações, construa um programa que solicite o número de diárias e informe o quanto deverá ser pago pelo hóspede.
# 15. No bairro do Janga existe uma lei que toda vez que um pescador traz um peso de peixes maior que o estabelecido pelo regulamento de pesca (50 quilos) deve pagar uma multa de R$4,00 por quilo excedente. A prefeitura precisa que você faça um programa que solicite o peso de certa quantidade de peixes e caso haja excesso de peso, mostre qual é este peso (em quilos) e quanto de multa deverá ser paga. Caso não haja excesso, deverá ser mostrada a mensagem “Parabéns por não ultrapassar o limite”.
# 16. Escreva um programa que implemente uma calculadora básica que realiza adição, subtração, multiplicação e divisão com base na escolha do usuário (solicita valor1, valor2, e operação).
# 17. Escreva um programa que solicita ao usuário um número e analise se o número é divisível por 2, por 3 e por 5. Imprima “O número é divisível por _”.