from dataclasses import dataclass
@dataclass
class State:
    id: str
    name: str
    capital: str
    lat : float
    lng:  float
    area: int
    population: int
    neighbors: str

def __str__(self):
    return f""