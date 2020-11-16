---
title: "Criando uma Janela"
date: 2020-10-29T21:02:14-03:00
draft: false
---

[Post Original](https://learnopengl.com/Getting-started/Creating-a-window)

A primeira coisa que precisamos fazer antes de começar a criar gráficos incríveis é criar um contexto OpenGL e uma janela da aplicação na qual desenhar. No entanto, essas operações são específicas para cada sistema operacional e a OpenGL propositalmente tenta se abstrair dessas operações. Isso significa que temos que criar uma janela, definir um contexto e lidar com a entrada do usuário por conta própria.

Felizmente, existem algumas bibliotecas por aí que fornecem a funcionalidade que buscamos, algumas voltadas especificamente para OpenGL. Essas bibliotecas nos poupam todo o trabalho específico do sistema operacional e nos fornecem uma janela e um contexto OpenGL para renderizar. Algumas das bibliotecas mais populares são GLUT, SDL, SFML e GLFW. No AprendaOpenGL estaremos usando a **GLFW**. Sinta-se à vontade para usar qualquer uma das outras bibliotecas, a configuração para a maioria é semelhante à configuração da GLFW.

## GLFW

A GLFW é uma biblioteca, escrita em C, voltada especificamente para OpenGL. A GLFW nos dá o as funções básicas necessárias para renderizar objetos na tela. Ela nos permite criar um contexto OpenGL, definir parâmetros de janela e lidar com a entrada do usuário, o que é suficiente para nossos propósitos.

O foco desta e da próxima seção é colocar a GLFW em funcionamento, certificando-se de que ela crie corretamente um contexto OpenGL e exiba uma janela simples para podermos nos divertir. Este capítulo apresenta uma abordagem passo a passo para baixar, compilar e _linkar_ a biblioteca GLFW. Usaremos o Microsoft Visual Studio 2019 no momento desta escrita (observe que o processo é o mesmo nas versões mais recentes do Visual Studio). Se você não estiver usando o Visual Studio (ou uma versão mais antiga), não se preocupe, o processo será semelhante na maioria das outras IDEs.

## Compilando a GLFW

A GLFW pode ser obtida na sua própria página de [download](http://www.glfw.org/download.html). A GLFW já tem binários pré-compilados e arquivos de cabeçalho para Visual Studio 2012 até 2019, mas para fins de completude, iremos compilar a GLFW a partir do código-fonte. Isso é para lhe dar uma ideia do processo de compilar bibliotecas de código aberto você mesmo, pois nem todas as bibliotecas terão binários pré-compilados disponíveis. Então, vamos baixar o _pacote de código-fonte_.

{{% notice warning %}}
Estaremos compilando todas bibliotecas como binários de 64-bits, então tenha certeza de pegar as versões de 64-bits caso vá usar os binários pré-compilados.
{{% /notice %}}

Depois de baixar o pacote, extraia-o e abra seu conteúdo. Estamos interessados ​​apenas em alguns itens:

    * A biblioteca resultante da compilação.
    * A pasta **include**.

Compilar a partir do código-fonte garante que a biblioteca resultante seja perfeitamente ajustada para sua CPU/OS, um luxo que os binários pré-compilados nem sempre oferecem (às vezes, binários pré-compilados nem estão disponíveis para seu sistema). O problema de fornecer código-fonte para o mundo todo, entretanto, é que nem todo mundo usa a mesma IDE ou sistema de compilação para desenvolver suas aplicações, o que significa que os arquivos de projeto/solução fornecidos podem não ser compatíveis com a configuração de outras pessoas. Portanto, as pessoas têm que configurar seu próprio projeto/solução com os arquivos .c/.cpp e .h/.hpp, o que é complicado. Exatamente por essas razões existe uma ferramenta chamada CMake.

## CMake

CMake é uma ferramenta que pode gerar arquivos de projeto/solução de escolha do usuário (por exemplo, Visual Studio, Code::Blocks, Eclipse) a partir de uma coleção de arquivos de código-fonte usando scripts CMake pré-definidos. Isso nos permite gerar um arquivo de projeto do Visual Studio 2019 a partir do pacote da GLFW do qual podemos usar para compilar a biblioteca. Primeiro, precisamos baixar e instalar o CMake, que pode ser baixado em sua página de [download](http://www.cmake.org/cmake/resources/software.html).

Assim que o CMake estiver instalado, você pode optar por executar o CMake a partir da linha de comando ou através de sua GUI. Como não estamos tentando complicar as coisas, vamos usar a GUI. O CMake requer uma pasta de código-fonte e uma pasta de destino para os binários. Para a pasta do código-fonte, vamos escolher a pasta raiz do pacote de origem da GLFW baixado e, para a pasta de compilação, criaremos umo novo diretório _build_ e, em seguida, selecionaremos esse diretório.

![GitHub Logo](https://learnopengl.com/img/getting-started/cmake.png)

Uma vez que as pastas de origem e destino tenham sido definidas, clique no botão **Configure** para que o CMake possa ler as configurações necessárias e o código-fonte. Temos então que escolher o gerador para o projeto e, como estamos usando o Visual Studio 2019, vamos escolher a opção **Visual Studio 16** (Visual Studio 2019 também é conhecido como Visual Studio 16). O CMake irá então exibir as opções de compilação possíveis para configurar a biblioteca. Podemos deixá-las com seus valores padrão e clicar em **Configure** novamente para armazenar as configurações. Depois de definir as configurações, clicamos em **Generate** e os arquivos de projeto resultantes serão gerados em sua pasta de **build**.

## Compilação

Na pasta **build**, um arquivo chamado **GLFW.sln** pode ser encontrado e o abrimos com o Visual Studio 2019. Como o CMake gerou um arquivo de projeto que já contém as configurações adequadas, só temos que compilar a solução. O CMake deveria ter configurado automaticamente a solução para que compile uma biblioteca de 64 bits; agora clique em **build solution**. Isso nos dará um arquivo de biblioteca compilado que pode ser encontrado em **build/src/Debug** denominado **glfw3.lib**.

Depois de gerar a biblioteca, precisamos ter certeza de que a IDE sabe onde encontrar a biblioteca e os arquivos de inclusão para nosso programa OpenGL. Existem duas abordagens comuns para fazer isso:

  1. Encontramos as pastas **/lib** e **/include** da IDE/compilador e adicionamos o conteúdo da pasta **include** ds GLFW à pasta **/include** da IDE e, da mesma forma, adicionamos **glfw3.lib** à pasta **/lib** ds IDE. Isso funciona, mas não é a abordagem recomendada. É difícil de manter sua biblioteca e incluir arquivos, e uma nova instalação da sua IDE/compilador resultaria em você ter que fazer todo este processo novamente.
  2. Outra abordagem (recomendada) é criar um novo conjunto de diretórios em um local de sua escolha que contenha todos os arquivos de cabeçalho/bibliotecas de terceiros aos quais você pode se referir a partir de sua IDE/compilador. Você pode, por exemplo, criar uma única pasta que contém uma pasta **Libs** e **Include** e armazenar todos os nossos arquivos de biblioteca e cabeçalho, respectivamente, para projetos OpenGL. Agora todas as bibliotecas de terceiros são organizadas em um único local (que pode ser compartilhado por vários computadores). O requisito, entretanto, é que cada vez que criarmos um novo projeto, teremos que dizer a IDE onde encontrar esses diretórios.

Assim que os arquivos necessários forem armazenados em um local de sua escolha, podemos começar a criar nosso primeiro projeto OpenGL GLFW.

## Nosso Primeiro Projeto

Primeiro, vamos abrir o Visual Studio e criar um novo projeto. Escolha `C++` se várias opções forem fornecidas e pegue o **Projeto Vazio** (Empty Project) (não se esqueça de dar ao seu projeto um nome adequado). Como faremos tudo em 64 bits e o padrão do projeto é de 32 bits, precisaremos alterar o menu na parte superior, próximo a Depurar (Debug) de x86 para x64:

![GitHub Logo](https://learnopengl.com/img/getting-started/x64.png)

Agora temos uma área de trabalho para criar nossa primeiríssima aplicação OpenGL!

## Linking

Para que o projeto use a GLFW, precisamos {{<definition linkar>}} (link) a biblioteca ao nosso projeto. Isso pode ser feito especificando o arquivo **glfw3.lib** nas configurações do linker, mas nosso projeto ainda não sabe onde encontrar o arquivo **glfw3.lib**, pois armazenamos nossas bibliotecas de terceiros em um diretório diferente. Portanto, precisamos primeiro adicionar este diretório ao projeto.

Podemos dizer a IDE para levar esse diretório em consideração quando precisar procurar por arquivos de biblioteca e incluir arquivos. Clique com o botão direito do mouse no nome do projeto no _solution explorer_ e vá para os diretórios **VC++**, conforme mostrado na imagem abaixo:

![GitHub Logo](https://learnopengl.com/img/getting-started/vc_directories.png)

A partir daí, você pode adicionar seus próprios diretórios para que o projeto saiba onde pesquisar. Isso pode ser feito inserindo-os manualmente no texto ou clicando na _string_ de localização apropriada e selecionando a opção **<Edit ..>**. Faça isso para os **Diretórios da Biblioteca** (Library Directories) e **Incluir Diretórios** (Include Directories):

![GitHub Logo](https://learnopengl.com/img/getting-started/include_directories.png)

Aqui você pode adicionar quantos diretórios extras desejar e, a partir desse ponto, a IDE também pesquisará esses diretórios ao procurar por arquivos de biblioteca e de cabeçalho. Assim que sua pasta **Include** da GLFW for incluída, você poderá encontrar todos os arquivos de cabeçalho para a GLFW incluindo **<GLFW / ..>**. O mesmo se aplica aos diretórios da biblioteca.

Uma vez que o VS agora pode encontrar todos os arquivos necessários, podemos finalmente linkar a GLFW ao projeto acessando as guias **Linker** e **Input**:

![GitHub Logo](https://learnopengl.com/img/getting-started/linker_input.png)

Para linkar a uma biblioteca, você deve especificar o nome da biblioteca para o _linker_. Como o nome da biblioteca é glfw3.lib, adicionamos isso ao campo **Dependências adicionais** (Additional Dependencies) (manualmente ou usando a opção **<Edit ..>**) e a partir desse ponto o GLFW será linkado quando compilarmos. Além da GLFW, também devemos adicionar um link para a biblioteca OpenGL, mas isso pode variar de acordo com o sistema operacional:

## Biblioteca OpenGL no Windows

Se você estiver no Windows, a biblioteca OpenGL **opengl32.lib** vem com o Microsoft SDK, que é instalado por padrão quando você instala o Visual Studio. Como este capítulo usa o compilador VS e está no Windows, adicionamos **opengl32.lib** às configurações do linker. Observe que o equivalente de 64 bits da biblioteca OpenGL é chamado **opengl32.lib**, assim como o equivalente de 32 bits, que é um nome um tanto infeliz.

## Biblioteca OpenGL no Linux

Em sistemas Linux, você precisa se linkar à biblioteca **libGL.so** adicionando **-lGL** às configurações do linker. Se você não conseguir encontrar a biblioteca, provavelmente precisará instalar qualquer um dos pacotes de desenvolvimento Mesa, NVidia ou AMD.

Então, depois de adicionar as bibliotecas GLFW e OpenGL às configurações do linker, você pode incluir os arquivos de cabeçalho para GLFW da seguinte maneira:

```cpp
#include <GLFW\glfw3.h>
```
{{% notice tip %}}
Para usuários Linux compilando com GCC, as seguintes opções de linha de comando podem ajudá-lo a compilar o projeto: -lglfw3 -lGL -lX11 -lpthread -lXrandr -lXi -ldl. Não linkar corretamente as bibliotecas correspondentes irá gerar muitos erros de referências indefinidas (_undefined references_).
{{% /notice %}}

Isso conclui a instalação e configuração da GLFW.

## GLAD

Ainda não chegamos lá, pois ainda há outra coisa que precisamos fazer. Como a OpenGL é realmente apenas um padrão/especificação, cabe ao fabricante do driver implementar a especificação em um driver compatível com a placa de vídeo específica. Como existem muitas versões diferentes de drivers OpenGL, a localização da maioria de suas funções não é conhecida no tempo de compilação e precisa ser consultada em tempo de execução. É então tarefa do desenvolvedor recuperar a localização das funções de que precisa e armazená-las em ponteiros de função para uso posterior. A recuperação desses locais é [específica do sistema operacional](https://www.khronos.org/opengl/wiki/Load_OpenGL_Functions). No Windows, é mais ou menos assim:

```cpp
// define o prototipo das funcoes
typedef void (*GL_GENBUFFERS) (GLsizei, GLuint*);
// encontra a funcao e a armazena em um ponteiro de funcao
GL_GENBUFFERS glGenBuffers  = (GL_GENBUFFERS)wglGetProcAddress("glGenBuffers");
// a funcao agora pode ser chamada normalmente
unsigned int buffer;
glGenBuffers(1, &buffer);
```

Como você pode ver, o código parece complexo e é um processo complicado fazer isso para cada função que você pode precisar que ainda não foi declarada. Felizmente, existem bibliotecas para este propósito também, onde a GLAD é uma biblioteca popular e atualizada.

## Configurando a GLAD

GLAD é uma biblioteca de [código aberto](https://github.com/Dav1dde/glad) que gerencia todo o trabalho pesado de que falamos. A GLAD tem uma configuração ligeiramente diferente da maioria das bibliotecas de código aberto comuns. A GLAD usa um [serviço da web](http://glad.dav1d.de/) onde podemos dizer a GLAD para qual versão do OpenGL gostaríamos de definir e carregar todas as funções OpenGL relevantes de acordo com essa versão.

Vá para o [serviço da web](http://glad.dav1d.de/) da GLAD, certifique-se de que a linguagem esteja definida como `C++` e, na seção API, selecione uma versão OpenGL de pelo menos 3.3 (que é o que usaremos; versões superiores também servem). Certifique-se também de que o _profile_ esteja definido como _Core_ e que a opção _Generate a loader_ esteja marcada. Ignore as extensões (por enquanto) e clique em _Generate_ para produzir os arquivos da biblioteca.

A GLAD agora deve ter fornecido a você um arquivo zip contendo duas pastas de _include_ e um único arquivo **glad.c**. Copie ambas as pastas de inclusão (**glad** e **KHR**) em seu diretório de inclusão (ou adicione um item extra apontando para essas pastas) e adicione o arquivo **glad.c** ao seu projeto.

Após as etapas anteriores, você deve ser capaz de adicionar a seguinte diretiva de inclusão acima do arquivo:

```cpp
#include <glad/glad.h> 
```

Apertar o botão de compilação não deveria dar a você nenhum erro, e nesse ponto iremos para o próximo capítulo, onde discutiremos como podemos realmente usar a GLFW e a GLAD para configurar um contexto OpenGL e gerar uma janela. Certifique-se de verificar se todos os seus diretórios de inclusão e biblioteca estão corretos e se os nomes das bibliotecas nas configurações do linker correspondem às bibliotecas correspondentes.

# Recursos adicionais

   * [GLFW: Window Guide](http://www.glfw.org/docs/latest/window_guide.html): guia oficial da GLFW sobre como instalar e configurar uma janela da GLFW.
   * [Building applications](http://www.opengl-tutorial.org/miscellaneous/building-your-own-c-application/): fornece ótimas informações sobre o processo de compilação/linkagem da sua aplicação e uma lista grande de possíveis erros (mais soluções) que podem surgir.
   * [GLFW with Code::Blocks](http://wiki.codeblocks.org/index.php?title=Using_GLFW_with_Code::Blocks): compilando a GLFW na IDE Code::Blocks.
   * [Running CMake](http://www.cmake.org/runningcmake/): breve visão geral de como executar o CMake no Windows e no Linux.
   * [Writing a build system under Linux](https://learnopengl.com/demo/autotools_tutorial.txt): um tutorial de autotools por Wouter Verholst sobre como escrever um sistema de compilação no Linux.
   * [Polytonic/Glitter](https://github.com/Polytonic/Glitter): um projeto simples que vem pré-configurado com todas as bibliotecas relevantes; ótimo se você deseja um projeto de base sem o incômodo de ter que compilar todas as bibliotecas você mesmo.

