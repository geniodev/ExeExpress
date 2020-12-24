
import os
import subprocess

#Bat final para instalador
bat = ""

ambvir = os.path.join( os.getcwd(), "ambvir.txt" )
print(ambvir)
print("---")
print(os.path.isfile(ambvir))

if ( os.path.isfile(ambvir) ):
    Tamb = open(ambvir, "r", encoding='UTF-8').read()
    print(Tamb)
    ambvir = Tamb
    if ( len( Tamb ) == 0):
        ambvir = input("Digite o nome do ambiente Virtual: \n")
        print("Ambvir: ", ambvir)

else:
    ambvir = input("Digite o nome do ambiente Virtual: \n")
    print("Ambvir: ", ambvir)

bat = bat + "@call activate " + str( ambvir ) + chr(10)
print("bat: ", bat)

bat = bat + str( os.getcwd() ).split(":")[0] + ":" + chr(10)
bat = bat + 'cd "' + str( os.getcwd() ) + '"' + chr(10)


ReqBase = ["pywin32", "pypiwin32", "pefile", "pyinstaller" ] #Requerimentos(bibliotecas) a instalar no ambiente virtual


for pit in ReqBase:
    bat = bat + "@call pip install " + pit + chr(10)


#Carregar o nome do projeto principal



import glob
pyonload = glob.glob( '*.py')
print(pyonload)
print("...")

#Eliminar o Arquivo Atual em execução "Install.py"
NListpy = []
for eli in pyonload:
    if "install" in eli.lower():
        pass
    else:
        NListpy.append( eli )

pyonload = NListpy  



#Puxa os arquivos no caso se tiver somente 1 arquivo python, senão ele procura no arquivo "pyprincpal"
if ( len( pyonload ) == 1):
    py_principal = str( pyonload[0] )

else:

    py_principal = os.path.join( os.getcwd(), "pyprincipal.txt" )
    print(py_principal)
    print("---")
    #print(os.path.isfile(py_principal))

    if ( os.path.isfile(py_principal) ):
        Tamb = open(py_principal, "r", encoding='UTF-8').read()
        print(Tamb)
        py_principal = Tamb
        if ( len( Tamb ) == 0):
            py_principal = input("Digite o nome do ambiente Virtual: \n")
            print("py_principal: ", py_principal)

    else:
        py_principal = input("Digite o nome do Arquivo Principal do Python: \n")
        print("py_principal: ", py_principal)


    #add extensão caso não esteja presente
    if ".py" in py_principal:
        pass
    else:
        py_principal = str(py_principal) + ".py"


## nao vai precisar criar o arquivo spec para alterar, usar direto no aqruivo py
#add comando para criar ".spec" do arquivo principal
#bat = bat + "@call pyi-makespec {}".format( str(py_principal) + chr(10) )

print("bat2: ", bat)
#--- agora colocar pra iniciar o projeto spec antes de add

#Criar e Executar o arquivo de Instalação bat
#bat = bat + "exit"


#Spec = open( "install.bat", "w" ).write(bat)

#subprocess.Popen("cmd install.bat")
#subprocess.call("install.bat")
#os.startfile(   os.path.join( os.getcwd() , "install.bat")    )
#os.startfile("cmd")

#Iniciando o projeto desabilitar o Debug e o Painel do CMD
#ou habilitar o modo Debug

"""
print("Execute 'install.txt' no seu cmd (Linha por Linha) e aparecera um arquivo .spec")
deb = input("Aperte Enter:")
"""

#Abrir o arquivo spec para mudar

#Spec = open( str(py_principal).replace(".py", ".spec"), "r", encoding="UTF-8" ).read()



"""# ------------Buscar arquivos no diretorio para colocar junto com a comptactação ...
##  nos includes
FullInclude = os.listdir( os.getcwd())

#Eliminar os arquivos padroes
NFull = []
for aiu in FullInclude:
    if "install" in aiu.lower():
        continue

    if "dll" in aiu.lower():
        continue
    
    elif "criarexe.bat" in aiu.lower():
        continue
    
    elif "ambvir.txt" in aiu.lower():
        continue
    
    elif ".dll" in aiu.lower():
        continue
    
    elif ".spec" in aiu.lower():
        continue
    
    elif ".so" in aiu.lower():
        continue
    
    elif str(py_principal).lower() in aiu.lower():
        continue
    
    else:
        NFull.append(aiu)

if ( len( NFull ) == 0):
    print("lista 'Data' Nula")
    Spec2 = open( str(py_principal).replace(".py", ".spec"), "r", encoding="UTF-8" ).read()
else:
    
    Spec2 = open( str(py_principal).replace(".py", ".spec"), "r", encoding="UTF-8" ).read()
    
    IncludeFull = ""
    for aup in NFull:
        IncludeFull = IncludeFull + (chr(34) +  str( os.path.join( os.getcwd(),  aup ) ) + chr(34) + ", ")
    
    IncludeFull = IncludeFull[:-2:]
    IncludeFull = IncludeFull.replace( chr(47), chr(92) ) #Substitui barra inversa pra nomral
    IncludeFull = IncludeFull.replace( chr(92), chr(92)+chr(92) )  #Substitui \ por \\
    
    AtuSpec2 = Spec2.replace("datas=[]", "datas=[{}]".format(IncludeFull))

    #open( str(py_principal).replace(".py", ".spec")  , 'w'  ).write(AtuSpec2)



#---------------------------  Incluir arquivo Txt das Dll's a acrescentar no programa

Dlllist = []

for aan in FullInclude:
    if ( "dll" in aan ):
        if ( "." in aan):
            pass
        else:
            Dlllist.append( aan  )

#Verifica se tem uma pasta com nome dll
## Se estiver buscar arquivo txt para nomes e inclementar
if ( len(Dlllist) == 0 ):
    pass
else:
    FullDll = os.listdir( os.path.join (os.getcwd(), Dlllist[0])  )
    
    DllsInc = open( os.path.join( os.getcwd(), str(Dlllist[0]), FullDll[0]), "r", encoding='UTF-8').readlines()
    
    FullWriteDll = ""
    for akkk in DllsInc:
        FullWriteDll = FullWriteDll + ( chr(34) +  str( akkk.replace( chr(10), "" ) )  + chr(34) + ", ")
    
    FullWriteDll = FullWriteDll[:-2:]
    FullWriteDl = FullWriteDll.replace( chr(47), chr(92) ) #Substitui barra inversa pra nomral
    FullWriteDl = FullWriteDll.replace( chr(92), chr(92)+chr(92) )  #Substitui \ por \\



    #Usar arquivo já aberto do AtuSpec2 para mudar
    try:
        AtuSpec2 = AtuSpec2.replace("binaries=[]", "binaries=[{}]".format(FullWriteDll))
    except Exception:
        AtuSpec2 = str( Spec2 )
        AtuSpec2 = AtuSpec2.replace("binaries=[]", "binaries=[{}]".format(FullWriteDll))


#Gravar Spec completo cmo Binaries(Dlls), e arquivos comuns(datas)
try:
    open( str(py_principal).replace(".py", ".spec")  , 'w'  ).write(AtuSpec2)
except Exception:
    open( str(py_principal).replace(".py", ".spec")  , 'w'  ).write(Spec2)



"""
#Arquivo Spec já configurado, agora executar o restante do PyInstaller
#bat = ""
#bat = bat + "@call activate {}{}".format(ambvir, chr(10))

#bat = bat + str( os.getcwd() ).split(":")[0] + ":" + chr(10)
#bat = bat + 'cd "' + str( os.getcwd() ) + '"' + chr(10)

bat = bat + "@call pyInstaller {} -F {}".format( str(py_principal), chr(10) )
bat = bat + "exit"
open( "criarexe.bat"  , 'w'  ).write(bat)



os.startfile(   os.path.join( os.getcwd() , "criarexe.bat")    )
#os.startfile("cmd")


#input("Apos executar tudo, feche os arquivos abertos e aperte enter aqui")
#Remover os arquivos desnecessários
try:
    os.remove( "install.bat" )
except Exception:
    pass


try:
    os.remove( "criarexe.bat" )
except Exception:
    pass

try:
    os.remove( "ambvir.txt" )
except Exception:
    pass





##Diretorios Inuteis da Instalação - Remover
try:
    os.remove( str(py_principal).replace(".py", ".spec") )      #Rem Arq .spec
except Exception:
    pass


#reve o diretorio "build" desneessário
import shutil
pathTest = str ( os.path.join( os.getcwd(), "build" ) )

try:
    shutil.rmtree(pathTest)
except OSError as e:
    print(e)
else:
    print("The directory is deleted successfully")
    

#revemo o pacote cache gerado pelo python
pathTest = str ( os.path.join( os.getcwd(), "__pycache__" ) )

try:
    shutil.rmtree(pathTest)
except OSError as e:
    print(e)
else:
    print("The directory is deleted successfully")



#Mover o Arquivo pronto e retirar da pasta 'Dist'
Exepath = str ( os.path.join( os.getcwd(), "dist", py_principal.split(".")[0]  ) )
shutil.move(Exepath, str( os.getcwd() ))


#Remover a pasta Dist que continha a pasta do arquivo em executavel
pathTest = str ( os.path.join( os.getcwd(), "dist" ) )

try:
    shutil.rmtree(pathTest)
except OSError as e:
    print(e)
else:
    print("The directory is deleted successfully")