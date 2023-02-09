from abc import ABC, abstractmethod


class AnimalSavannah(ABC):

    def __init__(self, strain, living_aria):
        """
        :param strain: received species group
        :param living_aria: where animal lives
        """
        self.__strain = strain
        self._living_aria = living_aria

    @abstractmethod
    def print_species_food(self):
        pass

    @abstractmethod
    def print_living_temperature(self):
        pass

    def print_strain(self):
        print(self.__strain)

    def fact(self):
        return "The creatures that live in the savannah are unique and varied. Some species are not found in other " \
               "climatic regions. "


class Lion(AnimalSavannah, ABC):
    def __init__(self):
        super(Lion, self).__init__("Strain: cats.", "Lions live in savannah.")

    def print_species_food(self):
        print("Lions eat meat.")

    def print_living_temperature(self):
        print("Lions prefer temperature around 24 degrease")

    def print_living_aria(self):
        print(self._living_aria)


class Zebra(AnimalSavannah, ABC):
    def __init__(self):
        super(Zebra, self).__init__("Strain: artiodactyls.", "Zebras live in savannah.")

    def print_species_food(self):
        print("Zebra eat grow.")

    def print_living_temperature(self):
        print("Zebra prefer temperature around 20 degrease")

    def print_living_aria(self):
        print(self._living_aria)

    def fact(self):
        basefact = super().fact()
        return f"{basefact}Animals in these regions suffer greatly from human activities. Livestock grazing destroys " \
               f"vegetation, " \
               "turning the savannah into a desert. The number of animals is greatly reduced by strong fires. "


if __name__ == "__main__":
    lion = Lion()
    lion.print_species_food()
    lion.print_living_aria()
    lion.print_living_temperature()
    lion.print_strain()
    print(lion.fact())

    zebra = Zebra()
    zebra.print_species_food()
    zebra.print_living_aria()
    zebra.print_living_temperature()
    zebra.print_strain()
    print(zebra.fact())
