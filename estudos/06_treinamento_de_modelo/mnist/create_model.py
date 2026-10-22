from pathlib import Path
import tensorflow as tf
from tensorflow.keras import layers, models

# Definindo a arquitetura da rede neural


def create_model(input_shape, num_classes):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model


if __name__ == "__main__":
    # Definindo parâmetros

    # Tamanho da imagem de entrada (28x28 pixels em escala de cinza)
    input_shape = (28, 28, 1)
    # Número de classes (por exemplo, para MNIST, 10 classes para dígitos de 0 a 9)
    num_classes = 10

    # Criando o modelo
    model = create_model(input_shape, num_classes)

    # Salvando o modelo
    pasta = Path(__file__).resolve().parent.parent / 'resultados'
    pasta.mkdir(parents=True, exist_ok=True)
    model.save(str(pasta / 'mnist_model_test.h5'))
