import subprocess

# Função para abrir um aplicativo
def abrir_app(Outlook):
    try:
        subprocess.Popen(Outlook)
        print(f"Aplicativo {Outlook} aberto com sucesso.")
    except FileNotFoundError:
        print(f"Aplicativo {Outlook} não encontrado.")

# Caminho completo do aplicativo que você deseja abrir
Outlook_app = r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"
abrir_app(Outlook_app)
