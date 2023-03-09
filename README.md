# APS2_ALGLIN

Esse é um projeto da matéria de Algebra Linear e Teoria da Informação do Insper para o curso de Ciência da Computação.

## Integrantes
Ale Wever e Sergio Ramella

## Descrição do Projeto
O projeto consiste em reproduzir, com funções em python e manipulação de matrizes, a máquina enigma de codificação de mensagens feita pelos alemães na Segunda Guerra Mundial. 

## Descrição Matemática de cada função
### Função para_one_hot
A função para_one_hot recebe uma string e retorna uma matriz de zeros e uns, onde cada letra da string é representada por uma linha da matriz, e cada coluna da matriz representa uma letra do alfabeto. A letra da string é representada por um 1 na coluna correspondente a ela no alfabeto, e 0 nas demais colunas.

Através da utilizacão de uma string alfabeto, que contém todas as letras do alfabeto, é possível percorrer cada letra da mensagem recebida e verificar se ela está presente na string alfabeto, se estiver, nós buscamos o índice correspondente em uma matriz identidade com o número de linhas e colunas igual ao tamanho da string alfabeto e adicionamos a linha correspondente em uma lista, após adicionar todas as linhas correspondete na lista, nós transformamos a lista em uma matriz com "np.array" e retornamos sua matriz transposta. 

### Função to_string
A função to_string recebe uma matriz de zeros e uns e retorna uma string, onde cada linha da matriz é representada por uma letra da string, e cada coluna da matriz representa uma letra do alfabeto. A letra da string é representada por um 1 na coluna correspondente a ela no alfabeto, e 0 nas demais colunas.

Para a função to_string, nós utilizamos a mesma string alfabeto para percorrer cada linha da matriz transposta e verificar se ela contém um 1, se contém, nós adicionamos a letra correspondente na string que será retornada.

### Função cifrar 
A função cifrar recebe uma string e uma matriz de zeros e uns, e retorna uma string, onde cada letra da string é representada por uma linha da matriz, e cada coluna da matriz representa uma letra do alfabeto. A letra da string é representada por um 1 na coluna correspondente a ela no alfabeto, e 0 nas demais colunas.

A função cifrar recebe uma string e uma matriz permutação,primeiramente a string é transformada em uma matriz one hot, através da função para_one_hot, em seguida, é feita uma multiplicão de matrizes entre a matriz one hot da mensagem recebida e a matriz permutação, onde utilizamos o método "np.roll()" para embaralhar os elementos da matriz. Depois, essa matriz resultante é transformada em string com a função para_string e essa nova string é retornada.

### Função decifrar
A função decifrar recebe uma string e uma matriz de zeros e uns, e retorna uma string, onde cada letra da string é representada por uma linha da matriz, e cada coluna da matriz representa uma letra do alfabeto. A letra da string é representada por um 1 na coluna correspondente a ela no alfabeto, e 0 nas demais colunas.

A função decifrar recebe uma string e uma matriz permutação,primeiramente a string é transformada em uma matriz one hot, através da função para_one_hot, em seguida, é utilizado o método "np.linalg.solve()", que realiza a multiplicação entre a matriz da mensagem recebida e a matriz inversa da matriz permutação. Depois, essa matriz resultante é transformada em string com a função para_string e essa nova string é retornada.

### Função enigma
A função enigma recebe uma string e uma lista de matrizes de zeros e uns, e retorna uma string, onde cada letra da string é representada por uma linha da matriz, e cada coluna da matriz representa uma letra do alfabeto. A letra da string é representada por um 1 na coluna correspondente a ela no alfabeto, e 0 nas demais colunas.

A função enigma recebe uma string, uma matriz permutação e uma matriz auxiliar. 

### Função de_enigma
A função de_enigma recebe uma string e uma lista de matrizes de zeros e uns, e retorna uma string, onde cada letra da string é representada por uma linha da matriz, e cada coluna da matriz representa uma letra do alfabeto. A letra da string é representada por um 1 na coluna correspondente a ela no alfabeto, e 0 nas demais colunas.

## Como rodar o projeto
Para rodar o projeto e testar cada função, basta acessar e rodar o arquivo demo.py, nesse arquivo você pode visualizar cada passo da codificação e decodificação de uma mensagem.

O arquivo app.py é onde está a api do projeto, feita com o framework Flask, para rodar a api basta rodar o arquivo app.py e acessar o link do servidor local. A aplicação recebe uma mensagem através do metodo POST e retorna a mensagem codificada e decodificada.