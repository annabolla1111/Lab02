from dictionary import Dictionary
class Translator:

    def __init__(self):
        self.dictionary = Dictionary()


    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("Traduttore")
        print("-----------------------")
        print("1. Aggiungi nuova parola \n","2. Cerca una traduzione \n","3. Cerca con wildcard \n", "5. Stampa dizionario \n", "4. Exit", sep="") #per non stampare lo spazio a capo
        print("-----------------------")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        #uso prop chiave-valore
        try:
            with open(dict, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip() #toglie spazi e ritorni a capo a inizio e fine linea
                    if line != "":
                        campi = line.split(" ")
                        if len(campi) >= 2: #possono esserci piu traduzioni
                            parola = campi[0].strip() #tolgo \n
                            traduzione = campi[1]

                            self.dictionary.addWord(parola, [traduzione])

        except FileNotFoundError:
            print("File not found")





    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        #nel main faccio inserire la parola
        parti = entry.lower().split() #metto il minuscolo
        if len(parti) < 2:
            print("Errore")
            return

        aliena = parti[0]
        traduzioni = parti[1:]

        #inserisco nel dizionario
        self.dictionary.addWord(aliena, traduzioni)
        print("Inserimento avvenuto")

        #inserisco nel file
        try:
            with open("dictionary.txt", "a", encoding="utf-8") as file: #"a" sta per append aggiunge dopo l'ultima riga
                stringa_traduzioni = " ".join(traduzioni)  #devo usare join per aggiungere alla lista di traduzioni
                line = "\n" + aliena + " " + stringa_traduzioni
                file.write(line)
            print("Inserimento in file")
        except Exception as e:
            print(f"Errore: {e}")



    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.lower().strip() #toglie spazi vuoti e mette il minuscolo
        risultato = self.dictionary.translate(query)
        if risultato:
            res = ", ".join(risultato) #tolgo il contenitore
            print(f"Traduzione di {query}: {res}")
        else:
            print("Parola non trovata")

            #problema se ho gia parola salvata sul file me la duplica


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        query = query.lower().strip()
        if query.count("?") != 1: #se ce piu di un ?
            print("Errore: solo un punto interrogativo")
            return
        risultati = self.dictionary.translateWordWildCard(query)

        if risultati:
            print(f"Risultati per {query}")
            for parola, traduzioni in risultati:
                stringa_traduzioni = ", ".join(traduzioni)
                print(f"{parola} -> {stringa_traduzioni}")
        else:
            print("Nessuna parola trovata")

        pass

    def stampaDizionario(self):
        data = self.dictionary.stampa()
        #ordine alfabetico
        for parola in sorted(data.keys()):
            traduzioni = ", ".join(data[parola]) #per stampare il contenuto della lista di traduzioni
            print(f"{parola}: {traduzioni}")
