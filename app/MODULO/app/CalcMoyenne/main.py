nbr_note = input("Quel est le nombre de notes que vous avez ?")
note = 0

for i in range(int(nbr_note)):
    noteI = input("Entrer votre note : ")
    note =note+ float(noteI)

result = float(note)/int(nbr_note)
print(f"Vous avez {result} de moyenne.")