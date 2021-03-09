# ExeExpress Python
Criador de "exe" Express Automatizada Pyhton para produção e debug

#Uso
Python

#como usar:
crie uma pasta e coloque todo o seu projeto e arquivos nele.
Copie um dos arquivos "InstallDebugInvisivel.exe"/"InstallNormalInvisivel.exe"/"InstallTelaExternaInvisivel.exe" para a pasta dos seu projeto.
Clique no arquivo executável.


#Como funciona:
O sistema de gerar o executável é automatico, se existir somente 1 arquivo .py onde estiver o gerador, então este será considerado o projeto, caso contrário ele irá perguntar na tela.
Ao executar um dos Install python ("InstallDebugInvisivel.exe", "InstallNormalInvisivel.exe", "InstallTelaExternaInvisivel.exe") dentro da sua pasta de projeto.
o aplicativo irá procurar pelo ambiente virtual do anaconda em sua maquina e instalar automaticamente as bibliotecas abaixo:
"pywin32", "pypiwin32", "pefile", "pyinstaller".
após as bibliotecas instaladas terá inicio da construção automatizada do processos. Leia os "Modo" abaixo para melhor entendimento.
sera pergutando qual projeto Principal caso tenha mais de 2 arquivos python no mesmo diretorio, caso não encontre o ambiente virtual ele tentará colocar o ambiente virtual padrão do anaconda, caso não encontre ele perguntará.
No final se tudo ocorrer bem, terá uma pasta e dentro dela o executavel ou o proprio arquivo executável em um só.


#Obrigatoriedades / Necessário
Ter o anaconda instalado e anexado ao seu path do sistema.
Ter somente 1 ambiente virtual criado no anaconda, o ambiente "base" padrão será carregado caso não encontre o ambiente virtual do seu projeto.
Não mudar o nome dos arquivos que irão executar a instalação(contem Install e é .exe), senão o sistema para.


#Modo Debug
arquivo: "InstallDebugInvisivel.exe"
Função: Liga o Modo Debug e Console. Usado para saber se a aplicação está importando as bibliotecas e executando sem erros internos.
Função Extra: Empacota arquivos e pastas dentro do seu projeto.
Codificação: Testado

#Modo Normal
arquivo: "InstallNormalInvisivel.exe"
Função: Não liga o modo Debug, mas liga o modo console. Usado quando seu aplicativo não possui telas para funcionar. Uso padrão para aplicação com unico arquivo sendo Pyhton.
Função Extra. Cria um executável único complemtamente empacotado em um unico arquivo.
Obs: não empacota arquivos ou dll's dentro do projeto. Somente o Arquivo de Extensão Python.
Codificação: Testado

#Modo TelaExtra
arquivo: "InstallTelaExternaInvisivel.exe"
Função: Desliga modo Debug e Console. Usado para aplicativo já testado no Debug. Uso para Entrega ou produção Final.
Obs: É necessário o aplicativo ter telas próprias, senão ira acarretar em error.
Codificação: Não Testado


#Sobre

Desenvolvimento Atual:
Versão: 2.0.0
os instaladores são como Templates prontos.
Ainda não possui a codificação para inclementar as Dll's que você colocar de forma extra ao empacotamento.
Ele não empacota os arquivos dentro do projeto. Futuramente irá implementar.
A Bibliteca "PyInstaller" busca as dependencias de forma automatizada.


#Consideração Final
1-Não sou responsável por erros que venha acontecer com a instalação ou falha em execuções por causa de arquivos ou dll. Cada projeto tem suas peculiaridades e são infinitas.
2-O Projeto não está completo, leia sobre o "Desenvolvimento Atual:"
3-O projeto visa automatizar muitas funções que o usuario faria manualmente, mas que a biblioteca "PyInstaller" possui porem desconhecidas por grande parte dos profissional.
4-O projeto seria como um template para criar executaveis de forma automatizada, porem necessita de testes e de orientação com um profissional.


Desenvolvedor: RA (Ricardo Andrade)
Versão: 2.0.0
Contato Whatsapp: (64) 9.8138-5940