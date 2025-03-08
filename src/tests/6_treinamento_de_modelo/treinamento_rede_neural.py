import torch
import torch.nn as nn
import torch.optim as optim

class Simple3DModel(nn.Module):
    def __init__(self):
        super(Simple3DModel, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(16, 3, kernel_size=2, stride=2),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# Instancia o modelo
modelo = Simple3DModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(modelo.parameters(), lr=0.001)

# Loop de treinamento (exemplo simplificado)
for epoch in range(10):
    inputs = torch.randn(1, 3, 64, 64)  # Dados de exemplo
    outputs = modelo(inputs)
    loss = criterion(outputs, inputs)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print(f"Época {epoch + 1}, Loss: {loss.item()}")

# Salva o modelo treinado
torch.save(modelo.state_dict(), "../resultados/passo_7/modelo_treinado.pth")
print("Modelo treinado salvo em resultados/passo_7/modelo_treinado.pth")