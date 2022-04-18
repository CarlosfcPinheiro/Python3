#Analisando Tupla de times

teams = ('São Paulo', 'Coritiba', 'Corinthians', 'Atlético-MG', 'Ceará', 'Avaí', 'Cuibá', 'Juventude', 'Red Bull Bragantino', 'Flamengo', 'Atlético-GO', 'Santos', 'Fluminense', 'Palmeiras', 'Fortaleza', 'América-MG', 'Botafogo', 'Internacional', 'Goiás', 'Athletico-PR')
print('Lista de times no Brasileirão:')
count = 1
for t in teams:
    print(f'{count}º {t}')
    count += 1
print('=-'*40+'=')
print(f'5 primeiros colocados: {teams[0:5]}')
print('=-'*40+'=')
print(f'Os 4 últimos colocados: {teams[-4:20]}')
print('=-'*40+'=')
print(f'Times em ordem alfabética: {sorted(teams)}')
print('=-'*40+'=')
ind = teams.index('Flamengo')
print(f'Posição do time da Flamengo: {ind+1}ª posição')


