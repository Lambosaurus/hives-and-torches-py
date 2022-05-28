from pygame import Vector2 as v2

def v2_mutate(v: v2, func: callable) -> v2:
    return v2(func(v[0]), func(v[1]))
    