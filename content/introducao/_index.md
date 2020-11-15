+++
title = "Introdução"
date = 2020-10-29T15:22:27-03:00
weight = 1
#chapter = true
pre = "<b>1. </b>"
+++

[Post Original](https://learnopengl.com/Introduction)

Já que veio aqui então você provavelmente quer aprender como Computação Gráfica funciona por debaixo dos panos e fazer sozinho todas as coisas super legais que a galera faz. Fazer as coisas por você mesmo é extremamente divertido, engenhoso e te dá um ótimo entendimento de programação gráfica. Entretanto, têm alguns itens que precisam ser considerados antes de começar sua grande jornada.

## Pré-requisitos

Já que a OpenGL é uma API (biblioteca) gráfica e não uma plataforma por si só, ela requer uma linguagem de programação para que possa operar e a linguagem escolhida é `C++`. Portanto um conhecimento razoável de `C++` é necessário para os capítulos a seguir. Tentarei explicar quase todos os conceitos utilizados, incluindo tópicos avançados de `C++` então não é preciso ser nenhum expert em `C++`, porém você deveria ser capaz de escrever mais do que um programa "Hello World". Caso não tenha muita experiencia com `C++` eu recomendo alguns [tutoriais](www.learncpp.com) de graça.
  
Além disso, vamos utilizar um pouco de matemática (algebra linear, geometria e trigonometria) durante o caminho e tentarei explicar todos conceitos necessários. Entretanto, não sou um matemático então, mesmo que minhas explicações sejam fáceis de entender, elas provavelmente serão incompletas. Apontareis boas fontes que explicam o material de forma mais completa. **Não se assuste sobre o conhecimento matemático necessário antes de começar sua jornada com a OpenGL**; quase todos conceitos podem ser entendidos com um conhecimento básico de matemática e tentarei manter a matemática num nível mínimo a medida que for possível. A maior parte da funcionalidade nem sequer exige que você entenda toda matemática contando que você saiba como usá-la.

## Estrutura

O AprendaOpenGL é dividido vários capítulos gerais. Cada seção contem várias seções das quais cada uma explica diferentes conceitos em maiores detalhes. Cada uma das seções pode ser encontrada no menu a sua esquerda. Os conceitos são ensinados de forma linear **(então é recomendado começar do topo até o final, a menos que seja instruído o contrário)**, onde cada seção explica a base teórica e os aspectos práticos.

A fim de tornar os conceitos mais fáceis de seguir, e estruturá-los um pouco mais, o texto contém _caixas_, _blocos de código_, _dicas coloridas_ e _referência de funções_.

## Caixas

{{% greenbox tip %}}
Caixas verdes contém algumas notas ou dicas úteis sobre OpenGL ou sobre o assunto sendo discutido.
{{% /greenbox %}}
{{% greenbox warning %}}
Caixas vermelhas contém avisos ou outras informações das quais você deve tomar um cuidado extra.
{{% /greenbox %}}

## Código

Você encontrará vários pedacinhos de código neste website que estão localizados em caixas escuras contendo código com sintaxe colorida, como pode ver abaixo:

```cpp
// esta caixa contem código
```
Como exibem apenas pedaços de código, sempre que necessário oferecerei um link para o código fonte inteiro respectivo ao seu assunto.

## Color hints

Algumas palavras são mostradas com uma cor diferente para deixar mais claro que carregam um significado especial:

* {{<definition Definição>}}: palavras verdes especificam uma definição, isto é, um aspecto/nome importante de alguma coisa que você provavelmente encontrará mais vezes.
* {{<struct Estrutura>}} {{<struct de>}} {{<struct Programa>}}: palavras vermelhas especificam nomes de funções ou classes.
* {{<variable Variáveis>}}: palavras azuis especificam variáveis incluindo todas constantes da OpenGL.

## Referencias de Funções OpenGL

Uma característica particularmente apreciada do LearnOpenGL é a habilidade de visitar a maioria das funções OpenGL toda vez que aparecem no texto. Toda vez que uma função é encontrada no conteúdo que é documentado no website, a função irá aparecer sublinhada. Você pode passar o mouse em cima e depois de um breve intervalo, uma janela irá mostrar informações relevantes sobre esta função incluindo um bom resumo sobre o que a função de fato faz. Passe seu mouse em cima de {{<struct glEnable>}} para ver a mágica acontecer.

{{% notice note %}}
Esse site não tem tanta magia quanto o original (nenhuma pra dizer a verdade), mas quem sabe um dia né **:)**. Por enquanto colocarei um link para documentação oficial no lugar. Desse jeito: [glEnable](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glEnable.xhtml).
{{% /notice %}}

Agora que você sentiu um pouco da estrutura do site, pule para o próximo capitulo e comece sua grande jornada em OpengGL!

