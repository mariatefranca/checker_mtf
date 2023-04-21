# checker_mtf
Aplicação em python que testa a conectividade de sites.


# Clonando o repositório:
  No prompt de comando do Windows ou o shell do Linux, entre na pasta que deseja clonar o repositório e execute:
 ```
 git clone git@github.com:mariatefranca/mtf-indicium.git
 ```

# Criando o ambiente de trabalho
  O ambiente de trabalho pode ser criado no Windows ou no Linux. 
## No windows:
  Inicie a Prompt de Comando, entre na pasta que deseja criar o repositório do projeto e execute os seguintes comandos:
```
py -m venv .env
```
  Ative o ambiente de trabalho:
```
.env\Scripts\activate
```
## No Linux:
  No Prompt de comandos do Linux, entre na pasta que deseja criar o repositório do projeto e execute os seguintes comandos:
```
 python -m venv .env
```
  Ative o ambiente de trabalho:
```
 source .env/bin/activate
```

# Carregando os pacotes utilizados no projeto atravé do uso de requirements.tx 
  Entre na pasta do repositório criado e execute o comando:
  ```
  pip install -r requirements.txt
  ```
# Rodando o aplicativo sitechecker
  Execute o comando abaixo para receber as intruções de como passar os sites a serem checados:
  ```
  python sitecker -h
  ```
É possivel fornecer as urls diretamente no shell, utilizando -u e digitando quantas URLs desejar:
 ```
 python sitechecker -u nomedosite.com outrosite.com.br

 ```
 É possivel fornecer fornecer um arquivo csv contendo as URLs a serem testas, utilizando -f e digitndo o caminho e nome do arquivo:
  ```
 python sitechecker -f lista.csv

 ```
  
 
 
  
  
