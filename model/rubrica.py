class rubrica:
    def __init__(self):
        self.contatto=[] #list

    def aggiungereContatto(self, nome, cognome, telefono):
        new_contatto = Contatto(nome, cognome, telefono)
        self.contatto.append(new_contatto)

    def rimuoviContatto(self, position):
        self.contatto.remove(self.contatto[position])


    def cercaContatto(self, key):
        #key=nome
        for i in self.contatto:
            if i.nome == key:
                return i
        pass

    def stampaContatto(self, position):
        print(self.contatto[position])


    def listaContatti(self):
        return self.contatto



class Contatto:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    def __str__(self):
        return self.nome + ' ' + self.cognome + ' ' + self.telefono
