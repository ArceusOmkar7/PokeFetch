import httpx
from typing import Dict, Union, Optional
from .pokemon import Pokemon

class PokeFetch:
    def __init__(self) -> None:
        self.BASE_URL = "https://pokeapi.co/api/v2/"
    
    def get_pokemon(self, poke:Union[str, int]) -> Optional[Pokemon]:
        poke = str(poke).lower()

        try:
            data = httpx.get(self.BASE_URL + "pokemon" + poke).json()
            return Pokemon(data)
        except IndexError:
            raise "Pokemon Not Found"

    