#First name and Surname

fn = str(input('Digite o seu primeiro nome: ').strip().lower())
sr = str(input('Agora digite o seu sobrenome: ').strip().lower())

fullname = fn.upper() + ' ' + sr.upper()

print((f'\nNOME COMPLETO: {fullname}'))
print(f'NÚMERO DE LETRAS: {len(fullname.replace(" ", ""))}')