def build_pyramid_with_given_height(height):
    astrix1 = "*"
    astrix2 = "**"
    height += height
    while len(astrix1) < height:
        print(astrix1.center(height))
        astrix1 += astrix2


build_pyramid_with_given_height(20)