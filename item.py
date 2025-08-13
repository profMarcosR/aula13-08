class Item:
    def __init__(self, nome, id, local, valor):
        self.nome = nome
        self.id = id
        self.local = local
        self.valor = valor



mesa = Item("mesa", 123, "lab_211", 500)
print(mesa.id)


