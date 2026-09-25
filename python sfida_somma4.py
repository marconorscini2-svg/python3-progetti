# 1.Chiedo i numeri
n1 = input("8: ")
n2 = input("7: ")
# 2. Trasformo le parole in numeri veri e propri
n1_numero = int(n1)
n2_numero = int(n2)
# 3. Faccio la somma
somma = n1_numero + n2_numero
# 4. Stampo il risultato
print(f"La somma è: {somma}")
if somma > 100:
    print("Accidenti, che numero grande! ")
else:
    print("Potevi fare di meglio, Che numero piccolo! ")
 