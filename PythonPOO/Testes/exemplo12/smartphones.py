from eletronicos import Eletronicos
from log import LogMixin

class smartphone(Eletronicos, LogMixin):

    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f"{self._nome} NÃO ESTÁ LIGADO"
            print(info)
            self.info(info)
            return
        
        if self._conectado:
            error = f"{self._nome} JÁ ESTÁ CONECTADO"
            print(error)
            self.error(error)
            return

        self._conectado = True
        info = f"{self._nome} CONECTADO COM SUCESSO"
        print(info)
        self.info(info)

    def desconectar(self):
        if not self._ligado:
            error = f"{self._nome} NÃO ESTÁ LIGADO"
            print(error)
            self.error(error)
            return
        
        if not self._conectado:
            error = f"{self._nome} JÁ ESTÁ DESCONECTADO"
            print(error)
            self.error(error)
            return

        self._conectado = False
        info = f"{self._nome} DESCONECTADO COM SUCESSO"
        print(info)
        self.info(info)

