import pyautogui as pa
import os
from datetime import datetime
from time import sleep

def caminho_pasta():
    if not os.path.exists('database.txt'):
        with open('database.txt', 'w'):
            pass
    with open ('database.txt','r') as a:
        linhas = a.readlines()
        ultima_linha = linhas[-1] 
        if '\\img' not in ultima_linha:
            path = str(input('Cole o caminho da pasta IMG: ')).replace('"','')
            with open ('database.txt','a') as a:
                a.write(path)
            return path
        else:
            return ultima_linha

def tab(i):
    for _ in range(i):
        pa.press('tab')
        sleep(0.1)

def verificar_marca_vazia(img,id_marca):
    nome = encontrar_marca(id_marca)
    try:
        pa.locateOnScreen(img)
    except:
        print(f'{id_marca+1}. {nome.replace(" *","")}: \033[32mSALVA\033[m')
        return False
    else:  
        print(f'{id_marca+1}. {nome.replace(" *","")}: \033[31mVAZIA\033[m')
        return True

def tela_aguarde(img):
    try:
        pa.locateOnScreen(img)
    except:
        return False
    else:
        return True
    
def encontrar_marca(id_marca):
    with open ('database.txt','r') as a:
        linhas = a.readlines() 
        linhas.pop()
    return linhas[id_marca].title().strip()

def criar_pasta(empresa):
    nomePasta = f'Catalogos {empresa} {datetime.now().strftime("%d-%m-%Y")}'

    # Obter o caminho da pasta Downloads do usuário
    caminhoDownloads = os.path.join(os.path.expanduser("~"), "Downloads")

    # Criar o caminho completo para a nova pasta
    caminhoCompleto = os.path.join(caminhoDownloads, nomePasta)

    # Verificar se a pasta já existe e criá-la se não existir
    if not os.path.exists(caminhoCompleto):
        os.makedirs(caminhoCompleto)
        print(f"Pasta '{nomePasta}' criada em '{caminhoDownloads}' com sucesso!")
    else:
        print(f"A pasta '{nomePasta}' já existe em '{caminhoDownloads}'.")
    return caminhoCompleto

def selecionar_empresa():
    while True:
        indice = int(input('[1] Thales\n[2] R Cruz\n[3] Matriz\nDigite qual o índice da empresa: '))
        if indice == 2:
            return 'R CRUZ'
        elif indice == 3:
            return 'MATRIZ'
        elif indice == 1:
            return 'THALES'
        else:
            print('Opção inválida. Tente novamente.\n')

def locateAllOnScreen(img, Ldist=5, Tdist=5):
    list_img = list(pa.locateAllOnScreen(img))
    return list_img[0].left + Ldist, list_img[0].top + Tdist

def left_top_box(img, Ibox, acresT = 0):
    boxes_selects = list(pa.locateAllOnScreen(img))
    box = str(boxes_selects[Ibox]).split()
    left = int(''.join(filter(str.isdigit, box[0])))
    top = int(''.join(filter(str.isdigit, box[1]))) + acresT
    return left, top

def off_havaiana_mercado(i):
    nome = encontrar_marca(i)
    if '*' in encontrar_marca(i):
        print(f'{i+1}. {nome}: \033[33mPULADO\033[m')
        return True