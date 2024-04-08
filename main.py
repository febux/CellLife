import pygame as pg

from app import App
from constants.constants import WIDTH, HEIGHT


def main():
    root = pg.display.set_mode((WIDTH, HEIGHT))
    app: App = App(WIDTH, HEIGHT, root)
    app.run()


if __name__ == '__main__':
    main()
