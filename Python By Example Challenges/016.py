#It's raining

rain = str(input('Está chovendo? ').strip().upper())

if (rain == 'SIM'):
    print('\nÉ bom pegar um guarda-chuva :)')
    windy = str(input('Agora me diga se está ventando: ').strip().upper())
    if (windy == 'SIM'):
        print('\nTalvez seja melhor ficar em casa -_-')

elif (rain == 'NÃO') or (rain == 'NAO'):
    print('\nAproveite seu dia :D')
