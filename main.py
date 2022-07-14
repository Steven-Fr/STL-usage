import vtkplotlib as vpl
from stl.mesh import Mesh
import numpy as np

# Read the STL using numpy-stl
filename ="car.stl"

mesh = Mesh.from_file(filename)

machine = "XS"
x_trasl = -2000
y_trasl = -1500
z_trasl = -1500


t = np.array([x_trasl, y_trasl, z_trasl])
mesh.translate(t)

if machine == "SPD":
    mesh2 =  Mesh.from_file(r"Modello 3D\SPD.stl")

elif machine == "DIA":
    mesh2 =  Mesh.from_file(r"Modello 3D\DIA.stl")
elif machine == "XS":
    mesh2 =  Mesh.from_file(r"Modello 3D\XS.stl")


R = mesh.get_rotation_matrix_from_xyz((np.pi / 2, 0, np.pi / 4))

mesh.rotate(0, theta ,point)

#mesh.rotate((90,90,90), (0, 0, 0))


def bounding_box(points):
    '''
    Calculate the bounding box edge lengths of an stl using the design coordinate system (not an object oriented bounding box),
    expect that input coordinates are in mm.
    '''
    v = points
    x = v[..., 0].flatten()
    y = v[..., 1].flatten()
    z = v[..., 2].flatten()

    x1 = x.max()
    x2 = x.min()
    y1 = y.max()
    y2 = y.min()
    z1 = z.max()
    z2 = z.min()

    return (x1,x2,y1,y2,z1,z2)


bb1 = bounding_box(mesh)
print(bb1)


p1 = vpl.scatter((bb1[0]+200,bb1[2]+200,bb1[4]+200),radius=20, color="r")
p2 = vpl.scatter((bb1[0]+200,bb1[3]-200,bb1[4]+200),radius=20, color="r")
p3 = vpl.scatter((bb1[1]-200,bb1[2]+200,bb1[4]+200),radius=20, color="r")
p4 = vpl.scatter((bb1[1]-200,bb1[3]-200,bb1[4]+200), radius=20,color="r")


#vtkplotlib.arrow(start, end, length=None, width_scale=1.0, color=None, opacity=None, fig='gcf', label=None)
vpl.arrow((-6000,-3000,-1800), (0,-3000,-1800), length=500, width_scale=1.0, color="r", label= "x")
vpl.arrow((-6000,-3000,-1800), (-6000,0,-1800), length=500, width_scale=1.0, color="b", label="y")
vpl.arrow((-6000,-3000,-1800), (-6000,-3000,0), length=500, width_scale=1.0, color="g", label="z")



vpl.mesh_plot(mesh, color = "orange")
vpl.mesh_plot(mesh2, opacity=0.3)


# Show the figure
vpl.show()

