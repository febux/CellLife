
# Application for simulating cell selection
```text
This application is designed to simulate the behavior of cells in a population. 
The user can select from a variety of cell types, including empty cells, 
which represent the absence of a cell type, and energy, green, and red cells, 
which represent the different stages of a cell's life cycle.

The simulation is based on the concept of cellular automata, 
which is a mathematical model that describes how cells interact 
with each other and with their environment over time. 
In this simulation, the cells are represented as squares on a grid, 
and their behavior is determined by a set of rules that determine 
how cells change state based on the states of their neighboring cells.

This application is designed to be a tool for exploring the principles 
of cellular automata and to provide a visual representation 
of complex systems that can be difficult 
to understand through traditional mathematical models.
```

### Cells:

| Cell             | File                                                  | Description                                                                                                                                                                           |
|------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _Empty cells_    | [empty_cell.py](cells/cell_types/empty_cell.py)       | _Empty cells_ are default cells for showing nothing.                                                                                                                                  |
| _Energy cells_   | [energy_cell.py](cells/cell_types/energy_cell.py)     | _Energy cells_ are cells for storing energy which use for increasing cell lifecycle.                                                                                                  |
| _Dead cells_     | [dead_cell.py](cells/cell_types/dead_cell.py)         | _Dead cells_ are cells whose storing some energy and kinda just dead.                                                                                                                 |
| _Green cells_    | [green_cell.py](cells/cell_types/green_cell.py)       | _Green cells_ are casual cells whose consume energy cells <br/>and reproduce mostly green cells (unlikely can reproduce _Yellow cell_).                                               |
| _Yellow cells_   | [yellow_cell.py](cells/cell_types/yellow_cell.py)     | _Yellow cells_ are uncommon cells whose consume energy cells, live longer <br/>and reproduce mostly yellow cells (unlikely can reproduce _Orange cell_).                              |
| _Purple cells_   | [purple_cell.py](cells/cell_types/purple_cell.py)     | _Purple cells_ are super aggressive cells whose consume mostly green and yellow cells and less energy cells, <br/>reproduce mostly purple cells (unlikely can reproduce _Pink cell_). |
| _Red cells_      | [red_cell.py](cells/cell_types/red_cell.py)           | _Red cells_ are aggressive cells whose consume mostly green and yellow cells and less energy cells, <br/>reproduce mostly red cells (unlikely can reproduce _Purple cell_).           |
| _Dead Red cells_ | [dead_red_cell.py](cells/cell_types/dead_red_cell.py) | _Dead Red cells_ are kind of poison cells whose poison red, yellow and green cells, and reduce their energy.                                                                          |
| _Pink cells_     | [pink_cell.py](cells/cell_types/pink_cell.py)         | _Pink cells_ mega aggressive cells whose consume mostly green and yellow cells and less energy cells, <br/>reproduce only pink cells.                                                 |
| _Orange cells_   | [orange_cell.py](cells/cell_types/orange_cell.py)     | _Orange cells_ are rare cells whose consume energy cells, live even longer <br/>and reproduce only Orange cells.                                                                      |

## Installation

Cell Life requires [Pygame](https://www.pygame.org) v2+ to run.

Install the dependencies using poetry and start the app.

```sh
poetry install 
```
```sh
python main.py
```


## License

MIT
