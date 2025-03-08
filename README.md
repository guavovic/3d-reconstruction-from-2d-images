# 🚀 Reconstrução 3D a partir de Imagens 2D

Bem-vindo ao repositório do meu projeto de TCC! Este projeto tem como objetivo desenvolver uma ferramenta capaz de converter imagens 2D em modelos 3D, utilizando técnicas de aprendizado de máquina e visão computacional. Abaixo, você encontrará uma visão geral do projeto, as tecnologias utilizadas, as etapas desenvolvidas e os resultados obtidos.

---

## 📋 Índice
1. [Visão Geral do Projeto](#1-visão-geral-do-projeto)
2. [Tecnologias Utilizadas](#2-tecnologias-utilizadas)
3. [Etapas do Projeto](#3-etapas-do-projeto)
4. [Resultados Finais](#4-resultados-finais)
5. [Como Executar o Projeto](#5-como-executar-o-projeto)
6. [Próximos Passos](#6-próximos-passos)
7. [Referências](#7-referências)

---

## 1. Visão Geral do Projeto
O objetivo deste projeto é criar uma ferramenta que permita a reconstrução de modelos 3D a partir de imagens 2D. A ferramenta utiliza técnicas de visão computacional e aprendizado de máquina para inferir a profundidade e a estrutura tridimensional de objetos a partir de uma ou mais imagens.

### Dificuldades
- Uma única imagem não contém informações completas sobre a profundidade e a geometria do objeto.
- A reconstrução 3D exige técnicas avançadas para "adivinhar" a estrutura tridimensional a partir de dados limitados.

---

## 2. Tecnologias Utilizadas
- **Python**: Linguagem principal para desenvolvimento.
- **OpenCV**: Processamento de imagens e detecção de características.
- **Trimesh**: Geração e manipulação de malhas 3D.
- **PyTorch**: Implementação e treinamento de redes neurais.
- **Open3D**: Visualização e processamento de dados 3D.
- **Blender**: Visualização e edição de modelos 3D.
- **MiDaS**: Modelo pré-treinado para estimativa de profundidade.

---

## 3. Resultados Finais

### 4.1 Modelos 3D Básicos
- **Cubo**:
  ![Cubo](resultados/cubo.png)
- **Esfera**:
  ![Esfera](resultados/esfera.png)

### 4.2 Estimativa de Profundidade
- **Mapa de Profundidade**:
  ![Mapa de Profundidade](resultados/mapa_profundidade.png)

### 4.3 Malhas 3D Geradas
- **Malha 3D a partir de Imagem 2D**:
  ![Malha 3D](resultados/malha_3d.png)

### 4.4 Modelos Complexos
- **Reconstrução de Objetos Complexos**:
  ![Objeto Complexo](resultados/objeto_complexo.png)

---

## 4. Como Executar o Projeto
Siga os passos abaixo para executar o projeto localmente:

1. Clone o repositório:
```
git clone https://github.com/seu-usuario/tcc-projeto-3d.git
cd tcc-projeto-3d
```
2. Crie e ative o ambiente virtual:
```
virtualenv venv
source venv/bin/activate  # No Linux/Mac
venv\Scripts\activate     # No Windows
```
3. Instale as dependências:
```
pip install -r requirements.txt
```
4. Execute os scripts:
```
python scripts/passo_1/processamento_imagens.py

Tips on Input Image
To optimize the generated results, we recommend you to use a standardized front view of the object you're going to generate as the input image, with a white background and no text or extraneous information. This ensures the best quality when converting your 2D sketch to a 3D model.

COLOCAR ALGO DO TIPO EM INGLES, PARA RECOMEDNAÇÕES DE TIPOS DE IMAGENS, SÓ QUE MESMO ASSIM TRATAR IMAGENS:

Recommended inputs:
✅ Single object in one image

✅ Standard front view of the object

✅ White/monochrome/no background

Not recommended inputs:
⚠️ Text on the image

⚠️ Multiple objects in one image

⚠️ Complex background

❌ Inappropriate imagery (including but not limited to harmful content, offensive content, and NSFW content)

```
---

## 5. Futuros Passos
Adicionar suporte para múltiplas imagens (fotogrametria).
Implementar uma interface gráfica utilizando Tkinter ou Streamlit.
Explorar técnicas mais avançadas, como NeRF (Neural Radiance Fields).

---

## 📂 Estrutura do Projeto
TCC-PROJECT/
├── dados/                  # Pasta para armazenar imagens e modelos 3D
├── scripts/                # Scripts Python para cada etapa do projeto
├── resultados/             # Resultados gerados (imagens, modelos 3D, etc.)
├── README.md               # Este arquivo
└── requirements.txt        # Lista de dependências do projeto

---

## 📄 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.