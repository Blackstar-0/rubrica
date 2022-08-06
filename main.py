from model.rubrica import *

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