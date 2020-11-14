---
title: "Olá Janela"
date: 2020-10-29T21:02:14-03:00
draft: false
katex: true
markup: "mmark"
---

[Post Original](https://learnopengl.com/Getting-started/Hello-Window)

Vamos ver se conseguimos fazer a GLFW rodar. Primeiro, crie um arquivo **.cpp** e adicione as seguintes linhas no seu início.

```cpp
#include <glad/glad.h>
#include <GLFW/glfw3.h>
```

{{% notice tip %}}
Certifique-se de incluir a GLAD antes da GLFW. O arquivo de inclusão para a GLAD inclui os cabeçalhos OpenGL necessários nos bastidores (como **GL/gl.h**), portanto, certifique-se de incluir o GLAD antes de outros arquivos de cabeçalho que requerem OpenGL (como GLFW).
{{% /notice %}}

A seguir, criamos a função {{<struct main>}} onde instanciaremos a janela GLFW:

```cpp
int main()
{
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    //glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
  
    return 0;
}
```

Na função main, primeiro inicializamos a GLFW com {{<struct glfwInit>}}, após o qual podemos configurar a GLFW usando {{<struct glfwWindowHint>}}. O primeiro argumento de {{<struct glfwWindowHint>}} nos diz qual opção queremos configurar, onde podemos selecionar a opção de um  enum de opções possíveis prefixadas com **GLFW_**. O segundo argumento é um inteiro que define o valor de nossa opção. Uma lista de todas as opções possíveis e seus valores correspondentes pode ser encontrada na documentação sobre [manipulação de janelas da GLFW](http://www.glfw.org/docs/latest/window.html#window_hints). Se você tentar executar o programa agora e houver muitos erros de referência indefinida, isso significa que você não linkou a biblioteca GLFW com sucesso.

Como o foco deste livro está na OpenGL versão 3.3, gostaríamos de dizer a GLFW que 3.3 é a versão OpenGL que queremos usar. Desta forma, a GLFW pode fazer os arranjos apropriados ao criar o contexto OpenGL. Isso garante que, quando um usuário não tiver a versão adequada do OpenGL, a GLFW não será executado. Definimos as versões principal e secundária para 3. Também informamos a GLFW que queremos usar explicitamente o _core-profile_. Dizer a GLFW que queremos usar o _core-profile_ significa que teremos acesso a um subconjunto menor de recursos da OpenGL sem compatibilidade com versões anteriores de que não precisamos mais. Observe que no Mac OS X você precisa adicionar {{<struct glfwWindowHint>}}(<variable GLFW_OPENGL_FORWARD_COMPAT>}}, {{<variable GL_TRUE>}}); ao seu código de inicialização para que isso funcione.

{{% notice tip %}}
Certifique-se de ter a OpenGL versão 3.3 ou superior instalada em seu sistema/hardware, caso contrário, o aplicativo irá travar ou exibir um comportamento indefinido. Para encontrar a versão OpenGL em sua máquina, chame **glxinfo** em máquinas Linux ou use um utilitário como o [OpenGL Extension Viewer](http://download.cnet.com/OpenGL-Extensions-Viewer/3000-18487_4-34442.html) para Windows. Se sua versão suportada for inferior, tente verificar se sua placa de vídeo suporta OpenGL 3.3+ (caso contrário, ela é muito antiga) e/ou atualize seus drivers.
{{% /notice %}}

Em seguida, somos obrigados a criar um objeto de janela. Este objeto de janela contém todos os dados de janelas e é exigido pela maioria das outras funções do GLFW.

```cpp
GLFWwindow* window = glfwCreateWindow(800, 600, "LearnOpenGL", NULL, NULL);
if (window == NULL)
{
    std::cout << "Failed to create GLFW window" << std::endl;
    glfwTerminate();
    return -1;
}
glfwMakeContextCurrent(window);
```

A função {{<struct glfwCreateWindow>}} requer a largura e altura da janela como seus dois primeiros argumentos, respectivamente. O terceiro argumento nos permite criar um nome para a janela; por enquanto, o chamamos de **"LearnOpenGL"**, mas você tem permissão para nomeá-lo como quiser. Podemos ignorar os 2 últimos parâmetros. A função retorna um objeto {{<struct GLFWwindow>}} que mais tarde precisaremos para outras operações GLFW. Depois disso, dizemos a GLFW para tornar o contexto de nossa janela o contexto principal na _thread_ corrente.

## GLAD

No capítulo anterior, mencionamos que a GLAD gerencia ponteiros de função para OpenGL, portanto, queremos inicializar a GLAD antes de chamar qualquer função OpenGL:
```cpp
if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
{
    std::cout << "Failed to initialize GLAD" << std::endl;
    return -1;
}  
```

## Janela de exibição (Viewport)

Antes de começarmos a renderizar, temos que fazer uma última coisa. Temos que dizer a OpenGL o tamanho da janela de renderização para que a OpenGL saiba como queremos exibir os dados e as coordenadas em relação à janela. Podemos definir essas dimensões por meio da função {{<struct glViewport>}}:
```cpp
glViewport(0, 0, 800, 600); 
```
Os primeiros dois parâmetros de {{<struct glViewport>}} definem a localização do canto esquerdo inferior da janela. O terceiro e quarto parâmetros definem a largura e a altura da janela de renderização em pixels, que definimos igual ao tamanho da janela da GLFW.

Na verdade, poderíamos definir as dimensões da janela de visualização com valores menores do que as dimensões da GLFW; então, toda a renderização da OpenGL seria exibida em uma janela menor e poderíamos, por exemplo, exibir outros elementos fora da janela de exibição OpenGL.

{{% notice tip %}}
Nos bastidores, a OpenGL usa os dados especificados via {{<struct glViewport>}} para transformar as coordenadas 2D que processou em coordenadas na tela. Por exemplo, um ponto processado de localização $(-0.5,0.5)$ seria (como sua transformação final) mapeado para $(200,450)$ nas coordenadas da tela. Observe que as coordenadas processadas em OpenGL estão entre $-1$ e $1$, portanto, mapeamos efetivamente do intervalo ($-1$ a $1$) a $(0, 800)$ e $(0, 600)$.
{{% /notice %}}

No entanto, no momento em que um usuário redimensiona a janela, a janela de visualização também deve ser ajustada. Podemos registrar uma função de _callback_ na janela toda vez que a janela é redimensionada. Esta função tem a seguinte assinatura:

```cpp
void framebuffer_size_callback(GLFWwindow* window, int width, int height);  
```
A função de tamanho do _framebuffer_ leva um {{<struct GLFWwindow>}} como seu primeiro argumento e dois inteiros indicando as novas dimensões da janela. Sempre que a janela muda de tamanho, a GLFW chama esta função e preenche os argumentos apropriados para você processar.

```cpp
void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    glViewport(0, 0, width, height);
}  
```

Nós temos que dizer a GLFW que queremos chamar esta função em todo redimensionamento da janela registrando a função:

```cpp
glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);   
```

Quando a janela é exibida pela primeira vez, {{<struct framebuffer_size_callback>}} é chamada também com as novas dimensões da janela. Para telas de retina, a largura {{<variable width>}} e a altura {{<variable height>}} serão significativamente maiores do que os valores de entrada originais.

Existem muitas funções {{<english callback>}} que podemos definir para registrar nossas próprias funções. Por exemplo, podemos fazer uma função para processar as mudanças na entrada do joystick, mensagens de erro do processo, etc. Registramos as funções {{<english callback>}} depois de criarmos a janela e antes do loop de renderização ser iniciado.

## Prepare seus motores

Não queremos que o programa desenhe uma única imagem e então feche imediatamente. Queremos que o programa continue desenhando imagens e manipulando a entrada do usuário até que ele seja explicitamente instruído a parar. Por esta razão, temos que criar um {{<english loop>}}, que agora chamamos de {{<definition loop>}} {{<definition de>}} {{<definition renderização>}} ({{<english rendering>}} {{<english loop>}}), que continua em execução até que digamos a GLFW para parar. O código a seguir mostra um loop de renderização muito simples:

```cpp
while(!glfwWindowShouldClose(window))
{
    glfwSwapBuffers(window);
    glfwPollEvents();    
} 
```

A função {{<struct glfwWindowShouldClose>}} verifica no início de cada iteração do loop se a GLFW foi instruída a fechar. Nesse caso, a função retorna **true** e o loop de renderização para de executar, e podemos fechar a aplicação.

A função {{<struct glfwPollEvents>}} verifica se algum evento é acionado (como entrada do teclado ou eventos de movimento do mouse), atualiza o estado da janela e chama as funções correspondentes (que podemos registrar por meio de {{<english callbacks>}}). O {{<struct glfwSwapBuffers>}} irá trocar o {{<english buffer>}} de cor (um grande buffer 2D que contém valores de cor para cada pixel na janela da GLFW) que é usado para renderizar durante esta iteração de renderização e mostrá-lo como saída na tela.

{{% notice tip %}}
**Buffer Duplo**: 
Quando um programa desenha em um único buffer, a imagem final pode exibir problemas de oscilação. Isso ocorre porque a imagem de saída não é desenhada em um instante, mas desenhada pixel por pixel e geralmente da esquerda para a direita e de cima para baixo. Como essa imagem não é exibida imediatamente para o usuário enquanto ainda está sendo renderizada, o resultado pode conter artefatos. Para contornar esses problemas, as aplicações aplicam um buffer duplo para a renderização. O buffer **frontal** ({{<english front>}} contém a imagem de saída final que é mostrada na tela, enquanto todos os comandos de renderização são direcionados ao buffer **posterior** ({{<english back>}}). Assim que todos os comandos de renderização forem concluídos, trocamos (**swap**) o buffer traseiro para o buffer frontal para que a imagem possa ser exibida sem ainda ter sido renderizada, removendo todos os artefatos mencionados acima.
{{% /notice %}}

## Para terminar

Assim que sairmos do loop de renderização, gostaríamos de limpar/deletar adequadamente todos os recursos da GLFW que foram alocados. Podemos fazer isso por meio da função {{<struct glfwTerminate>}} que chamamos no final da função principal.

```cpp
glfwTerminate ();
return 0;
```

Isso limpará todos os recursos e sairá do programa corretamente. Agora tente compilar sua aplicação e se tudo correr bem, você verá a seguinte saída:

![GitHub Logo](/inicio/ola_janela/images/hellowindow.png)

Se for uma imagem preta sem graça e entediante, você fez as coisas certas! Se você não obteve a imagem certa ou está confuso sobre como tudo se encaixa, verifique o código-fonte completo [aqui](https://learnopengl.com/code_viewer_gh.php?code=src/1.getting_started/1.1.hello_window/hello_window.cpp).

Se você tiver problemas para compilar, primeiro certifique-se de que todas as opções do linker estejam definidas corretamente e de que incluiu corretamente os diretórios corretos na sua IDE (conforme explicado no capítulo anterior). Verifique também se o seu código está correto; você pode verificá-lo comparando-o com o código-fonte completo.

## Entrada

Também queremos ter alguma forma de controle de entrada na GLFW e podemos fazer isso com várias funções de entrada da GLFW. Vamos usar a função {{<struct glfwGetKey>}} da GLFW que recebe a janela como entrada junto com uma chave. A função retorna se esta tecla está sendo pressionada. Estamos criando uma função {{<struct processInput>}} para manter todo o código de entrada organizado:

```cpp
void processInput(GLFWwindow *window)
{
    if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}
```

Aqui verificamos se o usuário pressionou a tecla {{<english escape>}} (se não for pressionada, {{<struct glfwGetKey>}} retorna {{<variable GLFW_RELEASE>}}). Se o usuário pressionou a tecla escape, fechamos a GLFW definindo sua propriedade {{<variable WindowShouldClose>}} como **true** usando {{<struct glfwSetwindowShouldClose>}}. A próxima verificação de condição do loop **while** principal falhará e o aplicativo será fechado.

Em seguida, chamamos {{<struct processInput>}} a cada iteração do loop de renderização:

```cpp
while (!glfwWindowShouldClose(window))
{
    processInput(window);

    glfwSwapBuffers(window);
    glfwPollEvents();
} 
```

Isso nos dá uma maneira fácil de verificar se há ações de teclas específicas e reagir de acordo a cada {{<definition frame>}} (quadro). Uma iteração do loop de renderização é mais comumente chamada de {{<definition frame>}}.

## Renderização

Queremos colocar todos os comandos de renderização no loop de renderização, já que queremos executar todos os comandos de renderização a cada iteração ou quadro do loop. Isso seria mais ou menos assim:

```cpp
// loop de renderizacao
while(!glfwWindowShouldClose(window))
{
    // entrada
    processInput(window);

    // comandos de renderizacao aqui
    ...

    // checar e chamar eventos e troca de buffers
    glfwPollEvents();
    glfwSwapBuffers(window);
}
```

Apenas para testar se as coisas realmente funcionam, queremos limpar a tela com uma cor de nossa escolha. No início do frame, queremos limpar a tela. Caso contrário, ainda veríamos os resultados do quadro anterior (pode ser o efeito que você está procurando, mas normalmente não). Podemos limpar o buffer de cor da tela usando {{<struct glClear>}}, onde passamos os bits de buffer para especificar qual buffer gostaríamos de limpar. Os bits possíveis que podemos definir são {{<variable GL_COLOR_BUFFER_BIT>}}, {{<variable GL_DEPTH_BUFFER_BIT>}} e {{<variable GL_STENCIL_BUFFER_BIT>}}. No momento, só nos importamos com os valores das cores, portanto, apenas limpamos o buffer de cores.

```cpp
glClearColor (0.2f, 0.3f, 0.3f, 1.0f);
glClear (GL_COLOR_BUFFER_BIT);
```

Observe que também especificamos a cor para limpar a tela usando {{<struct glClearColor>}}. Sempre que chamamos {{<struct glClear>}} e limpamos o buffer de cor, todo o buffer de cor será preenchido com a cor configurada por {{<struct glClearColor>}}. Isso resultará em uma cor verde-azulada escura.

{{% notice tip %}}
Como você deve se lembrar do capítulo OpenGL, a função {{<struct glClearColor>}} é uma função de configuração de estado e {{<struct glClear>}} é uma função que usa o estado atual para pegar a cor de compensação.
{{% /notice %}}

![GitHub Logo](/inicio/ola_janela/images/hellowindow2.png)

O código fonte completo da aplicação pode ser encontrado [aqui](https://learnopengl.com/code_viewer_gh.php?code=src/1.getting_started/1.2.hello_window_clear/hello_window_clear.cpp).

Agora temos tudo pronto para preencher o loop de renderização com um monte de chamadas de renderização, mas isso fica para o próximo capitulo. Acho que estamos divagando há tempo suficiente aqui.
