# produit.py
class Produit:
    def __init__(self,id,nom,prix):
        self.id=id
        self.nom=nom
        self.prix=prix
    def __str__(self):
        return f"Produit({self.id},{self.nom},{self.prix})"