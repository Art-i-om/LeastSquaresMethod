from dataclasses import dataclass, field

@dataclass()
class Chocolate:
    brand: str
    tasty: str
    volume_mg: float
    texture: str
    appearance: str
    cost: str
    density: str

@dataclass()
class Programming:
    language: str
    paradigm: str
    favourite_framework: str
    lines_written: int = 0
    caffeine_mg: int = 0
    bugs_introduced: int = 0
    bugs_fixed: int = 0
    started_year: int = 2025
    enthusiasm: float = 1.0
