import turtle
import math

"""
Task 2: Recursion. Drawing the Pythagoras Tree Fractal
"""

def setup_turtle():
    """Sets up turtle screen and turtle object."""
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Pythagoras Tree - Fractal")
    screen.setup(width=1000, height=800)
    
    t = turtle.Turtle()
    t.speed(0)
    # Uniform color
    t.color("brown")
    # Thin lines
    t.pensize(2)
    t.hideturtle()
    
    return screen, t

def draw_pythagoras_tree(t, branch_length, level, angle=45):
    """
    Recursively draws a classic Pythagoras tree.

    Args:
        t: Turtle object
        branch_length: Length of the current branch
        level: Recursion depth
        angle: Branch angle (default 45°)
    """
    if level == 0:
        return

    # Draw the current branch
    t.forward(branch_length)
    
    # Save current state
    position = t.pos()
    heading = t.heading()
    
    # Left branch
    t.left(angle)
    left_length = branch_length * math.cos(math.radians(angle))
    draw_pythagoras_tree(t, left_length, level - 1, angle)
    
    # Restore position and heading
    t.setpos(position)
    t.setheading(heading)
    
    # Right branch
    t.right(angle)
    right_length = branch_length * math.sin(math.radians(angle))
    draw_pythagoras_tree(t, right_length, level - 1, angle)

    # Restore again
    t.setpos(position)
    t.setheading(heading)

def main():
    """Main program."""
    # Ask user for recursion level (must be 3–10)
    level = 0
    while not (3 <= level <= 10):
        try:
            user_input = input("Enter recursion level (3-10): ")
            level = int(user_input)
            if not (3 <= level <= 10):
                print("Level must be between 3 and 10.")
        except ValueError:
            print("Please enter a valid integer between 3 and 10.")

    # Setup turtle
    screen, t = setup_turtle()
    
    # Initial positioning
    t.penup()
    t.goto(0, -300)
    t.setheading(90)
    t.pendown()
    
    # Initial branch length
    initial_length = max(80, 150 - level * 5)
    
    print(f"Drawing Pythagoras Tree at recursion level {level}...")
    draw_pythagoras_tree(t, initial_length, level)
    
    # Exit on click
    screen.exitonclick()
    print("Done.")

# Usage
if __name__ == "__main__":
    main()
