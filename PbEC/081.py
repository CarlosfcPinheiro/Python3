#Favorite subject

subject = str(input("Qual sua matéria favorita: ").strip().title())
count = 0
for c in subject:
    count += 1
    if (count == len(subject)):
        print(f"{c}", end=" ")
    else:
        print(f"{c}", end="-")