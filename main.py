import pyautogui as pa

from module import *
from time import sleep
pa.PAUSE = 0.1

telaVazia = './img/pag1-1.png'
aguarde = './img/aguarde.png'
down = 8
y = 390
empresa = ''
primeiro = 0

while True:
    indice = int(input('[2] R Cruz\n[3] Matriz\nDigite qual o indice da empresa: '))
    if indice == 2:
        empresa = 'R CRUZ'
        break 
    elif indice == 3:
        empresa = 'MATRIZ'
        break
    else:
        print('Opção inválida. Tente novamente.\n')

if indice == 2:
    empresa == 'R CRUZ'
else:
    empresa == 'MATRIZ'

caminhoPasta = criar_pasta(empresa)

sleep(3)

for i in range(0,62):
    pa.click(800,353) #Lista marcas
    if i < 56:
        for j in range(1,down):
            pa.press('down') #Tecla pra baixo até a proxima marca
        pa.click(788,375) #Marca na posição 1 da lista suspensa
        down += 1 #Soma 1 para a quantidade de cliques até a proxima marca
    else:
        for j in range(1,63):
            pa.press('down') #Tecla pra baixo até a ultima marca
        pa.click(788,y) #Vai seguir clicando em marcas da posição 2 em diante 
        y += 15.6 #Acrescenta 15 px para Y, assim irá selecionar a caixa de seleção da marca abaixo  
    pa.click(827,500) #Confirmar
    pa.click(1090,60) #Vizualizar
    sleep(1)

    while not tela_aguarde(aguarde): #Espera o pdf carregar
        sleep(0.1)
    
    sleep(1)
    if verificar_marca_vazia(telaVazia,i) == True: #Checa se pdf/marca tem produto
        pa.hotkey('alt','f4') #Se sim: fecha a pagina
    else: #Se não: salva o pdf
        sleep(1)
        pa.click(1085,95)
        pa.press('ENTER')
        sleep(1)
        if primeiro == 0: 
            sleep(1)
            tab(7)
            pa.press('ENTER')
            pa.write(caminhoPasta)
            sleep(1.2)
            pa.press('ENTER')
            sleep(1.2)
            primeiro = 1
            tab(7)
            sleep(1.2)
        pa.write(f'{encontrar_marca(i)} {empresa}')
        pa.press('ENTER')
        sleep(1.3)
        pa.press('right')
        pa.press('ENTER')
        sleep(1.5)
        pa.hotkey('alt','f4')
    sleep(1)

    pa.click(800,353) #Abre lista de marcas
    pa.click(788,375) #Marca a opção exibir todas
    pa.click(788,375) #Desmarca a opção exibir todas
    pa.click(827,500) #Clica no botão confirmar