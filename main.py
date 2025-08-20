import sys

from utils.lsm import LSM as LifeSession
from utils.bootstrap import run as enjoy
from utils.memory import Chocolate, Programming

chocolates = [Chocolate(
    brand="snickers",
    tasty="Say that again!",
    volume_mg=40,
    texture="smooth",
    appearance="dark, milk, childhood vibes",
    cost="beyond price",
    density="affects mouthfeel"
)
    for _ in range(15)]

programming = Programming(
    language="Brainfuck",
    paradigm="Metaprogramming",
    favourite_framework="Unity",
    lines_written=sys.maxsize,
    caffeine_mg=-1,
    bugs_introduced=sys.maxsize,
    bugs_fixed=0,
    started_year=2021,
    enthusiasm=100
)

life = LifeSession()
enjoy(life.including(programming, chocolates))