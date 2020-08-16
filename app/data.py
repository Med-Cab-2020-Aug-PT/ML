import pandas as pd
from random import choice


class GetData:

    def __init__(self, filename):
        self.data = pd.read_csv(
            filename,
        ).to_dict(orient='records')

        for row in self.data:
            row['Effects'] = eval((row['Effects']))
            row['Flavors'] = eval((row['Flavors']))

        self.name_lookup = {obj['Strain']: obj for obj in self.data}

    def recommendation(self):
        return choice(self.data)

    def strain_by_id(self, idx: int) -> dict:
        return self.data[idx]

    def strain_by_name(self, name: str) -> dict:
        return self.name_lookup[name]
