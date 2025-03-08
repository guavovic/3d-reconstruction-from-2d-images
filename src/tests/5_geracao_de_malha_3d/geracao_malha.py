import open3d as o3d
import numpy as np

# Carrega o mapa de profundidade
depth_map = np.load("../resultados/passo_5/mapa_profundidade.npy")

# Cria uma nuvem de pontos
point_cloud = o3d.geometry.PointCloud.create_from_depth_image(
    o3d.geometry.Image(depth_map),
    intrinsic=o3d.camera.PinholeCameraIntrinsic(
        width=depth_map.shape[1],
        height=depth_map.shape[0],
        fx=525.0,  # Parâmetros intrínsecos da câmera (ajuste conforme necessário)
        fy=525.0,
        cx=depth_map.shape[1] / 2,
        cy=depth_map.shape[0] / 2
    )
)

# Salva a malha 3D
o3d.io.write_point_cloud("../resultados/passo_6/malha.ply", point_cloud)

print("Malha 3D salva em resultados/passo_6/malha.ply")