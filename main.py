import pyautogui as pa
from module import *
from time import sleep
pa.PAUSE = 0.1

telaVazia = os.path.abspath('./img/pag1-1.png')
aguarde = os.path.abspath('./img/aguarde.png')
btn_visualizar = os.path.abspath('./img/visualizar.png')
btn_confirmar = os.path.abspath('./img/visualizar.png')
box_select = os.path.abspath('./img/select.png')
gerar_pdf = os.path.abspath('./img/gerar_pdf.png')
listar_marca = os.path.abspath('./img/listar_marca.png')
zaxy = os.path.abspath('./img/zaxy.png')
exibir_todos = os.path.abspath('./img/exibir_todos.png')

down = 8
empresa = ''
primeiro = True
box = 1

empresa = selecionar_empresa()
caminhoPasta = criar_pasta(empresa)

sleep(3)

left_marca, top_marca = locateAllOnScreen(listar_marca, 40, 20)

for i in range(62):
    pa.click(left_marca,top_marca) #Lista marcas
    if primeiro:
        left_ExTds, top_ExTds = locateAllOnScreen(exibir_todos)
        left_Confirm, top_Confirm = locateAllOnScreen(btn_confirmar)

    if i < 56:
        for _ in range(1,down):
            pa.press('down') #Tecla pra baixo até a proxima marca
        boxes_selects = list(pa.locateAllOnScreen(box_select))
        pa.click(boxes_selects[0])
        down += 1 #Soma 1 para a quantidade de cliques até a proxima marca
    else:
        for _ in range(62):
            pa.press('down') #Tecla pra baixo até a ultima marca
        if i == 61: 
            pa.click(pa.locateOnScreen(zaxy))
        else: 
            boxes_selects = list(pa.locateAllOnScreen(box_select))
            pa.click(boxes_selects[box])
            box += 1  
    pa.click(left_Confirm, top_Confirm) #Confirmar
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
        if primeiro: 
            sleep(1)
            tab(7)
            pa.press('ENTER')
            pa.write(caminhoPasta)
            sleep(1.2)
            pa.press('ENTER')
            sleep(1.2)
            tab(7)
            sleep(1.2)
            primeiro = False
        pa.write(f'{encontrar_marca(i)} {empresa}')
        pa.press('ENTER')
        sleep(1.3)
        pa.press('RIGHT')
        pa.press('ENTER')
        sleep(1.5)
        pa.hotkey('alt','f4')
    sleep(1)

    pa.click(left_marca,top_marca) #Abre lista de marcas
    pa.moveTo(820,40)
    
    pa.click(left_ExTds, top_ExTds)  
    pa.click(left_ExTds, top_ExTds)  
    pa.click(left_Confirm, top_Confirm) 