#importa bibliotecas
import PySimpleGUI as sg
from time import sleep

def main():
    #define tema
    sg.theme('DarkTeal10')   

    #layout da interface
    layout = [  [sg.Text('NÚMERO FELIZ')],
                [sg.Text('Digite um número inteiro positivo para testar:'), sg.InputText(size=(9, 1))],
                [sg.Output(key='-OUTPUT-', size=(46, 1))],
                [sg.Button('Testar'), sg.Button('Limpar'), sg.Button('Cancelar')] ]

    # cria janela
    window = sg.Window('NÚMERO FELIZ \U0001F606', layout)

    # loop de eventos
    while True:
        event, values = window.read()
        
        if (values[0].isnumeric()):
            if (IsHappy(values[0]) == True):
                print(values[0], " é feliz! :)")

            else:
                print(values[0], "não é feliz! :(")

        else: 
            print("Erro: a entrada não é um número inteiro positivo!")
        
        if event == 'Limpar':
            window['-OUTPUT-'].update('')

        if event == sg.WIN_CLOSED or event == 'Cancelar': # se usuário fechar a janela ou clicar em cancelar
            break

    window.close()

def IsHappy(n):
    soma = set()
    while (n := sum(int(dig) ** 2 for dig in str(n))) != 1:
        if n in soma:
            return False
        soma.add(n)
    return True

main()