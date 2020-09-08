#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Inspiration: Seeker Project

"""
Developer: Diego333-ms
GitHub: https://github.com/Diego333-ms
Group: Kerberos Sec
Version: 1.0
"""
import os #Módulo de Comandos do Sistema
import requests #Módulo que faz a Conexão com a API dos Encurtadores
import time #Módulo de funções para gerenciar delay e tempo
from shutil import which #Módulo para Verificar Requisitos do Programa

#Cores Utilizadas no Programa/Algoritmo
R = '\033[31m' # Vermelho
G = '\033[32m' # Verde
C = '\033[36m' # Ciano
W = '\033[0m'  # Branco

def dependencies(): #Abstração que verifica Requisitos #{
  print (G + "[" + W + "+" + G + "]" + C + " Verificando Dependências..." + W)
  time.sleep(1)
  print (G + "[" + W + "+" + G + "]" + C + " Verificando Status dos Serviços...")
  server1 = requests.get("https://is.gd")
  server2 = requests.get("https://tinyurl.com")
  if (server1.status_code == 200 and server2.status_code == 200):
    print ("\n" + W + "[" + G + "ON" + W + "]" + C + " Servidores Ativos")
  else:
    print ("\n" + W + "[" + R + "OFF" + W + "]" + C + " Servidor não Ativo")
    stop()
  time.sleep(1.5)
  pkgs = ["python3", "bash", "curl"]
  inst = True
  for pkg in pkgs:
        present = which(pkg)
        if (present == None):
                print (R + "[-] " + W + pkg + R + ' não foi instalado.')
                inst = False
        else:
                pass
  if (inst == False):
        exit()
  else:
        __init__() #}

def __init__(): #Banner do Programa
   os.system("clear")
   print (G +
        r'''
   _____          __
  /  _  \   _____/  |_  ___________  ____  ______
 /  /_\  \ /    \   __\/ __ \_  __ \/  _ \/  ___/
/    |    \   |  \  | \  ___/|  | \(  <_> )___ \
\____|__  /___|  /__|  \___  >__|   \____/____  >
        \/     \/          \/                 \/  ''')
   print ("\t" + W + ".:. Diego333-ms .:.")

def menu(): #Menu do Programa
   print ("\n" + G + "[" + W + "+" + G + "]" + C + " Escolha uma das opções abaixo:")
   print ("\n" + G + "[" + W + "01" + G + "]" + C + " Encurtador is.gd")
   print ("\n" + G + "[" + W + "02" + G + "]" + C + " Encurtador tinyurl")
   print ("\n" + G + "[" + W + "03" + G + "]" + C + " Localizar Endereço IP")
   option = str(input("\n" + W + "Anteros " + W + "> " + G))
   if (option == "01" or option == "1"): #Se a opção Datilografada for igual a 1 ou 01, redirecione para isgd()
     isgd()
   elif (option == "02" or option == "2"): #Se a opção Datilografada for igual a 2 ou 02, redirecione para tinyurl()
     tinyurl()
   elif (option == "03" or option == "3"): #Se a opção Datilografada for igual a 3 ou 03, redirecione para iptracker()
     print ("\n" + R + "[" + W + "-" + R + "]" + R + " Em Breve")
   else: #Se nenhuma das condições forem atingidas, Retorne ao Menu novamente
     print ("\n" + R + "[" + W + "-" + R + "]" + R + " Opção Inválida")
     time.sleep (2.5)
     __init__()
     menu()

def isgd(): #Definir opções do Programa
  print ("\n" + G + "[" + W + "01" + G + "]" + C + " Encurtar URL")
  print ("\n" + G + "[" + W + "02" + G + "]" + C + " Modificar URL")
  option = str(input("\n" + W + "Anteros " + "(" + R + "is.gd" + W + ")" + W + " > " + G))
  if (option == "01" or option == "1"): #Se a opção for 1 ou 01, será redirecionado para a abstração isgd_encurtar()
     isgd_encurtar()
  elif (option == "02" or option == "2"): #Se a opção for 2 ou 02, será redirecionado para a abstração isgd_modificar()
     isgd_modificar()
  else: #No caso de uma resposta alternativa fora dos parâmetros 1 e 2 acima, será redirecionado para datilografar novamente
     print ("\n" + R + "[" + W + "-" + R + "]" + R + " Opção Inválida")
     time.sleep (2.5)
     __init__()
     isgd()

def isgd_encurtar(): #Encurtar URL ou Link
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite a URL do Site:")
    url = str(input("\n" + W + "Anteros " + "(" + R + "is.gd" + W + ")" + W + " > " + G))
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Encurtando a URL %s..." %url)
    time.sleep(2)
    verificar_url(url)

def verificar_url(url): #Verificar a Existência e Comunicação com a URL
    server = requests.get(url)
    if (server.status_code == 200): #Se a resposta da Requisição for 200, indicando que o site ou serviço existe, passará para a próxima abstração
       encurtar_isgd1(url,server)
    else: #Se a Requisição resultar no status 400, indicando Erro, o código retornará
       print ("\n" + R + "[" + W + "-" + R + "]" + R + " a URL %s está inativa!" %url)
       time.sleep(2)
       __init__()
       isgd_encurtar()

def encurtar_isgd1(url,server): #Encurtamento da URL via API
    server = requests.post("https://is.gd/create.php?format=simple&url=%s" %url)
    if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
      print ("\n" + G + "[" + W + "+" + G + "]" + C + " URL Encurtada: " + W + "%s" %server.text)
    else: #Se não for sucedido, retornará Erro e retornará ao programa
      print ("\n" + R + "[" + W + "-" + R + "]" + R + " Não foi possível Encurtar a URL %s" %url)
      time.sleep(2)
      __init__()
      isgd_encurtar()

def isgd_modificar(): #Datilografia da URL ou Link
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite a URL do site:")
    url = str(input("\n" + W + "Anteros " + "(" + R + "is.gd" + W + ")" + W + " > " + G))
    time.sleep(2)
    verificar_url2(url)

def verificar_url2(url): #Verificar a Existência e Comunicação com a URL
    server = requests.get(url)
    if (server.status_code == 200):
       encurtar_isgd2(url,server)
    else:
       print ("\n" + R + "[" + W + "-" + R + "]" + R + " a URL %s está inativa!" %url)
       time.sleep(2)
       __init__()
       isgd_modificar()

def encurtar_isgd2(url,server): #Encurtamento via API
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite a URL Modificada:")
    url_modificada = str(input("\n" + W + "Anteros " + "(" + R + "is.gd" + W + ")" + " > " + G))
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Criando URL Modificada %s..." %url_modificada)
    time.sleep(2)
    server = requests.post("https://is.gd/create.php?format=json&callback=myfunction&url=%s&shorturl=%s" %(url,url_modificada))
    url_modificada = "https:" in server.text
    if (url_modificada == True):
       url_modificada_isgd = server.text[26:-1]
       url_modificada_isgd_link = url_modificada_isgd.replace("})", "")
       url_modificada_isgd_link_user = url_modificada_isgd_link.replace('"', '')
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " URL Modificada: " + W + "%s" %url_modificada_isgd_link_user)
    else:
       print ("\n" + R + "[" + W + "-" + R + "]" + " Não foi Possível Modificar a URL %s. Verifique se utilizou números e caracteres especiais para Modificar corretamente" %url)
       time.sleep(4)
       __init__()
       encurtar_isgd2(url,server)

def tinyurl(): #Encurtamento usando o Tinyurl
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite a URL do Site:")
    url = str(input("\n" + W + "Anteros " + "(" + R + "tinyurl" + W + ")" + W + " > " + G))
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Encurtando a URL %s..." %url)
    time.sleep(2)
    verificar_url3(url)

def verificar_url3(url): #Verificar URL
    server = requests.get(url)
    if (server.status_code == 200):
      encurtar_tinyurl(url,server)
    else:
      print ("\n" + R + "[" + W + "-" + R + "]" + R + " a URL %s está inativa!" %url)
      time.sleep(2)
      __init__()
      tinyurl()

def encurtar_tinyurl(url,server): #Encurtamento via API
    server = requests.post("http://tinyurl.com/api-create.php?url=%s" %url)
    if (server.status == 200):
      print ("\n" + G + "[" + W + "+" + G + "]" + C + " URL Encurtada: " + W + "%s" %server.text)
    else:
      print ("\n" + R + "[" + W + "-" + R + "]" + R + " Não foi possível encurtar a URL %s" %url)
      time.sleep(2)
      __init__()
      tinyurl()

def iptracker():
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite o Endereço IP Público do Alvo:")
    iptarget = str(input("\n" + W + "Anteros " + "(" + R + "IPtrack" + W + ")" + " > " + G))
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Rastreando Endereço IP %s..." %iptarget)
    time.sleep(2)
    iptarget_results(iptarget)

def iptarget_results(iptarget):
    server = requests.post("http://www.ip-tracker.org/locator/ip-lookup.php?ip=%s" %iptarget)
    print (server.text)

def stop():
    os.system("exit 1;")

try:
 dependencies()
 menu()

except KeyboardInterrupt:
 stop()

finally:
 print ("\n" + G + "[" + W + "+" + G + "]" + C + " Obrigado Por Utilizar o Programa" + W)

