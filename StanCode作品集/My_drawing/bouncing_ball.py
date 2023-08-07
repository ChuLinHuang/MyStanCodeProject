"""
File:bouncing_ball.py
Name:Chu-Lin Huang
-------------------------
TODO:
1. Creating a switch, when we turn on the switch, the animation will start
2. The animation should write in the main fun.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
ball.fill_color = 'black'
times = 0  # 計算次數
switch = 0  # 當作開關


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global switch, times
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(open_switch)

    while True:

        pause(200)

        if switch == 1:
            if times <= 2:
                times += 1
                vy = 0  # 初始最高點，y 方向初速為 0

                while True:
                    vy += GRAVITY  # Vt = V0 + at
                    ball.move(VX, vy)
                    pause(DELAY)
                    if (ball.y - SIZE) >= window.height:  # 球掉落超出視窗
                        if vy > 0:
                            vy = - (REDUCE * vy)  # 開始往上彈，vy 方向改變

                    if ball.x > window.width:  # 球超出視窗 x方向
                        window.remove(ball)  # 移除剛剛超出範圍的球
                        window.add(ball, x=START_X, y=START_Y)  # reset ball
                        switch = 0
                        break
            else:
                break


def open_switch(mouse):
    global switch
    switch = 1


if __name__ == "__main__":
    main()
