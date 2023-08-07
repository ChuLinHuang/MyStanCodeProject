"""
File:draw_line.py
Name:Chu-Lin Huang
-------------------------
TODO:
1. When mouse clicks, create a start point(a small circle).
2. Creating a variable 'times' in global. The 'times' is 1 in original.
3. In the fun, the first click will create start point (times +1), and the second click will create a line and remove
the start point (times = 1)
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

new_window = GWindow(800, 500, 'New Window')
SIZE = 10
start_point = GOval(SIZE, SIZE)
times = 1
x = 0
y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(build_line)


def build_line(mouse_click):
    global times, x, y
    if times % 2 != 0:
        new_window.add(start_point, mouse_click.x - SIZE / 2, mouse_click.y - SIZE / 2)
        times += 1
        x = mouse_click.x - SIZE / 2
        y = mouse_click.y - SIZE / 2

    else:
        line = GLine(x, y, mouse_click.x - SIZE / 2, mouse_click.y - SIZE / 2)
        new_window.add(line)
        new_window.remove(start_point)
        times = 1


if __name__ == "__main__":
    main()
