# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# unidade, dezena, centena e milhar

#forma matemática 
num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade {} \n Dezena {} \n Centena {} \n Milhar {}'.format(u, d, c, m))