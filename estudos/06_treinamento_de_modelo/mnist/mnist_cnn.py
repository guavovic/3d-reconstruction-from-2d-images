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


# Carregando e preparando o conjunto de dados MNIST
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalizando os valores dos pixels para o intervalo [0, 1]
train_images, test_images = train_images / 255.0, test_images / 255.0

# Adicionando uma dimensão de canal para as imagens (necessário para convoluções)
train_images = train_images[..., tf.newaxis]
test_images = test_images[..., tf.newaxis]

# Definindo parâmetros
input_shape = (28, 28, 1)
num_classes = 10

# Criando o modelo
model = create_model(input_shape, num_classes)

# Compilando o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Exibindo um resumo do modelo
model.summary()

# Treinando o modelo
model.fit(train_images, train_labels, epochs=5,
          validation_data=(test_images, test_labels))
