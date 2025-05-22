from tkinter import Tk, Canvas
import random


CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():

    #   Create the main window
    root = Tk()
    root.title("Random Circles")

        #   Make a canvas
    canvas = Canvas(root, width=300, height=300, bg="white")
    canvas.pack()

    for i in range(N_CIRCLES):
        draw_random_circles(canvas)

    root.mainloop()


def draw_random_circles(canvas):
    left_x = random.randint(0, CANVAS_WIDTH)
    top_y = random.randint(0, CANVAS_HEIGHT)
    right_x = left_x + CIRCLE_SIZE
    bottom_y = top_y - CIRCLE_SIZE
    color = random_color()

    canvas.create_oval(left_x,top_y,right_x,bottom_y, fill=color)




def random_color():
    colors = ['blue', 'purple', 'salmon','lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)


if __name__ == '__main__':
    main()
