#!/usr/bin/env python
# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020
import numpy as np
import cv2

#chama o classificador xml haarcascade
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#chama a imagem
imagem = cv2.imread('images/1.jpg')
#cinza -porque o opencv, reconhece melhor escalas de cinza
cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

#aplica o classificador na nossa imagem EM CINZA - scaleFactor=1.08, minNeighbors=vizinhos 1-9
faces = cascade.detectMultiScale(cinza, scaleFactor=1.08, minNeighbors=4)

#loop para criar os quadrados de reconhecimento
for(x, y, w, h) in faces:
    dectada = cv2.rectangle(imagem, (x, y), (x + w, y + h), (255,0,0), 2)



#final do codigo
cv2.imshow('Manicomio', imagem)
cv2.waitKey()
cv2.destroyAllWindows()