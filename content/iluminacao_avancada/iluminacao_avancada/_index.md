---
title: "Iluminação Avançada"
date: 2020-11-02T17:36:44-03:00
draft: false
katex: true
markup: "mmark"
---

Nos capítulos de [iluminação]({{< ref "/iluminacao/iluminacao_basica" >}} "Iluminação Básica"), apresentamos brevemente o modelo de iluminação Phong para trazer um mínimo de realismo às nossas cenas. O modelo Phong parece bom, mas tem algumas nuances nas quais nos concentraremos neste capítulo.

## Blinn-Phong

A iluminação Phong é uma aproximação excelente e muito eficiente da iluminação, mas seus reflexos especulares falham em certas condições, especificamente quando a propriedade de brilho é baixa, resultando em uma grande área especular (áspera). A imagem abaixo mostra o que acontece quando usamos um expoente de brilho especular de `1.0` em um plano com textura:

![altlogo](https://learnopengl.com/img/advanced-lighting/advanced_lighting_phong_limit.png)

Você pode ver nas bordas que a área especular é imediatamente cortada. Isso acontece porque o ângulo entre o vetor da câmera e o vetor de reflexão não ultrapassa 90 graus. Se o ângulo for maior que 90 graus, o produto escalar resultante torna-se negativo e isso resulta em um expoente especular de `0.0`. Você provavelmente está pensando que isso não será um problema, já que não devemos obter nenhuma luz com ângulos superiores a 90 graus, certo?

Errado, isso só se aplica a componente difusa, onde um ângulo superior a 90 graus entre a normal da superfície e a fonte de luz significa que a fonte de luz está abaixo da superfície iluminada e, portanto, a contribuição difusa da luz deve ser igual a `0.0`. No entanto, com a iluminação especular, não medimos o ângulo entre a fonte de luz e a normal da superfície, mas entre o vetor da câmera e o vetor de reflexão. Dê uma olhada nas duas imagens a seguir:

![altlogo](https://learnopengl.com/img/advanced-lighting/advanced_lighting_over_90.png)

Aqui, o problema deve se tornar aparente. A imagem à esquerda mostra os reflexos Phong como de costume, com $\theta$ sendo inferior a 90 graus. Na imagem da direita podemos ver que o ângulo $\theta$ entre o vetor da câmera e o vetor de reflexão é maior do que 90 graus, o que anula a contribuição especular. Isso geralmente não é um problema, uma vez que a direção da câmera está longe da direção da reflexão, mas se usarmos um expoente especular baixo, o raio especular é grande o suficiente para ter uma contribuição nessas condições. Como anulamos essa contribuição em ângulos maiores do que 90 graus, obtemos o artefato conforme visto na primeira imagem.

Em 1977, o modelo de shading {{<definition "Blinn-Phong">}} foi introduzido por James F. Blinn como uma extensão do shading de Phong que usamos até agora. O modelo Blinn-Phong é muito semelhante, mas se aproxima do modelo especular um pouco diferente de tal forma que resolve nosso problema. Em vez de depender de um vetor de reflexão, estamos usando o chamado {{<definition "vetor intermediário">}} ( {{<definition "halfway vector">}}), que é um vetor unitário exatamente no meio do caminho entre a direção da câmera e a direção da luz. Quanto mais próximo este vetor intermediário estiver alinhado com o vetor normal da superfície, maior será a contribuição especular.

![altlogo](https://learnopengl.com/img/advanced-lighting/advanced_lighting_halfway_vector.png)

Quando a direção da câmera está perfeitamente alinhada com o vetor de reflexão (agora imaginário), o vetor intermediário se alinha perfeitamente com o vetor normal. Quanto mais próxima a direção da câmera estiver da direção de reflexão original, mais forte será a luminosidade especular.

Aqui você pode ver que, seja qual for a direção de onde o observador olha, o ângulo entre o vetor intermediário e a normal da superfície nunca excede 90 graus (a menos que a luz esteja muito abaixo da superfície, é claro). Os resultados são ligeiramente diferentes das reflexões de Phong, mas geralmente mais plausíveis visualmente, especialmente com expoentes especulares baixos. O modelo de shading Blinn-Phong também é exatamente o modelo de shading usado no pipeline de função fixa anterior da OpenGL.

Obter o vetor intermediário é fácil, adicionamos o vetor de direção da luz e o vetor da câmera e normalizamos o resultado:

$$\bar{H} = \frac{\bar{L} + \bar{V}}{\parallel \bar{L} + \bar{V} \parallel}$$

Isso se traduz em código `GLSL` da seguinte maneira:

```cpp

vec3 lightDir   = normalize(lightPos - FragPos);
vec3 viewDir    = normalize(viewPos - FragPos);
vec3 halfwayDir = normalize(lightDir + viewDir);

```

Então, o cálculo real do termo especular torna-se um produto escalar limitado entre a normal da superfície e o vetor intermediário para obter o ângulo do cosseno entre eles que novamente elevamos a um expoente de brilho especular:

```cpp

float spec = pow(max(dot(normal, halfwayDir), 0.0), shininess);
vec3 specular = lightColor * spec;

```

E não há nada mais para Blinn-Phong do que o que acabamos de descrever. A única diferença entre a reflexão especular de Blinn-Phong e Phong é que agora medimos o ângulo entre o vetor normal e intermediário, em vez do ângulo entre o vetor da câmera e o vetor de reflexão.

Com a introdução do vetor intermediário, não deveríamos mais ter o problema de corte especular do shading de Phong. A imagem abaixo mostra a área especular de ambos os métodos com um expoente especular de `0.5`:

![altlogo](https://learnopengl.com/img/advanced-lighting/advanced_lighting_comparrison.png)

Outra diferença sutil entre o shading de Phong e Blinn-Phong é que o ângulo entre o vetor intermediário e a normal da superfície costuma ser menor do que o ângulo entre os vetores da câmera e reflexão. Como resultado, para obter visuais semelhantes ao shading de Phong, o expoente de brilho especular deve ser definido um pouco mais alto. Uma regra geral é configurá-lo entre 2 e 4 vezes o expoente de brilho Phong.

Abaixo está uma comparação entre os dois modelos de reflexão especular com o expoente Phong definido como `8.0` e o componente Blinn-Phong definido como `32.0`:

![altlogo](https://learnopengl.com/img/advanced-lighting/advanced_lighting_comparrison2.png)

Você pode ver que o expoente especular de Blinn-Phong é um pouco mais nítido em comparação com Phong. Geralmente, requer alguns ajustes para obter resultados semelhantes aos obtidos anteriormente com o shading de Phong. Mas vale a pena, pois o shading de Blinn-Phong é geralmente mais realista em comparação ao shading de Phong padrão.

Aqui, usamos um shader de fragmento simples que alterna entre reflexões Phong regulares e reflexões Blinn-Phong:

```cpp

void main()
{
    [...]
    float spec = 0.0;
    if(blinn)
    {
        vec3 halfwayDir = normalize(lightDir + viewDir);  
        spec = pow(max(dot(normal, halfwayDir), 0.0), 16.0);
    }
    else
    {
        vec3 reflectDir = reflect(-lightDir, normal);
        spec = pow(max(dot(viewDir, reflectDir), 0.0), 8.0);
    }

```

Você pode encontrar o código-fonte para a demonstração simples [aqui](/code_viewer_gh.php?code=src/5.advanced_lighting/1.advanced_lighting/advanced_lighting.cpp). Ao pressionar a tecla `b`, a demonstração muda de Phong para iluminação Blinn-Phong e vice-versa.



