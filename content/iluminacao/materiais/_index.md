---
title: "Materiais"
date: 2020-10-29T15:28:58-03:00
draft: false
katex: true
markup: "mmark"
---

[Post Original](https://learnopengl.com/Lighting/Materials)


No mundo real, cada objeto tem uma reação diferente à luz. objetos de aço são muitas vezes mais brilhante do que um vaso de argila, por exemplo, e um recipiente de madeira não reage da mesma à luz como um recipiente de aço. Alguns objetos refletem a luz sem muita dispersão resultando em pequenos reflexos especulares e outros espalhar um monte dando o destaque um raio maior. Se quisermos simular vários tipos de objetos em OpenGL temos que definir as propriedades do material específico para cada superfície.

No capítulo anterior, definido um objecto e cor da luz para definir a saída visual do objecto, combinado com um componente de intensidade ambiente e especular. Quando se descreve uma superfície que pode definir uma cor de material para cada um dos 3 componentes de iluminação ambiente, difusa e especular iluminação. Ao especificar uma cor para cada um dos componentes nós temos o controle de grão fino sobre a saída de cor da superfície. Agora adicione um componente brilho aos 3 cores e temos todas as propriedades do material que precisamos:

```cpp

#version 330 core
struct Material {
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float shininess;
}; 
  
uniform Material material;

```

No sombreador fragmento que criar uma estrutura para armazenar as propriedades do material da superfície. Nós também pode armazená-los como valores uniformes individuais, mas armazená-los como um struct mantém-lo mais organizado. Nós primeiro definir o layout da estrutura e depois simplesmente declarar uma variável uniforme com a estrutura recém-criada como seu tipo.

Como você pode ver, nós definimos um vetor de cor para cada um dos componentes da iluminação Phong. Os materiais define vector ambiente o que a cor da superfície reflecte sob iluminação ambiente; este é geralmente o mesmo que a cor da superfície. O vector de material difuso define a cor da superfície sob iluminação difusa. A cor é difusa (tal como a iluminação ambiente) ajustado a cor da superfície desejada. O material de vetor especular define a cor do realce especular sobre a superfície (ou possivelmente até mesmo refletir uma cor específica de superfície). Por último, os impactos brilho a dispersão / raio do realce especular.

Com estes 4 componentes que definem o material de um objeto que pode simular muitos materiais do mundo real. Uma tabela como encontrado em shows devernay.free.fr uma lista das propriedades dos materiais que simulam materiais reais encontrados no mundo exterior. A seguinte imagem mostra o efeito de vários desses valores materiais do mundo real tem na sua cubo:

(http://devernay.free.fr/cours/opengl/materials.html)

![altlogo](https://learnopengl.com/img/lighting/materials_real_world.png)

Como você pode ver, especificando corretamente as propriedades do material de uma superfície que parece mudar a percepção que temos do objeto. Os efeitos são claramente visíveis, mas para os resultados mais realistas precisaremos substituir o cubo com algo mais complicado. Nos Carregando capítulos modelo vamos discutir formas mais complicadas.

(https://learnopengl.com/Model-Loading/Assimp)

Descobrir as configurações de material certo para um objeto é um feito difícil que requer principalmente a experimentação e muita experiência. Não é incomum para destruir completamente a qualidade visual de um objeto por um material extraviado.

Vamos tentar implementar um sistema de tal material nos shaders.

# Setting materials

Nós criamos uma estrutura de material uniforme no shader de fragmento tão próxima que queremos mudar os cálculos de iluminação para cumprir com as novas propriedades dos materiais. Uma vez que todas as variáveis ​​relevantes são armazenados em uma estrutura que pode acessá-los a partir do uniforme de material:

```cpp

void main()
{    
    // ambient
    vec3 ambient = lightColor * material.ambient;
  	
    // diffuse 
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = lightColor * (diff * material.diffuse);
    
    // specular
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);  
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), material.shininess);
    vec3 specular = lightColor * (spec * material.specular);  
        
    vec3 result = ambient + diffuse + specular;
    FragColor = vec4(result, 1.0);
}

```

Como você pode ver que agora acessar todas as propriedades do material de struct onde quer que precisamos deles e desta vez calcular a cor de saída resultante com a ajuda de cores do material. Cada um dos atributos materiais do objeto são multiplicados com os respectivos componentes de iluminação.

Podemos definir o material do objeto no aplicativo, definindo os uniformes apropriados. A estrutura em GLSL, contudo, não é especial em qualquer consideração ao definir uniformes; uma estrutura realmente só funciona como um espaço de nomes de variáveis ​​uniformes. Se queremos preencher a estrutura que terá que definir os uniformes individuais, mas prefixado com o nome do struct:

```cpp

lightingShader.setVec3("material.ambient", 1.0f, 0.5f, 0.31f);
lightingShader.setVec3("material.diffuse", 1.0f, 0.5f, 0.31f);
lightingShader.setVec3("material.specular", 0.5f, 0.5f, 0.5f);
lightingShader.setFloat("material.shininess", 32.0f);

```

Vamos definir o ambiente e difusa componente para a cor que gostaria que o objeto a tem e definir o componente especular do objeto para uma cor meio-brilhante; não queremos que o componente especular a ser muito forte. Nós também manter o brilho em 32.

Agora podemos influenciar facilmente o material do objeto da aplicação. Executando o programa dá-lhe algo como isto:

![altlogo](https://learnopengl.com/img/lighting/materials_with_material.png)

Realmente não olhar embora certo?

## Light properties

O objeto é muito brilhante. A razão para o objeto a ser demasiado brilhante é que o ambiente, difusa e cores especulares são refletidas com força total a partir de qualquer fonte de luz. As fontes de luz também têm diferentes intensidades para o seu ambiente, difusa e componentes especulares respectivamente. No capítulo anterior, nós resolvemos isso, variando as intensidades ambiente e especular com um valor de força. Queremos fazer algo semelhante, mas desta vez especificando vetores de intensidade para cada um dos componentes de iluminação. Se tivéssemos visualizar LightColor como vec3 (1.0) o código ficaria assim:

```cpp

vec3 ambient  = vec3(1.0) * material.ambient;
vec3 diffuse  = vec3(1.0) * (diff * material.diffuse);
vec3 specular = vec3(1.0) * (spec * material.specular); 

```

Assim, cada propriedade do material do objeto é retornado com plena intensidade para cada um dos componentes da luz. Estes valores vec3 (1.0) pode ser influenciada individualmente, bem como para cada fonte de luz e este é geralmente o que queremos. Neste momento, o componente do ambiente do objecto é influenciar totalmente a cor do cubo. O componente de ambiente não deve realmente ter um impacto tão grande sobre a cor final para que possamos restringir a cor ambiente, definindo intensidade ambiente da luz para um valor mais baixo:

```cpp

vec3 ambient = vec3(0.1) * material.ambient;  

```

Podemos influenciar o difuso e intensidade especular da fonte de luz da mesma forma. Isto é muito semelhante ao que fizemos no capítulo anterior; você poderia dizer que já criou algumas propriedades de luz para influenciar cada componente de iluminação individualmente. Nós vamos querer criar algo semelhante para a estrutura material para as propriedades de luz:

(https://learnopengl.com/Lighting/Basic-Lighting)

```cpp

struct Light {
    vec3 position;
  
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};

uniform Light light;  

```

Uma fonte de luz tem uma intensidade diferente para o seu ambiente, difusa e componentes especulares. A luz ambiente é geralmente definida como uma baixa intensidade, porque não queremos que a cor do ambiente a ser demasiado dominante. O componente difuso de uma fonte de luz é geralmente definida como a cor exata que gostaria de uma luz para ter; muitas vezes uma cor branca brilhante. O componente especular é normalmente mantida a vec3 (1.0) que brilha com intensidade máxima. Note que nós também adicionamos da luz vetor posição para a estrutura.

Assim como com o uniforme de material que precisamos para atualizar o shader de fragmento:

```cpp

vec3 ambient  = light.ambient * material.ambient;
vec3 diffuse  = light.diffuse * (diff * material.diffuse);
vec3 specular = light.specular * (spec * material.specular);  

```

Em seguida, deseja definir as intensidades de luz na aplicação:

```cpp
 
lightingShader.setVec3("light.ambient",  0.2f, 0.2f, 0.2f);
lightingShader.setVec3("light.diffuse",  0.5f, 0.5f, 0.5f); // darken diffuse light a bit
lightingShader.setVec3("light.specular", 1.0f, 1.0f, 1.0f); 

```

Agora que nós modulada como as influências claras de material do objeto tenhamos uma saída visual que se parece muito com a saída do capítulo anterior. Desta vez, no entanto, tem o controle total sobre a iluminação e o material do objeto:

![altlogo](https://learnopengl.com/img/lighting/materials_light.png)

Alterando os aspectos visuais de objetos é relativamente fácil agora. de deixar as coisas apimentar um pouco!

## Different light colors

Até agora usamos cores claras apenas variar a intensidade de seus componentes individuais, escolhendo cores que variam do branco ao cinza ao preto, não afetando as cores reais do objeto (somente sua intensidade). Uma vez que agora têm acesso fácil às propriedades da luz que pode mudar suas cores ao longo do tempo para obter alguns efeitos muito interessantes. Uma vez que tudo já está configurado no shader de fragmento, mudando as cores da luz é fácil e imediatamente cria alguns efeitos funk:

![altlogo](https://learnopengl.com/img/lighting/materials_light_colors.png)

Como você pode ver, uma cor clara diferente influencia grandemente a saída de cores do objeto. Desde a cor da luz influencia diretamente as cores que o objeto pode refletir (como você pode se lembrar do capítulo cores) tem um impacto significativo sobre a saída visual.

(https://learnopengl.com/Lighting/Colors)

Nós podemos facilmente mudar as cores da luz ao longo do tempo, alterando cores ambientais e difusos da luz através do pecado e glfwGetTime:

```cpp

glm::vec3 lightColor;
lightColor.x = sin(glfwGetTime() * 2.0f);
lightColor.y = sin(glfwGetTime() * 0.7f);
lightColor.z = sin(glfwGetTime() * 1.3f);
  
glm::vec3 diffuseColor = lightColor   * glm::vec3(0.5f); 
glm::vec3 ambientColor = diffuseColor * glm::vec3(0.2f); 
  
lightingShader.setVec3("light.ambient", ambientColor);
lightingShader.setVec3("light.diffuse", diffuseColor);

```

Experimente e experimentar com vários iluminação e valores materiais e ver como eles afetam a saída visual. Você pode encontrar o código-fonte do aplicativo aqui.

(/code_viewer_gh.php?code=src/2.lighting/3.1.materials/materials.cpp)

## Exercises




você pode fazer com que a mudança da cor da luz muda a cor do objeto de cubo da luz?

você pode simular alguns dos objetos do mundo real através da definição de seus respectivos materiais como vimos no início deste capítulo? Note-se que os valores do ambiente da tabela não são os mesmos que os valores difusos; eles não levaram intensidades de luz em conta. Para definir corretamente seus valores você teria que definir todas as intensidades de luz para vec3 (1.0) para obter o mesmo resultado: solução de recipiente de plástico ciano.

(http://devernay.free.fr/cours/opengl/materials.html)

(/code_viewer_gh.php?code=src/2.lighting/3.2.materials_exercise1/materials_exercise1.cpp)

