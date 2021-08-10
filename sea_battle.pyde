from main import Main

main = None

def setup():
    size(1024, 800)
    rectMode(CENTER)
    textAlign(CENTER)
    textSize(24)
    global main
    main = Main()


def draw():
    background(255,255,255)
    main.run()


def mousePressed():
    main.touch_to()
