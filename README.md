<h1 align="center">Conexão SFTP com Python</h1>

Primeiramente, para conectar-se ao servidor é necessario incluir os dados do servidor no arquivo config.py mostrado abaixo

```Python
hostname = ''
username = ''
password = ''
port = 00
allow_agent = False
look_for_keys = False
```

Feito isso, basta chamar a função com a operação que deseja fazer, decidir deixar todas as funções no codigo para que cada usuario possa usar de diversas formas possiveis a medida do que for necessario.

A primeira função é para <strong>enviar arquivos para o servidor</strong>, essa função recebe 3 parametros, sendo o primeiro a pasta com os aquivos na sua maquina local, o segundo a extenção dos arquivos que precisão ser enviados e o terceiro a pasta dentro do servidor que os arquivos irão, caso seja necesasrio enviar para a pasta raiz não é necessario o preenchimento do parametro.

```Python
def putFiles(localFiles,extFile,remotePath = ''):
 for file in os.listdir(localFiles): 
   if file.endswith(extFile): 
     sftp.put(localFiles+file,remotePath+file)
     shutil.move(localFiles+file,localFiles+'enviados/'+file)

 files = sftp.listdir('in')
 print(files)
```

A segunda função verifica os arquivos do servidor e printa eles no console, caso os aquivos que deseja puxar esteja dentro de uma pasta do servidor será necessario passar o caminho dessa pasta como paremetro ao chamar a função.

```Python
def printFiles(pasta = ''):
  files = sftp.listdir(pasta)
  print(files)
```

A terceira função pega UM arquivo do servidor (remoteFile) e coloca na sua pasta local (localFile).

```Python
def getFile(remoteFile, localFile):
  sftp.get(remoteFile,localFile)
```

A quarta função delete UM arquivo do servidor(delFile).

```Python
def delFile(delFile):
  sftp.remove(delFile)
  print(delFile+'Deletado')
```

A quinta e última função, deleta todos os arquivos de uma pasta do servior que é passada como parametro, e caso não receba parametros ela deleta todos os aquivos da pasta raiz.

```Python
def delFiles(pasta = ''):
  files = sftp.listdir(pasta)
  print(files)

  for arq in sftp.listdir(pasta):
    sftp.remove(pasta+'/'+arq)

  files = sftp.listdir(pasta)
  print(files)
```
