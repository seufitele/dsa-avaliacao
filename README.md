# dsa-avaliacao

Trata-se de Projeto para Formação de Cientista de Dados da Data Science Academy (https://www.datascienceacademy.com.br).

Projeto de Markov Chain (Cadeia de Markov) para geração 'inteligente' de texto de forma automatizada.
O caso de uso escolhido foi geração de texto a partir de fontes de piadas obitdas na internet (one-liners, como eles chamam).

Por que Cadeia de Markov?

Embora a Cadeia de Markov fuja um pouco do Machine Learning 'tradicional', ele trata bastante da parte estatística e probabilidade condicional. É um assunto diferente e traz outra ferramenta para modelagem de modelos estocásticos.

Além disso, eu queria fazer algo um pouco diferente do que já foi apresentado, e tentei sair do lugar comum de implementar um Perceptron, por exemplo (nada contra isso, só queria algo diferente).


Para que serve a Cadeia de Markov?

A cadeia de Markov representa modelos de probabilidade condicional, onde se tenta prever o que está à frente baseando-se apenas no estado atual. No caso de geração de texto, isso significaria inferir a próxima palavra de uma sentença com base na palavra atual.


Por que esse tema específico?

Geração de texto (coerente) está bem próximo do que acreditamos ser uma parte da inteligência 'real'.
Já houve papers escritos de forma automatizada e que foram aceitos para publicação.
No reddit existe um subreddit onde apenas bots postam, comentam e interagem (https://www.reddit.com/r/SubredditSimulator/).

Achei interessante explorar o que se pode conseguir, especialmente com um conjunto de dados potencialmente restrito.
Escolhi pegar piadas porque texto gerado incoerente pode ser engraçado, mas utilizar piadas como fonte aumenta a chance de sair algo divertido.


Como usar?

O arquivo nmarkovchain

Segue abaixo fontes de inspiração e sites de onde obtive as piadas (através de webscraping).

https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
https://github.com/CrowdTruth/Short-Text-Corpus-For-Humor-Detection
http://www.laughfactory.com/
https://www.rd.com/jokes/one-liners
https://onelinefun.com/
