import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import os
import estudos.config as config

# Modelo de conversão de imagem para voxel grid
class ImageTo3D(nn.Module):
    def __init__(self):
        super(ImageTo3D, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(128 * 8 * 8, 1024),
            nn.ReLU()
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(1024, 128 * 8 * 8 * 8),
            nn.ReLU(),
            nn.Unflatten(1, (128, 8, 8, 8)),
            nn.ConvTranspose3d(128, 64, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            nn.ConvTranspose3d(64, 32, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            nn.ConvTranspose3d(32, 1, kernel_size=4, stride=2, padding=1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# Dataset de exemplo
class ImageTo3DDataset(Dataset):
    def __init__(self, img_dir, voxel_dir, transform=None):
        self.img_dir = img_dir
        self.voxel_dir = voxel_dir
        self.transform = transform
        self.images = os.listdir(img_dir)
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.images[idx])
        voxel_path = os.path.join(self.voxel_dir, self.images[idx].replace('.png', '.npy'))
        
        image = Image.open(img_path).convert('RGB')
        voxel = np.load(voxel_path)  # Assumindo que os voxels estão armazenados em arquivos .npy
        
        if self.transform:
            image = self.transform(image)
        
        voxel = torch.tensor(voxel, dtype=torch.float32).unsqueeze(0)  # (1, 32, 32, 32)
        return image, voxel

# Transforma imagens
transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])

# Inicializando dataset e dataloader
img_dir = str(config.PASTA_IMAGENS / "treino")
voxel_dir = str(config.PASTA_IMAGENS / "treino_voxels")
dataset = ImageTo3DDataset(img_dir, voxel_dir, transform=transform)
dataloader = DataLoader(dataset, batch_size=8, shuffle=True)

# Instancia modelo, loss e otimizador
model = ImageTo3D()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Treinamento
num_epochs = 10
for epoch in range(num_epochs):
    for imgs, voxels in dataloader:
        outputs = model(imgs)
        loss = criterion(outputs, voxels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

torch.save(model.state_dict(), f'{config.GENERETAD_MODEL_SAVE_PATH}/{config.GENERETAD_SAVED_MODEL_NAME}')