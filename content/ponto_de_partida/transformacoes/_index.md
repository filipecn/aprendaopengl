---
title: "Transformações"
date: 2020-10-29T15:28:58-03:00
draft: false
katex: true
markup: "mmark"
---

[Post Original](https://learnopengl.com/Getting-started/Transformations)


Sabemos agora como criar objetos, cor-los e / ou dar-lhes uma aparência detalhada usando texturas, mas ainda não é tão interessante, pois eles estão todos os objetos estáticos. Poderíamos tentar e fazê-los passar por mudar seus vértices e re-configurar seus buffers cada quadro, mas isso é complicado e custos bastante poder de processamento. Há muito melhores maneiras de transformar um objeto e isso é usando (múltiplos) objetos de matriz. Isso não significa que nós estamos indo falar sobre Kung Fu e um grande mundo artificial digital.

Matrizes são muito poderosas construções matemáticas que parecem assustador no começo, mas uma vez que você vai se acostumar a eles que eles vão revelar-se extremamente útil. Ao discutir matrizes, nós vamos ter que fazer um pequeno mergulhar em um pouco de matemática e para os leitores mais matematicamente Vou postar recursos adicionais para outras leituras.

No entanto, para compreender plenamente as transformações primeiro temos que aprofundar um pouco mais em vetores antes de discutir matrizes. O foco deste capítulo é dar-lhe um fundo matemática básica em temas que vai exigir mais tarde. Se as matérias são difíceis, tentar compreendê-los tanto quanto você pode e voltar a este capítulo mais tarde para rever os conceitos sempre que você precisar deles.

# Vectors

Em sua definição mais básica, vetores são sentidos e nada mais. Um vector tem uma direcção e uma amplitude (também conhecida como a sua resistência ou comprimento). Você pode pensar em vetores como instruções sobre um mapa do tesouro: 'Vá para a esquerda 10 passos, agora vá norte 3 etapas e ir direto 5 passos'; aqui 'esquerda' é a direção e '10 passos é a magnitude do vetor. As indicações para o mapa do tesouro, portanto, contém 3 vetores. Vetores podem ter qualquer dimensão, mas que geralmente trabalham com dimensões de 2 a 4. Se um vetor tem 2 dimensões que representa uma direção em um avião (pense em gráficos 2D) e quando ele tem 3 dimensões pode representar qualquer direção em um 3D mundo.

Abaixo, você verá 3 vetores, onde cada vetor é representado com (x, y) como flechas em um gráfico 2D. Porque é mais intuitivo para exibir vetores em 2D (ao invés de 3D) você pode pensar dos 2D vetores como 3D vetores com uma coordenada z de 0. Desde vetores representam as direções, a origem do vector não muda o seu valor. No gráfico abaixo, podemos ver que os vetores \ (\ color {vermelho} {\ bar {v}} \) e \ (\ color {azul} {\ bar {w}} \) são iguais mesmo que sua origem é diferente:

![altlogo](https://learnopengl.com/img/getting-started/vectors.png)

Quando vetores que descrevem os matemáticos preferem geralmente para descrever vetores como símbolos de caracteres com um pouco de bar sobre sua cabeça como \ (\ bar {v} \). Além disso, quando visualizadas em vectores de fórmulas eles são geralmente apresentados como se segue:
  
  \ [\ Bar {V} = \ begin {pmatrix} \ cor vermelho {} x \\ \ cor verde {} y \\ \ cor azul {} z \ final {pmatrix} \]

Porque vetores são especificados como direções às vezes é difícil visualizá-los como posições. Se quisermos visualizar vetores como posições podemos imaginar a origem do vetor de direção para ser (0,0,0) e depois apontar para uma certa direção que especifica o ponto, tornando-se um vetor posição (que também pode especificar um diferente origem e, em seguida, dizer: 'este vetor aponta para esse ponto no espaço a partir desta origem'). O vector de posição (3,5), em seguida, iria apontar para (3,5) no gráfico com uma origem de (0,0). Usando vetores podemos assim descrever orientações e posições no espaço 2D e 3D.

Assim como com números normais também pode definir várias operações em vetores (alguns dos quais você já visto).

## Scalar vector operations

Um escalar é um único dígito. Ao adicionar / subtrair / multiplicar ou dividir um vetor com um escalar nós simplesmente adicionar / subtrair / multiplicar ou dividir cada elemento do vector por escalar. Para além disso, ficaria assim:
  
  \ [\ Begin {pmatrix} \ cor vermelho {} 1 \\ \ cor verde {} 2 \\ \ cor azul {} 3 \ final {pmatrix} + x \ rightarrow \ begin {pmatrix} \ cor vermelho {} 1 \ \ \ cor verde {} 2 \\ \ cor azul {} 3 \ final {pmatrix} + \ begin {pmatrix} x \\ \\ x x \ final {pmatrix} = \ begin {pmatrix} \ cor vermelho {1} + x \\ \ cor verde {} 2 + x \\ \ cor azul {} 3 + x \ final {pmatrix} \]
  
  Onde \ (+ \) pode ser \ (+ \), \ (- \), \ (\ cdot \) ou \ (\ div \) onde \ (\ cdot \) é o operador de multiplicação.

## Vector negation

Negando um vector resulta em um vector na direcção inversa. Um vetor que aponta Nordeste apontaria Sudoeste depois de negação. Para negar um vetor que adicionar uma menos-sinal para cada componente (você também pode representá-lo como uma multiplicação escalar-vetor com um valor escalar -1):
  
  \ [- \ bar {v} = - \ begin {pmatrix} \ color {vermelho} {v_x} \\ \ color {azul} {v_y} \\ \ color {verde} {v_z} \ end {pmatrix} = \ begin {pmatrix} - \ color {vermelho} {v_x} \\ - \ color {azul} {v_y} \\ - \ color {verde} {v_z} \ end {pmatrix} \]

## Addition and subtraction

A adição de dois vectores é definida como a adição do componente-sábio, isto é, cada componente de um vector é adicionado ao mesmo componente do outro vector da seguinte forma:
  
  \ [\ Bar {V} = \ begin {pmatrix} \ cor vermelho {} 1 \\ \ cor verde {} 2 \\ \ cor azul {} 3 \ final {pmatrix}, \ bar {k} = \ {começar pmatrix} \ cor vermelho {} 4 \\ \ cor verde {} 5 \\ \ cor azul {} 6 \ final {pmatrix} \ rightarrow \ bar {v} + \ bar {k} = \ begin {pmatrix} \ cor {vermelho} 1 + \ cor vermelho {} 4 \\ \ cor verde {} 2 + \ cor verde {} 5 \\ \ cor azul {} 3 + \ cor azul {} 6 \ final {pmatrix} = \ {começar pmatrix} \ cor vermelho {} 5 \\ \ cor verde {} 7 \\ \ cor azul {} 9 \ final {pmatrix} \]
  
  Visualmente, parece que esta em vectores de v = (4,2) e k = (1,2), em que o segundo vector é adicionado em cima da extremidade do primeiro vector para encontrar o ponto final do vector resultante (cabeça-a método -tail):

![altlogo](https://learnopengl.com/img/getting-started/vectors_addition.png)

Assim como adição normal e subtracção, vector de subtracção é o mesmo como de adição com um segundo vector negada:
  
  \ [\ Bar {V} = \ begin {pmatrix} \ cor vermelho {} {1} \\ \ cor verde {} {2} \\ \ cor azul {} {3} \ final {pmatrix}, \ bar { k} = \ begin {pmatrix} \ cor vermelho {} {4} \\ \ cor verde {} {5} \\ \ cor azul {} {6} \ final {pmatrix} \ rightarrow \ bar {v} + - \ bar {k} = \ begin {pmatrix} \ cor vermelho {} {1} + (- \ cor vermelho {} {4}) \\ \ cor verde {} {2} + (- \ cor verde {} { 5}) \\ \ cor azul {} {3} + (- \ cor azul {} {6}) \ final {pmatrix} = \ begin {pmatrix} - \ cor vermelho {} {3} \\ - \ cor {verde} {3} \\ - \ color {azul} {3} \ end {pmatrix} \]

Subtraindo-se dois vectores de uns aos outros resulta num vector que é a diferença das posições de ambos os vectores estão a apontar na. Isso prova útil em certos casos em que precisamos para recuperar um vector que é a diferença entre dois pontos.

![altlogo](https://learnopengl.com/img/getting-started/vectors_subtraction.png)

## Length

Para recuperar o comprimento / magnitude de um vetor usamos o teorema de Pitágoras que você pode se lembrar de suas aulas de matemática. Um vector de forma um triângulo quando a visualizar a sua x individual e componente y como dois lados de um triângulo:

![altlogo](https://learnopengl.com/img/getting-started/vectors_triangle.png)

Desde o comprimento dos dois lados (x, y) são conhecidos e queremos saber o comprimento do lado inclinado \ (\ color {vermelho} {\ bar {v}} \) podemos calcular isso usando o teorema de Pitágoras como :
  
  \ [|| \ color {vermelho} {\ bar {v}} || = \ Sqrt {\ cor verde {} x ^ 2 + \ cor azul {} y ^ 2} \]
  
  Onde \ (|| \ cor vermelho {} {\ bar {v}} || \) é indicada como o comprimento de vector de \ (\ cor vermelho {} {\ bar {v}} \). Isto é facilmente estendido para 3D adicionando \ (z ^ 2 \) para a equação.

Neste caso, o comprimento de vector de (4, 2) é igual a:
  
  \ [|| \ color {vermelho} {\ bar {v}} || = \ Sqrt {\ cor {verde} 4 ^ 2 + \ cor {azul} 2 ^ 2} = \ sqrt {\ cor {verde} 16 + \ cor {azul} 4} = \ sqrt {20} = 4,47 \]
  
  Que é 4,47.

Há também um tipo especial de vetor que nós chamamos um vetor unitário. Um vetor de unidade tem uma propriedade extra e isso é que seu comprimento é exatamente 1. Nós podemos calcular um vetor de unidade \ (\ hat {n} \) a partir de qualquer vector, dividindo cada um dos componentes do vetor por seu comprimento:
  
  \ [\ Chapéu {n} = \ frac {\ bar {v}} {|| \ bar {V} ||} \]
  
  Chamamos isso de normalizar um vetor. vetores unitários são exibidos com um pouco de teto sobre sua cabeça e geralmente são mais fáceis de trabalhar, especialmente quando só se preocupam com suas direções (a direção não muda se mudarmos o comprimento de um vetor).

## Vector-vector multiplication

A multiplicação de dois vetores é um pouco de um caso estranho. multiplicação normal não está realmente definido em vetores, uma vez que não tem sentido visual, mas temos dois casos específicos que poderíamos escolher quando multiplicando: um é o produto escalar denotado como \ (\ bar {v} \ cdot \ bar {k } \) e o outro é o produto cruzado denotado como \ (\ bar {v} \ \ vezes bar {k} \).

O produto escalar de dois vectores é igual ao produto escalar dos seus comprimentos vezes o co-seno do ângulo entre elas. Se isso soa confuso dar uma olhada em sua fórmula:
  
  \ [\ Bar {V} \ cdot \ bar {k} = || \ bar {V} || \ Cdot || \ bar {k} || \ Cdot \ cos \ theta \]
  
  Quando o ângulo entre eles é representado como teta (\ (\ theta \)). Por que isso é interessante? Bem, imagine se \ (\ bar {v} \) e \ (\ bar {k} \) são vetores unitários, em seguida, seu comprimento seria igual a 1. Isso efetivamente reduzir a fórmula para:
  
  \ [\ Chapéu {V} \ cdot \ chapéu {k} = 1 \ cdot 1 \ cdot \ cos \ teta = \ cos \ teta \]
  
  Agora, o produto escalar só define o ângulo entre os dois vetores. Você pode se lembrar que o co-seno ou cos função se torna 0 quando o ângulo é de 90 graus ou 1 quando o ângulo é 0. Isso nos permite facilmente testar se os dois vetores são ortogonais ou paralelas entre si usando o produto de ponto (meio ortogonais as Os vectores estão em ângulo recto um com o outro). No caso de você querer saber mais sobre o pecado ou o cos funções sugiro os seguintes vídeos Khan Academy sobre trigonometria básica.

(https://www.khanacademy.org/math/trigonometry/basic-trigonometry/basic_trig_ratios/v/basic-trigonometry)

{{% greenbox tip %}}
Você também pode calcular o ângulo entre dois vetores não-unitárias, mas então você teria que dividir os comprimentos de ambos vetores do resultado a ser deixado com \ (cos \ theta \).

{{% /greenbox %}}

Então, como podemos calcular o produto dot? O produto escalar é uma multiplicação componente-wise onde adicionar os resultados juntos. Parece que este com dois vetores unitários (você pode verificar que ambos os seus comprimentos são exatamente 1):
  
  \ [\ Begin {pmatrix} \ cor vermelho {} {0,6} \\ - \ cor verde {} {0,8} \\ \ cor azul {} 0 \ final {pmatrix} \ cdot \ begin {pmatrix} \ {cor vermelho } 0 \\ \ cor verde {} 1 \\ \ cor azul {} 0 \ final {pmatrix} = (\ cor vermelho {} {0,6} * \ cor vermelho {} 0) + (- \ cor verde {} { 0,8} * \ cor verde {} 1) + (\ cor azul {} 0 * \ cor azul {} 0) = -0,8 \]
  
  Para calcular o grau entre estes dois vectores unitários que usamos o inverso da função de coseno \ cos (^ {- 1} \) e isto resulta em 143,1 graus. Nós agora efetivamente calculado o ângulo entre esses dois vetores. O produto escalar é muito útil ao fazer cálculos de iluminação mais tarde.

O produto cruzado é apenas definida no espaço 3D e leva dois vectores não-paralelas como entrada e produz um terceiro vector que é ortogonal tanto para os vectores de entrada. Se ambos os vectores de entrada são ortogonais entre si, bem como, um produto cruzado resultaria em 3 vectores ortogonais; isso vai ser útil nos próximos capítulos. Os seguintes imagem mostra que isso parece no espaço 3D:

![altlogo](https://learnopengl.com/img/getting-started/vectors_crossproduct.png)

Ao contrário das outras operações, o produto cruzado não é realmente intuitiva, sem aprofundar em álgebra linear por isso é melhor apenas memorizar a fórmula e você vai ficar bem (ou não fizer isso, você provavelmente vai ficar bem também). Abaixo, você verá o produto cruzado entre dois vetores ortogonais A e B:
  
  \ [\ Begin {pmatrix} \ cor vermelho {} {A_ {x}} \\ \ cor verde {} {A_ {y \\}} \ cor azul {} {A_ {z}} \ final {pmatrix} \ \ vezes começam {pmatrix} \ cor vermelho {} {B_ {x}} \\ \ cor verde {} {B_ {y \\}} \ cor azul {} {B_ {z}} \ final {pmatrix} = \ begin {pmatrix} \ color {verde} {A_ {y}} \ cdot \ color {azul} {B_ {z}} - \ color {azul} {A_ {z}} \ cdot \ color {verde} {B_ { y}} \\ \ cor azul {} {A_ {z}} \ cdot \ cor vermelho {} {B_ {x}} - \ cor vermelho {} {A_ {x}} \ cdot \ cor azul {} {B_ {z}} \\ \ cor vermelho {} {A_ {x}} \ cdot \ cor verde {} {B_ {y}} - \ cor verde {} {A_ {y}} \ cdot \ cor vermelho {} { B_ {x}} \ end {pmatrix} \]
  
  Como você pode ver, ele realmente não parece fazer sentido. No entanto, se você apenas seguir estes passos você obterá um outro vector que é perpendicular aos seus vetores de entrada.

# Matrices

Agora que nós discutimos quase tudo o que há de vetores é hora de entrar na matriz!
  A matriz é uma matriz rectangular de números, símbolos e / ou expressões matemáticas. Cada artigo individual numa matriz é chamado um elemento da matriz. Um exemplo de uma matriz de 2x3 é mostrado abaixo:
  
  \ [\ Begin {bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \ final {bmatrix} \]
  
  As matrizes são indexadas por (i, j), onde i é a linha e a coluna j é, por isso a matriz acima é chamado uma matriz de 2x3 (3 colunas e linhas 2, também conhecida como as dimensões da matriz). Este é o oposto do que você está acostumado ao indexar 2D gráficos como (x, y). Para recuperar o valor 4 teríamos posicioná-lo como (2,1) (segunda linha, primeira coluna).

Matrizes são basicamente nada mais do que isso, apenas matrizes retangulares de expressões matemáticas. Eles têm um muito bom conjunto de propriedades matemáticas e, assim como vetores podemos definir várias operações sobre matrizes, a saber: adição, subtração e multiplicação.

## Addition and subtraction

Além da matriz e subtração entre duas matrizes é feito em uma base per-elemento. Assim, as mesmas regras gerais aplicam-se de que está familiarizado com os números normais, mas feito sobre os elementos de ambas as matrizes com o mesmo índice. Isto significa que a adição e subtracção só é definida para matrizes com as mesmas dimensões. Uma matriz 3x2 e uma matriz de 2x3 (ou uma matriz 3x3 e uma matriz 4x4) não podem ser adicionados ou subtraídos juntos. Vamos ver como adição de matriz funciona em dois 2x2 matrizes:
  
  \ [\ Begin {bmatrix} \ cor vermelho {} 1 & \ cor vermelho {} 2 \\ \ cor verde {} 3 & \ cor verde {} 4 \ final {bmatrix} + \ begin {bmatrix} \ {cor vermelho } 5 & \ cor vermelho {} 6 \\ \ cor verde {} 7 & \ cor verde {} 8 \ final {bmatrix} = \ begin {bmatrix} \ cor vermelho {} 1 + \ cor vermelho {} 5 & \ cor vermelho {} 2 + \ cor vermelho {} 6 \\ \ cor verde {} 3 + \ cor verde {} 7 & \ cor verde {} + 4 \ cor verde {} 8 \ final {bmatrix} = \ {começar bmatrix} \ cor vermelho {} 6 & \ cor vermelho {} 8 \\ \ cor verde {} {} 10 & \ cor verde {} {} 12 \ final {bmatrix} \]
  
As mesmas regras se aplicam para a subtração de matriz:
  
   \ [\ Begin {bmatrix} \ color {red} 4 & \ color {red} 2 \\ \ color {verde} 1 & \ color {verde} 6 \ end {bmatrix} - \ begin {bmatrix} \ color {vermelho } 2 & \ color {red} 4 \\ \ color {verde} 0 & \ color {verde} 1 \ end {bmatrix} = \ begin {bmatrix} \ color {red} 4 - \ color {red} 2 & \ cor {red} 2 - \ color {red} 4 \\ \ color {verde} 1 - \ color {verde} 0 & \ color {verde} 6 - \ color {verde} 1 \ end {bmatrix} = \ begin { bmatrix} \ color {red} 2 & - \ color {red} 2 \\ \ color {verde} 1 & \ color {verde} 5 \ end {bmatrix} \]

## Matrix-scalar products

Uma matriz de escalar múltiplos produtos cada elemento da matriz por um escalar. O exemplo a seguir ilustra a multiplicação:
  
  \ [\ Cor verde {} 2 \ cdot \ begin {bmatrix} 1 & 2 \\ 3 & 4 \ final {bmatrix} = \ begin {bmatrix} \ cor verde {} 2 \ cdot 1 & \ cor verde {2} \ cdot 2 \\ \ cor verde {} 2 \ cdot 3 & \ cor verde {} 2 \ cdot 4 \ final {bmatrix} = \ begin {bmatrix} 2 & 4 & 8 6 \\ \ final {bmatrix} \]
  
Agora também faz sentido a respeito de porque esses números individuais são chamados de escalares. Um escalar basicamente escalas todos os elementos da matriz pelo seu valor. No exemplo anterior, todos os elementos foram dimensionadas por dois.

Até aí tudo bem, todos os nossos casos não foram realmente muito complicado. Isto é, até que começamos a multiplicação de matrizes-matriz.

## Matrix-matrix multiplication

Multiplicando as matrizes não é necessariamente complexa, mas bastante difícil de se sentir confortável com. A multiplicação de matrizes significa, basicamente, a seguir um conjunto de regras pré-definidas quando multiplicando. Existem algumas restrições, porém:

Você só pode multiplicar duas matrizes se o número de colunas na matriz do lado esquerdo é igual ao número de linhas na matriz do lado direito.

A multiplicação de matrizes não é comutativa, que é \ (A \ cdot B \ neq B \ cdot A \).

Vamos começar com um exemplo de uma multiplicação de matrizes de 2 2x2 matrizes:
  
  \ [\ Begin {bmatrix} \ cor vermelho {} 1 & \ cor vermelho {} 2 \\ \ cor verde {} 3 & \ cor verde {} 4 \ final {bmatrix} \ cdot \ begin {bmatrix} \ {cor azul} 5 & \ cor púrpura {} 6 \\ \ cor azul {} 7 & \ cor púrpura {} 8 \ final {bmatrix} = \ begin {bmatrix} \ cor vermelho {} 1 \ cdot \ cor azul {5} + \ cor 2 \ cdot \ cor 7 & \ cor vermelho {} 1 \ cdot \ cor púrpura {} 6 + \ cor vermelho {} 2 \ cdot \ cor púrpura {} 8 \\ \ {azul} {} {vermelho verde} 3 \ cdot \ cor {azul} 5 + \ cor {verde} 4 \ cdot \ cor {azul} 7 & \ cor {verde} 3 \ cdot \ cor {roxo} 6 + \ cor {verde} 4 \ cdot \ cor púrpura {} 8 \ final {bmatrix} = \ begin {bmatrix} 19 & 22 \\ 43 & 50 \ final {bmatrix} \]
  
  Agora você provavelmente está tentando descobrir o que diabos aconteceu? A multiplicação de matrizes é uma combinação de multiplicação normal e além utilizando linhas de o-matriz esquerda com colunas de o-matriz direita. Vamos tentar discutir isso com a seguinte imagem:

![altlogo](https://learnopengl.com/img/getting-started/matrix_multiplication.png)

Em primeiro lugar, tomar a linha superior da matriz esquerda e depois tomar uma coluna da matriz direita. A linha e coluna que escolhemos decide que valor da matriz 2x2 resultando vamos calcular a produção. Se tomarmos a primeira linha da matriz esquerda o valor resultante vai acabar na primeira linha da matriz resultado, então nós escolhemos uma coluna e se é a primeira coluna o valor do resultado vai acabar na primeira coluna da matriz resultado . Este é exatamente o caso da via vermelho. Para calcular o resultado inferior direito tomamos a linha inferior da primeira matriz e da coluna mais à direita da segunda matriz.

Para calcular o valor resultante que multiplicam o primeiro elemento da linha e da coluna em conjunto, utilizando multiplicação normal, fazemos o mesmo para o segundo elementos, terceiro, quarto, etc. Os resultados das multiplicações individuais são então somados e temos o nosso resultado. Agora, também faz sentido que um dos requisitos é que o tamanho das colunas de o-matriz para a esquerda e a matriz-direita de linhas forem iguais, caso contrário, não podemos terminar as operações!

O resultado é, em seguida, uma matriz que tem dimensões de (n, m), onde n é igual ao número de linhas da matriz do lado esquerdo e m é igual às colunas da matriz do lado direito.

Não se preocupe se você tem dificuldades imaginando as multiplicações dentro de sua cabeça. Apenas continue tentando fazer os cálculos à mão e retorno a esta página sempre que você tem dificuldades. Com o tempo, a multiplicação de matrizes torna-se uma segunda natureza para você.

Vamos acabar com a discussão de multiplicação de matrizes-matriz com um exemplo maior. Tente visualizar o padrão usando as cores. Como um exercício útil, veja se você pode vir até com sua própria resposta da multiplicação e, em seguida, compará-los com a matriz resultante (uma vez que você tentar fazer uma multiplicação de matrizes à mão você vai rapidamente obter a compreensão deles).
  
  \ [\ Begin {bmatrix} \ color {red} 4 & \ color {red} 2 & \ color {red} 0 \\ \ color {verde} 0 & \ color {verde} 8 & \ color {verde} 1 \ \ \ color {azul} 0 & \ color {azul} 1 & \ color {azul} 0 \ end {bmatrix} \ cdot \ begin {bmatrix} \ color 4 & \ color 2 & \ color {verde} {red} { azul} 1 \\ \ cor vermelho {} 2 & \ cor verde {} 0 & \ cor azul {} 4 \\ \ cor vermelho {} 9 & \ cor verde {} 4 & \ cor azul {} 2 \ final { bmatrix} = \ begin {bmatrix} \ color {red} 4 \ cdot \ color {red} 4 + \ color {red} 2 \ cdot \ color {red} 2 + \ color {red} 0 \ cdot \ color {vermelho } 9 & \ cor {vermelho} 4 \ cdot \ cor {verde} 2 + \ cor {vermelho} 2 \ cdot \ cor {verde} 0 + \ cor {vermelho} 0 \ cdot \ cor {} 4 & \ cor verde {vermelho} 4 \ cdot \ cor azul {} 1 + \ cor vermelho {} 2 \ cdot \ cor azul {} + 4 \ cor vermelho {} 0 \ cdot \ cor azul {} 2 \\ \ cor verde {} 0 \ cdot \ cor {vermelho} 4 + \ cor {verde} 8 \ cdot \ cor {vermelho} 2 + \ cor {verde} 1 \ cdot \ cor {vermelho} 9 & \ cor {verde} 0 \ cdot \ cor { verde} 2 + \ cor {verde} 8 \ cdot \ cor {verde} 0 + \ cor {verde} 1 \ cdot \ cor {verde} 4 & \ cor {verde} 0 \ cdot \ cor {azul} 1 + \ cor {verde} 8 \ cdot \ color {azul} 4 + \ color {verde} 1 \ cdot \ cor azul {} 2 \\ \ cor azul {} 0 \ cdot \ cor vermelho {} + 4 \ cor azul {} 1 \ cdot \ cor vermelho {} 2 + \ cor azul {} 0 \ cdot \ cor {vermelho} 9 & \ cor {azul} 0 \ cdot \ cor {verde} 2 + \ cor {azul} 1 \ cdot \ cor {verde} 0 + \ cor {azul} 0 \ cdot \ cor {verde} 4 & \ cor {azul} 0 \ cdot \ cor {azul} 1 + \ cor {azul} 1 \ cdot \ cor {azul} 4 + \ cor {azul} 0 \ cdot \ cor {azul} 2 \ final {bmatrix}
 \\ = \ begin {bmatrix} 20 & 8 & 12 \\ 25 & 4 & 34 \\ 2 & 0 & 4 \ final {bmatrix} \]

Como você pode ver, a multiplicação de matrizes de matriz é um processo bastante complicado e muito propenso a erros (que é por isso que normalmente permitir que computadores fazer isso) e isso fica bem rápido problemático quando as matrizes se tornam maiores. Se você ainda está sedento por mais e você está curioso sobre mais algumas das propriedades matemáticas de matrizes eu sugiro fortemente que você dê uma olhada nestes vídeos Khan Academy cerca de matrizes.

(https://www.khanacademy.org/math/algebra2/algebra-matrices)

De qualquer forma, agora que sabemos como matrizes multiplicar juntos, podemos começar a ficar para as coisas boas.

# Matrix-Vector multiplication

Até agora nós tivemos nossa parcela de vetores. Nós utilizado para representar posições, cores e coordenadas, mesmo textura. Vamos passar um pouco mais abaixo do furo de coelho e dizer que um vector é basicamente uma matriz Nx1 onde N é o número do vector de componentes (também conhecido como um vector n-dimensional). Se você pensar sobre isso, faz muito sentido. Os vectores são como matrizes uma matriz de números, mas com apenas uma coluna. Então, como é este novo pedaço de informação ajuda-nos? Bem, se temos um MxN matriz podemos multiplicar esta matriz com o nosso vector Nx1, já que as colunas da matriz são iguais ao número de linhas do vetor, assim, a multiplicação de matrizes é definida.

Mas porque é que nós nos importamos se nós pode multiplicar matrizes com um vector? Bem, acontece que há muitas interessantes transformações 2D / 3D que pode colocar dentro de uma matriz, e multiplicando que a matriz com um vector, em seguida, transforma essa vetor. No caso de você ainda está um pouco confuso, vamos começar com alguns exemplos e em breve você vai ver o que queremos dizer.

## Identity matrix

Em OpenGL que normalmente trabalham com matrizes de transformação 4x4 por várias razões e uma delas é que a maioria dos vetores são de tamanho 4. A matriz de transformação mais simples que podemos pensar é a matriz identidade. A matriz de identidade é uma matriz NxN com apenas 0s excepto na sua diagonal. Como você verá, esta transformação de matriz folhas um vetor completamente ileso:
  
  \ [\ Begin {bmatrix} \ color {red} 1 & \ color {red} 0 & \ color {red} 0 & \ color {red} 0 \\ \ color {verde} 0 & \ color {verde} 1 & \ color {verde} 0 & \ color {verde} 0 \\ \ color {azul} 0 & \ color {azul} 0 & \ color {azul} 1 & \ color {azul} 0 \\ \ color {roxo} 0 & \ cor púrpura {} 0 & \ cor púrpura {} 0 & \ cor púrpura {} 1 \ final {bmatrix} \ cdot \ begin {bmatrix} 1 2 \\ \\ \\ 3 4 \ final {bmatrix} = \ begin {bmatrix} \ cor vermelho {} 1 \ cdot 1 \\ \ cor verde {} 1 \ cdot 2 \\ \ cor azul {} 1 \ cdot 3 \\ \ cor púrpura {} 1 \ cdot 4 \ final {bmatrix } = \ begin {bmatrix} 1 2 \\ \\ \\ 3 4 \ final {bmatrix} \]
  
  O vector é completamente intactas. Isto torna-se óbvio a partir das regras de multiplicação: o primeiro elemento é resultado de cada elemento individual da primeira linha da matriz multiplicado com cada elemento do vector. Uma vez que cada um dos elementos da linha são 0, exceto a primeira, obtemos: \ (\ color {red} 1 \ cdot1 + \ color {red} 0 \ cdot2 + \ color {red} 0 \ cdot3 + \ color {vermelho} 0 \ cdot4 = 1 \) e o mesmo se aplica para os outros 3 elementos do vetor.

{{% greenbox tip %}}
Você pode estar se perguntando o que o uso é de uma matriz de transformação que não transforma? A matriz de identidade é geralmente um ponto de partida para gerar outras matrizes de transformação e se cavar ainda mais fundo álgebra linear, uma matriz muito útil para demonstração de teoremas e resolução de equações lineares.

{{% /greenbox %}}

## Scaling

Quando estamos escalar um vector estamos aumentando o comprimento da flecha pela quantidade que gostaríamos de escala, mantendo sua direção o mesmo. Uma vez que estamos a trabalhar em 2 ou 3 dimensões, podemos definir escala por um vector de 2 ou 3 variáveis ​​de escalonamento, cada um dimensionamento um eixo (x, y ou z).

Vamos tentar escalar o vector \ (\ color {vermelho} {\ bar {v}} = (3,2) \). Vamos escalar do vector ao longo do eixo-x por 0,5, tornando-se, assim, duas vezes mais estreita; e vamos escalar do vector por dois ao longo do eixo y, tornando-se duas vezes mais alta. Vamos ver o que parece que se dimensionar o vetor por (0.5,2) como \ (\ color {azul} {\ bar {s}} \):

![altlogo](https://learnopengl.com/img/getting-started/vectors_scale.png)

Tenha em mente que OpenGL normalmente opera no espaço 3D para que para este caso 2D poderíamos definir a escala do eixo z a 1, deixando-a ilesa. A operação de escala que acabou de realizar uma escala não uniforme, porque o fator de escala não é o mesmo para cada eixo. Se o escalar seria igual em todos os eixos que seria chamado de uma escala uniforme.

Vamos começar a construir uma matriz de transformação que faz o escalonamento para nós. Vimos a partir da matriz de identidade que cada um dos elementos da diagonal foram multiplicados com o seu elemento de vector correspondente. E se mudássemos os 1s na matriz de identidade para 3s? Nesse caso, estaríamos multiplicando cada um dos elementos do vetor por um valor de 3 e assim, efetivamente uniformemente escalar o vector por 3. Se nós representam as variáveis ​​de escala como \ ((\ color {vermelho} {S_1}, \ color { verde} {S_2}, \ cor azul {} {} s_3) \) que podem definir uma matriz de dimensionamento em qualquer vector \ ((x, y, z) \) como:
  
  \ [\ Begin {bmatrix} \ color {vermelho} {} S_1 & \ color {red} 0 & \ color {red} 0 & \ color {red} 0 \\ \ color {verde} 0 & \ color {verde} {S_2} e \ color {verde} 0 & \ color {verde} 0 \\ \ color {azul} 0 & \ color {azul} 0 & \ color {azul} {} s_3 & \ color {azul} 0 \\ \ cor púrpura {} 0 & \ cor púrpura {} 0 & \ cor púrpura {} 0 & \ cor púrpura {} 1 \ final {bmatrix} \ cdot \ begin {pmatrix} x \\ Y \\ z \\ 1 \ final {pmatrix} = \ begin {pmatrix} \ cor vermelho {} {} S_1 \ cdot x \\ \ cor verde {} {} S_2 \ cdot y \\ \ cor azul {} {} s_3 \ cdot z \\ 1 \ final {pmatrix} \]
  
  Note-se que mantemos o valor de escala 4º 1. O componente w é usado para outros fins, como veremos mais tarde.

## Translation

A tradução é o processo de adição de um outro vector no topo do vector original para voltar um novo vector com uma posição diferente, movendo-se assim o vector baseado em um vetor de translação. Nós já falamos sobre adição de vectores de modo que este não deve ser muito nova.

Assim como a matriz de escala existem vários locais em uma matriz de 4 por 4, que podemos usar para executar determinadas operações e para a tradução esses são os 3 principais valores da 4ª coluna. Se nós representam o vector de tradução como \ ((\ cor vermelho {} {} T_x, \ cor verde {} {} T_y, \ cor azul {} {} T_z) \) podemos definir a matriz de tradução por:
  
  \ [\ Begin {bmatrix} \ color {red} 1 & \ color {red} 0 & \ color {red} 0 & \ color {vermelho} {T_x} \\ \ color {verde} 0 & \ color {verde} 1 & \ color {verde} 0 & \ color {verde} {T_y} \\ \ color {azul} 0 & \ color {azul} 0 & \ color {azul} 1 & \ color {azul} {T_z} \\ \ cor púrpura {} 0 & \ cor púrpura {} 0 & \ cor púrpura {} 0 & \ cor púrpura {} 1 \ final {bmatrix} \ cdot \ begin {pmatrix} x \\ Y \\ z \\ 1 \ final {pmatrix} = \ begin {pmatrix} x + \ cor vermelho {} {} T_x \\ y + \ cor verde {} {} T_y \\ Z + \ cor azul {} {} T_z \\ 1 \ final { pmatrix} \]
  
  Isso funciona porque todos os valores de tradução são multiplicados por coluna w do vetor e acrescentou aos valores originais do vetor (lembre-se das regras matriz de multiplicação). Isto não teria sido possível com uma matriz 3-por-3.

{{% greenbox tip %}}

Homogeneous coordinates
  The w component of a vector is also known as a homogeneous coordinate.
  To get the 3D vector from a homogeneous vector we divide the x, y and z coordinate by its w coordinate. We usually do not notice this since the w component is 1.0 most of the time. Using homogeneous coordinates has several advantages: it allows us to do matrix translations on 3D vectors (without a w component we can't translate vectors) and in the next chapter we'll use the w value to create 3D perspective.

  Also, whenever the homogeneous coordinate is equal to 0, the vector is specifically known as a direction vector since a vector with a w coordinate of 0 cannot be translated.


{{% /greenbox %}}

Com uma matriz de tradução que pode mover objectos em qualquer dos 3 direcções dos eixos (x, y, z), tornando-se uma matriz de transformação muito útil para a nossa caixa de ferramentas de transformação.

## Rotation

Os últimos transformações eram relativamente fáceis de entender e visualizar em 2D ou 3D espaço, mas rotações são um pouco mais complicado. Se você quer saber exatamente como essas matrizes são construídos eu recomendo que você assista os itens de rotação de vídeos de álgebra linear da Khan Academy.

(https://www.khanacademy.org/math/linear-algebra/matrix_transformations)

Primeiro vamos definir o que uma rotação de um vetor é realmente. Uma rotação em 2D ou 3D é representado com um ângulo. Um ângulo poderia estar em graus ou radianos onde um círculo completo tem 360 graus ou 2 radianos PI. Eu prefiro explicar rotações usando graus como estamos geralmente mais acostumado a eles.
  

  A maioria das funções de rotação requer um ângulo em radianos, mas graus felizmente são facilmente convertidos em radianos:
ângulo em graus de ângulo em radianos = * (180 / PI)
ângulo em radianos = ângulo em graus * (PI / 180)
  Onde PI é igual a (arredondada) 3,14159265359.

  
  Rotativa roda metade de um círculo nos 360/2 = 180 graus de rotação e 1/5 para os meios adequados que rodam 360/5 = 72 graus para a direita. Isto é demonstrado por uma base 2D vector onde \ (\ cor {vermelho} {\ bar {v}} \) é rodado de 72 graus para a direita, ou no sentido horário, a partir de \ (\ cor {verde} {\ bar {k} } \):

(http://en.wikipedia.org/wiki/Pi)

{{% greenbox tip %}}
A maioria das funções de rotação requer um ângulo em radianos, mas graus felizmente são facilmente convertidos em radianos:
ângulo em graus de ângulo em radianos = * (180 / PI)
ângulo em radianos = ângulo em graus * (PI / 180)
  Onde PI é igual a (arredondada) 3,14159265359.

{{% /greenbox %}}

![altlogo](https://learnopengl.com/img/getting-started/vectors_angle.png)

Rotações em 3D são especificados com um ângulo e de um eixo de rotação. O ângulo específico, vai rodar o objecto ao longo do eixo de rotação dada. Tente visualizar esta girando a cabeça um certo grau enquanto continuamente olhando para baixo um eixo de rotação única. Ao rodar os vectores 2D num mundo 3D por exemplo, definir o eixo de rotação para o eixo z (tentam visualizar este).

Usando a trigonometria, é possível transformar vectores para vectores recém giradas a um ângulo. Isso geralmente é feito através de uma combinação inteligente das funções seno e cosseno (comumente abreviado para o pecado e cos). A discussão de como as matrizes de rotação são gerados está fora do escopo deste capítulo.

Uma matriz de rotação é definido para cada eixo unidade no espaço 3D, onde o ângulo é representado como o símbolo teta \ (\ teta \).

Rotação em torno do eixo-X:
  
  \ [\ Begin {bmatrix} \ color {red} 1 & \ color {red} 0 & \ color {red} 0 & \ color {red} 0 \\ \ color {verde} 0 & \ color {verde} {\ cos \ theta} e - \ color {verde} {\ sin \ theta} e \ color {verde} 0 \\ \ color {azul} 0 & \ color {azul} {\ sin \ theta} e \ color {azul} {\ cos \ theta} e \ color {azul} 0 \\ \ color {roxo} 0 & \ color {roxo} 0 & \ color {roxo} 0 & \ color {roxo} 1 \ end {bmatrix} \ cdot \ begin {pmatrix} x \\ Y \\ z \\ 1 \ final {pmatrix} = \ begin {pmatrix} x \\ \ cor verde {} {\ cos \ teta} \ cdot y - \ cor verde {} {\ sin \ teta} \ cdot z \\ \ cor azul {} {\ sin \ teta} \ cdot y + \ cor azul {} {\ cos \ teta} \ cdot z \\ 1 \ final {pmatrix} \]

Rotação em torno do eixo Y:
  
  \ [\ Begin {bmatrix} \ color {vermelho} {\ cos \ theta} e \ color {red} 0 & \ color {vermelho} {\ sin \ theta} e \ color {red} 0 \\ \ color {verde } 0 & \ color {verde} 1 & \ color {verde} 0 & \ color {verde} 0 \\ - \ color {azul} {\ sin \ theta} e \ color {azul} 0 & \ color {azul} {\ cos \ theta} e \ color {azul} 0 \\ \ color {roxo} 0 & \ color {roxo} 0 & \ color {roxo} 0 & \ color {roxo} 1 \ end {bmatrix} \ cdot \ begin {pmatrix} x \\ Y \\ z \\ 1 \ final {pmatrix} = \ begin {pmatrix} \ cor vermelho {} {\ cos \ teta} \ cdot x + \ cor vermelho {} {\ sin \ teta } \ cdot z \\ Y \\ - \ cor azul {} {\ sin \ teta} \ cdot x + \ cor azul {} {\ cos \ teta} \ cdot z \\ 1 \ final {pmatrix} \]

Rotação em torno do eixo Z:
  
  \ [\ Begin {bmatrix} \ color {vermelho} {\ cos \ theta} e - \ color {vermelho} {\ sin \ theta} e \ color {red} 0 & \ color {red} 0 \\ \ color { verde} {\ sin \ theta} e \ color {verde} {\ cos \ theta} e \ color {verde} 0 & \ color {verde} 0 \\ \ color {azul} 0 & \ color {azul} 0 & \ color {azul} 1 & \ color {azul} 0 \\ \ color {roxo} 0 & \ color {roxo} 0 & \ color {roxo} 0 & \ color {roxo} 1 \ end {bmatrix} \ cdot \ begin {pmatrix} x \\ Y \\ z \\ 1 \ final {pmatrix} = \ begin {pmatrix} \ cor vermelho {} {\ cos \ teta} \ cdot x - \ cor vermelho {} {\ sin \ teta } \ cdot y \\ \ cor verde {} {\ sin \ teta} \ cdot x + \ cor verde {} {\ cos \ teta} \ cdot y \\ z \\ 1 \ final {pmatrix} \]

Usando a rotação matrizes podemos transformar os nossos vetores posição em torno de um dos três eixos de unidade. Para girar em torno de um eixo 3D arbitrária podemos combinar todos 3 eles, em primeiro lugar girar em torno do eixo X, em seguida, Y e Z, em seguida, por exemplo. No entanto, este rapidamente introduz um problema chamado bloqueio cardan. Não vamos discutir os detalhes, mas a melhor solução é para girar em torno de uma unidade arbitrária eixo por exemplo (0.662,0.2,0.722) (note que este é um vetor unitário) de imediato, em vez de combinar as matrizes de rotação. Tal (detalhado) existe matriz e é dada abaixo com \ ((\ cor {vermelho} {R_x}, \ cor {verde} {R_y}, \ cor {azul} {R_z}) \) como o eixo de rotação arbitrária:
    
    \ [\ Begin {bmatrix} \ cos \ theta + \ color {vermelho} {R_x} ^ 2 (1 - \ cos \ theta) & \ color {vermelho} {R_x} \ color {verde} {R_y} (1 - \ cos \ theta) - \ color {azul} {R_z} \ sin \ theta & \ color {vermelho} {R_x} \ color {azul} {R_z} (1 - \ cos \ theta) + \ color {verde} { R_y} \ sin \ theta & 0 \\ \ color {verde} {R_y} \ color {vermelho} {R_x} (1 - \ cos \ theta) + \ color {azul} {R_z} \ sin \ theta & \ cos \ teta + \ cor {verde} {R_y} ^ 2 (1 - \ cos \ teta) {verde} {R_y} \ cor {azul} {R_z} & \ cor (1 - \ cos \ teta) - \ cor { vermelho} {R_x} \ sin \ theta & 0 \\ \ color {azul} {R_z} \ color {vermelho} {R_x} (1 - \ cos \ theta) - \ color {verde} {R_y} \ sin \ theta & \ color {azul} {R_z} \ color {verde} {R_y} (1 - \ cos \ theta) + \ color {vermelho} {R_x} \ sin \ theta & \ cos \ theta + \ color {azul} { R_z} ^ 2 (1 - \ cos \ teta) & 0 \\ 0 & 0 & 0 & 1 \ final {bmatrix} \]
    
    
    Uma discussão matemático de gerar tal matriz um está fora do âmbito do presente capítulo. Tenha em mente que mesmo essa matriz não impedir completamente bloqueio cardan (embora fica muito mais difícil). Para evitar que verdadeiramente Gimbal bloqueia temos para representar rotações usando quaternions, que não só são mais seguros, mas também computacionalmente mais amigável. No entanto, uma discussão sobre quaternions está fora do escopo deste capítulo.

## Combining matrices

O verdadeiro poder de usar matrizes para transformações é que podemos combinar várias transformações em uma única matriz, graças à multiplicação de matrizes-matriz. Vamos ver se podemos gerar uma matriz de transformação que combina várias transformações. Digamos que temos um vector (x, y, z) e que queremos dimensioná-lo por 2 e, em seguida, traduzi-lo por (1,2,3). Precisamos de uma tradução e uma matriz de escala para nossos passos necessários. A matriz de transformação resultante seria semelhante:
    
         \ [Trans. Escala = \ begin {bmatrix} \ color {red} 1 & \ color {red} 0 & \ color {red} 0 & \ color {red} 1 \\ \ color {verde} 0 & \ color {verde} 1 & \ cor verde {} 0 & \ cor verde {} 2 \\ \ cor azul {} 0 & \ cor azul {} 0 & \ cor azul {} 1 & \ cor azul {} 3 \\ \ cor púrpura {} 0 & \ color {roxo} 0 & \ color {roxo} 0 & \ color {roxo} 1 \ end {bmatrix}. \ Begin {bmatrix} \ color {red} 2 & \ color {red} 0 & \ color {red} 0 & \ color {red} 0 \\ \ color {verde} 0 & \ color {verde} 2 & \ color {verde} 0 & \ color {verde} 0 \\ \ color {azul} 0 & \ color {azul} 0 & \ color {azul} 2 & \ color {azul} 0 \\ \ color {roxo} 0 & \ cor {roxo} 0 & \ color {roxo} 0 & \ color {roxo} 1 \ end {bmatrix} = \ begin {bmatrix} \ color {red} 2 & \ color {red} 0 & \ color {red} 0 & \ color {red} 1 \\ \ color {verde} 0 & \ color {verde} 2 & \ color {verde} 0 & \ color {verde} 2 \\ \ color {azul} 0 & \ color {azul} 0 & \ cor azul {} 2 & \ cor azul {} 3 \\ \ cor púrpura {} 0 & \ cor púrpura {} 0 & \ cor púrpura {} 0 & \ cor púrpura {} 1 \ final {bmatrix} \ ]
    
    Note que primeiro fazer uma tradução e, em seguida, uma transformação de escala ao multiplicar matrizes. A multiplicação de matrizes não é comutativa, o que significa que sua ordem é importante. Ao multiplicar matrizes mais à direita da matriz é multiplicado primeiro com o vector de modo que você deve ler as multiplicações da direita para a esquerda. É aconselhável primeiro fazer operações, em seguida, rotações e, por último traduções quando combinando matrizes caso contrário eles podem (negativamente) afetam uns aos outros de escala. Por exemplo, se você primeiro fazer uma tradução e, em seguida, escala, o vetor de translação também escalável!

Executando a matriz de transformação final sobre os resultados do vetor no seguinte vetor:
    
\ [\ Begin {bmatrix} \ color {red} 2 & \ color {red} 0 & \ color {red} 0 & \ color {red} 1 \\ \ color {verde} 0 & \ color {verde} 2 & \ color {verde} 0 & \ color {verde} 2 \\ \ color {azul} 0 & \ color {azul} 0 & \ color {azul} 2 & \ color {azul} 3 \\ \ color {roxo} 0 & \ color {roxo} 0 & \ color {roxo} 0 & \ color {roxo} 1 \ end {bmatrix}. \ Begin {bmatrix} x \\ Y \\ z \\ 1 \ final {bmatrix} = \ begin {bmatrix} \ cor vermelho {} 2x + \ cor vermelho {} 1 \\ \ cor verde {} 2y + \ cor {verde} 2 \\ \ cor azul {} + 2z \ cor azul {} 3 \\ 1 \ final {bmatrix} \]
    
  Ótimo! O vector é primeiramente escalonado por dois e, em seguida, traduzido por (1,2,3).

# In practice

Agora que nós explicamos toda a teoria por trás de transformações, é hora de ver como nós podemos realmente usar esse conhecimento para nossa vantagem. OpenGL não tem qualquer forma de conhecimento matriz ou vector construído em, por isso temos de definir nossas próprias aulas de matemática e funções. Neste livro, prefiro abstrair de todos os pequenos detalhes matemáticos e simplesmente usar pré-fabricados bibliotecas de matemática. Felizmente, há um fácil de usar e adaptados-for-OpenGL matemática biblioteca chamada GLM.

## GLM

GLM significa OpenGL Matemática e é uma biblioteca somente cabeçalho, o que significa que só temos de incluir os arquivos de cabeçalho adequados e estamos a fazer; sem vinculação e compilar necessário.
  GLM pode ser baixado de seu site. Copie o diretório raiz dos arquivos de cabeçalho em seu inclui pasta e vamos rolar.

![altlogo](https://learnopengl.com/img/getting-started/glm.png)

(https://glm.g-truc.net/0.9.8/index.html)

A maioria das funcionalidades do GLM que precisamos podem ser encontrados em arquivos de 3 cabeçalhos que vamos incluir os seguintes:

```cpp

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

```

Vamos ver se podemos colocar nosso conhecimento transformação para uma boa utilização, traduzindo um vetor de (1,0,0) por (1,1,0) (note que nós defini-lo como um glm :: vec4 com seu coordenadas homogêneas definido para 1.0:

```cpp

glm::vec4 vec(1.0f, 0.0f, 0.0f, 1.0f);
glm::mat4 trans = glm::mat4(1.0f);
trans = glm::translate(trans, glm::vec3(1.0f, 1.0f, 0.0f));
vec = trans * vec;
std::cout << vec.x << vec.y << vec.z << std::endl;

```

Nós primeiro definir um vetor chamado vec usando a classe vector built-in da GLM. Em seguida, definir uma mat4 e inicializar explicitamente à matriz identidade por inicializar diagonais da matriz a 1,0; se não inicializá-lo para a matriz identidade a matriz seria uma matriz nula (todos os elementos 0) e todas as operações da matriz subseqüentes iria acabar uma matriz nula também.

O próximo passo é para criar uma matriz de transformação, passando a matriz de identidade com a GLM :: traduzir função, juntamente com um vector de tradução (dada matriz é então multiplicado por uma matriz de tradução e a matriz resultante é devolvido).
    Depois multiplicamos nosso vector pela matriz de transformação e de saída o resultado. Se ainda me lembro como tradução matriz funciona, então o vetor resultante deve ser (1 + 1,0 + 1,0 + 0) que é (2,1,0). Este trecho de código gera 210 de modo a matriz de tradução fez o seu trabalho.

Vamos fazer algo mais interessante e escala e girar o objeto recipiente do capítulo anterior:

```cpp

glm::mat4 trans = glm::mat4(1.0f);
trans = glm::rotate(trans, glm::radians(90.0f), glm::vec3(0.0, 0.0, 1.0));
trans = glm::scale(trans, glm::vec3(0.5, 0.5, 0.5));  

```

Em primeiro lugar, dimensionar o recipiente de 0,5 em cada um dos eixos e em seguida rodar o recipiente 90 graus em torno do eixo Z. GLM espera que seus ângulos em radianos para que converter os graus em radianos usando glm :: radianos. Note que o retângulo textura é no plano XY por isso queremos girar em torno do eixo Z. Tenha em mente que o eixo que gira em torno deve ser um vetor de unidade, por isso não deixe para normalizar o vetor primeiro se você não está girando em torno do X, Y ou eixo Z. Porque nós passar a matriz para cada uma das funções do GLM, GLM automaticamente múltiplos as matrizes em conjunto, resultando em uma matriz de transformação que combina todas as transformações.

A próxima grande questão é: como é que vamos chegar a matriz de transformação para os shaders? Nós brevemente mencionado antes que GLSL também tem um tipo mat4. Então, vamos adaptar o shader de vértice para aceitar uma variável mat4 uniforme e multiplicar o vetor posição pelo uniforme de matriz:

```cpp

#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoord;

out vec2 TexCoord;
  
uniform mat4 transform;

void main()
{
    gl_Position = transform * vec4(aPos, 1.0f);
    TexCoord = vec2(aTexCoord.x, aTexCoord.y);
} 

```

{{% greenbox tip %}}
GLSL também tem mat2 e mat3 tipos que permitem swizzling-like operações apenas como vetores. Todas as operações matemáticas acima mencionados (tais como multiplicação escalar da matriz, a multiplicação de matrizes do vector e multiplicação matriz-matriz) são permitidos nos tipos de matriz. Onde quer que são utilizadas operações com matrizes especiais, vamos ter certeza de explicar o que está acontecendo.

{{% /greenbox %}}

Adicionamos a uniforme e multiplicou-se o vector de posição com a matriz de transformação antes de passá-lo para gl_Position. O nosso recipiente deve agora ser duas vezes mais pequena e rodado 90 graus (inclinado para a esquerda). Nós ainda precisamos de passar a matriz de transformação para o shader no entanto:

```cpp

unsigned int transformLoc = glGetUniformLocation(ourShader.ID, "transform");
glUniformMatrix4fv(transformLoc, 1, GL_FALSE, glm::value_ptr(trans));

```

Em primeiro lugar, consultar a localização da variável uniforme e, em seguida, enviar os dados da matriz para os shaders utilizando glUniform com Matrix4fv como postfix. O primeiro argumento deve ser familiar até agora, que é a localização do uniforme. O segundo argumento diz ao OpenGL quantas matrizes gostaríamos de enviar, que é 1. O terceiro argumento nos pergunta se queremos transpor nossa matriz, que é trocar as colunas e linhas. desenvolvedores OpenGL costumam usar um layout de matriz interna chamada coluna-major ordenação que é o layout da matriz padrão no GLM por isso não há necessidade de transpor as matrizes; podemos mantê-lo em GL_FALSE. O último parâmetro é os dados da matriz reais, mas GLM armazena os dados de seus matrizes de uma maneira que nem sempre correspondem às expectativas do OpenGL para que primeiro converte os dados com value_ptr função built-in da GLM.

Nós criamos uma matriz de transformação, declarou um uniforme no shader de vértice e enviou a matriz para os shaders em que transformam nossas coordenadas dos vértices. O resultado deve ser algo como isto:

![altlogo](https://learnopengl.com/img/getting-started/transformations.png)

Perfeito! Nosso recipiente é realmente inclinado para a esquerda e duas vezes mais pequeno para que a transformação foi bem sucedida. Vamos ficar um pouco mais funky e ver se podemos rodar o recipiente ao longo do tempo, e para se divertir também vamos reposicionar o recipiente no lado inferior direito da janela.
Para rodar o recipiente ao longo do tempo nós temos que atualizar a matriz de transformação no circuito tornar porque ele precisa atualizar cada quadro. Nós usamos a função do tempo de GLFW para obter um ângulo ao longo do tempo:

```cpp

glm::mat4 trans = glm::mat4(1.0f);
trans = glm::translate(trans, glm::vec3(0.5f, -0.5f, 0.0f));
trans = glm::rotate(trans, (float)glfwGetTime(), glm::vec3(0.0f, 0.0f, 1.0f));

```

Tenha em mente que no caso anterior, poderíamos declarar a qualquer lugar matriz de transformação, mas agora temos que criá-lo cada iteração para atualizar continuamente a rotação. Isto significa que temos para recriar a matriz de transformação em cada iteração do circuito de renda. Normalmente, quando o processamento de cenas temos várias matrizes de transformação que são recriados com novos valores cada quadro.

Aqui podemos rodar o recipiente em torno da origem (0,0,0) e uma vez que é rodado, traduzimos a sua versão rodada para o canto inferior direito da tela. Lembre-se que a ordem de transformação real deve ser lida ao contrário: mesmo que no código que primeiro traduzir e depois girar, as transformações reais primeiro aplicar uma rotação e uma tradução. Compreender todas estas combinações de transformações e como se aplicam a objetos é difícil de entender. Experimente e experimentar transformações como estas e você vai rapidamente ter uma idéia dela.

Se você fez as coisas direito, você deve obter o seguinte resultado:

![altlogo](https://learnopengl.com/img/getting-started/transformations2.png)

E aí está. Um recipiente traduzido desse girado vez mais, tudo feito por uma única matriz de transformação! Agora você pode ver porque matrizes são uma construção tão poderosa na terra gráficos. Podemos definir uma quantidade infinita de transformações e combiná-los todos em uma única matriz que podemos voltar a usar tão frequentemente como gostaríamos. Usando transformações como este no shader de vértice nos salva o esforço de definição de re-os dados de vértice e nos poupa algum tempo de processamento, bem como, uma vez que não tem que re-enviar os nossos dados o tempo todo (que é bastante lento); tudo o que precisamos fazer é atualizar o uniforme transformação.

Se você não obter o resultado correto ou se você estiver em algum lugar preso outra coisa, dê uma olhada no código fonte ea classe shader atualizado.

(/code_viewer_gh.php?code=src/1.getting_started/5.1.transformations/transformations.cpp)

(https://learnopengl.com/code_viewer_gh.php?code=includes/learnopengl/shader_m.h)

No próximo capítulo vamos discutir como podemos usar matrizes para definir diferentes espaços de coordenadas para os nossos vértices. Este será o nosso primeiro passo para gráficos 3D!

## Further reading

Essência da Álgebra Linear: grande série de vídeo tutorial por Grant Sanderson sobre a matemática subjacente de transformações e álgebra linear.

(https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

## Exercises




Utilizando a última transformação no recipiente, tente trocar a ordem em torno de pelo primeiro rotativo e, em seguida, a tradução. Veja o que acontece e tentar razão por que isso acontece: solução.

(/code_viewer_gh.php?code=src/1.getting_started/5.2.transformations_exercise1/transformations_exercise1.cpp)

Tente desenhar um segundo recipiente com outra chamada para glDrawElements mas colocá-lo em uma posição diferentes, utilizando apenas transformações. Certifique-se que este segundo recipiente é colocado no canto superior esquerdo da janela e, em vez de girar, escalá-lo ao longo do tempo (usando a função pecado é útil aqui, nota que o uso de pecado fará com que o objeto para invertido assim que uma escala negativa é aplicada): solução.

(/code_viewer_gh.php?code=src/1.getting_started/5.2.transformations_exercise2/transformations_exercise2.cpp)

