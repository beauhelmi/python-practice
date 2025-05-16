from tkinter import Tk, Canvas

"""
Draw a square which has dimensions THIS_BIG by THIS_BIG
Each side of the square is THIS_BIG pixels long centered at CENTER_X, CENTER_Y
"""

THIS_BIG = 144
CENTER_X = 160
CENTER_Y = 160

def main():
    root = Tk()
    root.title('THIS big')

    # Make a canvas
    canvas = Canvas(root, width=400, height=300, bg="white")
    canvas.pack()

    # Calculate coordinates
    left_x = CENTER_X - THIS_BIG / 2
    top_y = CENTER_Y - THIS_BIG / 2
    right_x = CENTER_X + THIS_BIG / 2
    bottom_x = CENTER_Y + THIS_BIG / 2

    # Draw the square with fill keywords
    canvas.create_rectangle(left_x, top_y, right_x, bottom_x, fill="blue")

    root.mainloop() #   Start the event loop to display the window

if __name__ == '__main__':
    main()


