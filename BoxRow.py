from tkinter import Tk, Canvas


CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():

    #   Create the main window
    root = Tk()
    root.title("Haiku")

        #   Make a canvas
    canvas = Canvas(root, width=1000, height=1000, bg="white")
    canvas.pack()


    
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT / 2, "white", "black")
    for i in range(N_BOXES):
        left_x = i * BOX_SIZE
        top_y = CANVAS_HEIGHT / 2
        right_x = (i + 1) * BOX_SIZE
        bottom_y = CANVAS_HEIGHT
        
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "white", "black")
    
    
