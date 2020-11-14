---
title: "Correção Gama"
date: 2020-10-29T15:28:58-03:00
draft: false
katex: true
markup: "mmark"
---

[Post original](https://learnopengl.com/Advanced-Lighting/Gamma-Correction)

Logo que calculamos as cores finais de cada pixel, temos que mostrá-los em um monitor. Antigamente a maioria dos monitores utilizavam tubos de raios catódicos (_cathode-ray tube_ - CRT) para gerar imagens na tela. Nesses monitores, dobrar a tensão de entrada não resultava no dobro da quantidade de brilho. Dobrar a tensão de entrada resultava em um brilho que seguia uma relação exponencial de aproximadamente 2.2, conhecida como o _gama_ do monitor. Acontece que, coincidentemente, esta relação também se assemelha a como humanos medem o brilho, dado que este é mostrado na tela com uma relação similar de potência (inversa). Para melhor entender o que tudo isto significa veja a imagem seguinte:

![GitHub Logo](/iluminacao_avancada/correcao_gama/images/gamma_correction_brightness.png)

A linha de cima parece com uma escala de brilho correta para o olho humano, dobrando o brilho (de $$0.1$$ para $$0.2$$ por exemplo) parece de fato ser duas vezes mais brilhante com algumas diferenças consistentes. Porém, quando estamos falando do brilho físico da luz, ou seja, a quantidade de fótons vindos de uma fonte de luz, a escala debaixo mostra o brilho correto. Na escala inferior, o dobrar o brilho resulta no brilho físico correto, mas já que nossos olhos percebem brilho diferentemente (mais susceptível a mudanças em cores escuras) o brilho parece estranho.

Como o olho humano prefere enxergar o brilho das cores de acordo com a escala superior, monitores (ainda hoje) usam uma relação de potência para mostrar as cores de saída de tal forma que os brilhos físicos das cores originais sejam mapeados (não linearmente) a brilhos de cores na escala de cima.

Este mapeamento não linear feito pelos monitores resulta em brilhos mais agradáveis para os nossos olhos, mas quando se fala de renderizar gráficos existe um problema: todas opções de cor e brilho que nós configuramos em nossas aplicações são baseadas no que percebemos do monitor e portanto todas opções são de fato opções não lineares de brilho/cor. Olhe o gráfico a seguir:

![GitHub Logo](/iluminacao_avancada/correcao_gama/images/gamma_correction_gamma_curves.png)

A linha pontilhada representa valores de cor/luz no espaço linear e a linha cheia representa o espaço de cor que o monitor mostra. Se dobrarmos a cor no espaço linear, o resultado é de fato o dobro do valor. Por exemplo, pegue o vetor cor da luz $$(0.5, 0.0, 0.0)$$ que representa uma luz vermelha semiescura. Se fossemos dobrar esta luz no espaço linear teríamos $$(1.0, 0.0, 0.0)$$, como podemos ver no gráfico. Entretanto, a cor original é mostrada no monitor como $$(0.218, 0.0, 0.0)$$. Aqui é onde começam a surgir os problemas: uma vez que dobramos a luz vermelha escura no espaço linear, esta se torna mais de $$4.5$$ vezes mais brilhante no monitor! 

Até este capítulo, nós assumimos trabalhar no espaço linear, mas estivemos de fato trabalhando no espaço da saída do monitor, então todas variáveis de cor e iluminação que configuramos não estavam fisicamente corretas, mas mal pareciam (quase) certas no nosso monitor. Por esta razão, nós (e os artistas) geralmente definimos os valores de iluminação mais brilhantes do que deveriam ser (já que o monitor as escurece), que resulta em invalidar todos calculos feitos no espaço linear. Note que ambos o monitor (CRT) e o gráfico linear, começam e acabam na mesma posição: são os valores intermediários que são escurecidos pela tela.

Como as cores são baseadas na saída do monitor, todos cálculos (de iluminação) intermediários no espaço linear são fisicamente incorretos. Isto se torna óbvio quando utilizamos algoritmos de iluminação mais avançados, como podemos ver a seguir: 

![GitHub Logo](/iluminacao_avancada/correcao_gama/images/gamma_correction_example.png)

Você pode ver que a correção gama, os valores de cor (atualizados) funcionam melhor juntos e áreas mais escuras apresentam mais detalhes. No geral, um imagem de melhor qualidade com algumas poucas modificações.

Sem corrigir corretamente o gama do monitor, a iluminação parece errada e artistas terão um trabalho difícil para obter resultados realísticos. A solução é aplicar a **correção gama**.

# Correção Gama

A ideia da correção gama é aplicar o inverso do gama do monitor a cor final de saída andes de apresentá-la na tela. Relembrando a curva do gama no gráfico observamos uma outra linha tracejada que é a inversa da curva gama do monitor. Multiplicamos cada uma das cores lineares de saída pela sua curva inversa (tornando-as mais brilhantes) e, logo que são mostradas no monitor, a curva gama do monitor é aplicada e as cores resultantes se tornam lineares. Essencialmente, nós deixamos as cores intermediarias mais brilhantes para que assim que o monitor as escureçam, os valores fiquem balanceados.

Vamos a outro exemplo. Temos novamente o vermelho escuro $$(0.5, 0.0, 0.0)$$. Antes de imprimi-lo na tela, aplicamos a curva de correção gama ao valor da cor. Cores lineares mostradas por um monitor são aproximadamente escaladas por uma potência de $$2.2$$, então o inverso requer que as cores sejam escaladas a uma potência de $$1/2.2$$. O vermelho escuro corrigido então se torna 
$$(0.5,0.0,0.0)^{1/2.2}=(0.5,0.0,0.0)^{0.45}=(0.73,0.0,0.0)$$. As cores corrigidas são então enviadas para o monitor e como resultado a cor é mostrada como $$(0.73,0.0,0.0)2.2=(0.5,0.0,0.0)$$. Você pode ver que usando a correção gama, o monitor agora finalmente mostra as cores como as configuramos linearmente na aplicação.


{{% notice note %}}
Um valor gama de 2.2 é um valor padrão que aproximadamente estima o gama médio da maior parte dos monitores. O espaço de cor resultante do gama de valor 2.2 é chamado de espaço de cor sRGB (não 100% exato, mas próximo). Cada monitor tem sua própria curva gama, mas o gama de valor 2.2 gera bons resultados na maior parte dos monitores. Por essa razão, jogos normalmente permitem jogadores escolher a configuração para o gama do jogo já que este varia levemente entre monitores diferentes. 
{{% /notice %}}


Existem dois jeitos de se aplicar a correção gama a sua cena:

* Usar o suporte nativo da OpenGL de framebuffer sRGB
* Fazer a correção gama nós mesmos, no shader de fragmento.

A primeira opção é provavelmente a mais fácil, mas dá menos liberdade. Ao habilitar `GL_FRAMEBUFFER_SRGB` você diz a OpenGL para aplicar a correção gama aos pixels (do espaço de cor sRGB) antes de armazená-los no buffer de cor. O sRGB é um espaço de cor que corresponde aproximadamente a um gama $$2.2$$ e um padrão para maioria dos dispositivos. Depois de habilitar `GL_FRAMEBUFFER_SRGB`, a OpenGL automaticamente aplica a correção gama após executar cada shader de fragmento para todos os framebuffer subsequentes, incluindo o framebuffer padrão.

Habilitar `GL_FRAMEBUFFER_SRGB` é tão simples quanto chamar `glEnable`: 

```cpp
glEnable(GL_FRAMEBUFFER_SRGB); 
```

De agora em diante, as imagens renderizadas serão corrigidas e como isso é feito no hardware então é completamente de graça. Algo que você deve se lembrar neste método (e no outro também) é que a correção gama (também) transforma as cores do espaço linear para o espaço não linear, então é muito importante que você só aplique a correção no último passo. Se fizer a correção antes do último passo, todas operações posteriores nas cores resultantes irão trabalhar com valores incorretos. Por exemplo, se estiver usando múltiplos framebuffers, provavelmente vai querer que os resultados intermediários passados entre os framebuffers permaneçam no espaço linear e que a correção gama seja aplicada apenas ao último framebuffer antes de enviá-lo a tela do monitor. 

O segundo jeito requer um pouco mais de trabalho, mas também nos dá mais controle sobre as operações de correção gama. Aplicamos a correção gama no final de cada execução de shader de fragmento relevante para que as cores finais estejam corrigidas antes de enviá-las ao monitor:

```cpp
void main()
{
    // do super fancy lighting in linear space
    [...]
    // apply gamma correction
    float gamma = 2.2;
    FragColor.rgb = pow(fragColor.rgb, vec3(1.0/gamma));
}
```

A ultima linha de código efetivamente aumenta cada componente individual da cor `fragColor` para 1.0/gamma, corrigindo a cor de saída deste shader de fragmento.

Um problema com esse método é que para manter consistência você tem que aplicar a correção gama para cada shader de fragmento que contribui para a imagem final. Se você tiver uma dúzia de shaders de fragmento para múltiplos objetos, você deve adicionar o código para correção gama para cada um desses shaders. Uma solução mais fácil seria inserir um estágio de pós-processamento no seu loop de renderização e aplicar a correção gama no quadrilátero pós-processado como último passo, do qual você precisa fazer apenas uma vez.

Essa única linha representa a implementação técnica da correção gama. Nem um pouco impressionante, mas existem algumas coisas extras que deve considerar ao fazer a correção gama. 

# sRGB textures

Pelo fato dos monitores aplicarem o gama ao exibir as cores, toda vez que você desenha, edita, ou pinta uma imagem no seu computador, você deve escolher cores baseando-se no que exerga em seu monitor. Isso significa que todas imagens que você cria ou edita não estão no espaço linear, mas sim no espaço `sRGB` (ou seja, ao dobrar um vermelho escuro na sua tela baseando-se no brilho perceptivel, não é igual a simplesmente dobrar o valor da componente vermelha).

Como resultado, quando artistas de textura criam arte pela visão, todas os valores de texture estão no espaço `sRGB`, então se usarmos essas texturas na nossa aplicação devemos levar isso em conta. Antes de saber o que era correção gama, isso não era um problema, porque as textureas pareciam boas no espaço `sRGB` do qual era o mesmo com o qual trabalhávamos; as texturas eram exibidas exatamente do jeito que são. Entretanto, agora que estamos exibindo tudo no espaço linear, as cores dessas texturas ficarão estranhas como na imagem a seguir:

![GitHub Logo](/iluminacao_avancada/correcao_gama/images/gamma_correction_srgbtextures.png)

A imagem da textura é muito mais brilhante e isso acontece porque esta sendo corrigida duas vezes! Pense sobre isto, quando criamos uma imagem baseando-se no que enxergamos no monitor, efetivamente corrigimos os valores de cor da imagem de tal forma que pareça certa no monitor. Mas como aplicamos a correção gama ao renderizar, a imagem acaba ficando muito brilhante.
 
Para resolver este problema, deveríamos assegurar que os artistas de textura trabalhassem no espaço linear. Mas, já que é mais fácil trabalhar no espaço `sRGB` e a maioria das ferramentas nem suportam direito texturização linear, esta solução não é muito boa.

A solução mais plausível é recorrigir ou transformar essas texturas `sRGB` para o espaço linear antes de fazer qualquer cálculo com suas cores. Podemos fazer assim:

```cpp
float gamma = 2.2;
vec3 diffuseColor = pow(texture(diffuse, texCoords).rgb, vec3(gamma));
```

Para fazer isso com cada texture no espaço `sRGB` dá muito trabalho. Por sorte a OpenGL nos oferece uma outra solução para os nossos problemas ao nos permitir os formatos internos de textura `GL_SRGB` e `GL_SRGB_ALPHA`.

Se criarmos uma textura em OpenGL com qualquer um desses dois formatos de textura `sRGB`, a OpenGL vai automaticamente corrigir as cores para o espaço linear assim que forem usadas, nos possibilitando trabalhar no espaço linear. Podemos especificar uma textura como `sRGB` desse jeito:

```cpp
glTexImage2D(GL_TEXTURE_2D, 0, GL_SRGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);  
```

Se você também quiser incluir componentes alfa na sua textura terá então que especificar o formato interno da textura como `GL_SRGB_ALPHA`.

Devemos tomar cuidado ao especificar texturas no espaço `sRGB` já que nem todas texturas estarão de fato no espaço `sRGB`. Texturas utilizadas para colorir objetos (como texturas difusas) são quase sempre do tipo `sRGB`. Texturas usadas para recuperar parâmetros de iluminação (como mapas especulares e mapas de normais) estão quase sempre no espaço linear, então se configurássemos estas texturas como `sRGB` a iluminação vai ficar bem estranha. Seja cuidadoso com qual texturas configurar como `sRGB`.

Com as texturas difusas definidas como `sRGB` você terá o resultado visual esperado, mas dessa vez a correção gama ocorre apenas uma vez.

# Atenuação

Outra coisa que fica diferente com a correção gama é a atenuação da iluminação. No mundo real físico, a iluminação atenua aproximadamente inversamente proporcional a distancia quadrada da fonte de luz. Em português normal, isso significa que a força da luz reduz quadraticamente com a distancia a fonte de luz, como a seguir:

```cpp
float attenuation = 1.0 / (distance * distance); 
```

Todavia, quando usamos essa equação o efeito de atenuação é normalmente muito forte, dando as luzes um raio pequeno que não parece fisicamente correto. Por esta razão outras funções de atenuação são utilizadas (como discutimos no capítulo de iluminação básica) que dão muito mais controle, ou o equivalente linear pode ser usado:

```cpp
float attenuation = 1.0 / distance; 
```

O equivalente linear dá resultados mais plausíveis comparados a sua variante quadrática se a correção gama, mas quando habilitamos a correção gama a atenuação linear parece muito fraca e a atenuação quadrática fisicamente correta de repente oferece melhores resultados. A imagem abaixo mostras as diferenças:

![GitHub Logo](/iluminacao_avancada/correcao_gama/images/gamma_correction_attenuation.png) 

O porquê desta diferença é que as funções de atenuação da luz mudam o brilho, e como não estávamos visualizando nossa cena no espaço linear, escolhemos as funções de atenuação que pareciam melhores no nosso monitor, mas não eram fisicamente corretas. Pense na função de atenuação quadrática: se usássemos esta função sem a correção gama, a função se torna: $$(1.0/distance^2)^{2.2}$$ ao exibirmos no monitor. Isso cria uma atenuação muito maior do que originalmente teríamos antecipado. Isso também explica porque o equivalente linear faz muito mais sentido sem a correção gama já que se torna $$(1.0/distance)^{2.2}=1.0/distance^{2.2}$$, a qual se assemelha muito mais com sua equivalente física. 

{{% notice note %}}
A função de atenuação mais avançada discutida no capítulo [iluminação básica]({{site.url}}) ainda tem seu lugar em cenas com gama corrigido dado que ela dá mais controle sobre a atenuação exata (mas claro que requer diferentes parâmetros em uma cena com gama corrigido).
{{% /notice %}}

Você pode encontrar o código fonte desta cena demo simples [aqui](https://learnopengl.com/code_viewer_gh.php?code=src/5.advanced_lighting/2.gamma_correction/gamma_correction.cpp). Pressionando a barra de espaço trocamos entre uma cena com gama corrigido e uma cena sema a correção gama, com ambas cenas utilizando suas texturas e atenuação equivalentes. Não é a demonstração mais incrível, mas mostra como aplicar todas técnicas.

Em suma, a correção gama nos possibilita fazer todos nossos cálculos de shader/iluminação no espaço linear. Como o espaço linear faz sentido no mundo físico, a maioria das equações físicas passam a dar bons resultados (como uma atenuação real de luz). Quanto mais avançada sua iluminação se torna, mais fácil é conseguir resultados bonitos (e realísticos) com a correção gama. É por isso que também se é aconselhável que se ajuste os parametros de iluminacao só depois que tiver a correção gama no lugar.

# Recursos adicionais

  *  [O que todo programador deveria saber sobre gama](http://blog.johnnovak.net/2016/09/21/what-every-coder-should-know-about-gamma/): um artigo aprofundado e muito bem escrito por John Novak sobre correção gama.
  * [www.cambridgeincolour.com](https://www.cambridgeincolour.com/tutorials/gamma-correction.htm): mais sobre gama e correção gama.
  * [www.wolfire.com](http://blog.wolfire.com/2010/02/Gamma-correct-lighting): post por David Rosen sobre os benefícios da correção gama na renderização de gráficos.
  * [renderwonk.com](http://renderwonk.com/blog/index.php/archive/adventures-with-gamma-correct-rendering/): algumas considerações práticas extras.

[post]: https://learnopengl.com/Advanced-Lighting/Gamma-Correction
