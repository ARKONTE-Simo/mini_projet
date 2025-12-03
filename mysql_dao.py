import mysql.connector
from produit import Produit
from client import Client

CONFIG={"host":"localhost","user":"root","password":"pass","database":"boutique"}

def init_db():
    conn=mysql.connector.connect(**CONFIG)
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS produit(id INT PRIMARY KEY,nom VARCHAR(50),prix FLOAT)")
    c.execute("CREATE TABLE IF NOT EXISTS client(id INT PRIMARY KEY,nom VARCHAR(50),email VARCHAR(50))")
    conn.commit()
    conn.close()

def ajouter_produit(produit):
    conn=mysql.connector.connect(**CONFIG)
    c=conn.cursor()
    c.execute("INSERT INTO produit VALUES(%s,%s,%s)",(produit.id,produit.nom,produit.prix))
    conn.commit()
    conn.close()

def lister_produits():
    conn=mysql.connector.connect(**CONFIG)
    c=conn.cursor()
    c.execute("SELECT * FROM produit")
    rows=c.fetchall()
    conn.close()
    return [Produit(*r) for r in rows]

def ajouter_client(client):
    conn=mysql.connector.connect(**CONFIG)
    c=conn.cursor()
    c.execute("INSERT INTO client VALUES(%s,%s,%s)",(client.id,client.nom,client.email))
    conn.commit()
    conn.close()

def lister_clients():
    conn=mysql.connector.connect(**CONFIG)
    c=conn.cursor()
    c.execute("SELECT * FROM client")
    rows=c.fetchall()
    conn.close()
    return [Client(*r) for r in rows]

def chercher_client_email(email):
    conn=mysql.connector.connect(**CONFIG)
    c=conn.cursor()
    c.execute("SELECT * FROM client WHERE email=%s",(email,))
    row=c.fetchone()
    conn.close()
    if row:
        return Client(*row)
    return None

def modifier_prix(id,nouveau_prix):
    conn=mysql.connector.connect(**CONFIG)
    c=conn.cursor()
    c.execute("UPDATE produit SET prix=%s WHERE id=%s",(nouveau_prix,id))
    conn.commit()
    conn.close()
