from app___src.population import Population

CELL_SIZE = 5
FPS = 100
WIDTH = 900
HEIGHT = 900

POPULATION = Population(
    empty_cell__population=300,
    energy_cells__population=10,
    green_cells__population=20,
    red_cells__population=20,
).to_tuple()

