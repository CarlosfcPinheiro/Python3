#Conversor m(metros) para outra medida
v = float(input('digite um valor de distancia em metros:'))
print('a medida {}m corresponde a:'.format(v))
mm = v*1000
cm = v*100
dm = v*10
dam = v/10
hm = v/100
km = v/1000
print('{}mm'.format(mm))
print('{}cm'.format(cm))
print('{}dm'.format(dm))
print('{}dam'.format(hm))
print('{}hm'.format(hm))
print('{}km'.format(km))
