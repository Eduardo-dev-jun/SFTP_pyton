from threading import local
import paramiko
import os
import sys
sys.path.append("/config.py")
import config as config
import shutil


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=config.hostname, username=config.username, password=config.password, port=config.port,allow_agent=config.allow_agent, look_for_keys=config.look_for_keys)

sftp = client.open_sftp()


def putFiles(localFiles,extFile,remotePath = ''):#nome da pasta com os arquivos pra enviar Ex:'mnt/arquivos/'importante a barra no final,extenção dos arquivos a serem enviados,pasta que os itens serão enviados no servidor(se não preenchido envia pra raiz)
 for file in os.listdir(localFiles): #Colocar o caminhos dos aquivos que quer enviar
   if file.endswith(extFile): #Colocar nome da extensão do arquivo que quer enviar
     sftp.put(localFiles+file,remotePath+file)
     shutil.move(localFiles+file,localFiles+'enviados/'+file)#Após copiar o arquivo para o servidor ele envia o arquivo para uma pasta de 'enviados'

 files = sftp.listdir('in')#printa o conteudo do servidor
 print(files)


def printFiles(pasta = ''): #se a função for chamada sem o argumento ela printara a pasta raiz do servidor
  files = sftp.listdir(pasta)
  print(files)


def getFile(remoteFile, localFile):#lembrando que é necessario informar a localização do arquivo Ex:'in/arquivo'
  sftp.get(remoteFile,localFile)#(nome_do_arquivo_remoto, nome_pra_dar_arquivo_local)


def delFile(delFile):#lembrando que é necessario informar a localização do arquivo Ex:'in/arquivo'
  sftp.remove(delFile)#pasta/nome_do_arquivo
  print(delFile+'Deletado')

def delFiles(pasta = ''): #informe o caminho para a pasta que será limpa, Ex: 'in/enviados' irá limpar todos os arquivos da pasta 'enviador' dentro da pasta 'in'
  #printa o conteudo antes e depois de limpar toda a pasta do servidor selecionada
  files = sftp.listdir(pasta)
  print(files)

  for arq in sftp.listdir(pasta):
    sftp.remove(pasta+'/'+arq)

  files = sftp.listdir(pasta)
  print(files)

printFiles('in')
sftp.close()