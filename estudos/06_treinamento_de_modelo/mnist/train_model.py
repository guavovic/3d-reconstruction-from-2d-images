from pathlib import Path
import tensorflow as tf
from create_model import create_model

if __name__ == "__main__":
    # Carregando e preparando o conjunto de dados MNIST
    mnist = tf.keras.datasets.mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    train_images, test_images = train_images / 255.0, test_images / 255.0
    train_images = train_images[..., tf.newaxis]
    test_images = test_images[..., tf.newaxis]

    pasta = Path(__file__).resolve().parent.parent / 'resultados'
    pasta.mkdir(parents=True, exist_ok=True)

    # Carregando o modelo
    model = tf.keras.models.load_model(str(pasta / 'mnist_model.h5'))

    # Compilando o modelo
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Treinando o modelo
    model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))

    # Salvando o modelo treinado
    model.save(str(pasta / 'mnist_trained_model.h5'))
