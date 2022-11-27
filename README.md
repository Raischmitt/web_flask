## Projeto web com framework flask

##### criado por: Raissa Schmitt Joaquim 


##### Iniciando projeto:

1. Criando ambiente virtual python
  ```$ python3 -m venv venv ```

2. Ativando o ambiente virtual e instalando as dependencias
  - ativando ambiente virtual
    - linux  
    ```$ source venv/bin/activate```
    - windows
    ```$ .\venv\Scripts\activate```
  - instalando dependencias
    ```$ pip install -r requeriments.txt```

3. configurando banco de dados
  ```$ flask --app src init-db```

4. iniciando servidor
  ```$ flask --app src --debug run```

5. acessar pagina inicial (http://127.0.0.1:5000/)