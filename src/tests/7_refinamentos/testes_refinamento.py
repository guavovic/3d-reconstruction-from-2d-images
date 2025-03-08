import torch
from treinamento_rede_neural import Simple3DModel

# Carrega o modelo treinado
modelo = Simple3DModel()
modelo.load_state_dict(torch.load("../resultados/passo_7/modelo_treinado.pth"))
modelo.eval()

# Testa com uma nova imagem
input_tensor = torch.randn(1, 3, 64, 64)  # Substitua por uma imagem real
output = modelo(input_tensor)

# Salva o resultado
torch.save(output, "../resultados/passo_8/teste_imagem1.pt")
print("Resultado do teste salvo em resultados/passo_8/teste_imagem1.pt")