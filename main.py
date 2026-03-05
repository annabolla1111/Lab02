import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("Seleziona un opzione: ").strip() #toglie lo spazio


    #controllo che sia un numero e basta
    if not txtIn.isdigit():
        print("Inserire un numero valido")
        continue

    # Add input control here!

    if int(txtIn) == 1:
        print("Inserire la parola e la traduzione da aggiungere:")
        entry = input()
        t.handleAdd(entry) #prima le gestisco e una volta gestite le aggiungo
    if int(txtIn) == 2:
        print("Inserisci la parola da cercare:")
        query = input()
        t.handleTranslate(query)
    if int(txtIn) == 3:
        print("Inserisci la parola con wildcard:")
        query = input()
        t.handleWildCard(query)
    if int(txtIn) == 5:
        t.stampaDizionario()
    if int(txtIn) == 4:
        print("Chiusura programma")
        break

