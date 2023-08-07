"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    num_lives = 0

    # Add the animation loop here!
    while True:
        pause(200)

        switch = graphics.get_switch()
        if num_lives < 3:
            if switch == 1:
                vx = graphics.get_vx()
                vy = graphics.get_vy()
                while True:
                    num_bricks = graphics.get_num_bricks()
                    if num_bricks == 100:  # 當磚塊完全消除時，終止動畫
                        break
                    ball_x1 = graphics.ball.x
                    ball_y1 = graphics.ball.y
                    ball_x2 = graphics.ball.x + graphics.ball.width
                    ball_y2 = graphics.ball.y + graphics.ball.height
                    ball_lt = graphics.window.get_object_at(ball_x1, ball_y1)  # 球的左上角
                    ball_rt = graphics.window.get_object_at(ball_x2, ball_y1)  # 球的右上角
                    ball_lb = graphics.window.get_object_at(ball_x1, ball_y2)  # 球的左下角
                    ball_rb = graphics.window.get_object_at(ball_x2, ball_y2)  # 球的右下角
                    graphics.ball.move(vx, vy)
                    pause(FRAME_RATE)

                    # 設定球打擊到視窗上、左、右 以及 paddle 時會反彈
                    if ball_x1 <= 0:
                        if vx < 0:
                            vx = - vx
                    elif ball_x2 >= graphics.window.width:
                        if vx > 0:
                            vx = -vx
                    elif ball_y1 <= 0:
                        if vy < 0:
                            vy = - vy

                    # 球掉出界線，遊戲重新開始
                    elif ball_y2 >= graphics.window.height:
                        if num_lives <= 2:
                            num_lives += 1
                            graphics.window.remove(graphics.ball)
                            graphics.restart_game()
                            break
                        else:
                            graphics.window.remove(graphics.ball)

                    # 球的四個角落是否有打擊到磚塊
                    if ball_lt is not None:
                        if ball_lt is not graphics.paddle:
                            graphics.window.remove(ball_lt)
                            graphics.check_bricks()  # 確認磚塊是否全部消除
                            if vy < 0:  # 修改球會穿透磚塊的 bug
                                vy = - vy
                        else:
                            if vy > 0:
                                vy = - vy
                    else:
                        if ball_rt is not None:
                            if ball_rt is not graphics.paddle:
                                graphics.window.remove(ball_rt)
                                graphics.check_bricks()  # 確認磚塊是否全部消除
                                if vy < 0:  # 修改球會穿透磚塊的 bug
                                    vy = - vy
                            else:
                                if vy > 0:
                                    vy = - vy
                        else:
                            if ball_lb is not None:
                                if ball_lb is not graphics.paddle:
                                    graphics.window.remove(ball_lb)
                                    graphics.check_bricks()  # 確認磚塊是否全部消除
                                    if vy > 0:  # 修改球會穿透磚塊的 bug
                                        vy = - vy
                                else:
                                    if vy > 0:
                                        vy = - vy
                            else:
                                if ball_rb is not None:
                                    if ball_rb is not graphics.paddle:
                                        graphics.window.remove(ball_rb)
                                        graphics.check_bricks()  # 確認磚塊是否全部消除
                                        if vy > 0:  # 修改球會穿透磚塊的 bug
                                            vy = - vy
                                    else:
                                        if vy > 0:
                                            vy = - vy

        else:
            graphics.game_over()
            break


if __name__ == '__main__':
  main()
