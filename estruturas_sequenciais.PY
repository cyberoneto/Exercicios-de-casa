# ESTRUTURAS SEQUENCIAIS

# •	Estruturas Sequenciais
# 1.	Faça um Programa que mostre a mensagem "Alo mundo" na tela.
# 2.	Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# 3.	Faça um Programa que peça dois números e imprima a soma.
# 4.	Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# 5.	Faça um Programa que converta metros para centímetros.
# 6.	Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# 7.	Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# 8.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# 9.	Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# 	C = 5 * ((F-32) / 9).
# 10.	Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# 11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1.	o produto do dobro do primeiro com metade do segundo .
# 2.	a soma do triplo do primeiro com o terceiro.
# 3.	o terceiro elevado ao cubo.
# 12.	Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
# 13.	Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# 0.	Para homens: (72.7*h) - 58
# 1.	Para mulheres: (62.1*h) - 44.7
# 14.	João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
# 15.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# 0.	salário bruto.
# 1.	quanto pagou ao INSS.
# 2.	quanto pagou ao sindicato.
# 3.	o salário líquido.
# 4.	calcule os descontos e o salário líquido, conforme a tabela abaixo:Obs.: Salário Bruto - Descontos = Salário Líquido.
# 5.	+ Salário Bruto : R$
# 6.	- IR (11%) : R$
# 7.	- INSS (8%) : R$
# 8.	- Sindicato ( 5%) : R$
# 9.	= Salário Liquido : R$
# 16.	Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# 17.	Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# 	Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# 	comprar apenas latas de 18 litros;
# 	comprar apenas galões de 3,6 litros;
# 	misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# 18.	Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*


# **QUESTAO 1**
# Faça um Programa que mostre a mensagem "Alo mundo" na tela

# print ('Alô Mundo')

# ***************************************************************************************

# ** QUESTAO 2 **
# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

#  == Base ==

#  == Entrada de Dados ==
# numero =  float (input ( 'Por Favor Digite UM NUMERO' ))

#  == Processamento ==

#  == Saída De Dados ==
# print (f' O número informado foi {numero}')

# ******************************************************************************

# ** QUESTAO 3 **
# Faça um Programa que peça dois números e imprima a soma.

# numero1 = float (input ('Por Favor Digite o Primeiro Numero'))
# numero2 = float ( input ('Digite o Segundo Numero'))
# total = numero1 + numero2

# print (f' A Soma dos Numeros é {total}')

# ****************************************************************************************

# **QUESTAO 4 **
# 4.	Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# print (' Bom Dia Professor, informe a notas do aluno para saber a média')

# nota1 = float ( input ('DIgite a Primeira nota'))
# nota2 = float ( input ('DIgite a Segunda nota'))
# nota3 = float ( input ('DIgite a Terceira nota'))
# nota4 = float ( input ('Digite a Quarta nota'))
# media = (nota1 + nota2 + nota3 + nota4)/4

# print (f'A Média do Aluno foi {media}')


# ** QUESTAO 5**

# # 5.	Faça um Programa que converta metros para centímetros.

# metros = float (input ('Digite a Unidade em METROS, que Deseja Convertem em Centimentros'))
# centimetros = metros * 100

# print (f' {metros} é equivalente à {centimetros} CM')

# *******************************************************************

# **QUESTAO 6**

# 6.	Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#  RESUMO A =Pi X R AO QUADRADO

# raio =  int (input('Digite o Valor do Raio'))
# area = 3.14 *( raio**2)

# print (f' o valor da aréa do circulo é {area}')



# **QUESTAO 7**
# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# largura = float (input('Digite a Largura'))
# altura = float (input('Digite a Altura'))
# area = largura * altura
# dobro_area = area * 2

# print (f' O Dobro da Área digitada é {dobro_area}')

# ****************************************************************************************************************************

# ** QUESTAO 8 **

# 8.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

# valorhora = float (input ('Qual o Valor da Sua HORA de Trabalho?'))
# qnthoratrabalhada = float (input('Trabalha Quantas HORAS por Mes?'))
# resultado_valorhora_X_qnthora = valorhora * qnthoratrabalhada


# print (f' O Valor à receber é {resultado_valorhora_X_qnthora}')


# ***************************************************************************************************

# **Questão 9**

# 9.	Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# # 	C = 5 * ((F-32) / 9).

# para colocar o simbolo de Graus é ALT 0176

# fahrenheit = float (input ('Digite a Temperatura que Deseja Converter'))
# celsius =  5 * (fahrenheit - 32) / 9


# print ( f' (O Valor da Conversão Fica em {celsius})')


# *******************************************************************************

# **QUESTAO 10**

# 10.	Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.

# celsius = float (input ('Digite a Temperatura em Celsius'))
# c = {celsius}
# fahrenheit =  {c} = 5 * (F-32) / 9
# print ({fahrenheit})

# # Solicita a temperatura em Celsius
# celsius = float(input("Digite a temperatura em graus Celsius: "))

# # Converte a temperatura para Fahrenheit
# fahrenheit = (celsius * 9/5) + 32

# # Exibe o resultado
# print(f"A temperatura de {celsius}°C corresponde a {fahrenheit}°F.")


# ***************************************************************************************

# **Questao 11**

# # 11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# # 1.	o produto do dobro do primeiro com metade do segundo .
# # 2.	a soma do triplo do primeiro com o terceiro.
# # 3.	o terceiro elevado ao cubo.

# #Solicita os Números ao Usuario
# inteiro1 = int ( input ('Digite um Número inteiro: '))
# inteiro2 = int ( input ('Digite um Número inteiro: '))
# real= float (input ('Digite um Número Real: '))

# # Calculo
# resposta1 = (inteiro1 * 2) * (inteiro2 / 2)
# resposta2 = (inteiro1 * 3 ) + real
# resposta3 = real**3

# # Respostas
# print (f'A resposta 1 é: {resposta1}')
# print (f'A resposta 2 é: {resposta2}')
# print (f'A resposta 3 é: {resposta3}')


# ***************************************************************************************************

# # ** QUESTAO 12**

# #  12.	Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que 
# # calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

# # Solicita Dados da Pessoa
# altura = float (input ('Digite sua Altura:'))

# #  Solução 
# peso_ideal = (72.7 * altura) - 58

# # resultado

# print (peso_ideal)

# *******************************************************************************

# **Questao 13**

# ***********************************************************************************
# **Questao 14 **

# 14.	João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#  Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

# === Base ===

# === Entrada de Dados ===



# === Processamento === 



#  === Saída de Dados ===




