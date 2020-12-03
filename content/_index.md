---
title: "home"
date: 2020-10-29T15:28:58-03:00
---

# APRENDA OPENGL

Bem vindo(a) **:)**

Este website é uma tradução direta e _quase inteiramente_ fiel do website [https://learnopengl.com/](https://learnopengl.com/), originalmente escrito por Joey de Vries. O site oferece o conteúdo original do livro **Learn OpenGL - Graphics Programming**, disponível de graça no próprio site e que também tem sua versão impressa vendida por aí.

Este conteúdo é direcionado para quem quer aprender programação gráfica por meio da OpenGL. Mas também para aqueles(as) que quiserem aprender um pouco de Computação Gráfica na prática.

A intenção aqui é ajudar quem tem dificuldades em ler textos em inglês ou simplesmente se sente mais confortável com a língua portuguesa. 

Como não sou nenhum _expert_ em inglês, e MENOS ainda em português, espere encontrar algum erro de vez em quando. Não hesite em apontar os erros, dar sugestões, fazer críticas e até desabafos... sou todo ouvidos! Acredito sinceramente que mesmo com alguns errinhos aqui e ali, o aprendizado e informação transmitidos por esta tradução não serão afetados, então nada para se preocupar! 

## Como é feita a tradução?

Com sono, muito sono. De madrugada. MAS juro que é com 100% de cérebro que me sobra nessas horas.

No início traduzia a partir do zero, frase por frase, escrevendo tudo. Mas de repente ficou claro pra mim que iria demorar uns 100 anos pra escrever tudo na minha velocidade e cansaço! Então tomei a única decisão que alguém preguiçoso como eu tomaria: usar o 
_google translate_. Mas logo me deparei com frases do tipo **"We only want to use the first 3 floats of each vertex"** sendo traduzidas para 
**"Nós só quer usar os primeiros 3 carros alegóricos de cada vértice"** (lágrimas). No fim o trabalho árduo continuou, mas pelo menos agora dou risada no processo. 

Apesar de todas conjugações erradas, frases sem sentido nenhum e termos malucos, ainda é mais rápido revisar o texto todo esquisito e consertá-lo do que escrever todo ele do zero, então _google translate_ é o melhor _pior_ esquema que pude encontrar nos 5 minutos que lutei contra meu dilema.

## Quero ajudar!

Caso deseje me ajudar nessa empreitada, ou simplesmente achou o texto/site tão ruins que tem vontade de corrigir por conta própria, ou qualquer outra razão que tenha, eu serei eternamente grato! 

Para contribuir você pode:

* Contribuir diretamente no [repositório do github](https://github.com/filipecn/aprendaopengl) (clonando e submetendo mudanças). É realmente muito simples, basta criar/modificar os arquivos markdown que estão na pasta `content` na pasta raiz do repositório. O sistema de pastas/arquivos dentro de `content` estão organizadas de um jeito bem fácil e intuitivo.

* Modificar diretamente no github, clicando no botão **Edit this page** que estará no canto superior de cada página com o conteúdo traduzido. Este botão te leva diretamente pro arquivo markdown dentro do repositório do github e lá você pode fazer suas modificações e submetê-las.

Para aqueles(as) que quiserem se basear nas traduções do _google translate_ eu lhes dou de presente o [translate.py](https://github.com/filipecn/aprendaopengl/blob/main/translate.py) (que também se encontra na raiz do repositório), script mão na roda para traduzir o post inteiro e gerar o markdown de saída. Por exemplo, digamos que você queira traduzir a seção de materiais [https://learnopengl.com/Lighting/Materials](https://learnopengl.com/Lighting/Materials) e salvar a tradução direto no seu respectivo arquivo (que neste caso deve ser `content/iluminacao/materiais/_index.md`). O script aceita vários argumentos, mas apenas dois são realmente necessários: o link do post e o arquivo de saída. Bastaria então fazer algo do tipo (partindo da pasta raiz do repositório):

``` shell
 python3 translate.py https://learnopengl.com/Lighting/Materials content/iluminacao/materiais/_index.md
```
e esperar a porcentagem chegar a `100%`. Não precisa se preocupar com as imagens e links contidos no texto original, porque o script cuida deles pra você!

{{% greenbox warning%}}
**Esse script pode falhar, e provavelmente vai .... com certeza :)**. Todo texto que ele não consegue traduzir ele coloca o texto em inglês original no lugar, por isso mais um motivo para realmente revisar tudo. E não preciso reforçar o fato de que muitas frases vêm erradas, sem sentido... então a revisão é realmente necessária!
{{% /greenbox %}}

## Status

A seguir, temos a lista de todas seções do site com cores indicando quais {{<definition "já foram traduzidas e revisadas">}}, quais estão {{<english "sendo traduzidas no momento">}}, quais {{<variable "já foram traduzidas mas precisam de revisão">}} e por fim quais {{<struct "ainda nem foram traduzidas">}}:

|Capítulo|Seções|
|---|--------|
|{{<definition Introdução>}} | |
|{{<english "Ponto de Partida">}} | {{<variable "Criando uma Janela">}}, {{<variable "Olá Janela">}}, {{<variable "Olá Triângulo">}}, {{<struct "Shaders">}}, {{<struct "Texturas">}}, {{<english "Transformações">}}, {{<struct "Sistemas de Coordenadas">}}, {{<struct "Câmera">}}, {{<struct "Revisão">}} |
|{{<english "Iluminação">}} | {{<variable "Cores">}}, {{<variable "Iluminação Básica">}}, {{<english "Materiais">}}, {{<struct "Mapas de Iluminação">}}, {{<struct "Lançadores de Luz">}}, {{<struct "Múltiplas Luzes">}}, {{<struct "Revisão">}} |
|{{<struct "Carregamento de Modelos">}} | {{<struct "Assimp">}}, {{<struct "Malha">}}, {{<struct "Modelo">}} |
|{{<struct "OpenGL Avançada">}} | {{<struct "Teste de Profundidade">}}, {{<struct "Teste de Estêncil">}}, {{<struct "Mistura">}}, {{<struct "Seleção de Faces">}}, {{<struct "Framebuffers">}}, {{<struct "Mapas Cúbicos">}}, {{<struct "Dados Avançados">}}, {{<struct "GLSL Avançada">}}, {{<struct "Shader de Geometria">}}, {{<struct "Instanciação">}}, {{<struct "Anti-Aliasing">}} |
|{{<english "Iluminação Avançada">}} | {{<variable "Iluminação Avançada">}}, {{<variable "Correção Gama">}}, {{<struct "Sombras - Mapeamento de Sombra">}}, {{<struct "Sombras - Sombras Pontuais">}}, {{<struct "Mappeamento de Normais">}}, {{<struct "Mapeamento de Paralaxe">}}, {{<struct "HDR">}}, {{<struct "Bloom">}}, {{<struct "Deferred Shading">}}, {{<struct "SSAO">}} |
|{{<english "PBR">}} | {{<variable "Teoria">}}, {{<struct "Iluminação">}}, {{<struct "IBL - Irradiância Difusa">}}, {{<struct "IBL - IBL Especular">}} |
|{{<struct "Na Prática">}} | {{<struct "Depurando">}}, {{<struct "Renderização de Texto">}}, {{<struct "Jogo 2D">}}, {{<struct "- Breakout">}}, {{<struct "- Preparação">}}, {{<struct "Renderizando Sprites">}}, {{<struct "- Fases">}}, {{<struct "- Colisões">}}, {{<struct "-- Bola">}}, {{<struct "-- Detecção de Colisão">}}, {{<struct "-- Resolução de Colisão">}}, {{<struct "- Particulas">}}, {{<struct "- Pós-Processamento">}}, {{<struct "- Powerups">}}, {{<struct "- Áudio">}}, {{<struct "- Renderizar Texto">}}, {{<struct "- Considerações Finais">}} |
|{{<struct "Repositório do Código">}} | |

|Estatística|Contagem|
|----|----|
|{{<definition "já foram traduzidas e revisadas">}} | 1 |
|{{<english "sendo traduzidas no momento">}} | 6 |
|{{<variable "já foram traduzidas mas precisam de revisão">}} | 8 | 
|{{<struct "ainda nem foram traduzidas">}} | 55 |
| total | 70 |

