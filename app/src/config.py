from pathlib import Path

PASTA_APP = Path(__file__).resolve().parent.parent

CACHE_PATH = str(PASTA_APP / 'cache')
DEFAULT_DRAG_AND_DROP_IMAGE_PATH = str(PASTA_APP / 'images' / 'drag_and_drop_image.jpg')
LOADING_GIF_PATH = str(PASTA_APP / 'images' / 'loading_gif.gif')
GENERETAD_MODEL_SAVE_PATH = CACHE_PATH
