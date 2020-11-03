import vtkplotlib as vpl
from stl.mesh import Mesh

path='./test.stl'

mesh = Mesh.from_file(path)

vpl.mesh_plot(mesh)

vpl.save_fig('./ima.png')
