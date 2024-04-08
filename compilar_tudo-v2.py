import PyInstaller.__main__

# Solicitar ao usuário o nome da aplicação
app_name = input("Digite o nome da aplicação: ")

# Perguntar ao usuário se deseja uma aplicação com interface gráfica (--windowed)
use_windowed = input("Deseja uma aplicação com interface gráfica? (S/N): ").lower() == 's'

# Construir a lista de argumentos para o PyInstaller
args = [
    app_name + '.py',  # Usar o nome fornecido pelo usuário
    '--onefile'
]

# Adicionar '--windowed' à lista de argumentos se o usuário escolheu uma aplicação com interface gráfica
if use_windowed:
    args.append('--windowed')

# Executar o PyInstaller com os argumentos construídos
PyInstaller.__main__.run(args)
