import pyautogui as pa
from module import *
from time import sleep
pa.PAUSE = 0.1

telaVazia = os.path.abspath('./img/pag1-1.png')
aguarde = os.path.abspath('./img/aguarde.png')
btn_visualizar = os.path.abspath('./img/visualizar.png')
btn_confirmar = os.path.abspath('./img/visualizar.png')
box_select = os.path.abspath('./img/select.png')
gerar_pdfII = os.path.abspath('./img/gerar_pdf (2).png')
gerar_pdfIII = os.path.abspath('./img/gerar_pdf (3).png')
listar_marca = os.path.abspath('./img/listar_marca.png')
zaxy = os.path.abspath('./img/zaxy.png')
exibir_todos = os.path.abspath('./img/exibir_todos.png')

down = 8
empresa = ''
primeiro = True
box = 1

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
    gerar_pdf = gerar_pdfII
else:
    empresa == 'MATRIZ'
    gerar_pdf = gerar_pdfIII

caminhoPasta = criar_pasta(empresa)

sleep(3)

dropdown_marca = list(pa.locateAllOnScreen(listar_marca))

for value in dropdown_marca:
    left = value.left + 20
    top = value.top + 20

for i in range(0,63):
    pa.click(left,top) #Lista marcas
    if i < 56:
        for j in range(1,down):
            pa.press('down') #Tecla pra baixo até a proxima marca
        boxes_selects = list(pa.locateAllOnScreen(box_select))
        pa.click(boxes_selects[0])
        down += 1 #Soma 1 para a quantidade de cliques até a proxima marca
    else:
        for j in range(1,63):
            pa.press('down') #Tecla pra baixo até a ultima marca
        if i == 63: 
            pa.click(pa.locateOnScreen(zaxy))
        else: 
            boxes_selects = list(pa.locateAllOnScreen(box_select))
            pa.click(boxes_selects[box])
            box += 1  
    pa.click(pa.locateOnScreen(btn_confirmar)) #Confirmar
    pa.click(pa.locateOnScreen(btn_visualizar)) #Vizualizar
    pa.moveTo(820,40)

    while not tela_aguarde(aguarde): #Espera o pdf carregar
        sleep(0.1)
    
    sleep(1)
    if verificar_marca_vazia(telaVazia,i) == True: #Checa se pdf/marca tem produto
        pa.hotkey('alt','f4') #Se sim: fecha a pagina
    else: #Se não: salva o pdf
        sleep(1)
        pa.click(pa.locateOnScreen(gerar_pdf)) #Gerar o pdf 
        pa.press('ENTER')
        sleep(1)
        if primeiro == True: 
            sleep(1)
            tab(7)
            pa.press('ENTER')
            pa.write(caminhoPasta)
            sleep(1.2)
            pa.press('ENTER')
            sleep(1.2)
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

    pa.click(left,top) #Abre lista de marcas
    pa.moveTo(820,40)
    if primeiro == True:
        for value in list(pa.locateAllOnScreen(exibir_todos)):
            left_exibir_todos = value.left + 5
            top_exibir_todos = value.top + 5
        primeiro = False
    
    pa.click(left_exibir_todos, top_exibir_todos)  
    pa.click(left_exibir_todos, top_exibir_todos) 
    pa.click(pa.locateOnScreen(btn_confirmar))
    #pa.click(827,500) #Clica no botão confirmar