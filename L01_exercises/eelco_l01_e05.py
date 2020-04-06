def build_pyramid():
    astrix1 = "*"
    astrix2 = "**"
    while len(astrix1) < 10:
        print(astrix1.center(10))
        astrix1 += astrix2

build_pyramid()