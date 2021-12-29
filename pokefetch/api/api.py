import httpx
from typing import Dict, Union, Optional

class PokeInfo:
    def __init__(self, name_or_id) -> None:
        BASE_URL = "https://pokeapi.co/api/v2/"
        self.name_or_id = name_or_id
    
    def basic_info(self) -> Dict:
        data = httpx.get(self.BASE_URL + "pokemon/" + self.name_or_id).json()
        return data
