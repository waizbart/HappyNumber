# HappyNumber
Desafio P.S Futebol Omegabotz 2022

## Objetivo
O objetivo da aplicação é testar se o número inserido é um número feliz. 

Um número feliz é definido quando após uma sequência de somas o resultado final é igual a 1. Para isso são necessários o seguintes requisitos:

- O número inicial é positivo e inteiro
- Separar os números em digitos e somar todos os quadrados desses dígitos
- Repetir esse processo o quanto for necessário
- Quando o final do processo chegar em 1, esse número é feliz

Entrada: número inteiro positivo
Saída: verdadeiro ou falso

Exemplo:
Entrada: n = 19
Saída: VERDADEIRO

Explicação:
- 1² + 9² = 82
- 8² + 2² = 68
- 6² + 8² = 100
- 1² + 0² + 0² = 1


Entrada: n = 2
Saída: FALSO
