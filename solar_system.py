import math
import turtle


def create_planet(name, color, distance, size, speed, tilt=1.0):
    turtle_obj = turtle.Turtle()
    turtle_obj.shape("circle")
    turtle_obj.color(color)
    turtle_obj.shapesize(size)
    turtle_obj.penup()
    return {
        "name": name,
        "turtle": turtle_obj,
        "distance": distance,
        "size": size,
        "speed": speed,
        "angle": 0,
        "tilt": tilt,
    }


def draw_starfield(screen):
    stars = turtle.Turtle()
    stars.hideturtle()
    stars.speed(0)
    stars.penup()
    stars.color("white")
    for _ in range(120):
        x = random.randint(-450, 450)
        y = random.randint(-320, 320)
        stars.goto(x, y)
        stars.dot(2)


def main():
    screen = turtle.Screen()
    screen.bgcolor("#020611")
    screen.setup(1100, 800)
    screen.title("Realistic Solar System")
    screen.tracer(0)

    draw_starfield(screen)

    sun = turtle.Turtle()
    sun.shape("circle")
    sun.color("yellow")
    sun.shapesize(3.0)
    sun.penup()

    orbit_turtles = []
    for planet in [
        ("Mercury", "#8c8c8c", 70, 0.35, 0.09, 0.95),
        ("Venus", "#d78b2d", 110, 0.55, 0.06, 0.98),
        ("Earth", "#2d7ff9", 160, 0.6, 0.05, 1.0),
        ("Mars", "#c44e2d", 215, 0.45, 0.04, 1.02),
        ("Jupiter", "#c78f4b", 290, 1.0, 0.025, 1.05),
        ("Saturn", "#d8c17a", 365, 0.95, 0.02, 1.07),
    ]:
        name, color, distance, size, speed, tilt = planet
        orbit = turtle.Turtle()
        orbit.hideturtle()
        orbit.speed(0)
        orbit.color("#2f4368")
        orbit.penup()
        orbit.pensize(1)
        orbit.goto(0, 0)
        orbit.pendown()
        orbit.circle(distance)
        orbit.penup()
        orbit_turtles.append(orbit)

    planets = [
        create_planet("Mercury", "#8c8c8c", 70, 0.35, 0.09, 0.95),
        create_planet("Venus", "#d78b2d", 110, 0.55, 0.06, 0.98),
        create_planet("Earth", "#2d7ff9", 160, 0.6, 0.05, 1.0),
        create_planet("Mars", "#c44e2d", 215, 0.45, 0.04, 1.02),
        create_planet("Jupiter", "#c78f4b", 290, 1.0, 0.025, 1.05),
        create_planet("Saturn", "#d8c17a", 365, 0.95, 0.02, 1.07),
    ]

    for _ in range(5000):
        for planet in planets:
            planet["angle"] += planet["speed"]
            x = math.cos(planet["angle"]) * planet["distance"]
            y = math.sin(planet["angle"]) * planet["distance"] * planet["tilt"]
            planet["turtle"].goto(x, y)
            if planet["name"] == "Saturn":
                planet["turtle"].color("#d8c17a")
        screen.update()

    screen.bye()


if __name__ == "__main__":
    import random
    main()
