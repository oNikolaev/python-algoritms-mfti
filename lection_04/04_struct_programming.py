# Структурное программирование
from common import ezgraphics as gr


def build_house(window, x, y, width):
    """Функция, которая рисует дом"""
    canvas = window.canvas()
    canvas.drawRectangle(x, y, width, width)
    window.wait()

win = gr.GraphicsWindow(300, 300)
win.setTitle("Russian game")

build_house(win, 100, 100, 100)