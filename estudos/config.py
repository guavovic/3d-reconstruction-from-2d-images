from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA_IMAGENS = RAIZ / 'imagens'

DIRECTORY_TEST_IMAGES_LINKS = [
    str(PASTA_IMAGENS / 'objeto_exemplo_1.jpg'),
    str(PASTA_IMAGENS / 'objeto_exemplo_2.jpg'),
    str(PASTA_IMAGENS / 'objeto_exemplo_3.png'),
]

GENERETAD_SAVED_MODEL_NAME = 'modelo_treinado.pth'


def pasta_resultados(etapa, *subpastas):
    pasta = Path(__file__).resolve().parent / etapa / 'resultados'
    pasta = pasta.joinpath(*subpastas)
    pasta.mkdir(parents=True, exist_ok=True)
    return str(pasta)


GENERETAD_MODEL_SAVE_PATH = pasta_resultados('06_treinamento_de_modelo')
