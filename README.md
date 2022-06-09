<div align="center" style="flex-direction: column;">
  <h1>Processador de Imagens</h1>
  <p>Trabalho de descrição de um processador digital de imagens feito por Daniel Sansão Araldi e Jonathas Meine</p>
  <img src="https://wakatime.com/badge/user/920a7e43-2969-4212-82ff-1b375685ff58/project/e877a31b-05a9-4ed4-ad82-f9ed7df1bd35.svg" title="Wakatime" alt="Wakatime"/>
</div>

<hr></hr>

### Como executar

1. Na raiz do projeto.
2. Execute o seguinte comando abaixo:

```sh
python main.py
```

<hr></hr>

### Descrição do Trabalho

#### Introdução

Nosso trabalho foi desenvolvido em torno da conversão de imagens RGB para grayscale ponderado. Abaixo iremos descrever as etapas de execução do código para a conversão da imagem em grayscale.

#### Etapas:

1. **Bibliotecas**: Realizamos a instalação das bibliotecas [OpenCV](https://opencv.org/) e [Numpy](https://numpy.org/). A OpenCV é a biblioteca que utilizamos para lidar com o processamento de imagens e o Numpy é a biblioteca que utilizamos para processar grande quantidade de dados númericos multidimensionais. Realizamos a importação de ambas as bibliotecas usando a sintaxe de `import <nome_da_biblioteca>` no código, com isso, podemos trabalhar com suas funções.

2. **Leitura da Imagem**: Criamos uma varíavel chamada `image` que irá receber o valor da imagem. Usamos a função `imread` da biblioteca OpenCV para retornar o valor da imagem a varíavel `image`. A função `imread` faz a leitura de uma imagem, apenas passando o caminho de onde está o arquivo da imagem a ser lida.

3. **Separação do Valores RGB**: Definimos três novas variáveis, chamadas `blue`, `green` e `red`, que irão receber o valor de uma matriz retornada pela função `split` da biblioteca OpenCV, que separa um `array` de várias matrizes para matrizes únicas separadas. Assim, no nosso caso, são separadas as matrizes correspondentes às proporções de RGB da imagem para trabalhar com cada escala de cor de modo diferente.

4. **Cálculo da Imagem para Grayscale**: Temos uma varíavel chamada `imageGrayscalePondered` que irá receber a matriz que correspondente ao grayscale da imagem, a partir do cálculo realizado com as proporções de RGB (das varíaveis `blue`, `green` e `red`). Recorremos a função `array` da biblioteca Numpy para criar um novo `array` de matrizes, a partir da varíável `imageGrayscalePondered` e forçamos que o tipo dos valores das matrizes do `array` será `uint8` (um inteiro de 8 bits). Sendo assim, é atribuído o valor desse `array` de matrizes a variável `imageGrayscalePondered`.

5. **Mostrar a Imagem**: Por fim, usamos a função `imshow` do OpenCV para mostrar a imagem convertida em grayscale. Adicionamos a função `waitKey` que espera o clique de alguma tecla, para assim, executar a função `destroyAllWindows` logo abaixo (também são funções da biblioteca OpenCV), que irá fechar a janela que esta exibindo a imagem e finalizar a execução do código.

<hr></hr>

**Obs.:** Nós mudamos os nomes das variáveis e das imagens originais para ficarem autoexplicativas. Não mudamos nada da lógica do código, apenas explicamos.
