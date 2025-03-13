import pyautogui as pa
import os
from datetime import datetime
from time import sleep

def caminho_pasta():
    if not os.path.exists('path_img.txt'):
        with open('path_img.txt', 'w'):
            pass
    with open ('path_img.txt','r') as a:
        conteudo = a.read().strip()
        if conteudo == '':
            path = str(input('Cole o caminho da pasta IMG: ')).replace('"','')
            with open ('path_img.txt','w') as a:
                a.write(path)
            return path
        else:
            return conteudo

def tab(i):
    for _ in range(i):
        pa.press('tab')
        sleep(0.1)

def verificar_marca_vazia(img,id_marca):
    nome = encontrar_marca(id_marca)
    try:
        pa.locateOnScreen(img)
    except:
        print(f'{id_marca+1}. {nome}: \033[32mSALVA\033[m')
        return False
    else:  
        print(f'{id_marca+1}. {nome}: \033[31mVAZIA\033[m')
        return True

def tela_aguarde(img):
    try:
        pa.locateOnScreen(img)
    except:
        return False
    else:
        return True
    
def encontrar_marca(id_marca):
    marcas = [
        "activitta", 
        "azaleia", 
        "beira rio", 
        "bertelli", 
        "bkarellus", 
        "cartago", 
        "charmosinha", 
        "coca cola", 
        "dplaka", 
        "di valentini", 
        "dijean", 
        "duramax", 
        "everlast", 
        "evva", 
        "floral", 
        "gibizinho", 
        "giovanna dias",
        "grendene kids", 
        "grendha", 
        "havaianas", 
        "improviso", 
        "ipanema", 
        "kenner", 
        "kleenex", 
        "kta lixo", 
        "la vie", 
        "mariota", 
        "maxx baby", 
        "mimmo", 
        "minimercado", 
        "mizuno", 
        "modare", 
        "moleca", 
        "molekinha", 
        "molekinho", 
        "mormaii", 
        "nc", 
        "neve", 
        "nino", 
        "olympikus", 
        "oxn", 
        "pega forte", 
        "penalty", 
        "rainha", 
        "rayon", 
        "replay", 
        "rider", 
        "scala", 
        "scott", 
        "softli",
        "sound", 
        "copos", 
        "descartaveis", 
        "umbro", 
        "under armour",
        "velluti", 
        "vellutinho", 
        "via marte", 
        "via scarpa", 
        "vizzano", 
        "yvate", 
        "zaxy"
    ]
    return marcas[id_marca].title()

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
        indice = int(input('[2] R Cruz\n[3] Matriz\nDigite qual o índice da empresa: '))
        if indice == 2:
            return 'R CRUZ'
        elif indice == 3:
            return 'MATRIZ'
        else:
            print('Opção inválida. Tente novamente.\n')

def locateAllOnScreen(img, Ldist=5, Tdist=5):
    list_img = list(pa.locateAllOnScreen(img))
    return list_img[0].left + Ldist, list_img[0].top + Tdist
