import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QMessageBox, QTextEdit, QSplashScreen, QDialog, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from cryptography.fernet import Fernet

# Nome do arquivo da chave
key_file = '.filekey.key'

# Verifica se o arquivo da chave existe, se não, gera uma nova chave e salva no arquivo
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as filekey:
        filekey.write(key)

# Carrega a chave do arquivo
with open(key_file, 'rb') as filekey:
    key = filekey.read()
cipher = Fernet(key)

class CryptoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Blinder')
        self.setGeometry(100, 100, 400, 200)

        self.centralWidget = QTextEdit()
        self.setCentralWidget(self.centralWidget)

        menu = self.menuBar()
        arquivo_menu = menu.addMenu('Arquivo')

        criptografar_action = QAction('Criptografar Arquivos', self)
        criptografar_action.triggered.connect(self.criptografar_arquivos)
        arquivo_menu.addAction(criptografar_action)

        descriptografar_action = QAction('Descriptografar Arquivos', self)
        descriptografar_action.triggered.connect(self.descriptografar_arquivos)
        arquivo_menu.addAction(descriptografar_action)

        arquivo_menu.addSeparator()

        sair_action = QAction('Sair', self)
        sair_action.triggered.connect(self.close)
        arquivo_menu.addAction(sair_action)

        sobre_action = QAction('Sobre', self)
        sobre_action.triggered.connect(self.exibir_sobre)
        arquivo_menu.addAction(sobre_action)

        instrucoes_action = QAction('Instruções de Uso', self)
        instrucoes_action.triggered.connect(self.exibir_instrucoes)
        arquivo_menu.addAction(instrucoes_action)

    def criptografar_arquivos(self):
        dialogo = QFileDialog()
        dialogo.setFileMode(QFileDialog.ExistingFiles)
        arquivos, _ = dialogo.getOpenFileNames(self, 'Selecionar Arquivos para Criptografar',
                                               filter='Todos os arquivos (*.*)')
        if not arquivos:
            return

        diretorio_destino = QFileDialog.getExistingDirectory(self, 'Selecionar Diretório de Destino')

        for arquivo_origem in arquivos:
            with open(arquivo_origem, 'rb') as f_origem:
                dados = f_origem.read()
                dados_criptografados = cipher.encrypt(dados)
                nome_arquivo, extensao = os.path.splitext(os.path.basename(arquivo_origem))
                arquivo_destino = os.path.join(diretorio_destino, nome_arquivo + extensao + '.mm')
                with open(arquivo_destino, 'wb') as f_destino:
                    f_destino.write(dados_criptografados)

        QMessageBox.information(self, 'Sucesso', 'Arquivos criptografados com sucesso.')

    def descriptografar_arquivos(self):
        dialogo = QFileDialog()
        dialogo.setFileMode(QFileDialog.ExistingFiles)
        arquivos, _ = dialogo.getOpenFileNames(self, 'Selecionar Arquivos para Descriptografar',
                                               filter='Todos os arquivos (*.*)')
        if not arquivos:
            return

        diretorio_destino = QFileDialog.getExistingDirectory(self, 'Selecionar Diretório de Destino')

        for arquivo_origem in arquivos:
            with open(arquivo_origem, 'rb') as f_origem:
                dados = f_origem.read()
                dados_descriptografados = cipher.decrypt(dados)
                nome_arquivo, extensao = os.path.splitext(os.path.basename(arquivo_origem))
                nome_arquivo_sem_mm = nome_arquivo.replace('.mm', '')
                arquivo_destino = os.path.join(diretorio_destino, nome_arquivo_sem_mm)
                with open(arquivo_destino, 'wb') as f_destino:
                    f_destino.write(dados_descriptografados)

        QMessageBox.information(self, 'Sucesso', 'Arquivos descriptografados com sucesso.')

    def exibir_sobre(self):
        texto_sobre = "Blinder\n\n\
Aplicativo para criptografar e descriptografar arquivos.\n\n\
Desenvolvedor: Mario Medeiros\n\
Data: 2024-04-06\n\
Versão: 0.5.0"
        self.centralWidget.setText(texto_sobre)

    def exibir_instrucoes(self):
        dialogo = QDialog(self)
        dialogo.setWindowTitle('Instruções de Uso')
        layout = QVBoxLayout()
        texto = QLabel('Esta aplicação criptografa arquivo e/ou arquivos selecionados de um diretório para outro.\n\
Faz também o processo de descriptografar os arquivos para um outro diretório.\n\
Recomenado criar um diretório para os arquivos que serão criptografados e outro para os arquivos serão descriptografados.\n\
Isso garante que arquivos não sejam sobrepostos e melhora a organização.\n\n\
Outro ponto altamente importante é que esta aplicação gera um arquivo de chave criptográfica com atributo oculto (em Linux) chamado "filekey.key".\n\
Portanto é necessário manter esse arquivo guardado para que a aplicação a use para criptografar e descriptografar os arquivos.\n\n\
A perda deste arquivo (chave), impossibilitará descriptografar os arquivos gerados com essa chave.\n\
Iniciar a aplicação sem a chave original, fará com que seja gerada um nova chave, impedindo a descriptografia dos arquivos.\n\
Guarde-a e use-a com a aplicação.\n\n\
                       Mario Medeiros\n\
                       Disaster Developer\n\
                       Data: 2024-04-06')
        layout.addWidget(texto)
        dialogo.setLayout(layout)
        dialogo.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Carregar a imagem da splash screen
    splash_pix = QPixmap('splash_blinder.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()

    # Exibir a splash screen por 3 segundos
    QTimer.singleShot(3000, splash.close)

    window = CryptoApp()
    window.show()
    sys.exit(app.exec_())
