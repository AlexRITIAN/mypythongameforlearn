import numpy as np
import bezier

n1 = np.array([[0.0, 1.0],[1.5, 1.0],[1.0, 0.0],])
n2 = np.array([[0.0, 0.0],[1.0, 1.0],[1.0, 2.5],])
curve1 = bezier.Curve(n1, degree=2)
curve2 = bezier.Curve.from_nodes(n2)
intersections = curve1.intersect(curve2)

print (intersections)