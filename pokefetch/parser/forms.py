from pokefetch.api.api import PokeInfo
from ..api.api import PokeInfo

class Forms:
    def __init__(self, pokemon_name) -> None:
        self.pokemon = pokemon_name
        self.pokemon = PokeInfo(self.pokemon_name)
    

    def pokemon_forms(self):
        return self.pokemon.get('forms')