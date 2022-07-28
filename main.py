from model.rubrica import *
import mysql.connector
from model.sanita import *


connection = mysql.connector.connect(host='localhost',
                                         database='palestra',
                                         user='root',
                                         password='root')


#rubrica test

contatti = rubrica()
contatti.aggiungereContatto("Bolivar","boli", "5555")
contatti.aggiungereContatto("Arsene","arse", "2222")
b=contatti.listaContatti()
for i in b:
    print(i.telefono)
contatti.rimuoviContatto(0)
b=contatti.listaContatti()
for i in b:
    print(i)



#Sanita test

sanita = Sanita()

sanita.aggiungiDottore("bolivar","arsene","codiceFiscale",2039)
sanita.aggiungiDottore("bobo","gean","codiceFiscale1",2045)
sanita.aggiungiDottore("made","sees","codiceFiscale2",2023)
sanita.aggiungiPaziente("nugu","web","fiscalcodice1",1009)
sanita.aggiungiPaziente("elge","debe","fiscalcodice2",1065)
sanita.aggiungiPaziente("zcbe","mbuito","fiscalcodice3",1098)

sanita.assegnaMedico(2039,1009)
print(sanita.getPazienti(2039))
print(sanita.getDottore(2039))
print(sanita.getPaziente(1009))
sanita.salvaPazienti()