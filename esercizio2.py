nome = input("Come ti chiami? ")
anno_nascita = input("In che anno sei nato? ")
anno_nascita_numero = int(anno_nascita)

eta = 2026 - anno_nascita_numero

print(f"Nel 2026 avrai {eta} anni.")

# Ecco la parte nuova: la decisione
if eta >= 18:
    print("Sei maggiorene!")
else:
    print("Sei ancora minorenne!") 
   





