from collections import defaultdict
from typing import List
from pandas import read_csv
from Fortuna import random_value


class StrainData:
    """ Primary Data Object for MedCab """

    def __init__(self, filename):
        self.data = read_csv(filename).to_dict(orient='records')

        self.effect_lookup = defaultdict(list)
        self.flavor_lookup = defaultdict(list)
        self.type_lookup = defaultdict(list)

        for strain in self.data:
            self.type_lookup[strain['Type']].append(strain['Strain'])
            strain['Effects'] = strain['Effects'].split(',')
            for effect in strain['Effects']:
                self.effect_lookup[effect].append(strain['Strain'])
            strain['Flavors'] = strain['Flavors'].split(',')
            for flavor in strain['Flavors']:
                self.flavor_lookup[flavor].append(strain['Strain'])

        self.name_lookup = {obj['Strain']: obj for obj in self.data}

    def random_strain(self) -> dict:
        """ Returns a random Strain

        @return: dict
        """
        return random_value(self.data)

    def effects_list(self) -> List[str]:
        """ List of all Effects

        @return: List[str]
        """
        return list(self.effect_lookup.keys())

    def types_list(self) -> List[str]:
        """ List of all Types

        @return: List[str]
        """
        return list(map(lambda s: s.title(), self.type_lookup.keys()))

    def flavors_list(self) -> List[str]:
        """ List of all Flavors

        @return: List[str]
        """
        return list(self.flavor_lookup.keys())

    def strain_by_id(self, idx: str) -> dict:
        """ Strain lookup by Index

        @param idx: str
        @return: dict
        """
        return self.data[int(idx)]

    def strain_by_name(self, name: str) -> dict:
        """ Strain lookup by Name

        @param name: str
        @return: dict
        """
        return self.name_lookup[name]

    def strains_by_type(self, strain_type: str) -> List[dict]:
        """ List of Strains of the desired Type

        @param strain_type: str
        @return: List[str]
        """
        return self.type_lookup[strain_type]

    def strains_by_rating(self, rating: str) -> List[str]:
        """ List of Strains of the desired Rating or higher

        @param rating: str
        @return: List[str]
        """
        return list()

    def strains_by_effect(self, effect: str) -> List[str]:
        """ List of Strains that produce the desired Effect

        @param effect: str
        @return: List[str]
        """
        return self.effect_lookup[effect]

    def strains_by_flavor(self, flavor: str) -> List[str]:
        """ List of Strains that have the desired Flavor

        @param flavor: str
        @return: List[str]
        """
        return self.flavor_lookup[flavor]
