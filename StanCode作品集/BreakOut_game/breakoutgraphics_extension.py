"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 5    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
SPEED_UP = 1.2

# Variable
switch = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space

        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width/2-paddle_width/2), y=(self.window_height-paddle_offset))

        # Center a filled ball in the graphical window
        self.ball_size = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width/2-ball_radius/2), y=(self.window_height/2-ball_radius/2))

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmouseclicked(self.ball_move)
        onmousemoved(self.paddle_move)

        # Create Scoreboard
        self.scoreboard = GLabel("Score: 0")
        self.scoreboard.font = '-20'
        self.window.add(self.scoreboard, x=0, y=self.window_height)

        # Create lives reminder
        self.lives_remind = GLabel('Lives: 3')
        self.lives_remind.font = '-20'
        self.window.add(self.lives_remind, x=self.window_width - 90, y=self.window_height)

        # 新增的變數
        self.num_bricks = 0
        self.switch = 0
        self.lives = 3

        # Draw bricks
        for col in range(brick_cols):
            for row in range(brick_rows):
                self.bricks = GRect(width=brick_width, height=brick_height)
                self.bricks.filled = True
                if row < 2:
                    self.bricks.fill_color = 'red'
                elif 2 <= row < 4:
                    self.bricks.fill_color = 'orange'
                elif 4 <= row < 6:
                    self.bricks.fill_color = 'yellow'
                elif 6 <= row < 8:
                    self.bricks.fill_color = 'green'
                else:
                    self.bricks.fill_color = 'blue'

                self.window.add(self.bricks, x=(brick_width+brick_spacing) * col,
                                y=brick_offset+(brick_height+brick_spacing) * row)

    def paddle_move(self, mouse_move):
        if mouse_move.x <= self.paddle.width/2:
            self.window.add(self.paddle, x=0, y=self.paddle.y)
        elif mouse_move.x >= (self.window.width - (self.paddle.width/2)):
            self.window.add(self.paddle, x=self.window.width-self.paddle.width, y=self.paddle.y)
        else:
            self.window.add(self.paddle, x=(mouse_move.x - PADDLE_WIDTH/2), y=self.paddle.y)

    def ball_move(self, mouse_click):
        self.switch = 1

    def get_switch(self):
        return self.switch

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def restart_game(self):
        self.window.add(self.ball, x=(self.window_width/2-self.ball_size/2), y=(self.window_height/2-self.ball_size/2))
        self.switch = 0

    def game_over(self):
        game_over = GLabel("Game Over !")
        game_over.font = '-30'
        self.window.add(game_over, x=(self.window_width/2 - 90), y=(self.window_height/2))

    def check_bricks(self):
        self.num_bricks += 1
        self.window.remove(self.scoreboard)
        self.scoreboard = GLabel('Score: ' + str(self.num_bricks))
        self.scoreboard.font = '-20'
        self.window.add(self.scoreboard, x=0, y=self.window_height)
        if self.num_bricks == BRICK_COLS * BRICK_ROWS:  # 消除完全部磚塊
            win = GLabel("You Win !")
            win.font = '-30'
            self.window.add(win, x=(self.window_width/2 - 70), y=(self.window_height/2))

    def get_num_bricks(self):  # 取得目前已消除的磚塊數量
        return self.num_bricks

    def speedup(self):
        speed_up = GLabel("Speed UP !")
        speed_up.font = '-30'
        self.window.add(speed_up, x=(self.window_width/2 - 70), y=(self.window_height/2))
        self.__dx *= SPEED_UP
        self.__dy *= SPEED_UP
        pause(550)
        self.window.remove(speed_up)

    def live_reminder(self):
        self.lives -= 1
        self.window.remove(self.lives_remind)
        self.lives_remind = GLabel('Lives: ' + str(self.lives))
        self.lives_remind.font = '-20'
        self.window.add(self.lives_remind, x=self.window_width - 90, y=self.window_height)

    def get_live(self):
        return self.lives
