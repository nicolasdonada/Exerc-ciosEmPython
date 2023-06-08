class BancoDeDados:

    def __init__(self):
        self.__dados = {}

    def lista_adicionar(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def mostrar_lista(self):
        for id, nome in self.__dados["clientes"].items():
            print(f"ID: {id}\nNOME: {nome}")

bd = BancoDeDados()
bd.lista_adicionar(1, "Nicolas")
bd.mostrar_lista()
