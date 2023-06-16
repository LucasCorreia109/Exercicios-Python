from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem cosseno de {:.2f}'.format(angulo, cosseno))
tagente = tan(radians(angulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tagente))