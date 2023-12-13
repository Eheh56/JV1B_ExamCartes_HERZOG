
class Carte:

    def __init__(self, cout_mana, nom, description):
        self.__cout_mana = cout_mana
        self.__nom = nom
        self.__description = description
        print(self.__nom)
        print(self.__cout_mana)
        print(self.__description)

class Mage:
    def __init__(self, nom, pv, total_mana, mana_actuel,main,defausse,zdj):
        self.__nom = nom
        self.__pv = pv
        self.__total_mana = total_mana
        self.__mana_actuel = mana_actuel
        self.__main = main
        self.__defausse = defausse
        self.__zdj = zdj
    def jouer_carte(self):
        if Carte.__cout_mana <= self.__mana_actuel:
            self.__mana_actuel -= Carte.__cout_mana
            self.__main.remove(Carte)
            self.__zdj.append(Carte)
        else:
            print("Pas assez de mana pour jouer cette carte.")

    def recuperer_mana(self):
        self.__mana_actuel = self.__total_mana

class Cristal(Carte):

    def __init__(self, cout_mana, nom, description, valeur):
        Carte().__init__(cout_mana, nom, description)
        self.valeur = valeur

    def jouer(self):
        Mage.total_mana += self.valeur

