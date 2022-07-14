import numpy as np
import stl
from stl import mesh
import os

def combined_stl(meshes, save_path="./output.stl"):    #nome file uscita
    combined = mesh.Mesh(np.concatenate([m.data for m in meshes]))
    combined.save(save_path, mode=stl.Mode.ASCII)




direc = r"C:\Users\sat11\Desktop\stl_python\Modello 3D\DIA"    #cartella con tutti stl da unire
paths = [os.path.join(direc, i) for i in os.listdir(direc)]
meshes = [mesh.Mesh.from_file(path) for path in paths]
combined_stl(meshes)