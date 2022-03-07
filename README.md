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

## Inicialização 
Instalação da biblioteca PySimpleGUI:
```
pip install pysimplegui
```

## Features
Para um visual mais intuitivo foi usada a biblioteca PySimpleGUI para criar uma interface gráfica:

![image](https://user-images.githubusercontent.com/63511690/157034079-f26b864d-9f50-4da2-a7eb-94699655a312.png)

Caso o usuário digite algo que não é um número, ou um número que não é um inteiro positivo o programa retorna um erro:

![image](https://user-images.githubusercontent.com/63511690/157034287-c1e0224e-40bd-4420-9f27-f4436554c361.png)

Para caso o número seja feliz ou não: 

![image](https://user-images.githubusercontent.com/63511690/157034471-2b0c937f-21a8-4201-ad5b-45221cfb4e39.png)
![image](https://user-images.githubusercontent.com/63511690/157034552-8abb28ea-86cb-42fb-acfc-8e1aa7385429.png)

O botão "Limpar" limpa a caixa de texto de output, e o botão cancelar fecha o programa

