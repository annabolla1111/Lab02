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
        print("1. Aggiungi nuova parola \n","2. Cerca una traduzione \n","3. Cerca con wildcard \n","4. Exit", sep="") #per non stampare lo spazio a capo
        print("-----------------------")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        #uso prop chiave-valore
        try:
            with open(dict, "r", encoding="utf-8") as file:
                for line in file:
                    if line != "":
                        campi = line.split(" ")
                        if len(campi) >= 2: #possono esserci piu traduzioni
                            parola = campi[0]
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

        self.dictionary.addWord(aliena, traduzioni)
        print("Inserimento avvenuto")



    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.lower().strip() #toglie spazi vuoti e mette il minuscolo

        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

