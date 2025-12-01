#Esercizio Casting

#Punto 1 (input del numero intero)
try:
    scelta = int(input("Inserisci un numero: "))

    #Punto 2 (Casting numero intero in float)

    num_decimale = float(scelta)

    print(f"Il decimale del numero scelto è: {num_decimale}")
    
    #Punto 3 (stampa il numero con un messaggio)
    print(f"Hai inserito la stringa {str(scelta)}")

#Eccezione al ValueError con frase personalizzata
except ValueError:
    print("ERRORE! Devi inserire un numero intero!")







