import open3d as o3d
import numpy as np
import cv2

def main():
    # Constantes para caminhos de arquivos
    DEPTH_MAP_PATH = 'results/tests/4_estimativa_de_profundidade/mapa_profundidade.png'
    OUTPUT_POINT_CLOUD_PATH = 'results/tests/5_geracao_de_malha_3d/malha.ply'

    # Parâmetros intrínsecos da câmera (ajuste conforme necessário)
    CAMERA_FX = 100  # Distância focal em pixels (eixo x)
    CAMERA_FY = 100  # Distância focal em pixels (eixo y)
    CAMERA_CX = 100  # Centro óptico (eixo x) - será calculado com base na imagem
    CAMERA_CY = 100   # Centro óptico (eixo y) - será calculado com base na imagem

    # Carrega o mapa de profundidade usando OpenCV
    depth_map = cv2.imread(DEPTH_MAP_PATH, cv2.IMREAD_UNCHANGED)  # Use IMREAD_UNCHANGED para garantir que a imagem seja carregada como está

    # Verifica se a imagem foi carregada corretamente
    if depth_map is None:
        raise ValueError(f"Não foi possível carregar a imagem de profundidade em: {DEPTH_MAP_PATH}")

    # Converte a imagem para escala de cinza (single-channel) se necessário
    if len(depth_map.shape) > 2:
        depth_map = cv2.cvtColor(depth_map, cv2.COLOR_BGR2GRAY)

    # Normaliza a imagem de profundidade (se necessário)
    depth_map = depth_map.astype(np.float32)  # Converte para float32
    depth_map /= 255.0  # Normaliza para o intervalo [0, 1] (ajuste conforme necessário)

    # Calcula os centros ópticos (cx e cy) com base nas dimensões da imagem
    CAMERA_CX = depth_map.shape[1] / 2  # Centro da imagem no eixo x
    CAMERA_CY = depth_map.shape[0] / 2  # Centro da imagem no eixo y

    # Cria uma nuvem de pontos
    try:
        point_cloud = o3d.geometry.PointCloud.create_from_depth_image(
            o3d.geometry.Image(depth_map),
            intrinsic=o3d.camera.PinholeCameraIntrinsic(
                width=depth_map.shape[1],
                height=depth_map.shape[0],
                fx=CAMERA_FX,
                fy=CAMERA_FY,
                cx=CAMERA_CX,
                cy=CAMERA_CY
            )
        )

        # Salva a nuvem de pontos
        o3d.io.write_point_cloud(OUTPUT_POINT_CLOUD_PATH, point_cloud)
        print(f"Malha 3D salva em: {OUTPUT_POINT_CLOUD_PATH}")

    except Exception as e:
        print(f"Erro ao criar a nuvem de pontos: {e}")
        
    pcd = o3d.io.read_point_cloud('results/tests/5_geracao_de_malha_3d/malha.ply')
    o3d.visualization.draw_geometries([pcd])
    
if __name__ == "__main__":
    main()