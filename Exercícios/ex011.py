print('==== Pintando a parede ====')
b = float(input('Qual a largura da parede?(m) '))
h = float(input('Qual a altura da parede?(m) '))
A = float(b*h)
res = float(A/2)
print(f'A área da sua parede é de {A:.2f}m².\nE a quantidade de tinta necessária para pinta a parede é de {res:.1f}(l) (1l=2m²).')
