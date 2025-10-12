from random import randint
import math

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        dx = obj.x - body.x
        dy = obj.y - body.y
        r = math.sqrt(dx ** 2 + dy ** 2)
        if r == 0:
            continue
        F = gravitational_constant * body.m * obj.m / r ** 2
        body.Fx += F * dx / r
        body.Fy += F * dy / r


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.Vx += ax * dt
    body.Vy += ay * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt


def calculate_angular_velocity(body, central_body):
    """Вычисляет угловую скорость тела относительно центрального тела.

    Параметры:

    **body** — тело, для которого вычисляется угловая скорость

    **central_body** — центральное тело
    """

    rx = body.x - central_body.x
    ry = body.y - central_body.y
    vx = body.Vx - central_body.Vx
    vy = body.Vy - central_body.Vy
    r = math.sqrt(rx ** 2 + ry ** 2)
    if r == 0:
        return 0
    angular_velocity = (rx * vy - ry * vx) / (r ** 2)
    return angular_velocity


def calculate_kepler_second_law(body, central_body, dt):
    """Проверяет второй закон Кеплера (закон площадей).

    Параметры:

    **body** — тело, для которого проверяется закон

    **central_body** — центральное тело

    **dt** — шаг по времени
    """

    r1x = body.x - central_body.x
    r1y = body.y - central_body.y
    r2x = (body.x + body.Vx * dt) - central_body.x
    r2y = (body.y + body.Vy * dt) - central_body.y
    area = 0.5 * abs(r1x * r2y - r1y * r2x)
    return area


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


def recalculate_kepler_second_law(space_objects, dt):
    """Проверка второго закона Кеплера (дополнительно)

    Параметры:

    ** space_objects ** — список оьъектов, для которых нужно проверить второй закон кеплера.

    ** dt ** — шаг по времени
    """
    star = None
    for obj in space_objects:
        if obj.type == "Star":
            star = obj
            break
    if star:
        for body in space_objects:
            if body.type == "Planet":
                body.angular_velocity = calculate_angular_velocity(body, star)
                body.swept_area = calculate_kepler_second_law(body, star, dt)
                body.sectorial_velocity = body.swept_area / dt

if __name__ == "__main__":
    print("This module is not for direct call!")