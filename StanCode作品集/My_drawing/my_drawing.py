"""
File:my_drawing.py
Name:Chu-Lin Huang
----------------------
TODO:Creating a Mario
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow


def main():
    """
    Title：My childhood

    Mario is one of my favorite games in my childhood. I hope that one day I can create some interesting games in
    the future
    """
    window = GWindow(800, 500)
    background = GRect(800, 500)
    background.filled = True
    background.fill_color = 'powderblue'
    window.add(background)

    hat = GRect(275, 80, x=250, y=10)
    hat.filled = True
    hat.fill_color = 'red'
    hat.color = 'red'
    window.add(hat)

    hat_b1 = GRect(30, 40, x=250, y=10)
    hat_b1.filled = True
    hat_b1.fill_color = 'powderblue'
    hat_b1.color = 'powderblue'
    window.add(hat_b1)

    hat_b2 = GRect(100, 40, x=430, y=10)
    hat_b2.filled = True
    hat_b2.fill_color = 'powderblue'
    hat_b2.color = 'powderblue'
    window.add(hat_b2)

    head = GRect(300, 130, x=250, y=90)
    head.filled = True
    head.fill_color = 'moccasin'
    head.color = 'moccasin'
    window.add(head)

    hair = GRect(60, 20, x=250, y=90)
    hair.filled = True
    hair.fill_color = 'saddlebrown'
    hair.color = 'saddlebrown'
    window.add(hair)

    hair2 = GRect(40, 60, x=210, y=110)
    hair2.filled = True
    hair2.fill_color = 'saddlebrown'
    hair2.color = 'saddlebrown'
    window.add(hair2)

    hair3 = GRect(20, 60, x=270, y=110)
    hair3.filled = True
    hair3.fill_color = 'saddlebrown'
    hair3.color = 'saddlebrown'
    window.add(hair3)

    hair4 = GRect(60, 40, x=210, y=170)
    hair4.filled = True
    hair4.fill_color = 'saddlebrown'
    hair4.color = 'saddlebrown'
    window.add(hair4)

    hair_b = GRect(60, 30, x=210, y=190)
    hair_b.filled = True
    hair_b.fill_color = 'powderblue'
    hair_b.color = 'powderblue'
    window.add(hair_b)

    eye = GRect(30, 45, x=430, y=90)
    eye.filled = True
    eye.fill_color = 'black'
    eye.color = 'black'
    window.add(eye)

    beard = GRect(100, 35, x=430, y=155)
    beard.filled = True
    beard.fill_color = 'black'
    beard.color = 'black'
    window.add(beard)

    beard2 = GRect(40, 20, x=460, y=135)
    beard2.filled = True
    beard2.fill_color = 'black'
    beard2.color = 'black'
    window.add(beard2)

    head_b1 = GRect(100, 20, x=480, y=90)
    head_b1.filled = True
    head_b1.fill_color = 'powderblue'
    head_b1.color = 'powderblue'
    window.add(head_b1)

    head_b2 = GRect(100, 20, x=535, y=110)
    head_b2.filled = True
    head_b2.fill_color = 'powderblue'
    head_b2.color = 'powderblue'
    window.add(head_b2)

    head_b3 = GRect(100, 70, x=530, y=155)
    head_b3.filled = True
    head_b3.fill_color = 'powderblue'
    head_b3.color = 'powderblue'
    window.add(head_b3)

    head_b4 = GRect(100, 70, x=510, y=192)
    head_b4.filled = True
    head_b4.fill_color = 'powderblue'
    head_b4.color = 'powderblue'
    window.add(head_b4)

    clothes = GRect(400, 150, x=180, y=220)
    clothes.filled = True
    clothes.fill_color = 'red'
    clothes.color = 'red'
    window.add(clothes)

    clothes_b = GRect(100, 15, x=140, y=220)
    clothes_b.filled = True
    clothes_b.fill_color = 'powderblue'
    clothes_b.color = 'powderblue'
    window.add(clothes_b)

    clothes_b2 = GRect(100, 15, x=120, y=235)
    clothes_b2.filled = True
    clothes_b2.fill_color = 'powderblue'
    clothes_b2.color = 'powderblue'
    window.add(clothes_b2)

    clothes_b3 = GRect(150, 15, x=450, y=220)
    clothes_b3.filled = True
    clothes_b3.fill_color = 'powderblue'
    clothes_b3.color = 'powderblue'
    window.add(clothes_b3)

    clothes_b4 = GRect(150, 15, x=550, y=235)
    clothes_b4.filled = True
    clothes_b4.fill_color = 'powderblue'
    clothes_b4.color = 'powderblue'
    window.add(clothes_b4)

    r_hand = GRect(50, 65, x=180, y=290)
    r_hand.filled = True
    r_hand.fill_color = 'moccasin'
    r_hand.color = 'moccasin'
    window.add(r_hand)

    r_hand2 = GRect(80, 15, x=185, y=305)
    r_hand2.filled = True
    r_hand2.fill_color = 'moccasin'
    r_hand2.color = 'moccasin'
    window.add(r_hand2)

    l_hand = GRect(50, 65, x=530, y=290)
    l_hand.filled = True
    l_hand.fill_color = 'moccasin'
    l_hand.color = 'moccasin'
    window.add(l_hand)

    l_hand2 = GRect(80, 50, x=495, y=305)
    l_hand2.filled = True
    l_hand2.fill_color = 'moccasin'
    l_hand2.color = 'moccasin'
    window.add(l_hand2)

    pants = GRect(230, 110, x=265, y=270)
    pants.filled = True
    pants.fill_color = 'mediumblue'
    pants.color = 'mediumblue'
    window.add(pants)

    clothes_b5 = GRect(50, 65, x=180, y=355)
    clothes_b5.filled = True
    clothes_b5.fill_color = 'powderblue'
    clothes_b5.color = 'powderblue'
    window.add(clothes_b5)

    clothes_b6 = GRect(80, 65, x=515, y=355)
    clothes_b6.filled = True
    clothes_b6.fill_color = 'powderblue'
    clothes_b6.color = 'powderblue'
    window.add(clothes_b6)

    pants2 = GRect(100, 80, x=230, y=320)
    pants2.filled = True
    pants2.fill_color = 'mediumblue'
    pants2.color = 'mediumblue'
    window.add(pants2)

    pants3 = GRect(100, 80, x=415, y=320)
    pants3.filled = True
    pants3.fill_color = 'mediumblue'
    pants3.color = 'mediumblue'
    window.add(pants3)

    pants4 = GRect(35, 50, x=310, y=220)
    pants4.filled = True
    pants4.fill_color = 'mediumblue'
    pants4.color = 'mediumblue'
    window.add(pants4)

    pants5 = GRect(35, 35, x=415, y=235)
    pants5.filled = True
    pants5.fill_color = 'mediumblue'
    pants5.color = 'mediumblue'
    window.add(pants5)

    button1 = GRect(35, 35, x=310, y=270)
    button1.filled = True
    button1.fill_color = 'yellow'
    button1.color = 'yellow'
    window.add(button1)

    button2 = GRect(35, 35, x=415, y=270)
    button2.filled = True
    button2.fill_color = 'yellow'
    button2.color = 'yellow'
    window.add(button2)

    r_shoes1 = GRect(70, 40, x=210, y=400)
    r_shoes1.filled = True
    r_shoes1.fill_color = 'saddlebrown'
    r_shoes1.color = 'saddlebrown'
    window.add(r_shoes1)

    r_shoes2 = GRect(100, 30, x=180, y=420)
    r_shoes2.filled = True
    r_shoes2.fill_color = 'saddlebrown'
    r_shoes2.color = 'saddlebrown'
    window.add(r_shoes2)

    l_shoes1 = GRect(70, 40, x=465, y=400)
    l_shoes1.filled = True
    l_shoes1.fill_color = 'saddlebrown'
    l_shoes1.color = 'saddlebrown'
    window.add(l_shoes1)

    l_shoes2 = GRect(100, 30, x=465, y=420)
    l_shoes2.filled = True
    l_shoes2.fill_color = 'saddlebrown'
    l_shoes2.color = 'saddlebrown'
    window.add(l_shoes2)


if __name__ == '__main__':
    main()
