from tkinter import Tk, Canvas

FIRST_LINE_LEFT_X = 50
FIRST_LINE_TOP_Y = 50
FONT_SIZE = 12

def main():

    # Create the main window
    root = Tk()
    root.title("Haiku")

    #   Make a canvas
    canvas = Canvas(root, width=1000, height=1000, bg="white")
    canvas.pack()

    # Store the haiku lines in a list for easy iteration
    lines = [
        "An old silent pond...",
        "A frog jumps into the pond,",
        "splash! Silence again."
        ]

    # Start at the first line's y-coordinate
    y = FIRST_LINE_TOP_Y

    # Loop through the three lines
    for i in range(3):
        # Draw the -th line a t (FIRST_LINE_LEFT_X, y) with Courier font

        canvas.create_text(FIRST_LINE_LEFT_X, y, text=lines[i], font=("Courier", FONT_SIZE), anchor="w")
        # Increment by 30 pixels (font size + gap) to stack the next line
        y += 30

    root.mainloop() #   Start the event loop to display the window

if __name__ == '__main__':
    main()
