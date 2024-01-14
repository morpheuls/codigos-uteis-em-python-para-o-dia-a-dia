# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageOps, ImageChops, ImageFilter

# def remove_background(input_path, output_path):
#     input_image = Image.open(input_path)
#     input_image = input_image.convert("RGBA")

#     mask = Image.new("L", input_image.size, 0)
#     mask_data = []

#     for pixel in input_image.getdata():
#         if pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200:
#             mask_data.append(255)
#         else:
#             mask_data.append(0)

#     mask.putdata(mask_data)
#     input_image.putalpha(mask)

#     input_image.save(output_path, "PNG")

# def choose_file():
#     input_path = filedialog.askopenfilename(title="Escolher Arquivo")
#     if input_path:
#         remove_background(input_path, "output_image.png")
#         result_label.config(text="Fundo removido com sucesso!")

# # Criação da janela
# root = tk.Tk()
# root.title("Remover Fundo de Imagem")
# root.geometry("600x400")  # Defina as dimensões desejadas (largura x altura)

# # Título da janela
# title_label = tk.Label(root, text="Remover Fundo de Imagem")
# title_label.pack()

# # Botão para escolher o arquivo de imagem
# choose_button = tk.Button(root, text="Escolher Arquivo", command=choose_file)
# choose_button.pack()

# # Rótulo para exibir o resultado
# result_label = tk.Label(root, text="")
# result_label.pack()

# # Botão para sair
# quit_button = tk.Button(root, text="Sair", command=root.quit)
# quit_button.pack()

# root.mainloop()
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from rembg import remove

# Função para remover o fundo da imagem
def remove_background():
    input_file = filedialog.askopenfilename(title="Selecione a imagem de entrada")
    output_file = filedialog.asksaveasfilename(title="Salvar como")

    if input_file and output_file:
        input_image = Image.open(input_file)
        output_image = remove(input_file)
        output_image.save(output_file)

# Criação da janela
root = tk.Tk()
root.title("Remover Fundo de Imagem")

# Botão para selecionar e processar a imagem
process_button = tk.Button(root, text="Selecionar e Remover Fundo", command=remove_background)
process_button.pack()

# Botão para sair
quit_button = tk.Button(root, text="Sair", command=root.quit)
quit_button.pack()

root.mainloop()
