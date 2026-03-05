class Dictionary:
    def __init__(self):
        self._dict = {}

    def addWord(self,parola,traduzioni):
        if parola in self._dict:
            for t in traduzioni: #aggiunge solo traduzioni nuove
                if t not in self._dict[parola]:
                    self._dict[parola].append(t) #la aggiungo al dizionario
        else:
            self._dict[parola] = list(traduzioni)

    def translate(self, parola):
        return self._dict.get(parola, None) #se uso get e il programma non trova la parola restituisce none e non si blocca
                #self._dict[parola] #se non trova la parola si blocca

    def translateWordWildCard(self,query):
        risultati = [] #ci puo essere piu di una parola

        for parola, traduzioni in self._dict.items():
            #devono avere la stessa lunghezza
            if len(parola) == len(query):
                corrisponde = True
                #confronto i caratteri
                for i in range(len(query)):
                    if query[i] != "?" and query[i] != parola[i]:
                        corrisponde = False
                        break
                if corrisponde:
                    risultati.append((parola, traduzioni)) #gli passo una tupla con le doppie parentesi
        return risultati


    def stampa(self):
        return self._dict