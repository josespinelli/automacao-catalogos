import pyautogui as pa
from module import *
from time import sleep
pa.PAUSE = 0.1

caminho_img = caminho_pasta()
with open('database.txt', 'r') as a:
    lenMarcas = len(a.readlines()) - 1

telaVazia = os.path.join(caminho_img, 'pag1-1.png')
btn_visualizar = os.path.join(caminho_img,'visualizar.png')
box_select = os.path.join(caminho_img, 'select.png')
gerar_pdf = os.path.join(caminho_img, 'gerar_pdf.png')
listar_marca = os.path.join(caminho_img, 'listar_marca.png')

down = 8
empresa = ''
primeiro = True
box = 1
img = ''
top = 0

empresa = selecionar_empresa()
caminhoPasta = criar_pasta(empresa)


try:
    sleep(3)
    img = 'listar_marca'
    left_marca, top_marca = locateAllOnScreen(listar_marca, 40, 20)

    for i in range(lenMarcas):
        nome_marca = encontrar_marca(i)
        if empresa == 'THALES':
            if '*' in nome_marca:
                print(f'{i+1}. {nome_marca}: \033[33mPULADO\033[m')
                down += 1
                continue
        pa.click(left_marca,top_marca) #Lista marcas
        sleep(0.2)
        if i < (lenMarcas - 8):
            for _ in range(1,down):
                pa.press('down') #Tecla pra baixo até a proxima marca
            if primeiro:
                img = 'select'
                left_prime_box, top_prime_box = left_top_box(box_select,0)
            pa.click(left_prime_box, top_prime_box)
            down += 1 #Soma 1 para a quantidade de cliques até a proxima marca
        else:
            for _ in range(lenMarcas):
                pa.press('down') #Tecla pra baixo até a ultima marca
            img = 'select'
            pa.click(left_prime_box, (top_prime_box + top))
            top += 15.5
            
            # if i == (lenMarcas - 1): 
            #     img = 'select'
            #     left_zaxy, top_zaxy = left_top_box(box_select,5,17.5)
            #     pa.click(left_zaxy, top_zaxy)
            # else: 
            #     boxes_selects = list(pa.locateAllOnScreen(box_select))
            #     pa.click(boxes_selects[box])
            #     box += 1  
        img = 'visualizar'
        pa.click(pa.locateOnScreen(btn_visualizar)) #Visualizar
        pa.moveTo(820,40)

        while not tela_aguarde(gerar_pdf): #Espera o pdf carregar
            sleep(0.2)
        
        sleep(1)
        img = 'pag1-1'
        if verificar_marca_vazia(telaVazia,i) == True: #Checa se pdf/marca tem produto
            pa.hotkey('alt','f4') #Se sim: fecha a pagina
        else: #Se não: salva o pdf
            sleep(1)
            img = 'gerar_pdf'
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
            pa.write(f'{nome_marca.replace(" *","")} {empresa}')
            pa.press('ENTER')
            sleep(2.5)
            pa.press('RIGHT')
            pa.press('ENTER')
            sleep(1.5)
            pa.hotkey('alt','f4')
        sleep(1)

        pa.click(left_marca,top_marca) #Abre lista de marcas
        pa.moveTo(820,40)
        
        pa.click(left_prime_box, top_prime_box)
        pa.click(left_prime_box, top_prime_box)  
        pa.click((left_marca-100), top_marca)

except FileNotFoundError:
    pa.hotkey('ALT','TAB')
    print('\n\033[31mERRO AO EXECUTAR SCRIPT, TENTE NOVAMENTE\033[m')
    print('-'*80)
    print(f'Erro: imagem "{img}.png" não encontrada')
    print('-'*80)
    print('Se o problema continuar, mande mensagem pro José Spinelli (91)988803703 (:')
    input('Pressione "ENTER" para fechar o prompt')
    sleep(1)

except Exception as e:
    if str(e) == '':
        e = 'DESCONHECIDO'
    pa.hotkey('ALT','TAB')
    print('\n\033[31mERRO AO EXECUTAR SCRIPT, TENTE NOVAMENTE\033[m')
    print('-'*80)
    if str(e) == 'Could not locate the image.':
        print(f'Erro: imagem "{img}.png" não encontrada')
    else:
        print(f'Erro: {e}')
    print('-'*80)
    print('Se o problema continuar, mande mensagem pro José Spinelli (91)988803703 (:')
    input('Pressione "ENTER" para fechar o prompt')
    sleep(1)

else:
    pa.hotkey('ALT','TAB')
    print('\n\033[32mSCRIPT EXECUTADO COM SUCESSO\033[m')
    input('Pressione "ENTER" para fechar o prompt')
    sleep(1)