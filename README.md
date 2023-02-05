# URI_Ad_hoc
Exercises realized for the site URI Online Judge in Python3


### Observacoes:
---
#### Exercício 1032 - O Primo de Josephus:
- Minha idéia foi colocar uma lista de números primos, criados em computador, para serem usados na resposta do problema, já que este usa casos com número de participantes muito grandes! Escolhi cria a lista de primos apenas para a resposta ser encontrada mais rápida.

#### Exercício 1090 - Set:
- **O enunciado do problema não fala que é válido retirar as cartas da mesma coluna, mas em duas situações isso ocorre. Somente consegui resolver realizando esta operação**
- URI_1090 - Set_PrimeiraIdeia_nOK - não teve sucesso, foi uma versão muito simples do problema, apenas para reconhecimento
- URI_1090 - Set_IF_nOK - não houve sucesso, não pegava todos os casos possíveis
- URI_1090 - Set_Combinatoria_nOK - sem sucesso. Excedia os recursos da maquina, pois há casos em que havia mais de 20.000 cartas na mesa!
- URI_1090 - Set_Matriz_OK - sucesso ao encontrar as respostas, mas excedia no tempo limite de 2 segundos. Esta versão é a mais completa. Para estudo do problema e trabalhar com um arquivo contendo mais de 800.000 linhas!
- URI_1090 - Set_Submetido_OK - versão enxuta da opção anterior, porém sem sucesso. Excede o tempo limite
- 1090_valores - Casos de teste com mais de 800.000 linhas
- 1090_resposta - Resposta dos casos de teste acima
- 1090_valores_1 - Apenas um caso de teste. Para verificar com o arquivo URI_1090 - Set_Matriz_OK porque ocorre tal resposta
- 1090_testes - planilha XLSX para reprodução visual de como são os cálculos

#### Exercício 3172 - Dali e Dila:
- Acho que a resposta se baseia na brincadeira da Torre de Hanoi. Mas não avancei muito nisso. Minha idéia era algo mais simples, retirar os brinquedos das pilhas em ordem crescente. Trocando a vez somente quando acabavam os brinquedos de uma pilha e tinha q mudar para outra. Resposta: Wrong Answer!
