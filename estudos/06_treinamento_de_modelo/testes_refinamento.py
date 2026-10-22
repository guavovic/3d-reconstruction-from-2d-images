import torch
from treinamento_rede_neural import Simple3DModel
import estudos.config as config

modelo = Simple3DModel()
modelo.load_state_dict(torch.load(f'{config.GENERETAD_MODEL_SAVE_PATH}/{config.GENERETAD_SAVED_MODEL_NAME}'))
modelo.eval()

# Testa com uma nova imagem
input_tensor = torch.randn(1, 3, 64, 64)  # Substitua por uma imagem real
output = modelo(input_tensor)

# Salva o resultado
torch.save(output, f"{config.GENERETAD_MODEL_SAVE_PATH}/teste_imagem1.pt")
print(f"Resultado do teste salvo em {config.GENERETAD_MODEL_SAVE_PATH}")