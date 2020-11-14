---
title: "Olá Triângulo"
date: 2020-10-29T15:28:58-03:00
draft: false
katex: true
markup: "mmark"
---


Na OpenGL tudo está no espaço 3D, mas a tela ou janela é uma matriz 2D de pixels, então uma grande parte do trabalho da OpenGL é transformar todas as coordenadas 3D em pixels 2D que cabem na sua tela. O processo de transformação de coordenadas 3D em pixels 2D é gerenciado pelo {{<definition " pipeline  gráfico " >}} ( {{<english  " graphic pipeline " >}}) da OpenGL. O pipeline gráfico pode ser dividido em duas grandes partes: a primeira transforma suas coordenadas 3D em coordenadas 2D e a segunda transforma as coordenadas 2D em pixels coloridos. Neste capítulo, discutiremos brevemente o pipeline gráfico e como podemos usá-lo a nosso favor para criar pixels sofisticados.

O pipeline gráfico recebe como entrada um conjunto de coordenadas 3D e as transforma em pixels 2D coloridos na tela. Ele pode ser dividido em várias etapas onde cada etapa requer a saída da etapa anterior como sua entrada. Todas essas etapas são altamente especializadas (têm uma função específica) e podem ser facilmente executadas em paralelo. Por causa de sua natureza paralela, as placas gráficas de hoje têm milhares de pequenos núcleos de processamento para processar rapidamente seus dados dentro do pipeline gráfico. Os núcleos de processamento executam pequenos programas na GPU para cada etapa do pipeline. Esses pequenos programas são chamados de {{<definition " shaders " >}}.

Alguns desses shaders são configuráveis, o que nos permite escrever nossos próprios shaders para substituir os shaders existentes. Isso nos dá um controle muito mais refinado sobre partes específicas do pipeline e, como elas são executadas na GPU, também podem economizar um valioso tempo de CPU. Os shaders são escritos em {{<definition " OpenGL  Shading  Language " >}} ({{<definition " GLSL " >}}) e vamos nos aprofundar mais nisso no próximo capítulo.



Abaixo você encontrará uma representação abstrata de todos os estágios do pipeline gráfico. Observe que as seções em azul representam seções onde podemos injetar nossos próprios shaders.

![altlogo](https://learnopengl.com/img/getting-started/pipeline.png)

Como você pode ver, o pipeline gráfico contém um número grande de seções em que cada uma lida com uma parte específica da conversão dos dados dos seus vértices em um pixel totalmente renderizado. Explicaremos resumidamente cada parte do pipeline de uma forma simplificada para fornecer uma boa visão geral de como o pipeline funciona.

Como entrada do pipeline gráfico, passamos uma lista de três coordenadas 3D que devem formar um triângulo em um {{<english  " array " >}} aqui chamado de **Vertex Data**; esse _vertex data_ é uma coleção de vértices. Um {{<definition " vértice " >}} ( {{<definition " vertex " >}}) é uma coleção de dados por coordenada 3D. Os dados de cada vértice são representados por {{<definition " atributos  de  vértice " >}} ( {{<definition " vertex  attributes " >}}) que podem conter quaisquer dados que desejarmos, mas para simplificar vamos assumir que cada vértice consiste em apenas uma posição 3D e algum valor de cor.

{{% greenbox %}}
Para que a OpenGL saiba o que fazer com sua coleção de coordenadas e valores de cor, você deve indicar a natureza dos tipos de renderização que deseja formar com os dados. Queremos os dados renderizados como uma coleção de pontos, uma coleção de triângulos ou talvez apenas uma longa linha? Essas dicas são chamadas de {{<definition " primitivas " >}} ({{<definition " primitives " >}}) e são fornecidas a OpenGL ao chamar qualquer um dos comandos de desenho. Algumas dessas dicas são {{<variable GL_POINTS>}}, {{<variable GL_TRIANGLES>}} e {{<variable GL_LINE_STRIP>}}.
{{% /greenbox %}}

A primeira parte do pipeline é o {{<definition " shader  de  vértice " >}} ( {{<definition " vertex  shader " >}}) que recebe como entrada um único vértice. O objetivo principal do shader de vértice é transformar coordenadas 3D em diferentes coordenadas 3D (mais sobre isso mais tarde) e também nos permite fazer algum processamento básico nos atributos de vértice.

O estágio de {{<definition " montagem  de  primitivas " >}} ( {{<definition " primitive  assembly " >}}) recebe como entrada todos os vértices (ou vértice se {{<variable GL_POINTS>}} for escolhido) do shader de vértice que pertencem a uma primitiva e reúne todos os pontos para formar a primitiva fornecida; neste caso, um triângulo.

A saída do estágio de montagem de primitivas é passada para o {{<definition " shader  de  geometria " >}} ( {{<definition " geometry  shader " >}}). O shader de geometria recebe como entrada uma coleção de vértices que formam uma primitiva e tem a capacidade de gerar outras formas, emitindo novos vértices para formar novas (ou outras) primitivas. Neste caso de exemplo, ele gera um segundo triângulo com a forma fornecida.

A saída do shader de geometria é então passada para o {{<definition " estágio  de  rasterização " >}} ( {{<definition " rasterization  stage " >}}), onde mapeia a(s) primitiva(s) resultante(s) para os pixels correspondentes na tela final, resultando em fragmentos para o shader de fragmento usar. Antes que os shaders de fragmento sejam executados, um {{<definition " recorte " >}} ( {{<definition " clipping " >}}) é executado. O clipping descarta todos os fragmentos que estão fora de sua visão, aumentando o desempenho.

{{% notice tip %}}
Um fragmento em OpenGL são todos os dados necessários para que a OpenGL renderize um único pixel.
{{% /notice %}}

O principal objetivo do {{<definition " shader  de  fragmento " >}} ( {{<definition " fragment  shader " >}}) é calcular a cor final de um pixel e geralmente é o estágio em que todos os efeitos OpenGL avançados ocorrem. Normalmente, o shader de fragmento contém dados sobre a cena 3D que pode usar para calcular a cor final do pixel (como luzes, sombras, cor da luz e assim por diante).

Depois que todos os valores de cor correspondentes foram determinados, o objeto final passará por mais um estágio que chamamos de {{<definition " teste  alfa " >}} ( {{<definition " alpha  test " >}}) e estágio de {{<definition " mistura " >}} ( {{<definition " blending " >}}). Este estágio verifica o valor de profundidade ( {{<english  " depth " >}}) (e estêncil ( {{<english  " stencil " >}})) correspondente (veremos mais tarde) do fragmento e os usa para verificar se o fragmento resultante está na frente ou atrás de outros objetos e portanto ser descartado ou não. O estágio também verifica os valores {{<definition " alfa " >}} (os valores alfa definem a opacidade de um objeto) e combina ( {{<definition " blend " >}}) os objetos de acordo. Portanto, mesmo que a cor de saída de um pixel seja calculada no shader de fragmento, a cor final do pixel ainda pode ser algo totalmente diferente ao renderizar vários triângulos.

Como você pode ver, o pipeline gráfico é bastante complexo e contém muitas partes configuráveis. Porém, para quase todos os casos, só temos que trabalhar com os shaders de vértice e fragmento. O shader de geometria é opcional e geralmente configurado em seu padrão. Há também o estágio de tesselação e o loop de feedback de transformação que não representamos aqui, mas isso fica para depois.

Na OpenGL moderna, **precisamos** definir pelo menos um shader de vértice e fragmento por conta própria (não há shaders de vértice / fragmento padrão na GPU). Por esta razão, muitas vezes é muito difícil começar a aprender OpenGL moderna, uma vez que é necessário um grande conhecimento antes de ser capaz de renderizar seu primeiro triângulo. Depois de finalmente renderizar seu triângulo no final deste capítulo, você saberá muito mais sobre programação gráfica.

## Vertex input (Entrada de vértices)

Para começar a desenhar algo, primeiro temos que fornecer a OpenGL alguns dados de vértice de entrada. A OpenGL é uma biblioteca de gráficos 3D, portanto, todas as coordenadas que especificamos em OpenGL estão em 3D (coordenadas x, y e z). Ela não transforma simplesmente **todas** as suas coordenadas 3D em pixels 2D na tela; só processa coordenadas 3D quando elas estão em um intervalo específico entre $-1.0$ e $1.0$ em todos os 3 eixos (**x**, **y** e **z**). Todas as coordenadas dentro do chamado intervalo de {{<definition " coordenadas  de  dispositivo  normalizadas " >}} ( {{<definition " normalized  device  coordinates " >}}) ficarão visíveis na tela (e todas as coordenadas fora desta região não).

Como queremos renderizar um único triângulo, queremos especificar um total de três vértices com cada vértice tendo uma posição 3D. Nós os definimos em coordenadas de dispositivo normalizadas (a região visível da OpenGL) em um array de `float`:

```cpp
float vertices[] = {
    -0.5f, -0.5f, 0.0f,
     0.5f, -0.5f, 0.0f,
     0.0f,  0.5f, 0.0f
};  
```

Como a OpenGL funciona no espaço 3D, renderizamos um triângulo 2D com cada vértice tendo uma coordenada z de $0.0$. Desta forma, a _profundidade_ do triângulo permanece a mesma, fazendo com que pareça 2D.


{{% greenbox tip %}}

 <h3>Coordenadas de dispositivo normalizadas (CDN)</h3> 
 
 Uma vez que suas coordenadas de vértice foram processadas no shader de vértice, elas devem estar em coordenadas de dispositivo normalizadas, que é um pequeno espaço onde os valores **x**, **y** e **z** variam de $-1.0$ a $1.0$. Quaisquer coordenadas que caiam fora desse intervalo serão descartadas/cortadas e não ficarão visíveis na tela. Abaixo você pode ver o triângulo que especificamos dentro das CDN (ignorando o eixo z):
![altlogo](https://learnopengl.com/img/getting-started/ndc.png)

  Ao contrário das coordenadas normais da tela, os pontos positivos do eixo y apontam para para cima e as coordenadas $(0,0)$ estão no centro do gráfico, em vez de no canto superior esquerdo. Eventualmente, você deseja que todas as coordenadas (transformadas) terminem neste espaço de coordenadas, caso contrário, elas não ficarão visíveis.

  Suas coordenadas CDN serão então transformadas em {{<definition " coordenadas de espaço de tela " >}} ( {{<definition "screen-space coordinates " >}}) por meio da {{<definition " transformação  da  janela  de  visualização " >}} ( {{<definition " viewport  transform " >}}) usando os dados fornecidos com a {{<struct glViewport>}}. As coordenadas de espaço de tela resultantes são então transformadas em fragmentos como entradas para o shader de fragmento.

{{% /greenbox %}}

Com os dados do vértice definidos, gostaríamos de enviá-los como entrada para o primeiro processo do pipeline gráfico: o shader de vértice. Isso é feito criando memória na GPU onde armazenamos os dados de vértice, configurando como a OpenGL deve interpretar a memória e especificando como enviar os dados para a placa gráfica. O shader de vértice então processa tantos vértices quanto lhe dizemos de sua memória.

Gerenciamos essa memória por meio dos chamados {{<definition " objetos  de  buffer  de  vértice " >}} ( {{<definition " vertex  buffer  objects " >}}) (VBO), que podem armazenar um grande número de vértices na memória da GPU. A vantagem de usar esses objetos de buffer é que podemos enviar grandes lotes de dados de uma vez para a placa de vídeo e mantê-los lá se houver memória suficiente, sem ter que enviar dados de um vértice de cada vez. O envio de dados da CPU para a placa de vídeo é relativamente lento, portanto, sempre que podemos, tentamos enviar o máximo de dados possível de uma vez. Uma vez que os dados estão na memória da placa gráfica, o shader de vértice tem acesso quase instantâneo aos vértices tornando-o extremamente rápido.

Um VBO é a nosso primeiro encontro com um objeto OpenGL, conforme discutimos no capítulo [OpenGL](https://learnopengl.com/Getting-Started/OpenGL). Assim como qualquer objeto em OpenGL, este objeto de buffer tem um ID exclusivo correspondente ao buffer, então podemos gerar um com um ID de buffer usando a função {{<struct glGenBuffers>}}:

```cpp
unsigned int VBO;
glGenBuffers(1, &VBO);  

```

A OpenGL tem muitos tipos de objetos de buffer e o tipo de buffer de um VBO é {{<variable GL_ARRAY_BUFFER>}}. A OpenGL nos permite conectar a vários buffers de uma vez, desde que eles tenham um tipo de buffer diferente. Podemos associar ( {{<english  " bind " >}}) o buffer recém-criado ao alvo {{<variable GL_ARRAY_BUFFER>}} com a função {{<struct glBindBuffer>}}:

```cpp
glBindBuffer(GL_ARRAY_BUFFER, VBO);  
```

A partir desse ponto, qualquer chamada de buffer que fizermos (no destino {{<variable GL_ARRAY_BUFFER>}}) será usada para configurar o buffer atualmente associado, que é o VBO. Então podemos fazer uma chamada para a função {{<struct glBufferData>}} que copia os dados de vértice definidos anteriormente para a memória do buffer:

```cpp
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

```

{{<struct glBufferData>}} é uma função voltada especificamente para copiar dados definidos pelo usuário para o buffer atualmente associado. Seu primeiro argumento é o tipo de buffer para o qual queremos copiar os dados: o objeto buffer de vértices atualmente associado ao alvo {{<variable GL_ARRAY_BUFFER>}}. O segundo argumento especifica o tamanho dos dados (em bytes) que queremos passar para o buffer; um simples `sizeof` dos dados de vértice é suficiente. O terceiro parâmetro são os dados de fato que queremos enviar.

O quarto parâmetro especifica como queremos que a placa gráfica gerencie os dados fornecidos. Isso pode assumir três formas:

* {{<variable GL_STREAM_DRAW>}}: os dados são modificados apenas uma vez e utilizados pela GPU poucas vezes.
* {{<variable GL_STATIC_DRAW>}}: os dados são modificados uma única vez e utilizados muitas vezes.
* {{<variable GL_DYNAMIC_DRAW>}}: os dados são modificados e utilizados muitas vezes.

Os dados de posição do triângulo não mudam, são muito usados ​​e permanecem os mesmos para cada chamada de renderização, então seu tipo de uso deve ser {{<variable GL_STATIC_DRAW>}}. Se, por exemplo, alguém tiver um buffer com dados que provavelmente mudam com frequência, um tipo de uso de {{<variable GL_DYNAMIC_DRAW>}} garante que a placa gráfica colocará os dados na memória que permite gravações mais rápidas.

A partir de agora, armazenamos os dados de vértice na memória da placa de vídeo gerenciados por um objeto de buffer de vértices chamado VBO. Em seguida, queremos criar um shader de vértice e fragmento que realmente processem esses dados, então vamos começar a construí-los.

## Shader de Vértice (Vertex Shader)

O shader de vértice é um dos shaders programáveis ​​por pessoas como nós. A OpenGL moderna requer que configuremos pelo menos um shader de vértice e fragmento se quisermos fazer alguma renderização, portanto, apresentaremos rapidamente os shaders e configuraremos dois shaders muito simples para desenhar nosso primeiro triângulo. No próximo capítulo, discutiremos os shaders com mais detalhes.

A primeira coisa que precisamos fazer é escrever o shader de vértice na linguagem de shader {{<definition " GLSL " >}} ( {{<definition " OpenGL  Shading  Language " >}}) e, em seguida, compilar esse shader para que possamos usá-lo em nossa aplicação. Abaixo você encontrará o código-fonte de um shader de vértice muito básico em `GLSL`:

```cpp
#version 330 core
layout (location = 0) in vec3 aPos;

void main()
{
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
}
```
Como você pode ver, `GLSL` é semelhante a `C`. Cada shader começa com uma declaração de sua versão. Desde a OpenGL 3.3 e superior, os números de versão de `GLSL` correspondem à versão da OpenGL (`GLSL` versão 420 corresponde a OpenGL versão 4.2, por exemplo). Também mencionamos explicitamente que estamos usando a funcionalidade de _core-profile_.

Em seguida, declaramos todos os atributos de vértice de entrada no shader de vértice com a palavra-chave `in`. No momento, só nos importamos com os dados de posição, portanto, precisamos apenas de um único atributo de vértice. A `GLSL` tem um tipo de dados vetorial que contém de 1 a 4 `floats` com base em seu dígito de sufixo. Como cada vértice possui uma coordenada 3D, criamos uma variável de entrada `vec3` com o nome {{<variable aPos>}}. Também definimos especificamente a localização da variável de entrada por meio de `layout (location = 0)` e você verá mais tarde por que precisaremos dessa localização.

{{% greenbox tip %}}
**Vetor**

Na programação gráfica, usamos o conceito matemático de vetor com bastante frequência, uma vez que ele representa claramente as posições / direções em qualquer espaço e tem propriedades matemáticas úteis. Um vetor em `GLSL` tem um tamanho máximo de 4 e cada um de seus valores pode ser accessado via `vec.x`, `vec.y`, `vec.z` e `vec.w` respectivamente, onde cada um deles representa uma coordenada no espaço. Observe que a componente `vec.w` não é usado como uma posição no espaço (estamos lidando com 3D, não 4D), mas é usado para algo chamado {{<definition " divisão  de  perspectiva " >}} ( {{<definition " perspective  division " >}}. Discutiremos os vetores com muito mais profundidade em um capítulo posterior.
{{% /greenbox %}}

Para definir a saída do shader de vértice, temos que atribuir os dados de posição à variável predefinida {{<variable gl_Position>}} que é um `vec4`. No final da função {{<struct main>}}, tudo o que definirmos como {{<variable gl_Position>}} será usado como a saída do shader de vértice. Como nossa entrada é um vetor de tamanho 3, temos que convertê-lo em um vetor de tamanho 4. Podemos fazer isso inserindo os valores de `vec3` dentro do construtor de `vec4` e definir sua componente `w` para `1.0f` (explicaremos o porquê em um capítulo posterior).

O shader de vértice atual é provavelmente o shader de vértice mais simples que podemos imaginar, porque não fizemos nenhum processamento nos dados de entrada e simplesmente os encaminhamos para a saída do shader. Em aplicações reais, os dados de entrada geralmente não estão em coordenadas de dispositivo normalizadas, portanto, primeiro temos que transformar os dados de entrada em coordenadas que caiam na região visível da OpenGL.

## Compiling a shader

Pegamos o código-fonte do shader de vértice e o armazenamos em uma string `const` `C` no topo do arquivo de código por enquanto:

```cpp
const char *vertexShaderSource = "#version 330 core\n"
    "layout (location = 0) in vec3 aPos;\n"
    "void main()\n"
    "{\n"
    "   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
    "}\0";
```

Para que a OpenGL use o shader, ela precisa compilá-lo dinamicamente em tempo de execução a partir de seu código-fonte. A primeira coisa que precisamos fazer é criar um objeto shader, novamente referenciado por um ID. Portanto, armazenamos o shader de vértice como um `unsigned int` e criamos o shader com {{<struct glCreateShader>}}:

```cpp
unsigned int vertexShader;
vertexShader = glCreateShader(GL_VERTEX_SHADER);
```

Fornecemos o tipo de shader que queremos criar como um argumento para {{<struct glCreateShader>}}. Como estamos criando um shader de vértice, passamos {{<variable GL_VERTEX_SHADER>}}.

Em seguida, anexamos o código-fonte do shader ao objeto shader e compilamos o shader:

```cpp
glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
glCompileShader(vertexShader);
```

A função {{<struct glShaderSource>}} pega o objeto shader para compilar como seu primeiro argumento. O segundo argumento especifica quantas strings estamos passando como código-fonte, que é apenas uma. O terceiro parâmetro é o código-fonte propriamente dito do shader de vértice e podemos deixar o quarto parâmetro como `NULL`.

{{% greenbox tip %}}
Você provavelmente deseja verificar se a compilação foi bem-sucedida após a chamada de glCompileShader e, caso contrário, quais erros foram encontrados para que você possa corrigi-los. A verificação de erros em tempo de compilação é realizada da seguinte maneira:
  
```cpp
int success;
char infoLog [512];
glGetShaderiv (vertexShader, GL_COMPILE_STATUS, & sucess);
```

   Primeiro, definimos um inteiro para indicar o sucesso e um recipiente de armazenamento para as mensagens de erro (se houver). Em seguida, verificamos se a compilação foi bem-sucedida com glGetShaderiv. Se a compilação falhar, devemos recuperar a mensagem de erro com glGetShaderInfoLog e imprimir a mensagem de erro.
  
```cpp
if (!success)
{
    glGetShaderInfoLog (vertexShader, 512, NULL, infoLog);
    std::cout << "ERROR::SHADER::VERTEX::COMPILATION_FAILED\n" << infoLog << std::endl;
}
```
<p></p>
{{% /greenbox %}}

Se nenhum erro foi detectado durante a compilação do shader de vértice, agora ele está compilado.

## Shader de Fragmento (Fragment shader)

O shader de fragmento é o segundo e último shader que iremos criar para renderizar um triângulo. O shader de fragmento tem como objetivo calcular a cor de saída de seus pixels. Para manter as coisas simples, o shader de fragmento sempre produzirá uma cor laranja.

{{% greenbox tip %}}
As cores na Computação Gráfica são representadas como um array de 4 valores: a componente vermelho, verde, azul e alfa (opacidade), comumente chamadas de RGBA. Ao definir uma cor em OpenGL ou `GLSL`, definimos a influencia de cada componente como um valor entre $0.0$ e $1.0$. Se, por exemplo, definirmos o vermelho como $1.0$ e o verde como $1.0$, obteremos uma mistura de ambas as cores e com isso a cor amarela. Com essas três componentes de cores, podemos gerar mais de 16 milhões de cores diferentes!
{{% /greenbox %}}

```cpp

#version 330 core
out vec4 FragColor;

void main()
{
    FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
} 

```

O shader de fragmento requer apenas uma variável de saída e essa é um vetor de tamanho 4 que define a cor final de saída que devemos calcular nós mesmos. Podemos declarar valores de saída com a palavra-chave `out`, que chamamos aqui prontamente de {{<variable FragColor>}}. Em seguida, simplesmente atribuímos um `vec4` à saída de cor como uma cor laranja com um valor alfa de $1.0$ ($1.0$ sendo completamente opaco).

O processo para compilar um shader de fragmento é semelhante ao shader de vértice, embora desta vez usemos a constante {{<variable GL_FRAGMENT_SHADER>}} como o tipo de shader:

```cpp

unsigned int fragmentShader;
fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
glCompileShader(fragmentShader);

```

Ambos os shaders agora estão compilados e a única coisa que resta a fazer é atrelar os dois objetos de shader em um {{<definition "programa de shader">}} ({{<definition "shader program">}}) que podemos usar para renderização. Certifique-se de verificar se há erros de compilação aqui também!

## Programa de Shader (Shader Program)

Um objeto de programa de shader é a versão final _linkada_ de vários shaders combinados. Para usar os shaders compilados recentemente, temos que atrelálos-los ( {{<definition "link">}}) a um objeto de programa de shader e, em seguida, ativar este programa de shader ao renderizar objetos. Os shaders do programa de shader ativado serão usados  quando fizermos chamadas de renderização.

Ao atrelar os shaders a um programa, ele associa as saídas de cada shader às entradas do próximo shader. É aqui também que você obterá erros de _linkagem_ ( {{<english "linking">}}) se suas saídas e entradas não corresponderem.

Criar um objeto de programa é fácil:

```cpp
unsigned int shaderProgram;
shaderProgram = glCreateProgram();
```

A função glCreateProgram cria um programa e retorna a referência ID para o objeto de programa recém-criado. Agora precisamos anexar os shaders compilados anteriormente ao objeto do programa e, em seguida, conectá-los com glLinkProgram:

```cpp
glAttachShader(shaderProgram, vertexShader);
glAttachShader(shaderProgram, fragmentShader);
glLinkProgram(shaderProgram);
```

O código deveria ser autoexplicativo, nós anexamos os shaders ao programa e os associamos via glLinkProgram.

{{% greenbox tip %}}
Assim como a compilação de shader, também podemos verificar se o _linking_ de um programa de shader falhou e recuperar o _log_ correspondente. No entanto, em vez de usar glGetShaderiv e glGetShaderInfoLog, agora usamos:

```cpp

glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
if(!success) {
    glGetProgramInfoLog(shaderProgram, 512, NULL, infoLog);
    ...
}

```
<p></p>
{{% /greenbox  %}}
O resultado é um objeto de programa que podemos ativar chamando glUseProgram:

```cpp
glUseProgram(shaderProgram);
```

Cada shader e chamada de renderização após glUseProgram agora usarão esse objeto de programa (e, portanto, os shaders).

Ah, sim, e não se esqueça de excluir os objetos de shader depois de associá-los ao objeto de programa; não precisamos mais deles:

```cpp
glDeleteShader(vertexShader);
glDeleteShader(fragmentShader);  
```

Agora enviamos os dados de vértice de entrada para a GPU e instruímos a GPU como ela deve processar os dados de vértice em um shader de vértice e fragmento. Estamos quase lá, mas ainda não. A OpenGL ainda não sabe como deve interpretar os dados do vértice na memória e como deve conectar os dados do vértice aos atributos do shader de vértice. Seremos legais e diremos a OpenGL como fazer isso.

## _Linkando_ Attributos de Vértice (Linking Vertex Attributes)

O shader de vértice nos permite especificar qualquer entrada que desejamos na forma de atributos de vértice e, embora isso permita grande flexibilidade, significa que temos que especificar manualmente que parte de nossos dados de entrada vai para qual atributo de vértice no shader de vértice. Isso significa que temos que especificar como a OpenGL deve interpretar os dados do vértice antes da renderização.

Nossos dados de buffer de vértices são formatados da seguinte maneira:

![altlogo](https://learnopengl.com/img/getting-started/vertex_attribute_pointer.png)

* Os dados de posição são armazenados como valores de ponto flutuante de 32 bits (4 bytes).
* Cada posição é composta por 3 desses valores.
* Não há espaço (ou outros valores) entre cada conjunto de 3 valores. Os valores são compactados ({{<definition "tightly packed">}} no array.
* O primeiro valor nos dados está no início do buffer.


Com esse conhecimento, podemos dizer a OpenGL como ela deve interpretar os dados do vértice (por atributo de vértice) usando glVertexAttribPointer:

```cpp

glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
glEnableVertexAttribArray(0);  

```

A função glVertexAttribPointer tem alguns parâmetros, então vamos examiná-los cuidadosamente:

* O primeiro parâmetro especifica qual atributo de vértice queremos configurar. Lembre-se de que especificamos a localização do atributo de vértice de posição no shader de vértice com `layout (location = 0)`. Isso define a localização do atributo de vértice como `0` e, como queremos passar dados para esse atributo de vértice, passamos `0`.

* O próximo argumento especifica o tamanho do atributo. É um `vec3`, portanto, é composto por 3 valores.

* O terceiro argumento especifica o tipo de dado que é `GL_FLOAT` (um `vec*` em `GLSL` consiste em valores de ponto flutuante).

* O próximo argumento especifica se queremos que os dados sejam normalizados. Se estivermos inserindo tipos de dados inteiros (`int`, `byte`) e definimos isso como `GL_TRUE`, os dados inteiros são normalizados para 0 (ou -1 para dados com sinal) e 1 quando convertidos para `float`. Isso não é relevante para nós, então deixaremos como `GL_FALSE`.

* O quinto argumento é conhecido como {{<definition "stride">}} e nos indica o espaço entre atributos de vértices consecutivos. Como o próximo conjunto de dados de posição está localizado a exatamente 3 vezes o tamanho de um `float`, especificamos esse valor como o _stride_. Observe que, como sabemos que o array está compactado (não há espaço entre o próximo valor de atributo do vértice), poderíamos também ter especificado a distância como 0 para permitir que a OpenGL determine a distância (isso só funciona quando os valores estão compactados). Sempre que temos mais atributos de vértice, temos que definir cuidadosamente o espaçamento entre cada atributo, mas veremos mais exemplos disso mais tarde.

* O último parâmetro é do tipo `void *` e, portanto, requer aquela conversão ({{<english "cast">}}) estranha. Este é o {{<definition "deslocamento">}} ({{<definition "offset">}}) de onde os dados de posição começam no buffer. Uma vez que os dados de posição estão no início do array de dados, este valor é apenas 0. Exploraremos este parâmetro em mais detalhes posteriormente.

{{% greenbox tip %}}
Cada atributo de vértice obtém seus dados da memória gerenciada por um VBO e de qual VBO ele obtém seus dados (você pode ter vários VBOs) é determinado pelo VBO atualmente associado a {{<variable GL_ARRAY_BUFFER>}} ao chamar glVertexAttribPointer. Como o VBO definido anteriormente ainda está associado antes de chamar glVertexAttribPointer, o atributo de vértice `0` agora está associado a seus dados de vértice.
{{% /greenbox %}}

Agora que especificamos como a OpenGL deve interpretar os dados do vértice, devemos também habilitar o atributo do vértice com glEnableVertexAttribArray fornecendo a localização do atributo do vértice como seu argumento; atributos de vértice são desabilitados por padrão. A partir desse ponto, temos tudo configurado: inicializamos os dados de vértice em um buffer usando um objeto de buffer de vértices, configuramos um shader de vértice e fragmento e informamos a OpenGL como conectar os dados de vértice aos atributos de vértice do shader de vértice. Desenhar um objeto em OpenGL agora seria assim:

```cpp
// 0. copia nosso array de vertices em um buffer para a OpenGL usar
glBindBuffer(GL_ARRAY_BUFFER, VBO);
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
// 1. configure os ponteiros dos atributos de vertice
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
glEnableVertexAttribArray(0);  
// 2. use nosso programa de shader quando quisermos renderizar um objeto
glUseProgram(shaderProgram);
// 3. agora desenhe o objeto 
someOpenGLFunctionThatDrawsOurTriangle();   

```

Temos que repetir esse processo toda vez que quisermos desenhar um objeto. Pode não parecer muito, mas imagine se tivermos mais de 5 atributos de vértice e talvez centenas de objetos diferentes (o que não é incomum). Associar os objetos de buffer apropriados e configurar todos os atributos de vértice para cada um desses objetos rapidamente se torna um processo complicado. E se houvesse alguma maneira de armazenar todas essas configurações de estado em um objeto e simplesmente associar esse objeto para restaurar seu estado?


## Objecto de _Array_ de Vértices (Vertex Array Object)

Um {{<definition "objeto de array de vértice">}} ({{<definition "vertex array object">}}) (também conhecido como {{<definition "VAO">}}) pode ser associado igual a um objeto de buffer de vértices e qualquer chamada de atributo de vértice desse ponto em diante será armazenada dentro do VAO. Isso tem a vantagem de que, ao configurar ponteiros de atributo de vértice, você só precisa fazer essas chamadas uma vez e sempre que quisermos desenhar o objeto, podemos apenas associar o VAO correspondente. Isso torna a troca entre diferentes dados de vértice e configurações de atributo tão fácil quanto associar um VAO diferente. Todo o estado que acabamos de definir é armazenado dentro do VAO.

{{% greenbox warning %}}
A OpenGL requer que usemos um VAO para que ela saiba o que fazer com nossas entradas de vértice. Se não conseguirmos associar um VAO, a OpenGL provavelmente se recusará a desenhar qualquer coisa.
{{% /greenbox  %}}

Um objeto de array de vértices armazena o seguinte:

* Chamadas para glEnableVertexAttribArray ou glDisableVertexAttribArray.

* Configurações de atributo de vértice via glVertexAttribPointer.

* Objectos de buffer de vérticess associados com atributos de vértice através de chamadas de glVertexAttribPointer.

![altlogo](https://learnopengl.com/img/getting-started/vertex_array_objects.png)

O processo para gerar um VAO é semelhante ao de um VBO:

```cpp
unsigned int VAO;
glGenVertexArrays(1, &VAO);  

```

Para usar um VAO, tudo o que você precisa fazer é associar o VAO usando glBindVertexArray. A partir desse ponto, devemos associar/configurar o(s) VBO(s) e o(s) ponteiro(s) de atributo correspondentes e, em seguida, desassociar o VAO para uso posterior. Assim que quisermos desenhar um objeto, simplesmente associamos o VAO com as configurações que quisermos antes de desenhar o objeto e pronto. No código, seria mais ou menos assim:

```cpp
// ..:: Codigo de inicializacao (feito uma vez (a menos que seu objeto sofra alteracoes)) :: ..
// 1. associe Vertex Array Object
glBindVertexArray(VAO);
// 2. copie nosso array de vertices em um buffer para OpenGL usar
glBindBuffer(GL_ARRAY_BUFFER, VBO);
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
// 3. entao defina nossos ponteiros de atributos de vertices
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
glEnableVertexAttribArray(0);  

  
[...]

// ..:: Codigo de desenho (no loop de renderizacao) :: ..
// 4. desenhe o objeto
glUseProgram(shaderProgram);
glBindVertexArray(VAO);
someOpenGLFunctionThatDrawsOurTriangle();   

```

E é isso! Tudo o que fizemos nos últimos milhões de páginas levou a este momento, um VAO que armazena nossa configuração de atributo de vértice e qual VBO usar. Normalmente, quando você tem vários objetos que deseja desenhar, primeiro gera / configura todos os VAOs (e, portanto, o VBO necessário e os ponteiros de atributo) e os armazena para uso posterior. No momento em que queremos desenhar um de nossos objetos, pegamos o VAO correspondente, o associamos e, em seguida, desenhamos o objeto e desassociamos o VAO novamente.

## O Triângulo que todos nós estivemos esperando

Para desenhar nossos objetos de escolha, a OpenGL nos fornece a função glDrawArrays que desenha primitivas usando o shader ativo no momento, a configuração de atributo de vértice definida anteriormente e os dados de vértice do VBO (indiretamente associados por VAO).

```cpp

glUseProgram(shaderProgram);
glBindVertexArray(VAO);
glDrawArrays(GL_TRIANGLES, 0, 3);

```

A função glDrawArrays toma como primeiro argumento o tipo de primitiva OpenGL que gostaríamos de desenhar. Como eu disse no início que queríamos desenhar um triângulo, não gosto de mentir para vocês, passamos {{<variable GL_TRIANGLES>}}. O segundo argumento especifica o índice inicial do array de vértices que gostaríamos de desenhar; apenas deixamos isso em `0`. O último argumento especifica quantos vértices queremos desenhar, que é `3` (renderizamos apenas 1 triângulo de nossos dados, que tem exatamente 3 vértices de comprimento).

Agora tente compilar o código e checar seus passos novamente caso apareça algum erro. Assim que sua aplicação for compilada, você verá o seguinte resultado:

![altlogo](https://learnopengl.com/img/getting-started/hellotriangle.png)

O código-fonte do programa completo pode ser encontrado [aqui](code_viewer_gh.php?code=src/1.getting_started/2.1.hello_triangle/hello_triangle.cpp).

Se sua saída não parecer a mesma, você provavelmente fez algo errado ao longo do caminho, então verifique o código-fonte completo e veja se você esqueceu alguma coisa.

##  Objetos de Buffer de Elementos (Element Buffer Objects) 

Há uma última coisa que gostaríamos de discutir ao renderizar vértices: {{<definition "objetos de buffer de elementos">}} ( {{<definition "element buffer objects">}}) abreviados para EBO. Para explicar como os objetos de buffer de elementos funcionam, é melhor dar um exemplo: suponha que desejamos desenhar um retângulo em vez de um triângulo. Podemos desenhar um retângulo usando dois triângulos (a OpenGL funciona principalmente com triângulos). Isso irá gerar o seguinte conjunto de vértices:

```cpp
	
float vertices[] = {
    // primeiro triangulo
     0.5f,  0.5f, 0.0f,  // canto superior direito
     0.5f, -0.5f, 0.0f,  // canto inferior direito
    -0.5f,  0.5f, 0.0f,  // canto superior esquerdo 
    // segundo triangulo
     0.5f, -0.5f, 0.0f,  // canto inferior direito
    -0.5f, -0.5f, 0.0f,  // canto inferior esquerdo
    -0.5f,  0.5f, 0.0f   // canto superior esquerdo
}; 

```

Como você pode ver, há alguma sobreposição nos vértices especificados. Especificamos o canto inferior direito e o canto superior esquerdo duas vezes! Isso é um _overhead_ de 50%, já que o mesmo retângulo também pode ser especificado com apenas 4 vértices, em vez de 6. Isso só vai piorar assim que tivermos modelos mais complexos com mais de 1000 triângulos onde haverá grandes pedaços que se sobrepõem. O que seria uma solução melhor é armazenar apenas os vértices únicos e, em seguida, especificar a ordem em que queremos desenhar esses vértices. Nesse caso, teríamos apenas que armazenar 4 vértices para o retângulo e, em seguida, apenas especificar em que ordem gostaríamos de desenhá-los. Não seria ótimo se a OpenGL nos fornecesse um recurso como esse?

Felizmente, os objetos de buffer de elementos funcionam exatamente assim. Um EBO é um buffer, assim como um objeto de buffer de vértices, que armazena índices que a OpenGL usa para decidir quais vértices desenhar. Este chamado {{<definition "desenho indexado">}} ( {{<definition "indexed drawing">}}) é exatamente a solução para o nosso problema. Para começar, primeiro temos que especificar os vértices (únicos) e os índices para desenhá-los como um retângulo:

```cpp

float vertices[] = {
     0.5f,  0.5f, 0.0f,  // canto superior direito
     0.5f, -0.5f, 0.0f,  // canto inferior direito
    -0.5f, -0.5f, 0.0f,  // canto inferior esquerdo
    -0.5f,  0.5f, 0.0f   // canto superior esquerdo
};
unsigned int indices[] = {  // note que comecamos com 0!
    0, 1, 3,   // primeiro triangulo
    1, 2, 3    // segundo triangulo
};  

```

Você pode ver que, ao usar índices, precisamos apenas de 4 vértices em vez de 6. Em seguida, precisamos criar o objeto buffer de elementos:

```cpp
unsigned int EBO;
glGenBuffers(1, &EBO);

```

Semelhante ao VBO, associamos o EBO e copiamos os índices no buffer com glBufferData. Além disso, assim como o VBO, queremos colocar essas chamadas entre uma chamada `bind` e uma chamada `unbind`, embora desta vez especifiquemos {{<variable GL_ELEMENT_ARRAY_BUFFER>}} como o tipo de buffer.

```cpp

glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW); 

```

Observe que agora estamos fornecendo {{<variable GL_ELEMENT_ARRAY_BUFFER>}} como o destino do buffer. A última coisa que falta fazer é substituir a chamada de glDrawArrays por glDrawElements para indicar que queremos renderizar os triângulos de um buffer de índices. Ao usar glDrawElements, vamos desenhar usando índices fornecidos no objeto de buffer de elementos atualmente associado:

```cpp

glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

```

O primeiro argumento especifica o modo que queremos desenhar, semelhante a glDrawArrays. O segundo argumento é a contagem ou número de elementos que gostaríamos de desenhar. Especificamos 6 índices, então queremos desenhar 6 vértices no total. O terceiro argumento é o tipo dos índices que é do tipo GL_UNSIGNED_INT. O último argumento nos permite especificar um deslocamento no EBO (ou passar uma matriz de índice, mas isso é quando você não está usando objetos de buffer de elemento), mas vamos apenas deixar isso em 0.

A função glDrawElements obtém seus índices do EBO atualmente associado ao alvo {{<variable GL_ELEMENT_ARRAY_BUFFER>}}. Isso significa que temos que associar o EBO correspondente cada vez que quisermos renderizar um objeto com índices, o que, novamente, é um pouco complicado. Acontece que um objeto de array de vértices também mantém registro de associações de objeto de buffer de elementos. O último objeto de buffer de elementos que é associado enquanto um VAO está associado é armazenado como o objeto de buffer de elementos do VAO. A associação a um VAO também vincula automaticamente esse EBO.

![altlogo](https://learnopengl.com/img/getting-started/vertex_array_objects_ebo.png)

{{% greenbox warning %}}
Um VAO armazena as chamadas glBindBuffer quando o destino é {{<variable GL_ELEMENT_ARRAY_BUFFER>}}. Isso também significa que ele armazena suas chamadas de desassociação, portanto, certifique-se de não desassociar o buffer de array de elementos antes de desassociar seu VAO, caso contrário, ele não terá um EBO configurado.
{{% /greenbox %}}

A inicialização resultante e o código de desenho agora se parecem com isto:

```cpp

// ..:: Codigo de inicializacao :: ..
// 1. associe o Vertex Array Object
glBindVertexArray(VAO);
// 2. copie nosso array de vertices em um buffer de vertices para a OpenGL usar
glBindBuffer(GL_ARRAY_BUFFER, VBO);
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
// 3. copie nosso array de indices em um buffer de elementos para a OpenGL usar
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
// 4. entao configure os ponteiros de atributos de vertice
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
glEnableVertexAttribArray(0);  

[...]
  
// ..:: Codigo de desenho (no loop de renderizacao) :: ..
glUseProgram(shaderProgram);
glBindVertexArray(VAO);
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0)
glBindVertexArray(0);

```

A execução do programa deve fornecer uma imagem conforme ilustrado abaixo. A imagem da esquerda deve parecer familiar e a imagem da direita é o retângulo desenhado no modo {{<definition "wireframe">}}. O retângulo de wireframe mostra que o retângulo de fato consiste em dois triângulos.

![altlogo](https://learnopengl.com/img/getting-started/hellotriangle2.png)

{{% greenbox tip %}}
**Modo Wireframe**

  Para desenhar seus triângulos no modo wireframe, você pode configurar como a OpenGL desenha suas primitivas via glPolygonMode (GL_FRONT_AND_BACK, GL_LINE). O primeiro argumento diz que queremos aplicá-lo à frente e atrás de todos os triângulos e a segunda linha nos diz para desenhá-los como linhas. Quaisquer chamadas de desenho subsequentes irão renderizar os triângulos no modo wireframe até que o definamos de volta ao seu padrão usando glPolygonMode (GL_FRONT_AND_BACK, GL_FILL).
{{% /greenbox %}}

Se você tiver algum erro, retroceda e veja se esqueceu alguma coisa. Você pode encontrar o código-fonte completo [aqui](code_viewer_gh.php?code=src/1.getting_started/2.2.hello_triangle_indexed/hello_triangle_indexed.cpp).

Se você conseguiu desenhar um triângulo ou retângulo exatamente como fizemos, parabéns, você conseguiu passar por uma das partes mais difíceis da OpenGL moderno: desenhar seu primeiro triângulo. Esta é uma parte difícil, pois é necessário um grande conhecimento antes de ser capaz de desenhar o primeiro triângulo. Felizmente, agora superamos essa barreira e os próximos capítulos serão muito mais fáceis de entender.

# Recursos Adicionais

* [antongerdelan.net/hellotriangle](http://antongerdelan.net/opengl/hellotriangle.html): A discussão de Anton Gerdelan sobre a renderização do primeiro triângulo.

* [open.gl/drawing](https://open.gl/drawing): Versão do Alexander Overvoorde.

* [antongerdelan.net/vertexbuffers](http://antongerdelan.net/opengl/vertexbuffers.html): alguns insights extras sobre objetos de buffer de vértices.

* [learnopengl.com/In-Practice/Debugging](https://learnopengl.com/In-Practice/Debugging): há várias etapas envolvidas neste capítulo; se você estiver travado, pode valer a pena ler um pouco sobre depuração em OpenGL (até a seção de saída de depuração).

# Exercícios

Para realmente ter uma boa compreensão dos conceitos discutidos, alguns exercícios foram preparados. É aconselhável trabalhar com eles antes de passar para o próximo assunto para ter certeza de ter uma boa compreensão do que está acontecendo.

1. Tente desenhar 2 triângulos próximos um do outro usando glDrawArrays adicionando mais vértices aos seus dados: [solução](code_viewer_gh.php?code=src/1.getting_started/2.3.hello_triangle_exercise1/hello_triangle_exercise1.cpp).

2. Agora crie os mesmos 2 triângulos usando dois VAOs e VBOs diferentes para seus dados: [solução](code_viewer_gh.php?code=src/1.getting_started/2.4.hello_triangle_exercise2/hello_triangle_exercise2.cpp).

3. Crie dois programas de shader onde o segundo programa usa um shader de fragmento diferente que produz a cor amarela; desenhe os dois triângulos novamente, onde um resulta na cor amarela: [solução](/code_viewer_gh.php?code=src/1.getting_started/2.5.hello_triangle_exercise3/hello_triangle_exercise3.cpp).



