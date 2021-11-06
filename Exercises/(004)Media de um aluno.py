#Esse programa irá pedir 4 médias bimestrais e irá calcular sua média
nota1 = float(input("Digite a primeira média do aluno: "))
nota2 = float(input("Digite a segunda média do aluno: "))
nota3 = float(input("Digite a terceira média do aluno: "))
nota4 = float(input("Digite a quarta média do aluno: "))
media = float((nota1 + nota2 + nota3 + nota4)/4)
print("Dado as médias {}, {}, {} e {}, a média total do aluno foi de {}".format(nota1, nota2, nota3, nota4, media))