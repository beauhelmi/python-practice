from tkinter import Tk, Canvas

"""
An exercise project to work with graphics.
Creates small rectangles across the canvas with:
1. Color gradient from blue to red.
2. 5px spacing between squares.
3. Index number centered in each square.
"""

def main():
    # Create the main window
    root = Tk()
    root.title("Gradient Squares")

    # Make a canvas
    canvas = Canvas(root, width=300, height=300, bg="white")
    canvas.pack()

    # Make 20 squares with gradient, 5px spacing, and index numbers
    for i in range(20):
        # Calculate position with 5px spacing
        value = i * 15  # 10px for square width + 5px gap

        # Create color gradient from blue to red
        t = i / 19  # Normalize to [0, 1] over 20 squares
        r = int(0 + t * 255)  # Red: 0 to 255
        g = 0                 # Green: stays 0
        b = int(255 - t * 255)  # Blue: 255 to 0
        color = f"#{r:02x}{g:02x}{b:02x}"  # Format as #RRGGBB

        # Coordinates for rectangle
        left_x = value
        top_y = value
        right_x = value + 10  # 10px square
        bottom_y = value + 10

        # Create rectangle (use fill=color instead of positional color)
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill=color, outline=color)

        # Create index number centered in square
        center_x = (left_x + right_x) / 2
        center_y = (top_y + bottom_y) / 2
        canvas.create_text(center_x, center_y, text=str(i), font=("Arial", 8), fill="white")

        # Print index for debugging
        print(i)

    # Start the main event loop
    root.mainloop()

if __name__ == '__main__':
    main()
