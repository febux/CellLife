
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

The simulation can be run in either real-time or time-lapse mode, 
and the user can adjust the speed of the simulation, 
as well as the size of the grid and the number of cells in the population. 

The simulation also includes an option to save a screenshot 
of the simulation at regular intervals.

This application is designed to be a tool for exploring the principles 
of cellular automata and to provide a visual representation 
of complex systems that can be difficult 
to understand through traditional mathematical models.
```

### Cells:

| Cell             | File                                       | Description                                                                                                                                                                |
|------------------|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _Empty cells_    | [empty_cell.py](cells/empty_cell.py)       | _Empty cells_ are default cells for showing nothing.                                                                                                                       |
| _Energy cells_   | [energy_cell.py](cells/energy_cell.py)     | _Energy cells_ are cells for storing energy which use for increasing cell lifecycle.                                                                                       |
| _Dead cells_     | [dead_cell.py](cells/dead_cell.py)         | _Dead cells_ are cells whose storing some energy and kinda just dead.                                                                                                      |
| _Green cells_    | [green_cell.py](cells/green_cell.py)       | _Green cells_ are casual cells whose consume energy cells <br/>and reproduce mostly green cells (unlikely can reproduce _Yellow cell_).                                    |
| _Yellow cells_   | [yellow_cell.py](cells/yellow_cell.py)     | _Yellow cells_ are uncommon cells whose consume energy cells, live longer <br/>and reproduce only yellow cells.                                                            |
| _Purple cells_   | [purple_cell.py](cells/purple_cell.py)     | _Purple cells_ are super aggressive cells whose consume mostly green and yellow cells and unlikely energy cells, <br/>reproduce only purple cells.                              |
| _Red cells_      | [red_cell.py](cells/red_cell.py)           | _Red cells_ are aggressive cells whose consume mostly green and yellow cells and unlikely energy cells, <br/>reproduce mostly red cells (unlikely can reproduce _Purple cell_). |
| _Dead Red cells_ | [dead_red_cell.py](cells/dead_red_cell.py) | _Dead Red cells_ are kind of poison cells whose poison red, yellow and green cells, and reduce their energy.                                                               |

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