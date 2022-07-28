class Sanita:
    def __init__(self):
        self.dottori = {}
        self.pazienti = {}

    def aggiungiDottore(self, nome, cognome, codiceFiscale, matricola):
        new_doctore = Dottore(nome,cognome, codiceFiscale, matricola)
        self.dottori[matricola] = new_doctore
        return

    def aggiungiPaziente(self, nome, cognome, codiceFiscale, codicePaziente):
        new_pazienti = Paziente(nome, cognome, codiceFiscale, codicePaziente)
        self.pazienti[codicePaziente] = new_pazienti
        return

    # restituisce il paziente dato il codice
    def getPaziente(self, codicePaziente):
        return self.pazienti.get(codicePaziente)

    # restituisce il medico data la matricola
    def getDottore(self, matricola):
        return self.dottori.get(matricola)

    # assegna un aziente a un medico
    def assegnaMedico(self, matricola, codice):
        add_dottore = self.dottori.get(matricola)
        add_paziente = self.pazienti.get(codice)
        self.pazienti.get(codice).add_dottore(add_dottore)
        self.dottori.get(matricola).add_patiente(add_paziente)
        return

    # restituisce una stringa contenente l'elenco dei pazienti assegnati a un medico
    def getPazienti(self, matricola):
        list_doc = self.dottori.get(matricola).list_patient()
        vis=""
        for i in list_doc:
            vis = vis+str(i)+","
        return vis

    # salva sul file pazienti.txt l'elenco dei pazienti
    def salvaPazienti(self):
        f = open("patient.txt", "w")
        for i in self.pazienti.values():
            f.write(str(i)+"\n")
        return

# sia il dottore che il paziente hanno come attributo nome cognome e codice fiscale
# il paziente ha un codice univoco e il dottore una matricola


class Dottore:
    def __init__(self, nome, cognome, codiceFiscale, matricola):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale
        self.pazienti = []

    def add_patiente(self,paziente):
        self.pazienti.append(paziente)

    def list_patient(self):
        return self.pazienti

    def __str__(self):
        return self.nome + ' ' + self.cognome + ' ' + self.codiceFiscale


class Paziente:
    def __init__(self, nome, cognome, codiceFiscale, codice):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale
        self.dottori = []

    def add_dottore(self,dottore):
        self.dottori.append(dottore)

    def list_doc(self):
        return self.dottori

    def __str__(self):

        return self.nome + ' ' + self.cognome + ' ' + self.codiceFiscale
