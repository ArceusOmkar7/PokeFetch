from typing import Union, Dict, List

class Pokemon:
    def __init__(self, data:Dict) -> None:
        self.data = data
    
    @property
    def name(self) -> str:
        return self.data.get("name")
    
    @property
    def id(self) -> int:
        return self.data.get("id")
    
    @property
    def height(self) -> int:
        return self.data.get("height")

    @property
    def forms(self) -> dict:
        return self.data.get("forms")
    
    @property
    def weight(self) -> int:
        return int(self.data.get("weight"))
    
    @property
    def forms(self) -> List[str]:
        if not self.data.get("forms"):
            return None
        return [data.get("name") for data in self.data.get("forms")]

    @property
    def moves(self) -> List[str]:
        if not self.data.get("moves"):
            return None
        return [
            (data.get("move").get("name")) for data in self.data.get("moves")
        ]
    
    @property
    def type(self) -> List[str]:
        if not self.data.get("types"):
            return None
        return [
            ((data.get("slot"), data.get("type").get("name")) for data in self.data.get("types"))
        ]