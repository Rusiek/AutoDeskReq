# Write a program in Python which:
# - accepts as an input a number of points,
# - generates that many points on a 2d plane in the range [-100; 100] for both axes,
# - finds and prints three points from which the smallest triangle can be built.

# What kind of error handling would you implement? How to validate that the triangle is valid? How to speed up the algorithm to avoid calculating all possible combinations?

import numpy as np

def generate_points(n: int):
    x = np.random.uniform(-100, 100, n)
    y = np.random.uniform(-100, 100, n)
    points = np.array([x, y]).T
    return points

if __name__ == '__main__':
    n = input('Enter number of points: ')
    try:
        n = 20
        points = generate_points(n)
    except ValueError:
        print('Number of generated points must be an integer')

    min_area = float('inf')
    min_points = [None, None, None]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p1, p2, p3 = points[i], points[j], points[k]
                area = np.linalg.norm(np.cross(p2 - p1, p3 - p1)) / 2
                if area < min_area:
                    min_area = area
                    min_points = [p1, p2, p3]

    print(min_points)
