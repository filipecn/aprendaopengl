---
title: "OpenGL"
date: 2020-10-29T21:02:14-03:00
draft: false
weight: 5
---

[Post Original](https://learnopengl.com/Getting-started/OpenGL)

Antes de começar nossa jornada devemos primeiro definir o que de fato é a OpenGL. A OpenGL é sobretudo considerada uma API ({{<definition Application>}} {{<definition Programming>}} {{<definition Interface>}}) que provê uma variedade de funções que podemos usar para manipular gráficos e imagens. Porém, a OpenGL por si só não é uma API, mas meramente uma especificação, desenvolvida e mantida pelo [Grupo Khronos](https://www.khronos.org/).

A especificação da OpenGL define exatamente o que o resultado/saída de cada função deveria ser e como deveria funcionar. Fica então para os desenvolvedores _implementar_ essa especificação e pensar em uma solução em como as funções deveria operar. Como a especificação da OpenGL não nos dá os detalhes de implementação, as versões da OpenGL que são de fato desenvolvidas têm permissão de ter diferentes implementações, desde que seus resultados concordem com a especificação (e são portanto os mesmos para o usuário).

As pessoas que desenvolvem as bibliotecas da OpenGL são normalmente os fabricantes de placas gráficas. Cada placa gráfica que você compra suporta versões específicas da OpenGL, que são desenvolvidas especificamente para aquela (série) placa. Quando se usa um sistema Apple a biblioteca da OpenGL é mantida pela própria Apple e sob o Linux existe uma combinação de fornecedores de versões adaptações de hobistas dessas bibliotecas. Isso significa que sempre que a OpenGL mostrar um comportamento estranho, provavelmente a culpa é dos fabricantes de placas gráficas (ou quem quer que tenha desenvolvido/mantido a biblioteca).

{{% notice tip %}}
Já que a maioria das implementações é feita por fabricantes de placas gráficas, sempre que existir um erro de implementação o problema é normalmente resolvido ao atualizar os drivers da placa de vídeo; esses drivers incluem as versões mais novas da OpenGL que a placa suporta. Esta é uma das razões pela qual é recomendável ocasionalmente atualizar os drivers gráficos.
{{% /notice %}}

O Khronos hospeda publicamente todos documentos com a especificação de todas versões da OpenGL. O leitor interessado pode encontrar as especificações da versão 3.3 da OpenGL (que é a versão que vamos utilizar) [aqui](https://www.opengl.org/registry/doc/glspec33.core.20100311.withchanges.pdf), que é uma boa leitura se você quiser mergulhar nos detalhes da OpenGL (note como eles descrevem mais os resultados do que as implementações). As especificações também dão uma boa referencia para encontrar o funcionamento **exato** das suas funções.

## Core-profile vs Immediate mode (modo imediato)

Antigamente, usar a OpenGL significava desenvolver em {{<definition modo>}} {{<definition imediato>}} (normalmente referido como o pipeline de funções fixas (the {{<definition fixed>}} {{<definition function>}} {{<definition pipeline>}})), o qual era um método fácil-de-usar para desenhar gráficos. A maior parte da funcionalidade da OpenGL era escondida dentro da biblioteca e os desenvolvedores não tinham muito controle sobre como a OpenGL faz seus cálculos. Os desenvolvedores eventualmente ficaram famintos por mais flexibilidade e com o tempo as especificações se tornaram mais flexíveis como resultado; os desenvolvedores ganharam mais controle sobre seus gráficos. O modo imediato é realmente fácil de usar e entender, mas é extremamente ineficiente. Por essa razão a especificação começou a descontinuar a funcionalidade de modo imediato da versão 3.2 em diante e começou a motivar os programadores a desenvolver no modo {{<definition core-profile>}} da OpenGL, que é uma divisão da especificação da OpenGL que removeu toda funcionalidade antiga e descontinuada.

Quando se usa o core-profile da OpenGL, a OpenGL nos força a seguir praticas modernas. Sempre que tentarmos utilizar uma função descontinuada, a OpenGL cospe um erro e para de desenhar. A vantagem de aprender a abordagem moderna é que ela é muito flexível e eficiente. Porém, é também mais difícil de aprender. O modo imediato abstraiu demais muitas das operações executadas pela OpenGL e, enquanto era fácil de aprender, era mais difícil de entender como a OpenGL realmente funciona. A abordagem moderna requer que o programador verdadeiramente entenda a OpenGL, e enquanto isso é meio difícil, permite muito mais flexibilidade, mais eficiência e o mais importante: um entendimento muito melhor de programação de gráficos.

Essa é também a razão do porque esse livro é engrenado no core-profile da versão 3.3 da OpenGL. Embora seja mais difícil, vale muito a pena o esforço.

Atualmente, versões mais altas da OpenGL estão disponíveis sobre as quais você pode perguntar: porque eu quero aprender OpenGL 3.3 se existe a 4.6? A resposta para esta questão é relativamente simples. Todas versões posteriores a 3.3 adicionam funcionalidades extras a OpenGL sem mudar a mecânica do núcleo da OpenGL; as versões mais novas introduzem modos mais eficientes ou mais úteis para completar as mesmas tarefas. O resultado é que todos conceitos e técnicas permanecem os mesmos pelas versões da OpenGL moderna, então é perfeitamente válido aprender a OpenGL 3.3. Sempre que estiver pronto e/ou mais experiente, você pode facilmente usar uma funcionalidade especifica de versões da OpenGL mais recentes.

{{% notice warning %}}
Quando se utiliza a versão mais recente da OpenGL, apenas as placas gráficas mais modernas terão capacidade de rodar sua aplicação. Por isso a maioria dos desenvolvedores geralmente visa versões mais baixas da OpenGL e opcionalmente habilitam funcionalidades de versões mais altas.
{{% /notice %}}

Em alguns capítulos você encontrará recursos mais modernos que são anotados como tais.

## Extensões

Um recurso muito bom da OpenGL é seu suporte a extensões. Sempre que uma empresa de gráficos aparece com uma técnica nova ou uma otimização importante para renderização, estas novidades são normalmente encontradas em uma {{<definition extensão>}} implementada nos drivers. Se o hardware suporta uma extensão em particular, o programador pode usar a sua funcionalidade em busca de aplicações gráficas mais avançadas e eficientes. Deste modo, um desenvolvedor de gráficos pode ainda usar estas técnicas novas de renderização sem ter que esperar pela inclusão da funcionalidade nas versões futuras da OpenGL, tendo apenas que checar se a extensão é suportada pela placa gráfica. Frequentemente, quando uma extensão é popular ou muito útil ela eventualmente é incorporada a versões futuras da OpenGL.

O programador deve inquerir se algumas dessas extensões estáo disponíveis antes de utilizá-las (ou usar uma biblioteca de extensão da OpenGL). Isto permite que o programador faça coisas de um jeito melhor ou mais eficiente, baseado se uma extensão pode ser usada:
```cpp
if(GL_ARB_extension_name)
{
    // Fazer coisas maneiras e modernas suportadas pelo hardware
}
else
{
    // Extensao nao eh suportada: fazer isso do jeito antigo
}
```

Com a versão 3.3 da OpenGL nós raramente precisamos de uma extensão para maioria das técnicas, mas sempre que for necessário instruções serão dadas.

## Máquina de Estados

A OpenGL é uma grande máquina de estados: uma coleção de variáveis que definem como a OpenGL deveria se comportar. O estado da OpenGL é comumente referido como o contexto da OpenGL. Quando utilizamos a OpenGL, normalmente mudamos seu estado através da configuração de algumas opções, manipulação de alguns buffers e então renderizamos o contexto corrente.

Sempre que dizemos a OpenGL que agora queremos desenhar linhas ao invés de triângulos por exemplo, mudamos o estado da OpenGL através de algumas variáveis de contexto que definem como a OpenGL deveria desenhar. Assim que mudamos o contexto ao dizer a OpenGL que esta deveria desenhar linhas, os próximos comandos de desenho irão desenhar linhas ao invés de triângulos.

Ao trabalhar com a OpenGL iremos esbarrar com várias funções de mudança de estado que mudam o contexto e várias funções que dependem do estado corrente da OpenGL. Contando que você mantenha na sua mente que a OpenGL é basicamente uma grande máquina de estados, a maioria de suas funcionalidades farão mais sentido.

## Objetos

As bibliotecas da OpenGL são escritas em `C` e permitem muitas derivações em outras linguagens, mas no seu núcleo ela permanece uma biblioteca em `C`. Como várias construções da linguagem `C` não traduzem bem para outras linguagens de alto nível, a OpenGL foi desenvolvida com uma variedade de abstrações em mente. Uma dessas abstrações são os {{<definition objetos>}} em OpenGL.

Um objeto na OpenGL é uma coleção de opções que representam um subconjunto do estado da OpenGL. Por exemplo, poderíamos ter um objeto que representa as configurações da janela de desenho; nós poderíamos então definir seu tamanho, quantas cores ela suporta e assim em diante. Alguém poderia visualizar um objeto como uma estrutura do `C`:
```cpp
struct object_name {
    float  option1;
    int    option2;
    char[] name;
};}
```
Sempre que quisermos usar objetos, geralmente vão se parecer com isso (com o contexto da OpenGL visualizado como uma grande estrutura):
```cpp
// The State of OpenGL
struct OpenGL_Context {
  	...
  	object_name* object_Window_Target;
  	...  	
};
```
```cpp
// create object
unsigned int objectId = 0;
glGenObject(1, &objectId);
// bind/assign object to context
glBindObject(GL_WINDOW_TARGET, objectId);
// set options of object currently bound to GL_WINDOW_TARGET
glSetObjectOption(GL_WINDOW_TARGET, GL_OPTION_WINDOW_WIDTH,  800);
glSetObjectOption(GL_WINDOW_TARGET, GL_OPTION_WINDOW_HEIGHT, 600);
// set context target back to default
glBindObject(GL_WINDOW_TARGET, 0);
```

Este pedacinho de código é uma rotina que você irá encontrar frequentemente quando estiver trabalhando com a OpenGL. Nós primeiro criamos um objeto e armazenamos uma referencia para ele como um id (o dado real do objeto é armazenado nos bastidores). Então nós ligamos (_bind_) o objeto (usando seu id) ao uma localização alvo do contexto (a localização do exemplo é definida como {{<variable GL_WINDOW_TARGET>}}). Em seguida, definimos as opções da janela e finalmente desconectamos o objeto ao setar o id do objeto corrente da janela alvo para 0. As opções que definimos são armazenadas no objeto referenciado por {{<variable objectId>}} e restauradas assim que ligamos o objeto de volta a {{<variable GL_WINDOW_TARGET>}}. 

{{% notice warning %}}
Os códigos mostrados até agora são apenas aproximações de como a OpenGL opera; ao longo deste livro você encontrará exemplos de verdade o suficiente.
{{% /notice %}}

O lado bom de utilizar esses objetos é que podemos definir mais de um objeto em nossa aplicação, definir suas opções e sempre que começarmos uma operação que usa o estado da OpenGL, podemos conectar o objeto com nossas configurações. Existem objetos por exemplo, que agem como objetos recipientes para dados de modelos 3D (uma casa ou um personagem) e sempre que quisermos desenhar um deles, nós ligamos o objeto contendo os dados do modelo que queremos desenhar (dado que primeiramente criamos e setamos suas opções). Ter vários objetos nos permite especificar vários modelos e sempre que quisermos desenhar um modelo específico, basta conectar o objeto correspondente antes de desenhar sem ter que configurar todas opções de novo.

## Vamos começar

Você aprendeu um pouco sobre a OpenGL como uma especificação e uma biblioteca, como aproximadamente a OpenGL opera por debaixo dos panos e alguns truques customizados que a OpenGL utiliza. **Não se preocupe se não entendeu tudo**; ao longo do livro vamos passar por cada passo e você verá exemplos o suficientes para realmente pegar o jeito da OpenGL.

# Recursos Adicionais
* [opengl.org](https://www.opengl.org/): website oficial da OpenGL
* [OpenGL registry](https://www.opengl.org/registry/): hospeda as especificações e extensões de todas versões da OpenGL.







