import turtle
import math

def draw_heart(size, color):
    """Matematiksel olarak düzgün bir kalp çizer."""
    pen = turtle.Turtle()
    pen.color(color)
    pen.fillcolor(color)
    pen.pensize(2)
    pen.speed(200)
    
    pen.begin_fill()
    for t in range(0, 360):  # 0'dan 360 dereceye kadar
        angle = math.radians(t)  # Açıları radyana çeviriyoruz
        x = size * math.sin(angle) ** 3  # X ekseni için denklem
        y = size * (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) / 16  # Y ekseni için denklem
        pen.goto(x, y)
    pen.end_fill()
    pen.hideturtle()

def draw_nested_hearts():
    """İç içe geçen düzgün kalpler çizer."""
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("İç İçe Geçen Kalpler")

    colors = ["red", "pink", "purple", "blue"]  # Kalplerin renkleri
    sizes = [200, 150, 100, 50]  # Kalplerin boyutları

    for size, color in zip(sizes, colors):
        pen = turtle.Turtle()
        pen.penup()
        pen.goto(0, -size / 2)  # Kalbi ortalamak için
        pen.pendown()
        draw_heart(size, color)

    screen.mainloop()

draw_nested_hearts()
