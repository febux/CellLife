import pygame as pg

from app.app import App
from constants import WIDTH, HEIGHT


def main():
    root = pg.display.set_mode((WIDTH, HEIGHT))
    app: App = App(root)
    app.run()


if __name__ == '__main__':
    main()
