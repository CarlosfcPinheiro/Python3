#Mostrando Sequência de Fibonacci

print('{0}SEQUÊNCIA DE FIBONACCI{0}'.format('=-'*10 + '='))
terms = int(input('Me diga quantos termos você deseja ver dessa sequência: '))
count = 3
t1 = 0
t2 = 1
print('{0} - {1}'.format(t1, t2), end='')
while count != terms:
    t3 = t1 + t2
    print(' - {0}'.format(t3), end='')
    count += 1
    t1 = t2
    t2 = t3
print('- FIM')