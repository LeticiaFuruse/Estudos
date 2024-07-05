import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import moviepy.editor as mp
import os
# necessario importar essas biliotecas

def download_audio():
    url = url_entry.get()
    folder = filedialog.askdirectory()
    
    if not url or not folder:
        messagebox.showerror("Erro", "Por favor, forneça um URL válido e selecione uma pasta.")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        output_path = stream.download(output_path=folder)
        
        base, ext = os.path.splitext(output_path)
        new_file = base + '.mp3'
        
        audio_clip = mp.AudioFileClip(output_path)
        audio_clip.write_audiofile(new_file)
        audio_clip.close()
        
        os.remove(output_path)
        
        messagebox.showinfo("Sucesso", "Download completo e arquivo convertido para MP3!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Criação da interface gráfica
root = tk.Tk()
root.title("Conversor de Música do YouTube")

tk.Label(root, text="URL do YouTube:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Baixar e Converter", command=download_audio)
download_button.pack(pady=20)

root.mainloop()
