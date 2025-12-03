from produit import Produit
from client import Client
import sqlite_dao as dao  # ou mysql_dao

dao.init_db()
dao.ajouter_produit(Produit(1,"Stylo",1.5))
dao.ajouter_produit(Produit(2,"Cahier",3.0))
dao.ajouter_client(Client(1,"Alice","alice@mail.com"))

for p in dao.lister_produits():
    print(p)
for c in dao.lister_clients():
    print(c)

c=dao.chercher_client_email("alice@mail.com")
print("Recherche email:",c)

dao.modifier_prix(1,2.0)
for p in dao.lister_produits():
    print("Apres modification:",p)
