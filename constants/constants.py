from app___src.population import Population

CELL_SIZE = 5
FPS = 1000
WIDTH = 900
HEIGHT = 900
ENERGY_ITERATION_VALUE = 10

POPULATION: Population = Population(
    empty_cell__population=70,
    energy_cells__population=10,
    green_cells__population=10,
    red_cells__population=10,
)

