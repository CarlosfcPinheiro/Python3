#Password

password = str(input("Digite uma senha: ").strip())
attempt = str(input("Digite sua senha novamente: ").strip())

if (password == attempt):
    print("Obrigado :)")
elif (password.lower() == attempt.lower()):
    print("Elas devem estar no mesmo caso.")
else:
    print("\nVocê digitou sua senha errado.")
