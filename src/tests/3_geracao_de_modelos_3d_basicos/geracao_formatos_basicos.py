import trimesh
import exportacao

def criar_esfera(raio=1.0, subdivisoes=3):
    return trimesh.creation.icosphere(subdivisions=subdivisoes, radius=raio)

def criar_triangulo():
    vertices = [[0, 0, 0], [1, 0, 0], [0.5, 1, 0]]
    faces = [[0, 1, 2]]
    return trimesh.Trimesh(vertices=vertices, faces=faces)

def criar_cubo():
    return trimesh.creation.box(extents=[1, 1, 1])

def criar_retangulo():
    return trimesh.creation.box(extents=[2, 1, 0.1])

def criar_plano():
    return trimesh.creation.box(extents=[2, 2, 0.1])

def criar_cilindro(raio=0.5, altura=2.0):
    return trimesh.creation.cylinder(radius=raio, height=altura)

def criar_piramide(lado_base=1.0, altura=1.0):
    vertices = [
        [0, 0, 0],               # Vértice 0
        [lado_base, 0, 0],        # Vértice 1
        [lado_base, lado_base, 0], # Vértice 2
        [0, lado_base, 0],        # Vértice 3
        [lado_base / 2, lado_base / 2, altura]  # Vértice 4 (topo)
    ]
    
    faces = [
        [0, 1, 4],  # Face frontal
        [1, 2, 4],  # Face direita
        [2, 3, 4],  # Face traseira
        [3, 0, 4]   # Face esquerda
    ]

    return trimesh.Trimesh(vertices=vertices, faces=faces)

def criar_pirulito(raio_pirulito=1.0, comprimento_cabo=5.0, espessura_cabo=0.2):
    # Parte côncava (meia esfera)
    esfera = trimesh.creation.icosphere(radius=raio_pirulito, subdivisions=3)
    esfera.vertices[:, 2] -= raio_pirulito  # Move a esfera para baixo

    # Cabo (cilindro)
    cabo = trimesh.creation.cylinder(radius=espessura_cabo, height=comprimento_cabo)
    cabo.vertices[:, 2] += comprimento_cabo / 2  # Centraliza o cabo

    pirulio = trimesh.util.concatenate([esfera, cabo])
    return pirulio

def criar_garfo(comprimento_cabo=5.0, espessura_cabo=0.2, comprimento_dentes=1.0, espessura_dentes=0.1):
    # Cabo (cilindro)
    cabo = trimesh.creation.cylinder(radius=espessura_cabo, height=comprimento_cabo)
    cabo.vertices[:, 2] += comprimento_cabo / 2  # Centraliza o cabo

    # Dentes (cilindros finos)
    dentes = []
    for i in range(4):  # Quatro dentes
        dente = trimesh.creation.cylinder(radius=espessura_dentes, height=comprimento_dentes)
        dente.vertices[:, 0] += (i - 1.5) * espessura_dentes * 2  # Espaça os dentes
        dente.vertices[:, 2] += comprimento_cabo + comprimento_dentes / 2  # Posiciona os dentes
        dentes.append(dente)

    garfo = trimesh.util.concatenate([cabo] + dentes)
    return garfo

exportacao.exportar_malha(criar_esfera(), tipo_malha='esfera')
exportacao.exportar_malha(criar_triangulo(), tipo_malha='triangulo')
exportacao.exportar_malha(criar_cubo(), tipo_malha='cubo')
exportacao.exportar_malha(criar_retangulo(), tipo_malha='retangulo')
exportacao.exportar_malha(criar_plano(), tipo_malha='plano')
exportacao.exportar_malha(criar_cilindro(), tipo_malha='cilindro')
exportacao.exportar_malha(criar_piramide(), tipo_malha='piramide')
exportacao.exportar_malha(criar_pirulito(), tipo_malha='pirulito')
exportacao.exportar_malha(criar_garfo(), tipo_malha='garfo')