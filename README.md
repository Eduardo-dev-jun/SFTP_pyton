<h1 align="center">Conecxão SFTP com Python</h1>

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
def printFiles(pasta = ''): #se a função for chamada sem o argumento ela printara a pasta raiz do servidor
  files = sftp.listdir(pasta)
  print(files)
```
