---
title: "Cores"
date: 2020-10-29T15:28:58-03:00
draft: false
katex: true
markup: "mmark"
---

Usamos e manipulamos rapidamente as cores nos capítulos anteriores, mas nunca as definimos adequadamente. Aqui, discutiremos o que são as cores e começaremos a preparar o terreno para os próximos capítulos de Iluminação.

No mundo real, as cores podem assumir qualquer valor de cor conhecido, com cada objeto tendo sua(s) própria(s) cor(es). No mundo digital, precisamos mapear as (infinitas) cores reais para valores digitais (limitados) e, portanto, nem todas as cores do mundo real podem ser representadas digitalmente. As cores são representadas digitalmente usando uma componente **vermelha**, **verde** e **azul** comumente abreviadas como **RGB**. Usando diferentes combinações apenas desses 3 valores, dentro de um intervalo de `[0,1]`, podemos representar quase qualquer cor que existe. Por exemplo, para obter uma cor de coral, definimos um vetor de cor como:

```cpp

glm::vec3 coral(1.0f, 0.5f, 0.31f);   

```

A cor de um objeto que vemos na vida real não é a cor que ele realmente tem, mas é a cor {{<definition "refletida">}} ( {{<definition "reflected">}} do objeto. As cores que não são absorvidas (rejeitadas) pelo objeto são as cores que percebemos dele. Por exemplo, a luz do sol é percebida como uma luz branca que é a soma combinada de muitas cores diferentes (como você pode ver na imagem). Se jogarmos essa luz branca em um brinquedo azul, ele absorverá todas as subcores da cor branca, exceto a cor azul. Como o brinquedo não absorve a parte de cor azul, ela é refletida. Essa luz refletida entra em nossos olhos, fazendo com que pareça que o brinquedo tem uma cor azul. A imagem a seguir mostra isso para um brinquedo de cor coral, onde reflete várias cores com intensidade diferentes:

![altlogo](https://learnopengl.com/img/lighting/light_reflection.png)

Você pode ver que a luz do sol branca é uma coleção de todas as cores visíveis e o objeto absorve uma grande parte dessas cores. Ele reflete apenas as cores que representam a cor do objeto e a combinação delas é o que percebemos (neste caso, uma cor coral).

{{% greenbox tip %}}
Tecnicamente, é um pouco mais complicado, mas chegaremos a isso nos capítulos de PBR.
{{% /greenbox %}}

Essas regras de reflexão de cores se aplicam diretamente no _mundo dos gráficos_. Quando definimos uma fonte de luz em OpenGL, queremos dar uma cor a essa fonte de luz. No parágrafo anterior, tínhamos uma cor branca, então daremos à fonte de luz uma cor branca também. Se multiplicássemos a cor da fonte de luz pelo valor da cor de um objeto, a cor resultante seria a cor refletida do objeto (e, portanto, sua cor percebida). Vamos revisitar nosso brinquedo (desta vez com um valor coral) e ver como calcularíamos sua cor percebida no _mundo dos gráficos_. Obtemos o vetor de cor resultante fazendo uma multiplicação de componentes entre os vetores de luz e cor do objeto:

```cpp

glm::vec3 lightColor(1.0f, 1.0f, 1.0f);
glm::vec3 toyColor(1.0f, 0.5f, 0.31f);
glm::vec3 result = lightColor * toyColor; // = (1.0f, 0.5f, 0.31f);

```

Podemos ver que a cor do brinquedo _absorve_ grande parte da luz branca, mas reflete vários valores de vermelho, verde e azul com base em seu próprio valor de cor. Esta é uma representação de como as cores funcionariam na vida real. Podemos, portanto, definir a cor de um objeto como a quantidade de cada componente de cor que ele reflete de uma fonte de luz. Agora, o que aconteceria se usássemos uma luz verde?

```cpp

glm::vec3 lightColor(0.0f, 1.0f, 0.0f);
glm::vec3 toyColor(1.0f, 0.5f, 0.31f);
glm::vec3 result = lightColor * toyColor; // = (0.0f, 0.5f, 0.0f);

```

Como podemos ver, o brinquedo não possui luz vermelha e azul para absorver e / ou refletir. O brinquedo também absorve metade do valor da componente verde da luz, mas também reflete metade desse valor. A cor do brinquedo que percebemos seria então uma cor esverdeada escura. Podemos ver que se usarmos uma luz verde, apenas as componentes da cor verde podem ser refletidas e, portanto, percebidas; nenhuma cor vermelha e azul é percebida. Como resultado, o objeto coral subitamente se torna um objeto esverdeado escuro. Vamos tentar mais um exemplo com uma luz de cor verde-oliva escura:

```cpp

glm::vec3 lightColor(0.33f, 0.42f, 0.18f);
glm::vec3 toyColor(1.0f, 0.5f, 0.31f);
glm::vec3 result = lightColor * toyColor; // = (0.33f, 0.21f, 0.06f);

```

Como você pode ver, podemos obter cores interessantes de objetos usando cores de luz diferentes. Não é difícil ser criativo com as cores.

Mas chega de cores, vamos começar a construir uma cena onde possamos fazer experiências.

## Uma Cena de Iluminação

Nos próximos capítulos, criaremos visuais interessantes simulando a iluminação do mundo real fazendo uso extensivo de cores. Como agora usaremos fontes de luz, queremos exibi-las como objetos visuais na cena e adicionar pelo menos um objeto para simular a iluminação.

A primeira coisa de que precisamos é um objeto para lançar a luz e usaremos o infame cubo contêiner dos capítulos anteriores. Também precisaremos de um objeto de luz para mostrar onde a fonte de luz está localizada na cena 3D. Para simplificar, representaremos a fonte de luz com um cubo também (já temos os [dados do vértice](https://learnopengl.com/code_viewer.php?code=getting-started/cube_vertices_pos), certo?).



Portanto, preencher um objeto de buffer de vértices, definir ponteiros de atributo de vértice e tudo mais deve ser familiar para você agora, portanto, não o(a) conduziremos por essas etapas. Se você ainda não faz idéia sobre esses assuntos envolvendo vértices, sugiro que reveja os capítulos [anteriores]({{< ref "/ponto_de_partida/ola_triangulo" >}} "Olá Triângulo") e trabalhe com os exercícios, se possível, antes de continuar.

Portanto, a primeira coisa de que precisaremos é um shader de vértice para desenhar o contêiner. As posições dos vértices do contêiner permanecem as mesmas (embora não precisemos de coordenadas de textura neste momento), portanto, o código não deve ser nada novo. Estaremos usando uma versão simplificada do shader de vértice dos últimos capítulos:

```cpp

#version 330 core
layout (location = 0) in vec3 aPos;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view * model * vec4(aPos, 1.0);
} 

```

Certifique-se de atualizar os dados dos vértices e os ponteiros de atributos para corresponder ao novo shader de vértice (se quiser, você pode realmente manter os dados de textura e ponteiros de atributo ativos; apenas não os estamos usando agora).

Como também iremos renderizar um cubo de fonte de luz, queremos gerar um novo VAO especificamente para a fonte de luz. Poderíamos renderizar a fonte de luz com o mesmo VAO e, em seguida, fazer algumas transformações de posição de luz na matriz {{<variable "model">}}, mas nos próximos capítulos iremos alterar os dados de vértice e os ponteiros de atributo do objeto com bastante frequência e não queremos que essas alterações se propaguem para o objeto de fonte de luz (nos preocupamos apenas com as posições dos vértices do cubo de luz), então criaremos um novo VAO:

```cpp

unsigned int lightVAO;
glGenVertexArrays(1, &lightVAO);
glBindVertexArray(lightVAO);
// we only need to bind to the VBO, the container's VBO's data already contains the data.
glBindBuffer(GL_ARRAY_BUFFER, VBO);
// set the vertex attribute 
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
glEnableVertexAttribArray(0);

```

O código deve ser relativamente simples. Agora que criamos o contêiner e o cubo da fonte de luz, resta uma coisa a definir: o shader de fragmento para o recipiente e a fonte de luz:

```cpp

#version 330 core
out vec4 FragColor;
  
uniform vec3 objectColor;
uniform vec3 lightColor;

void main()
{
    FragColor = vec4(lightColor * objectColor, 1.0);
}

```

O shader de fragmento aceita uma cor de objeto e uma cor de luz de variáveis uniformes. Aqui, multiplicamos a cor da luz pela cor (refletida) do objeto, como discutimos no início deste capítulo. Novamente, esse shader deve ser fácil de entender. Vamos definir a cor do objeto para a cor coral da última seção com uma luz branca:

```cpp

// nao se esqueca de ativar o programa de shader correspondente primeiro (para configurar os uniformes)
lightingShader.use();
lightingShader.setVec3("objectColor", 1.0f, 0.5f, 0.31f);
lightingShader.setVec3("lightColor",  1.0f, 1.0f, 1.0f);

```

Uma coisa a se notar é que quando começarmos a atualizar esses _shaders de iluminação_ nos próximos capítulos, o cubo da fonte de luz também será afetado, e não é isso que queremos. Não queremos que a cor do objeto da fonte de luz seja afetada nos cálculos de iluminação, mas sim manter a fonte de luz isolada do resto. Queremos que a fonte de luz tenha uma cor brilhante constante, não afetada por outras mudanças de cor (isso faz com que pareça que o cubo da fonte de luz realmente é a fonte da luz).

Para resolver isso, precisamos criar um segundo conjunto de shaders que usaremos para desenhar o cubo da fonte de luz, portanto, protegidos de quaisquer mudanças nos shaders de iluminação. O shader de vértice é o mesmo que o shader de vértice de iluminação, então você pode simplesmente copiar o código-fonte. O shader de fragmento do cubo da fonte de luz garante que a cor do cubo permaneça brilhante, definindo uma cor branca constante na lâmpada:

```cpp

#version 330 core
out vec4 FragColor;

void main()
{
    FragColor = vec4(1.0); // define todos 4 valores do vetor para 1.0
}

```

Quando quisermos renderizar, queremos renderizar o objeto recipiente (ou possivelmente muitos outros objetos) usando o shader de iluminação que acabamos de definir, e quando quisermos desenhar a fonte de luz, usamos os shaders da fonte de luz. Durante os capítulos de Iluminação, estaremos atualizando gradativamente os shaders de iluminação para obter resultados mais realistas.

O objetivo principal do cubo da fonte de luz é mostrar de onde vem a luz. Normalmente definimos a posição de uma fonte de luz em algum lugar da cena, mas esta é simplesmente uma posição sem significado visual. Para mostrar onde a fonte de luz realmente está, renderizamos um cubo no mesmo local da fonte de luz. Renderizamos este cubo com o shader de cubo de fonte de luz para garantir que o cubo sempre permaneça branco, independentemente das condições de luz da cena.

Então, vamos declarar uma variável `vec3` global que representa a localização da fonte de luz nas coordenadas de mundo:

```cpp

glm::vec3 lightPos(1.2f, 1.0f, 2.0f);

```

Em seguida, transladamos o cubo da fonte de luz para a posição da fonte de luz e o redimensionamos antes de renderizá-lo:

```cpp

model = glm::mat4(1.0f);
model = glm::translate(model, lightPos);
model = glm::scale(model, glm::vec3(0.2f)); 

```

O código de renderização resultante para o cubo da fonte de luz deve ser semelhante a este:

```cpp

lightCubeShader.use();
// define os uniformes das matrizes de model, view e projection
[...]
// desenhe o objeto do cubo de luz
glBindVertexArray(lightCubeVAO);
glDrawArrays(GL_TRIANGLES, 0, 36);			

```

O posicionamento de todos os fragmentos de código em seus locais apropriados resultaria em uma aplicação OpenGL devidamente configurada para fazer experiências com iluminação. Se tudo compilar, deve ficar assim:

![altlogo](https://learnopengl.com/img/lighting/colors_scene.png)

Não há muito o que ver agora, mas prometo que ficará mais interessante nos próximos capítulos.

Se você tiver dificuldades para descobrir onde todos os fragmentos de código se encaixam no programa como um todo, verifique o código-fonte [aqui](/code_viewer_gh.php?code=src/2.lighting/1.colors/colors.cpp) e consulte  cuidadosamente o código / comentários.

Agora que temos um bom conhecimento sobre as cores e criamos uma cena básica para fazer experiências com iluminação, podemos pular para o [próximo]({{< ref "/iluminacao/iluminacao_basica" >}} "Iluminação Básica") capítulo, onde começa a verdadeira magia.

