import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def show_3d_model():
    """
    Exibe o modelo 3D gerado.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Carrega o modelo 3D do arquivo .obj
    vertices = []
    faces = []
    with open("models/modelo_gerado.obj", "r") as f:
        for line in f:
            if line.startswith("v "):
                vertices.append(list(map(float, line.strip().split()[1:])))
            elif line.startswith("f "):
                faces.append([int(i.split('/')[0]) for i in line.strip().split()[1:]])
    
    vertices = np.array(vertices)
    faces = np.array(faces) - 1  # Ajusta os índices para começar em 0
    
    # Plota as faces
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], faces, vertices[:, 2], cmap='viridis')
    
    plt.show()