import trimesh as tm
import exportacao as exp
import estudos.config as config

def criar_esfera(raio=1.0, subdivisoes=3):
    return tm.creation.icosphere(subdivisions=subdivisoes, radius=raio)

def criar_triangulo():
    vertices = [[0, 0, 0], [1, 0, 0], [0.5, 1, 0]]
    faces = [[0, 1, 2]]
    return tm.Trimesh(vertices=vertices, faces=faces)

def criar_cubo():
    return tm.creation.box(extents=[1, 1, 1])

def criar_retangulo():
    return tm.creation.box(extents=[2, 1, 0.1])

def criar_plano():
    return tm.creation.box(extents=[2, 2, 0.1])

def criar_cilindro(raio=0.5, altura=2.0):
    return tm.creation.cylinder(radius=raio, height=altura)

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

    return tm.Trimesh(vertices=vertices, faces=faces)

def criar_pirulito(raio_pirulito=1.0, comprimento_cabo=5.0, espessura_cabo=0.2):
    # Parte côncava (meia esfera)
    esfera = tm.creation.icosphere(radius=raio_pirulito, subdivisions=3)
    esfera.vertices[:, 2] -= raio_pirulito  # Move a esfera para baixo

    # Cabo (cilindro)
    cabo = tm.creation.cylinder(radius=espessura_cabo, height=comprimento_cabo)
    cabo.vertices[:, 2] += comprimento_cabo / 2  # Centraliza o cabo

    pirulio = tm.util.concatenate([esfera, cabo])
    return pirulio

def criar_garfo(comprimento_cabo=5.0, espessura_cabo=0.2, comprimento_dentes=1.0, espessura_dentes=0.1):
    # Cabo (cilindro)
    cabo = tm.creation.cylinder(radius=espessura_cabo, height=comprimento_cabo)
    cabo.vertices[:, 2] += comprimento_cabo / 2  # Centraliza o cabo

    # Dentes (cilindros finos)
    dentes = []
    for i in range(4):  # Quatro dentes
        dente = tm.creation.cylinder(radius=espessura_dentes, height=comprimento_dentes)
        dente.vertices[:, 0] += (i - 1.5) * espessura_dentes * 2  # Espaça os dentes
        dente.vertices[:, 2] += comprimento_cabo + comprimento_dentes / 2  # Posiciona os dentes
        dentes.append(dente)

    garfo = tm.util.concatenate([cabo] + dentes)
    return garfo


def main():
    OUTPUT_DIRECTORY = config.pasta_resultados('03_geracao_de_modelos_3d_basicos', 'objetos_gerados')

    exp.exportar_malha(malha=criar_esfera(),tipo_malha='esfera',output_directory=OUTPUT_DIRECTORY)
    exp.exportar_malha(malha=criar_triangulo(), tipo_malha='triangulo',output_directory=OUTPUT_DIRECTORY)
    exp.exportar_malha(malha=criar_cubo(), tipo_malha='cubo',output_directory=OUTPUT_DIRECTORY)
    exp.exportar_malha(malha=criar_retangulo(), tipo_malha='retangulo',output_directory=OUTPUT_DIRECTORY)
    exp.exportar_malha(malha=criar_plano(), tipo_malha='plano',output_directory=OUTPUT_DIRECTORY)
    exp.exportar_malha(malha=criar_cilindro(), tipo_malha='cilindro',output_directory=OUTPUT_DIRECTORY)
    exp.exportar_malha(malha=criar_piramide(), tipo_malha='piramide',output_directory=OUTPUT_DIRECTORY)
    exp.exportar_malha(malha=criar_pirulito(), tipo_malha='pirulito',output_directory=OUTPUT_DIRECTORY)
    exp.exportar_malha(malha=criar_garfo(), tipo_malha='garfo',output_directory=OUTPUT_DIRECTORY)

if __name__ == "__main__":
    main()