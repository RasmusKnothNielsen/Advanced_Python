import turtle, tkinter

turtle.setup(1920, 1080, 0, 0)

canvas = turtle.Screen()
escher = turtle.Turtle()
escher.speed(5)

#instructions = "FF+F-FF--FF+FF+F+FF++FFFFFF-F-F+"
instructions = "UBBBBBBDF-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++"

for task in instructions:
    if task == "F":
        escher.forward(25)
    elif task == "B":
        escher.backward(25)
    elif task == "U":
        escher.penup()
    elif task == "D":
        escher.pendown()
    elif task == "+":
        escher.right(45)
    elif task == "-":
        escher.left(45)

tkinter.mainloop()