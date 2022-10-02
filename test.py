import pytest
from razas import *


class Test_unitariossetter():
    def test_crear(self):
        frodo = Hobbit()
        aragorn = Humano()
        gimbli = Enano()
        legolas = Elfo()
        gandalf = Mago()
        azog = Orco()

    def test_enano(self):
        gimbli = Enano()
        assert(isinstance(gimbli, Mortal))
        assert(isinstance(gimbli, MortalCodicioso))

        assert(gimbli.salud == 100)
        gimbli.salud = 50
        gimbli.beber()
        assert(gimbli.salud == 70)

        assert(gimbli.dinero == 10)
        gimbli.minar()
        assert(gimbli.dinero == 11)

        gimbli.codicia()
        assert(gimbli.salud == 60)
        assert(gimbli.dinero == 16)

    def test_hobbit(self):
        frodo = Hobbit()

        frodo.salud = 10

        frodo.comer()
        assert(frodo.salud == 100)

    def test_mago(self):
        frodo = Hobbit()
        aragorn = Humano()
        gimbli = Enano()
        legolas = Elfo()
        gandalf = Mago()
        azog = Orco()
        assert(not isinstance(gandalf, Mortal))
        gandalf.anadir_miembro_compania(frodo)
        gandalf.anadir_miembro_compania(aragorn)
        gandalf.anadir_miembro_compania(gimbli)
        gandalf.anadir_miembro_compania(legolas)

        assert(len(gandalf._compania) == 4)

    def test_properties(self):
        isinstance(Enano().salud, property)
        isinstance(Enano().dinero, property)


class Test_integracion():

    def test_orco(self):
        azog = Orco()
        gimbli = Enano()

        azog.atacar(gimbli)
        assert(gimbli.salud == 90)

    def test_humano(self):
        aragorn = Humano()
        assert(isinstance(aragorn, Mortal))
        assert(isinstance(aragorn, MortalCodicioso))

        assert(aragorn.salud == 100)
        aragorn._salud = 50
        aragorn.beber()
        assert(aragorn.salud == 60)

        assert(aragorn.dinero == 10)

        aragorn.codicia()
        assert(aragorn.salud == 50)
        assert(aragorn.dinero == 15)

        for i in range(11):
            aragorn.beber()
        assert(aragorn.salud == 100)

        gimbli = Enano()
        aragorn.atacar(gimbli)
        assert(gimbli.salud == 90)

    def test_elfo(self):
        legolas = Elfo()
        gimbli = Enano()

        assert(legolas.flechas == 10)
        legolas.recargar()
        legolas.disparar_flecha(gimbli)
        assert(gimbli.salud == 90)
        assert(legolas.flechas == 9)

    def test_sanar(self):
        legolas = Elfo()
        gandalf = Mago()
        legolas.salud -= 20
        gandalf.sanar(legolas)
        assert(legolas.salud == 100)


class Test_excepciones():

    def test_elfo_no_preparado(self):
        legolas = Elfo()
        gimbli = Enano()

        with pytest.raises(FlechaNoPreparada) as e:
            legolas.disparar_flecha(gimbli)
        assert e.type == FlechaNoPreparada

    def test_compania_sin_hobbit(self):
        frodo = Hobbit()
        aragorn = Humano()
        gimbli = Enano()
        legolas = Elfo()
        gandalf = Mago()
        azog = Orco()
        with pytest.raises(CompaniaSinHobbit) as e:
            gandalf.anadir_miembro_compania(aragorn)
        assert e.type == CompaniaSinHobbit

    def test_orco_compania(self):
        frodo = Hobbit()
        aragorn = Humano()
        gimbli = Enano()
        legolas = Elfo()
        gandalf = Mago()
        azog = Orco()
        gandalf.anadir_miembro_compania(frodo)
        with pytest.raises(OrcoEnCompania) as e:
            gandalf.anadir_miembro_compania(azog)
        assert e.type == OrcoEnCompania

    def test_properties(self):
        isinstance(Enano().salud, property)
        isinstance(Enano().dinero, property)
