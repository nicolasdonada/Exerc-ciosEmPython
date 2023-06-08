class Cachorro:
    def latir(self):
        print('au au au')


class Pessoa:
    def afagar_animal(self, animal):
        animal.latir()


roberto = Pessoa()
rex = Cachorro()
roberto.afagar_animal(rex)