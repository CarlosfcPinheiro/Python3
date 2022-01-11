#Tabuada 2.0

num = (int(input('Digite de que número você deseja ver a tabuada: ')))
print('=-'*6 + '=')
for count in range(1, 11):
    print('{0} x {1} = {2}'.format(num, count, (num*count)))
print('=-'*6 + '=')