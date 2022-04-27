#Analisando expressões matemáticas

par1 = [] #(
par2 = [] #)
allpar = [] #evita um primeiro ')'
exp = str(input('Digite uma expressão matemática (SOMENTE COM PARÊNTESES): '))
for c in exp:
    if c == '(':
        par1.append(c)
        allpar.append(c)
    elif c == ')':
        par2.append(c)
        allpar.append(c)
if (len(par1) == len(par2)) and allpar[0] != ')':
    print('\033[0;34mESSA EXPRESSÃO É VÁLIDA.')
else:
    print('\033[0;31mESSA EXPRESSÃO É INVÁLIDA.')