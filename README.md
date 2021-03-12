# ExeExpress Python
![](https://raw.githubusercontent.com/geniodev/ExeExpress/main/pythonToExe.jpg)</br>
&nbsp;
*Criador de "exe" Express Automatizada Pyhton para produção e debug*</br>
&nbsp;
Linguagem Python</br>




&nbsp;
&nbsp;

*Índices*
&nbsp;
- <a href="https://github.com/geniodev/ExeExpress#exeexpress-python" target="_self">Inicio</a>
- <a href='https://github.com/geniodev/ExeExpress#documenta%C3%A7%C3%A3o' target='_self'>Documentação</a>
  - <a href='https://github.com/geniodev/ExeExpress#como-usar' target='_self'>Como usar</a>
  - <a href='https://github.com/geniodev/ExeExpress#como-funciona' target='_self'>Como funciona</a>
  - <a href='https://github.com/geniodev/ExeExpress#obrigatoriedades--necess%C3%A1rio' target='_self'>Obrigatoriedades / Necessário</a>
  - <a href='https://github.com/geniodev/ExeExpress#modo-debug' target='_self'>Modo Debug</a>
  - <a href='https://github.com/geniodev/ExeExpress#modo-normal' target='_self'>Modo Normal</a>
  - <a href='https://github.com/geniodev/ExeExpress#modo-telaextra' target='_self'>Modo TelaExtra</a>
  - <a href='https://github.com/geniodev/ExeExpress#sobre' target='_self'>Sobre</a>
  - <a href='https://github.com/geniodev/ExeExpress#considera%C3%A7%C3%A3o-final' target='_self'>Consideração Final</a>




&nbsp;
# Documentação</br>


&nbsp;
#### Como usar:</br>
&nbsp;
Crie uma pasta e coloque todo o seu projeto e arquivos nele.</br>
Copie um dos arquivos "InstallDebugInvisivel.exe"/"InstallNormalInvisivel.exe"/"InstallTelaExternaInvisivel.exe" para a pasta dos seu projeto.</br>
Clique no arquivo executável.</br>
&nbsp;
&nbsp;

&nbsp;
#### Como funciona:</br>
&nbsp;
O sistema de gerar o executável é automatico, se existir somente 1 arquivo .py onde estiver o gerador, então este será considerado o projeto, caso contrário ele irá perguntar na tela.</br>
Ao executar um dos Install python ("InstallDebugInvisivel.exe", "InstallNormalInvisivel.exe", "InstallTelaExternaInvisivel.exe") dentro da sua pasta de projeto.</br>
o aplicativo irá procurar pelo ambiente virtual do anaconda em sua maquina e instalar automaticamente as bibliotecas abaixo:</br>
  "pywin32", "pypiwin32", "pefile", "pyinstaller".</br>
após as bibliotecas instaladas terá inicio da construção automatizada do processos. Leia os "Modo" abaixo para melhor entendimento.</br>
sera pergutando qual projeto Principal caso tenha mais de 2 arquivos python no mesmo diretorio, caso não encontre o ambiente virtual ele tentará colocar o ambiente virtual padrão do anaconda, caso não encontre ele perguntará.</br>
No final se tudo ocorrer bem, terá uma pasta e dentro dela o executavel ou o proprio arquivo executável em um só.</br>
&nbsp;
&nbsp;



&nbsp;
#### Obrigatoriedades / Necessário</br>
&nbsp;
Ter o anaconda instalado e anexado ao seu path do sistema.</br>
Ter somente 1 ambiente virtual criado no anaconda, o ambiente "base" padrão será carregado caso não encontre o ambiente virtual do seu projeto.</br>
Não mudar o nome dos arquivos que irão executar a instalação(contem Install e é .exe), senão o sistema para.</br>
&nbsp;
&nbsp;




&nbsp;
#### Modo Debug</br>
&nbsp;
arquivo: "InstallDebugInvisivel.exe"</br>
Função: Liga o Modo Debug e Console. Usado para saber se a aplicação está importando as bibliotecas e executando sem erros internos.</br>
Função Extra: Empacota arquivos e pastas dentro do seu projeto.</br>
Codificação: Testado</br>
&nbsp;
&nbsp;



&nbsp;
#### Modo Normal</br>
&nbsp;
arquivo: "InstallNormalInvisivel.exe"</br>
Função: Não liga o modo Debug, mas liga o modo console. Usado quando seu aplicativo não possui telas para funcionar. Uso padrão para aplicação com unico arquivo sendo Pyhton.</br>
Função Extra. Cria um executável único complemtamente empacotado em um unico arquivo.</br>
Obs: não empacota arquivos ou dll's dentro do projeto. Somente o Arquivo de Extensão Python.</br>
Codificação: Testado
&nbsp;
&nbsp;




&nbsp;
#### Modo TelaExtra</br>
&nbsp;
arquivo: "InstallTelaExternaInvisivel.exe"
Função: Desliga modo Debug e Console. Usado para aplicativo já testado no Debug. Uso para Entrega ou produção Final.
Obs: É necessário o aplicativo ter telas próprias, senão ira acarretar em error.
Codificação: Não Testado
&nbsp;
&nbsp;




&nbsp;
#### Sobre:</br>
&nbsp;
Desenvolvimento Atual:</br>
os instaladores são como Templates prontos.</br>
Ainda não possui a codificação para inclementar as Dll's que você colocar de forma extra ao empacotamento.</br>
Ele não empacota os arquivos dentro do projeto. Futuramente irá implementar.</br>
A Bibliteca "PyInstaller" busca as dependencias de forma automatizada.</br>
&nbsp;
&nbsp;






&nbsp;
#### Consideração Final</br>
&nbsp;
1-Não sou responsável por erros que venha acontecer com a instalação ou falha em execuções por causa de arquivos ou dll ou outros motivos. Cada projeto tem suas peculiaridades e são infinitas.</br>
2-O Projeto não está perfeitamente completo, leia sobre o "Desenvolvimento Atual:"</br>
3-O projeto visa automatizar muitas funções que o usuario faria manualmente, mas que a biblioteca "PyInstaller" possui porem desconhecidas por grande parte dos profissionais.</br>
4-O projeto seria como um template para criar executaveis de forma automatizada, porem necessita de testes e de orientação com um profissional.</br>
&nbsp;
&nbsp;




&nbsp;
<h6 align="center">Desenvolvedor: RA (Ricardo Andrade)</h6>
<h6 align="center">Versão: Versão: 2.0.0</h6>
