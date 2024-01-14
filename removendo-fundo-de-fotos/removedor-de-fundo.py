#pip install rembg
#pip install tk 
#pip install pillow
#Lembre-se o python usando é 3.10.12

import tkinter as tk
from tkinter import filedialog
from PIL import Image
from rembg import remove
import os

# Função para remover o fundo da imagem
def remove_background():
    input_file = filedialog.askopenfilename(title="Selecione a imagem de entrada")

    if input_file:
        try:
            # Carregar a imagem de entrada
            input_image = Image.open(input_file)

            # Remover o fundo da imagem
            output_image = remove(input_image)

            # Solicitar o nome do arquivo de saída (sem extensão)
            file_name = filedialog.asksaveasfilename(title="Salvar como", filetypes=[("PNG files", "*.png")])

            if file_name:
                # Adicionar a extensão .png se não estiver presente
                if not file_name.endswith(".png"):
                    file_name += ".png"

                # Salvar a imagem de saída
                output_image.save(file_name)

        except Exception as e:
            # Lidar com possíveis erros
            result_label.config(text=f"Erro: {str(e)}")

# Criação da janela
root = tk.Tk()
root.title("Remover Fundo de Imagem")

# Definir a largura e altura da janela
root.geometry("800x600")

# Botão para selecionar e processar a imagem
process_button = tk.Button(root, text="Remover Fundo da Imagem", command=remove_background)
process_button.pack()

# Rótulo para exibir o resultado
result_label = tk.Label(root, text="")
result_label.pack()

# Botão para sair
quit_button = tk.Button(root, text="Sair", command=root.quit)
quit_button.pack()

root.mainloop()
