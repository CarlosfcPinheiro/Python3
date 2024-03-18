#First name and surname.2

fn = str(input('Digite seu primeiro nome: ').strip().lower())
sn = str(input('Digite seu sobrenome: ').strip().lower())

fullname = fn.title() + ' ' + sn.title()

print((f'\nNOME COMPLETO: {fullname}'))

