# 1. Escreva um programa que peça dois números do usuário e exiba a soma deles.
# (Saída deve ser “A soma é _____”).
# 2. Escreva um programa que leia três números do usuário e exiba a média deles
# (Saída deve ser “A média é _____”).
# 3. Escreva um programa que leia o raio de um círculo e calcule sua área (Saída deve
# ser “A área é _____”).
# 4. Escreva um programa que leia a largura e a altura de um retângulo e calcule seu
# perímetro (Saída deve ser “O perímetro é _____”).
# 5. Escreva um programa que leia a largura e altura de um retângulo e calcule sua
# área (Saída deve ser “A área é _____”).
# 6. Escreva um programa que solicite do usuário a distância em km e o consumo de
# gasolina (em km/litro) e informe a quantidade de litros que ele utilizará para
# percorrer essa distância (Saída deve ser “Serão utilizados _____ litros”).
# 7. Escreva um programa que leia um número de horas e converta para minutos
# (Saída deve ser “____ horas equivale a _____ minutos”).
# 8. Escreva um programa que leia um número de dias e converta para horas (Saída
# deve ser “___ dias equivale a _____ horas”).
# 9. Escreva um programa que leia uma distância de quilômetros e a converta para
# milhas. (1 quilômetro = 0.621371 milhas) (Saída deve ser “___ km equivale a
# _____ milhas”).
# 10. Escreva um programa que leia um valor e um percentual de aumento e exiba o
# novo valor após o aumento(Saída deve ser “o salário antes do aumento era de
# _____, após o aumento de ____ resultou no salário final de ____”).
# 11. Escreva um programa que leia um valor e um percentual de desconto e exiba o
# valor após aplicar o desconto (Saída deve ser “o valor antes do aumento era de
# _____, após o desconto de ____ resultou no valor final de ____”).
# 12. Escreva um programa que leia a largura de um cubo (em metros) e calcule qual
# a sua capacidade de volume (Saída deve ser “o cubo possui ___ metros de
# comprimento e tem uma capacidade de ___ metros cúbicos” ).
# 13. Escreva um programa que leia o salário mensal de um usuário e calcule o salário
# anual (A saída deve ser “o salário mensal é de ___ e o anual é ___”).
# Questões antigas:
# 14. Você foi contratado por uma loja para criar um programa que calcula o preço
# final de um produto após um desconto. O programa deve ler o preço original do
# produto (reais e centavos) e a porcentagem de desconto.
# Fuctura Tecnologia
# Curso: Python- Módulo1
# Professor: Márcio Barros
# Email: profmarcioluan@gmail.com
# 15. Você foi contratado por um banco para criar um programa que converte um
# valor em reais para dólares. O programa deve ler o valor em reais e a cotação do
# dólar no momento.
# 16. Você foi contratado por uma empresa de nutrição para criar um programa que
# calcula o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve ler o
# peso (em kg) e a altura (em metros) da pessoa. O IMC é dado pelo peso dividido
# pela altura ao quadrado peso / (altura **2).
# 17. Você foi contratado por uma escola para criar um programa que calcula a média
# aritmética de 3 notas fornecidas pelo usuário.
# 18. Você foi contratado por um banco para realizar um sistema de saque onde o
# usuário deve digitar o saldo inicial e em seguida o valor a ser sacado. O programa
# deve retornar o saldo final.
# 19. Uma concessionária de motos revende uma moto acrescidos 26% referidos a
# impostos, 2% referente ao seguro, 8% do lucro da revendedora e 1% da comissão
# do vendedor. Sabendo-se que estas porcentagens são calculadas com relação ao
# preço de fábrica (preço que a revendedora compra a moto), desenvolva um
# programa que calcule o preço de venda desta moto na concessionária.
# 20. No bairro do Janga-PE existe uma empresa que fabrica tonéis cilíndricos de aço
# que são utilizados para armazenar água. Cada tonel produzido possui uma tampa
# lisa feita do mesmo material do tonel. Sabendo que a empresa gasta R$ 2,50 para
# pintar um m2 desta tampa com um tipo especial de tinta, desenvolva um
# programa que solicite as medidas desta tampa e a quantidade de tampas a serem
# pintadas e informe ao usuário quanto a empresa irá gastar para pintá-las.
# 21. Desenvolva um programa que calcule os gastos com combustível em uma
# viagem. O programa deve solicitar ao usuário a distância a ser percorrida em
# km, o consumo do carro em km/litro e o preço do litro do combustível. Como
# resposta o programa deverá informar qual o valor em R$ a ser gasto com
# combustível na viagem.
# 22. Para se produzir um determinado tipo de fertilizante, uma fábrica precisa
# misturar três partes de Nitrogênio (N), duas partes de Potássio (K) e uma parte
# de Fósforo (P). De posse dessa informação, desenvolva um programa que
# solicite como informação uma determinada quantidade (em Kg) deste
# fertilizante e informe ao usuário a quantidade (em Kg) necessária de Nitrogênio,
# Potássio e Fósforo para a mistura.
# 23. Faça um programa que calcule o volume de água em metros cúbicos de
# piscinas retangulares. Solicite do usuário os valores de comprimento, altura e
# largura e retorne o volume. (Volume= comprimento * largura * altura).



# ** QUESTÃO 1 **

# 1. Escreva um programa que peça dois números do usuário e exiba a soma deles.
# (Saída deve ser “A soma é _____”).

# # === Base ===
# # pedir num1
# #       num2
# # somar num1 e num2
# # print resultado

# # === Entrada de Dados ===

# num1 = float (input ( 'Insira um Numero:'))
# num2 = float ( input ( 'Insira o Segundo Numero'))


# # === Processamento === 

# soma = num1 + num2

# #  === Saída de Dados ===

# print (f' A soma é {soma}')

# *************************************************************************************

# ** QUESTÃO 2 **
# 2. Escreva um programa que leia três números do usuário e exiba a média deles
# (Saída deve ser “A média é _____”).

# ==Base==
# pedir num1
# pedir num2
# pedir num3
# somar num1 num2 num3 dividir 3

# # ==ENTRADA DE DADOS==

# num1 = int ( input ('Digite o PRIMEIRO Número da média: '))
# num2 = int ( input ('Digite o SEGUNDO Número da média: '))
# num3 = int ( input (' Digite o TERCEIRO Número da média: '))


# # ==PROCESSAMENTO==

# media = ( num1 + num2 + num3 ) / 3


# # ==SAÍDA DE DADOS==
# print (f' A média é: {media}')

# *****************************************************************************************

# **  QUESTÃO 3 **
# 3. Escreva um programa que leia o raio de um círculo e calcule sua área (Saída deve
# ser “A área é _____”).

# == BASE ==
#        RAIO= ?

# # ==ENTRADA DE DADOS==

# raio = float ( input ('Insira a medida do Raio: '))

# # ==PROCESSAMENTO==

# area_circulo = 3.14 * ( raio **2)

# # == SAÍDA DE DADOS ==

# print (f' A área é {area_circulo}')

# ** Questão 4 **
# Escreva um programa que leia a largura e a altura de um retângulo e calcule seu
# perímetro (Saída deve ser “O perímetro é _____”).

# ==BASE==
# PEDIR LARGURA
# PEDIR ALTURA
# CALCULAR PERIMETRO

# # ==ENTRADA DE DADOS ==
# print ('Todas nossos calculos serão em METROS')
# largura =  float (input ('Digite a LARGURA: '))
# altura =  float (input ('Digite a ALTURA: '))

# # ==PROCESSAMENTO ==
# perimetro = (largura * 2) + (altura * 2)

# # ==SAÍDA DE DADOS==

# print (f' O perimetro é {perimetro}')

# ** QUESTAO 5 **

# 5. Escreva um programa que leia a largura e altura de um retângulo e calcule sua
# área (Saída deve ser “A área é _____”).

# == BASE ==
# PEDIR ALTURA
# PEDIR LARGURA
# CALCULAR AREA =largura *altura
# # 

# # ENTRADA DE DADOS ==
# print ('Todas as medidas serão calculadas em METROS')
# altura = float ( input ('Por Favor digite a ALTURA: '))
# largura = float (input ('Por Favor digite a Largura: '))

# # ==PROCESSAMENTO ==
# area = altura * largura

# # ==SAÍDA DE DADOS ==
# print (f'  A área é {area} m² ')

# ****************************************************************************

# ** QUESTÃO 6 **

#  6. Escreva um programa que solicite do usuário a distância em km e o consumo de
# gasolina (em km/litro) e informe a quantidade de litros que ele utilizará para
# percorrer essa distância (Saída deve ser “Serão utilizados _____ litros”).

# # # == BASE ==
# # DISTANCIA = ? INSERIR
# # quanto consome pro km rodado = ? INSERIR
# # LITROS CONSUMIDO =? CALCULAR

# # == ENTRADA DE DADOS ==
# distancia = float ( input ( 'Digite a Distancia em QUILOMETROS a percorrer: '))
# media = float ( input ( 'Digite a quantos Quilometros por litro seu Automóvel faz: '))

# # == PROCESSAMENTO ==
# consumo = float (distancia / media)

# # == SAÍDA DE DADOS ==
# print (f' Você vai usar {consumo} litros de combustível.')

# **************************************************************************************************

# ** QUESTÃO 7 **
#  7. Escreva um programa que leia um número de horas e converta para minutos
# (Saída deve ser “____ horas equivale a _____ minutos”).

# # == BASE ==
# # PEDIR QNT HORAS
# # CONVERTER HORAS MINUTOS

# # == ENTRADA DE DADOS ==
# horas = float (input ('Insira quantas HORAS deseja converter: '))


# # == PROCESSAMENTO ==
# horas_minutos = horas * 60

# # == SAÍDA DE DADOS ==
# print (f' {horas} horas equivale a {horas_minutos} minutos. ')

# ** QUESTÃO 8 **

# 8. Escreva um programa que leia um número de dias e converta para horas (Saída
# deve ser “___ dias equivale a _____ horas”)

# # == BASE ==
# # PEDIR QNT DE DIAS
# # CONVERTER DIAS EM HORAS 1D = 24HORAS 
# #  
# # == ENTRADA DE DADOS==
# dia = float (input ('Digite a quantidade de Dia(s):'))


# # == PROCESSAMENTO DE DADOS ==
# horas = dia * 24

# # == SAÍDA DE DADOS ==
# print (f' {dia} dias equivale a {horas} horas. ')

# ** QUESTÃO 9 **
# 9. Escreva um programa que leia uma distância de quilômetros e a converta para
# milhas. (1 quilômetro = 0.621371 milhas) (Saída deve ser “___ km equivale a
# _____ milhas”).

# == BASE ==
# PEDIR DISTANCIA EM KM
# CONVERTER KM INSERIDO EM MILHAS

# # == ENTRADA DE DADOS ==
# km = float ( input ( 'Digite quantos KM vai converter para milhas: '))

# # == PROCESSAMENTO ==
# km_milhas = km * 0.621371                                                                   olhar esse aqui

# # == SAÍDA DE DADOS ==

# print (f' {km} equivale a {km_milhas} milhas.')

# ****************************************************

# **QUESTÃO 10 **
# 10. Escreva um programa que leia um valor ee um percentual de aumento e exiba o
# novo valor após o aumento(Saída deve ser “o salário antes do aumento era de
# _____, após o aumento de ____ resultou no salário final de ____”).

# == BASE ==
# DIGITE O VALOR
# DIGITE PERCENTUAL DE AUMENTO
# VALOR DEPOIS DO AUMENTO

# == ENTRADA DE DADOS ==

# salario = float ( input (' Digite o valor do Salário : '))
# percentual_aumento = float ( input ( ' Digite o valor do percentual de aumento: '))

# # == PROCESSAMENTO ==
 
# novo_salario = salario * (percentual_aumento / 100 ) + salario

# # == SAÍDA DE DADOS ==

# print (f' O sarário antes do aumento era de {salario}, 
# após o aumento de {percentual_aumento}% resultou no salário final de {novo_salario}. ')


# ********************************************************************************************

# ** QUESTÃO 11**

# == BASE ==


# == ENTRADA DE DADOS ==
# == PROCESSAMENTO DE DADOS ==
# == SAÍDA DE DADOS ==

#  **QUESTÃO 20**

# 20. No bairro do Janga-PE existe uma empresa que fabrica tonéis cilíndricos de aço
# que são utilizados para armazenar água. Cada tonel produzido possui uma tampa
# lisa feita do mesmo material do tonel. Sabendo que a empresa gasta R$ 2,50 para
# pintar um m2 desta tampa com um tipo especial de tinta, desenvolva um
# programa que solicite as medidas desta tampa e a quantidade de tampas a serem
# pintadas e informe ao usuário quanto a empresa irá gastar para pintá-las.

# # ==Base==
# # GASTO POR TAMPA M2 DE TAMPA -2,50
# # SOLICITA MEDIDAS DE TAMPA
# # QUANTIDADE DE TAMPA

# # ==ENTRADA DE DADOS==
# custo_m2 = 2.5
# raio = float ( input ('Digite o raio da tampa a ser pintada em metros : '))
# qnt_tampa = int ( input (' Digite a quantidade de Tampa a ser pintada:  '))

# # ==PROCESSAMENTO DE DADOS==
# area_circulo =  float ( 3.14 * raio**2 )
# custo_final = area_circulo * custo_m2 * qnt_tampa

# # # == SAÍDA DE DADOS==

# print  (f' O custo para pintar cada tampa foi: {custo_final :.2f} ')

