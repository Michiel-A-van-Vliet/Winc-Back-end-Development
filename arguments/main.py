# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greet_template="Hello, <name>!"):
    return greet_template.replace("<name>", name)


surface_gravity = {
    "sun": 274,
    "jupiter": 24.9,
    "neptune": 11.2,
    "saturn": 10.4,
    "earth": 9.8,
    "uranus": 8.9,
    "venus": 8.9,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.6
}


def force(mass, body="earth"):
    return mass * surface_gravity[body]


G = 6.674 * 0.1**11


def pull(m1, m2, d):
    return G * ((m1 * m2) / d**2)


if __name__ == '__main__':
    print(20*"=")
    print(greet("Doc"))
    print(greet('Bob', "What's up, <name>!"))
    print(20*"=")
    print(force(10))
    print(force(10, "venus"))
    print(20*"=")
    print(pull(800, 1500, 3))
    print(pull(0.1, 5.972 * 10**24, 6.371 * 10**6))