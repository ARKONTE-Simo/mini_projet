import sqlite3
from produit import Produit
from client import Client

DB="boutique.db"

def init_db():
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS produit(id INTEGER PRIMARY KEY,nom TEXT,prix REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS client(id INTEGER PRIMARY KEY,nom TEXT,email TEXT)")
    conn.commit()
    conn.close()

def ajouter_produit(produit):
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("INSERT INTO produit VALUES(?,?,?)",(produit.id,produit.nom,produit.prix))
    conn.commit()
    conn.close()

def lister_produits():
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("SELECT * FROM produit")
    rows=c.fetchall()
    conn.close()
    return [Produit(*r) for r in rows]

def ajouter_client(client):
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("INSERT INTO client VALUES(?,?,?)",(client.id,client.nom,client.email))
    conn.commit()
    conn.close()

def lister_clients():
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("SELECT * FROM client")
    rows=c.fetchall()
    conn.close()
    return [Client(*r) for r in rows]

def chercher_client_email(email):
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("SELECT * FROM client WHERE email=?",(email,))
    row=c.fetchone()
    conn.close()
    if row:
        return Client(*row)
    return None

def modifier_prix(id,nouveau_prix):
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("UPDATE produit SET prix=? WHERE id=?",(nouveau_prix,id))
    conn.commit()
    conn.close()
