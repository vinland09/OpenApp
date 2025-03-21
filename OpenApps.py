import subprocess

# Função para abrir um aplicativo
def abrir_app(canvas):
    try:
        subprocess.Popen(canvas)
        print(f"Aplicativo {canvas} aberto com sucesso.")
    except FileNotFoundError:
        print(f"Aplicativo {canvas} não encontrado.")

# Caminho completo do aplicativo que você deseja abrir
canvas_app = r"C:\Users\Vinicius\AppData\Local\Programs\Canva\Canva.exe"
abrir_app(canvas_app)
