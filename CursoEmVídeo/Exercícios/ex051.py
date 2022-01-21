#Prograssão Aritimética

first = int(input('Me informe o PRIMEIRO NÚMERO desta Progressão Aritimética (P.A): '))
reason = int(input('Agora, me informe a RAZÃO desta Progressão Aritimética (P.A): '))
last = first + (10 - 1)*reason
print('=-'* 20 + '=')
print('Esses são os dez primeiros números dessa Progressão Aritimética (P.A):')
for PA in range(first, last + reason, reason):
    print(PA, end=' ')