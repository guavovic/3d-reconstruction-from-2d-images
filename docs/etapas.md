# Projeto de TCC: Reconstrução 3D a partir de Imagens 2D

Este projeto tem como objetivo desenvolver uma ferramenta capaz de converter imagens 2D em modelos 3D, utilizando técnicas de aprendizado de máquina e visão computacional. Abaixo estão detalhadas as etapas realizadas, desde a configuração inicial até a implementação de técnicas avançadas.

---

## 📋 Índice
1. [Definição do Escopo Inicial](#1-definição-do-escopo-inicial)
2. [Configuração do Ambiente de Desenvolvimento](#2-configuração-do-ambiente-de-desenvolvimento)
3. [Aprendizado Básico sobre Processamento de Imagens](#3-aprendizado-básico-sobre-processamento-de-imagens)
4. [Geração de Modelos 3D Básicos](#4-geração-de-modelos-3d-básicos)
5. [Entendimento do Formato .obj](#5-entendimento-do-formato-obj)
6. [Abordagem Inicial: Geração de Modelos 3D a partir de Imagens 2D](#6-abordagem-inicial-geração-de-modelos-3d-a-partir-de-imagens-2d)
7. [Técnicas Avançadas: Estimativa de Profundidade e Geração de Malhas 3D](#7-técnicas-avançadas-estimativa-de-profundidade-e-geração-de-malhas-3d)
8. [Treinamento de um Modelo de Aprendizado de Máquina](#8-treinamento-de-um-modelo-de-aprendizado-de-máquina)
9. [Testes e Refinamento](#9-testes-e-refinamento)
10. [Documentação e Apresentação](#10-documentação-e-apresentação)
11. [Próximos Passos](#11-próximos-passos)

# TODO: SEPARA DEPPOIS EM DOCUMENTOS CADA ETAPA PARA ORGANIZAR MELHOR, PARA ESSE DOCUMENTO NAO FICAR MUITO EXTENSO

---

## 1. Definição do Escopo Inicial
O objetivo inicial foi criar um protótipo capaz de gerar modelos 3D básicos (como cubos e esferas) a partir de imagens 2D simples. A ideia era começar com algo simples e evoluir gradualmente para objetos mais complexos, como vasos ou animais.

---

## 2. Configuração do Ambiente de Desenvolvimento
Para garantir um ambiente de desenvolvimento isolado e controlado, foi utilizada a ferramenta **virtualenv** para criar um ambiente virtual Python. O ambiente foi configurado da seguinte forma:

1. Criou-se um ambiente virtual na raiz do projeto:
```
virtualenv virtual
```
2. Ativou-se o ambiente virtual:
```
cd virtual/Scripts
activate
```

3. Transforme o Diretório src/ em um Pacote Instalável 

a) Crie um Arquivo setup.py
Na raiz do seu projeto (tcc-project/), crie um arquivo chamado setup.py com o seguinte conteúdo:
```
from setuptools import setup, find_packages

setup(
    name="tcc_project",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
```

b) Instale o Pacote no Modo de Desenvolvimento
No terminal, navegue até a raiz do projeto (tcc-project/) e execute o seguinte comando:
```
pip install -e .
```
O comando pip install -e . instala o pacote no modo de desenvolvimento. Isso significa que qualquer alteração no código será refletida automaticamente, sem precisar reinstalar o pacote.

2. Estrutura do Projeto Após a Instalação
Agora, a estrutura do seu projeto deve ser assim:
```
tcc-project/
├── src/
├── setup.py  # Arquivo de configuração do pacote
```

4. Instalaram-se as bibliotecas essenciais:
```
pip install numpy opencv-python matplotlib tensorflow torch torchvision trimesh open3d
```
Além disso, o **Blender** foi instalado para visualização e edição de modelos 3D.

---

## 3. Aprendizado Básico sobre Processamento de Imagens
Nesta etapa, foram realizados os primeiros experimentos com a biblioteca **OpenCV** para processamento de imagens. O foco foi aprender a carregar, exibir e manipular imagens 2D. Também foram exploradas técnicas como redimensionamento, conversão para escala de cinza e aplicação de filtros.

---

## 4. Geração de Modelos 3D Básicos
Utilizando a biblioteca **trimesh**, foram gerados modelos 3D básicos, como cubos e esferas. 
Os modelos gerados foram visualizados no Blender para verificação. Os modelos foram gerados na extensão `.obj`.

### 4.1 Entendimento do Formato .obj
O formato `.obj` foi estudado para compreender como os modelos 3D são representados. Um arquivo `.obj` contém vértices, faces e, opcionalmente, texturas. A biblioteca **trimesh** foi utilizada para carregar e manipular esses arquivos. (Artigo falando sobre .obj)[https://www.adobe.com/br/products/substance3d/discover/what-are-obj-files.html#:~:text=Os%20arquivos%20OBJ%20s%C3%A3o%20um,e%20texturas%20de%20um%20design]

---

## 5. Abordagem Inicial: Geração de Modelos 3D a partir de Imagens 2D
Nesta etapa, foi desenvolvida uma abordagem simples para gerar modelos 3D a partir de imagens 2D. O processo envolveu:

1. Detecção de contornos na imagem usando **OpenCV**:
Foi utlizada uma tecnica de processamento de iamgem, a (**Segmentação**)[https://pt.wikipedia.org/wiki/Segmenta%C3%A7%C3%A3o_(processamento_de_imagem)]. Para começar, foi utlizado do tipo de (**Detecção de Bordas**)[https://pt.wikipedia.org/wiki/Detec%C3%A7%C3%A3o_de_borda] e também em um tipo baseado em caracteristicas de pixel, a **Segmentação de Intensidades**.

2. Remoção de fundo, com foco no objeto principal da imagem (opcional por enqunanto):
Para focar no objeto principal e remover o fundo das imagens, foram usadas técnicas de segmentação de imagem. Pontos importantes para seguir:

a) Detectar o objeto principal:
Usando técnicas de detecção de contornos ou segmentação por cor.

b) Criar uma máscara:
Uma imagem binária onde o objeto principal é branco (255) e o fundo é preto (0).

c) Aplicar a máscara:
Usar a máscara para remover o fundo da imagem original.

3. Geração de um modelo 3D básico a partir dos contornos  detectados. 

---

## 6. Técnicas Avançadas: Estimativa de Profundidade e Geração de Malhas 3D
Para melhorar a qualidade dos modelos 3D, foram exploradas técnicas avançadas, como a estimativa de profundidade e a geração de malhas 3D. O modelo **MiDaS** foi utilizado para estimar a profundidade a partir de imagens 2D:

A partir do mapa de profundidade, foi gerada uma malha 3D utilizando a biblioteca **open3d**:

---

## 7. Treinamento de um Modelo de Aprendizado de Máquina
Foi implementada uma rede neural simples para mapear imagens 2D para modelos 3D. A arquitetura utilizada foi um **autoencoder**, conforme o exemplo abaixo:

O modelo foi treinado utilizando o dataset ShapeNet.

---

## 8. Testes e Refinamento
BOTAR ALGO QUE TIPO "Foram realizados testes com diferentes imagens para avaliar a qualidade dos modelos 3D gerados. Métricas como erro de reconstrução e comparação visual foram utilizadas para aprimorar o modelo."
"
---

## 9. Documentação e Apresentação
BOTAR ALGO QUE TIPO "Todo o processo foi documentado, desde a configuração inicial até os resultados finais. Um relatório detalhado foi preparado, explicando cada etapa, os desafios enfrentados e as soluções implementadas. Além disso, uma demonstração prática foi desenvolvida para mostrar o funcionamento da ferramenta."

---

## 10. Futuros Passos
- Adicionar suporte para múltiplas imagens (fotogrametria).
- Implementar uma interface gráfica utilizando Tkinter ou Streamlit.
- Explorar técnicas mais avançadas, como NeRF (Neural Radiance Fields).