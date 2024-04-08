# blinder
Sistema Python Simples de Criptografia de Arquivos

Esta aplicação criptografa arquivo e/ou arquivos selecionados de um diretório para outro.
Faz também o processo de descriptografar os arquivos para um outro diretório.
Recomenado criar um diretório para os arquivos que serão criptografados e outro para os arquivos serão descriptografados.
Isso garante que arquivos não sejam sobrepostos e melhora a organização.
Outro ponto altamente importante é que esta aplicação gera um arquivo de chave criptográfica com atributo oculto (em Linux) chamado "filekey.key".
Portanto é necessário manter esse arquivo guardado para que a aplicação a use para criptografar e descriptografar os arquivos.
A perda deste arquivo (chave), impossibilitará descriptografar os arquivos gerados com essa chave.
Iniciar a aplicação sem a chave original, fará com que seja gerada um nova chave, impedindo a descriptografia dos arquivos.
Guarde-a e use-a com a aplicação.

O código fonte possui a versão para Linux e Para MS-Windows (64bits)
A diferença entre os fontes se dá pela característica de como lidam com arquivos ocultos.
No caso do Linux é simplesmente adicionar o caracter "." no início do arquivo/diretório.
Para sistemas MS-Windows é necessário um comando específico para isso. 

Portanto os nomes dos códigos fontes são:

blinder.py (Linux)
blinder_w.py (MS-Windows)

Para facilitar o uso em plataforma MS-Windows, deixei também o binário compilado com o nome blinder_w.exe

Dependências:
PyQT5
cryptography
win32api (MS-Windows)

Desenvolvido por: Mario Medeiros - Disaster Developer
Data: 2024-04-06
Versão: 0.5.0 (Linux)
Versão: 0.5.0-W (MS-Windows - 64bits)
