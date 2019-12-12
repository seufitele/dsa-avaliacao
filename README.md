
<h1>Projeto de Cadeia de Markov</h1>

Trata-se de Projeto para Formação de Cientista de Dados da [Data Science Academy](https://www.datascienceacademy.com.br).

Projeto de Cadeia de Markov [(Markov Chain)](https://en.wikipedia.org/wiki/Markov_chain) para geração inteligente de texto de forma automatizada.
O caso de uso escolhido foi geração de texto a partir de fontes de piadas obtidas na internet (*one-liners*).

<h3>Por que Cadeia de Markov?</h3>

Embora a Cadeia de Markov fuja um pouco do Machine Learning 'tradicional', ele trata bastante da parte estatística e probabilidade condicional. É um assunto diferente e traz outra ferramenta para modelagem de modelos estocásticos.

Além disso, eu queria fazer algo um pouco diferente do que já foi apresentado, e tentei sair do lugar comum de implementar um Perceptron, por exemplo (nada contra isso, só queria algo diferente).

<h3>Para que serve a Cadeia de Markov?</h3>

A cadeia de Markov representa modelos de probabilidade condicional, onde se tenta prever o que está à frente baseando-se apenas no estado atual. No caso de geração de texto, isso significaria inferir a próxima palavra de uma sentença com base na palavra atual.


<h3>Por que esse tema específico?</h3>

Geração de texto (coerente) está bem próximo do que acreditamos ser uma parte da inteligência 'real'.
Já houve papers escritos de forma automatizada e que foram aceitos para publicação.
No reddit existe um subreddit onde apenas bots postam, comentam e interagem (https://www.reddit.com/r/SubredditSimulator/).

Achei interessante explorar o que se pode conseguir, especialmente com um conjunto de dados potencialmente restrito.
Escolhi pegar piadas porque texto gerado incoerente pode ser engraçado, mas utilizar piadas como fonte aumenta a chance de sair algo divertido.


<h3>Como usar?</h3>

Basta rodar o arquivo `nmarkovchain.py`. Será perguntado qual a ordem da Cadeia de Markov. O valor padrão é 0.
Valores maiores retornarão frases mais coesas, mas isso acabará repetindo as frases originais. Recomendo os valores 1 e 2.

<h3>Trabalho posterior</h3>

A eficácia de qualquer modelo está diretamente relacionada à quantidade de dados.
Obter mais dados é um excelente maneira de melhorar os resultados. Foi possível ver isso na prática com cada arquivo adicionado.

Um outro ponto interessante seria variar o Modelo de Markov para dar prioridade para estados com mais opções. 
Dessa forma seria possível aumentar os estados sem prejudicar a variabilidade das frases.


Segue abaixo fontes de inspiração e sites de onde obtive as piadas (através de webscraping):

https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71  
https://github.com/CrowdTruth/Short-Text-Corpus-For-Humor-Detection  
http://www.laughfactory.com/  
https://www.rd.com/jokes/one-liners  
https://onelinefun.com/  
