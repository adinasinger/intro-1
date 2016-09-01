import turtle
window = turtle.Screen()
window.bgcolor("green")


def draw_square(new_turtle):
    for x in range(0, 4):
        new_turtle.pendown()
        new_turtle.right(90)
        new_turtle.forward(150)


def main():
    # create an instance of Turtle
    fred = turtle.Turtle()

    # set values on attributes in the Turtle module
    fred.shape("turtle")
    fred.turtlesize(stretch_wid=4,stretch_len=4, outline=2)
    fred.color("yellow", "purple")  # outline color, fill color
    fred.penup()
    fred.setx(150)

    # create another instance of Turtle and set its values
    ginger = turtle.Turtle()
    ginger.shape("turtle")
    ginger.turtlesize(stretch_wid=4,stretch_len=4, outline=2)
    ginger.color("blue")
    ginger.penup()
    ginger.setx(-150)

    # draw one square filled with color with the fred instance
    fred.begin_fill()
    draw_square(fred)
    fred.end_fill()

    # draw offset squares in a loop with the ginger instance
    for x in range(0, 50):
        draw_square(ginger)
        ginger.right(50)
        draw_square(fred)
        fred.left(50)

    window.exitonclick()


if __name__ == '__main__':
    main()

