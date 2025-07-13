import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import threading
from src.generate_3d import generate_3d_model
from src.viewer_3d import show_3d_model
from src.utils import log_message
import src.config as congif
from gui.ui_elements import UIElements

class App:
    WINDOW_WIDTH, WINDOW_HEIGTH = 500, 500
    
    def __init__(self, root):
        self.root = root
        self.root.title("Ferramenta de 2D para 3D")      
        self.root.geometry(f"{App.WINDOW_WIDTH}x{App.WINDOW_HEIGTH}")
        self.center_window()
        
        self.ui = UIElements(root, self.load_image, self.generate)
        
        self.image = None
        self.load_default_image()
        
        # Variáveis para o overlay e GIF de carregamento
        self.overlay = None
        self.loading_label = None
        self.loading_frames = []
        self.loading_frame_index = 0
        
    def center_window(self):
        """
        Centraliza a janela no meio da tela.
        """
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"+{x}+{y}")
        
    def load_default_image(self):
        """Carrega a imagem padrão no início da aplicação."""
        try:
            self.default_image = Image.open(congif.DEFAULT_DRAG_AND_DROP_IMAGE_PATH)
            self.default_image.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(self.default_image)
            self.ui.update_image(img_tk)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar a imagem padrão: {e}")
        
    def load_image(self, file_path):
        """Carrega a imagem escolhida pelo usuário."""
        try:
            self.image = Image.open(file_path)
            self.image.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(self.image)
            self.ui.update_image(img_tk)
            log_message(self.ui.log_label, f"Imagem carregada: {file_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar a imagem: {e}")
        
    def generate(self):
        if self.image is None:
            messagebox.showwarning("Aviso", "Por favor, carregue uma imagem primeiro.")
            return
        
        # Escurece a tela e exibe o GIF de carregamento
        self.show_loading_screen()
        
        def task():
            log_message(self.ui.log_label, "Gerando modelo 3D...")
            modelo_gerado = generate_3d_model(self.image) 
            return modelo_gerado
        
        def on_task_complete(future):
            """Função chamada quando a tarefa é concluída."""
            try:
                log_message(self.ui.log_label, "Modelo 3D gerado com sucesso!")
                modelo_gerado = future.result()
                show_3d_model(modelo_gerado)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao gerar o modelo 3D: {e}")
            finally:
                # Remove o overlay e o GIF de carregamento
                self.hide_loading_screen()
        
        # Cria uma thread para executar a tarefa
        future = threading.Thread(target=task)
        future.start()
        
        # Usa um loop para verificar se a thread terminou
        self.check_thread_completion(future, on_task_complete)

    def check_thread_completion(self, thread, callback):
        """Verifica se a thread terminou e chama o callback."""
        if thread.is_alive():
            # Se a thread ainda estiver em execução, verifica novamente após 100ms
            self.root.after(100, self.check_thread_completion, thread, callback)
        else:
            # Se a thread terminou, chama o callback
            callback(thread)

    def show_loading_screen(self):
        """Exibe o overlay escuro e o GIF de carregamento."""
        # Cria uma imagem semi-transparente para o overlay
        overlay_image = Image.new("RGBA", (500, 500), (0, 0, 0, 128))  # Preto com 50% de transparência
        overlay_photo = ImageTk.PhotoImage(overlay_image)
        
        # Cria um Label para o overlay
        self.overlay = tk.Label(self.root, image=overlay_photo)
        self.overlay.image = overlay_photo  # Mantém uma referência para evitar garbage collection
        self.overlay.place(relwidth=1, relheight=1)
        
        # Carrega o GIF de carregamento
        self.loading_frames = self.load_gif(congif.LOADING_GIF_PATH)
        self.loading_label = tk.Label(self.root, bg="black")
        self.loading_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Inicia a animação do GIF
        self.animate_loading_gif(0)

    def hide_loading_screen(self):
        """Remove o overlay e o GIF de carregamento."""
        if self.overlay:
            self.overlay.destroy()
        if self.loading_label:
            self.loading_label.destroy()

    def load_gif(self, gif_path):
        """Carrega os frames de um GIF."""
        gif = Image.open(gif_path)
        frames = []
        try:
            for frame in ImageSequence.Iterator(gif):
                frame = frame.resize((App.WINDOW_WIDTH, App.WINDOW_HEIGTH))  # Redimensiona o GIF
                frames.append(ImageTk.PhotoImage(frame))
        except Exception as e:
            print(f"Erro ao carregar o GIF: {e}")
        return frames

    def animate_loading_gif(self, frame_index):
        """Anima o GIF de carregamento."""
        if self.loading_label:
            self.loading_label.config(image=self.loading_frames[frame_index])
            self.loading_frame_index = (frame_index + 1) % len(self.loading_frames)
            self.root.after(100, self.animate_loading_gif, self.loading_frame_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()