# checker_mtf
Aplicação em python que testa a conectividade de sites.


# Clonando o repositório:
  No prompt de comando do Windows ou o shell do Linux, entre na pasta que deseja clonar o repositório e execute:
 ```
 git clone git@github.com:mariatefranca/mtf-indicium.git
 ```

# Criando o ambiente de trabalho
  O ambiente de trabalho pode ser criado no Windows ou no Linux. 
## No Windows:
  Inicie a Prompt de Comando, entre na pasta do repositório do projeto e execute os seguintes comandos:
```
py -m venv .env
```
  Ative o ambiente de trabalho:
```
.env\Scripts\activate
```
## No Linux:
  No shell do Linux, entre na pasta do projeto e execute os seguintes comandos:
```
 python3 -m venv .env
```
  Ative o ambiente de trabalho:
```
 source .env/bin/activate
```

# Instalando os pacotes utilizados no projeto através do arquivo requirements.txt
  Entre na pasta do repositório criado e execute o comando:
  ```
  pip install -r requirements.txt
  ```

# Rodando o aplicativo sitechecker manualmente
  Execute o comando abaixo no shell para receber as intruções de como passar os sites a serem checados. Caso voc6e utilize a linha de comando do Windows substitua '`python` por `py` nos comandos abaixo.
  ```
  python -m sitechecker -h
  ```
  É possivel fornecer as urls diretamente na linha de comando, utilizando -u e digitando quantas URLs desejar:

```
python -m sitechecker -u nomedosite.com outrosite.com.br
```
 
  É possível fornecer fornecer um arquivo csv contendo as URLs a serem testas, utilizando -f e digitndo o caminho e nome do arquivo:
 
```
python -m sitechecker -f lista.csv
```
 
 # Rodando o sitechecker uma vez por dia usando o cron
 
  No shell do Linux, execute o comando:
```
./install_checker.sh
```

  O script está programado para verificar as URLs que estão no arquivo `cron_urls.csv` todo dia às 23 horas. Você pode editar esse arquivo com as URLs que deseja.

