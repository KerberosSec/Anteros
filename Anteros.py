#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Inspiration: Seeker Project

"""
Developer: Diego333-ms
GitHub: https://github.com/Diego333-ms
Group: Kerberos Sec
Version: 1.6
"""
import os #Módulo de Comandos do Sistema
import sys #Módulo de Recursos Sistemáticos
import argparse #Módulo de linhas de comandos diretos
import requests #Módulo que faz a Conexão com a API dos Encurtadores
import time #Módulo de funções para gerenciar delay e tempo
import os.path #Módulo de Busca por Arquivos
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
                print (R + "[" + W + "-" + R + "]" + W + pkg + " não foi instalado.")
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
   print ("\n" + G + "[" + W + "04" + G + "]" + C + " Sair do Programa")
   option = str(input("\n" + W + "Anteros " + W + "> " + G))
   if (option == "01" or option == "1"): #Se a opção Datilografada for igual a 1 ou 01, redirecione para isgd()
     isgd()
   elif (option == "02" or option == "2"): #Se a opção Datilografada for igual a 2 ou 02, redirecione para tinyurl()
     tinyurl()
   elif (option == "03" or option == "3"): #Se a opção Datilografada for igual a 3 ou 03, redirecione para iptracker()
     iptracker()
   elif (option == "04" or option == "4"): #Se a opção Datilografada for igual a 4 ou 04, faça isso
     stop()
   else: #Se nenhuma das condições forem atingidas, Retorne ao Menu novamente
     print ("\n" + R + "[" + W + "-" + R + "]" + W + " Opção Inválida")
     time.sleep (2.5)
     __init__()
     menu()

def isgd(): #Definir opções do Programa
  print ("\n" + G + "[" + W + "01" + G + "]" + C + " Encurtar URL")
  print ("\n" + G + "[" + W + "02" + G + "]" + C + " Modificar URL")
  print ("\n" + G + "[" + W + "99" + G + "]" + C + " Voltar ao Menu")
  option = str(input("\n" + W + "Anteros " + "(" + R + "is.gd" + W + ")" + W + " > " + G))
  if (option == "01" or option == "1"): #Se a opção for 1 ou 01, será redirecionado para a abstração isgd_encurtar()
     isgd_encurtar()
  elif (option == "02" or option == "2"): #Se a opção for 2 ou 02, será redirecionado para a abstração isgd_modificar()
     isgd_modificar()
  elif (option == "99"):
     __init__()
     menu()
  else: #No caso de uma resposta alternativa fora dos parâmetros 1 e 2 acima, será redirecionado para datilografar novamente
     print ("\n" + R + "[" + W + "-" + R + "]" + W + " Opção Inválida")
     time.sleep (2.5)
     __init__()
     isgd()

def isgd_encurtar(): #Encurtar URL ou Link
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite a URL do Site:")
    url = str(input("\n" + W + "Anteros " + "(" + R + "is.gd" + W + ")" + W + " > " + G))
    try:
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Encurtando a URL %s..." %url)
       time.sleep(2)
       verificar_url(url)
    except requests.exceptions.MissingSchema:
       DIT = str(input("\n" + R + "[" + W + "-" + R + "]" + C + " A URL %s é Inválida. Voce quis dizer https://%s Y|n?: " %(url,url)))
       if (DIT == "Y" or DIT == "y" or DIT == "Yes" or DIT == "YES" or DIT == "yes"):
         url = "https://" + url
         verificar_url(url)
       else:
         time.sleep(2.5)
         __init__()
         isgd_encurtar()

def verificar_url(url): #Verificar a Existência e Comunicação com a URL
    server = requests.get(url)
    if (server.status_code == 200): #Se a resposta da Requisição for 200, indicando que o site ou serviço existe, passará para a próxima abstração
         encurtar_isgd1(url,server)
    else: #Se a Requisição resultar no status 400, indicando Erro, o código retornará
         print ("\n" + R + "[" + W + "-" + R + "]" + W + " a URL %s está inativa!" %url)
         time.sleep(2)
         __init__()
         isgd_encurtar()

def encurtar_isgd1(url,server): #Encurtamento da URL via API
    server = requests.post("https://is.gd/create.php?format=simple&url=%s" %url)
    if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
      print ("\n" + G + "[" + W + "+" + G + "]" + C + " URL Encurtada: " + W + "%s" %server.text)
      retorno()
    else: #Se não for sucedido, retornará Erro e retornará ao programa
      print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
      time.sleep(2)
      __init__()
      isgd_encurtar()

def isgd_modificar(): #Datilografia da URL ou Link
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite a URL do site:")
    url = str(input("\n" + W + "Anteros " + "(" + R + "is.gd" + W + ")" + W + " > " + G))
    try:
       time.sleep(2)
       verificar_url2(url)
    except requests.exceptions.MissingSchema:
       DIT = str(input("\n" + R + "[" + W + "-" + R + "]" + C + " A URL %s é Inválida. Voce quis dizer https://%s Y|n?: " %(url,url)))
       if (DIT == "Y" or DIT == "y" or DIT == "Yes" or DIT == "YES" or DIT == "yes"):
         url = "https://" + url
         verificar_url2(url)
       else:
         time.sleep(2.5)
         __init__()
         isgd_modificar()

def verificar_url2(url): #Verificar a Existência e Comunicação com a URL
    server = requests.get(url)
    if (server.status_code == 200):
       encurtar_isgd2(url,server)
    else:
       print ("\n" + R + "[" + W + "-" + R + "]" + W + " a URL %s está inativa!" %url)
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
       retorno()
    else:
       print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi Possível Modificar a URL %s. Verifique se utilizou números e caracteres especiais para Modificar corretamente" %url)
       time.sleep(4)
       __init__()
       encurtar_isgd2(url,server)

def tinyurl(): #Encurtamento usando o Tinyurl
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite a URL do Site:")
    url = str(input("\n" + W + "Anteros " + "(" + R + "tinyurl" + W + ")" + W + " > " + G))
    try:
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Encurtando a URL %s..." %url)
       time.sleep(2)
       verificar_url3(url)
    except requests.exceptions.MissingSchema:
       DIT = str(input("\n" + R + "[" + W + "-" + R + "]" + C + " A URL %s é Inválida. Voce quis dizer https://%s Y|n?: " %(url,url)))
       if (DIT == "Y" or DIT == "y" or DIT == "Yes" or DIT == "YES" or DIT == "yes"):
         url = "https://" + url
         verificar_url3(url)
       else:
         time.sleep(2.5)
         __init__()
         tinyurl()

def verificar_url3(url): #Verificar URL
    server = requests.get(url)
    if (server.status_code == 200):
      encurtar_tinyurl(url,server)
    else:
      print ("\n" + R + "[" + W + "-" + R + "]" + W + " a URL %s está inativa!" %url)
      time.sleep(2)
      __init__()
      tinyurl()

def encurtar_tinyurl(url,server): #Encurtamento via API
    server = requests.post("http://tinyurl.com/api-create.php?url=%s" %url)
    if (server.status_code == 200):
      print ("\n" + G + "[" + W + "+" + G + "]" + C + " URL Encurtada: " + W + "%s" %server.text)
      retorno()
    else:
      print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível encurtar a URL %s" %url)
      time.sleep(2)
      __init__()
      tinyurl()

def iptracker():
    __init__()
    verificar_arquivo = os.path.exists("log.txt")
    if (verificar_arquivo == True):
        print ("\n" + G + "[" + W + "+" + G + "]" + C + " Deseja usar a Key Salva? Y/n:")
        choices = str(input("\n" + W + "Anteros " + "(" + R + "IPtrack" + W + ")" + " > " + G))
        if (choices == "Y" or choices == "y" or choices == "yes"):
          iptracker_use()
        else:
          iptracker_not_log()
    else:
        iptracker_not_log()

def iptracker_not_log():
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Acesse o Site:" + R + " https://www.ipinfodb.com/register" + C + " e crie uma conta. Em seguida copie a Key de acesso")
    time.sleep(1.5)
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite a Key da sua Conta:")
    api_key = str(input("\n" + W + "Anteros " + "(" + R + "IPtrack" + W + ")" + " > " + G))
    os.system("touch log.txt")
    file = open("log.txt","w")
    file.write(api_key)
    file.close()
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite o Endereço IP Público do Alvo:")
    iptarget = str(input("\n" + W + "Anteros " + "(" + R + "IPtrack" + W + ")" + " > " + G))
    print ("\n" + G + "[" + W + "+" + G + "]" + C + " Rastreando Endereço IP %s..." %iptarget)
    time.sleep(2)
    iptarget_results(api_key,iptarget)

def iptarget_results(api_key,iptarget):
    __init__()
    server = requests.post("http://api.ipinfodb.com/v3/ip-city/?key=%s&ip=%s" %(api_key,iptarget))
    iptarget_track = "OK" in server.text
    if (iptarget_track == True):
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Dados do Endereço IP: " + G + "%s" %iptarget)
       time.sleep(1.2)
       country = server.text[23:-51]
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " País: " + G + "%s" %country)
       state = server.text[30:-45]
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Estado: " + G + "%s" %state)
       city = server.text[36:-35]
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Cidade: " + G + "%s" %city)
       latitude = server.text[56:-16]
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Latitude: " + G + "%s" %latitude)
       longitude = server.text[65:-7]
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Longitude: " + G + "%s" %longitude)
       time.sleep(1.5)
       retorno()
    else:
       print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Localizar o Endereço IP: %s" %iptarget)
       time.sleep(2.5)
       iptracker()

def iptracker_use():
      print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite o Endereço IP Público do Alvo:")
      iptarget = str(input("\n" + W + "Anteros " + "(" + R + "IPtrack" + W + ")" + " > " + G))
      print ("\n" + G + "[" + W + "+" + G + "]" + C + " Rastreando Endereço IP %s..." %iptarget)
      time.sleep(2)
      iptarget_results2(iptarget)

def iptarget_results2(iptarget):
    api_key = open("log.txt","r")
    api_key = api_key.readline()
    __init__()
    server = requests.post("http://api.ipinfodb.com/v3/ip-city/?key=%s&ip=%s" %(api_key,iptarget))
    iptarget_track = "OK" in server.text
    if (iptarget_track == True):
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Dados do Endereço IP: " + G + "%s" %iptarget)
       time.sleep(1.2)
       country = server.text[23:-51]
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " País: " + G + "%s" %country)
       state = server.text[30:-45]
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Estado: " + G + "%s" %state)
       city = server.text[36:-35]
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Cidade: " + G + "%s" %city)
       latitude = server.text[56:-16]
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Latitude: " + G + "%s" %latitude)
       longitude = server.text[65:-7]
       print ("\n" + G + "[" + W + "+" + G + "]" + C + " Longitude: " + G + "%s" %longitude)
       time.sleep(1.5)
       retorno()
    else:
       print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Localizar o Endereço IP: %s" %iptarget)
       time.sleep(2.5)
       iptracker()

def stop():
    sys.exit(1)

def retorno():
    time.sleep(3)
    print  ("\n" + G + "[" + W + "+" + G + "]" + C + " Deseja Escolher outra opção? " + W + "Y/n:")
    choice = str(input("\n" + W + "Anteros" + W + " > " + G))
    if (choice == "Sim" or choice == "sim" or choice == "yes" or choice == "Yes" or choice == "Y" or choice == "y"):
        __init__()
        menu()
    else:
        stop()
try:
 dependencies()
 menu()

except KeyboardInterrupt:
 stop()

finally:
 print ("\n" + G + "[" + W + "+" + G + "]" + C + " Obrigado Por Utilizar o Programa" + W)

