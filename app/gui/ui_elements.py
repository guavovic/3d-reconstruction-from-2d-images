import tkinter as tk
from tkinter import filedialog

class UIElements:
    def __init__(self, root, load_image_callback, generate_callback):
        self.root = root
        self.load_image_callback = load_image_callback
        self.generate_callback = generate_callback
        
        # Frame para carregar a imagem
        self.image_frame = tk.Frame(root, width=400, height=300, bg='lightgray')
        self.image_frame.pack(pady=10)
        
        # Label para mostrar a imagem
        self.image_label = tk.Label(self.image_frame, text="Arraste e solte uma imagem aqui", bg='lightgray')
        self.image_label.pack(expand=True)
        
        # Botão para carregar imagem
        self.load_button = tk.Button(root, text="Carregar Imagem", command=self.open_file_dialog)
        self.load_button.pack(pady=5)
        
        # Botão para gerar
        self.generate_button = tk.Button(root, text="Gerar", command=self.generate_callback)
        self.generate_button.pack(pady=10)
        
        # Label para mostrar o log
        self.log_label = tk.Label(root, text="Log: ", bg='white')
        self.log_label.pack(fill=tk.X, pady=10)
        
    def open_file_dialog(self):
        """Abre uma caixa de diálogo para o usuário selecionar uma imagem."""
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.load_image_callback(file_path)
    
    def update_image(self, img_tk):
        """Atualiza a imagem exibida no label."""
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk
        self.image_label.text = ""