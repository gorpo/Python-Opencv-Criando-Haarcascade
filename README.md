
[![Build](https://img.shields.io/badge/dev-gorpo-brightgreen.svg)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/python-v3.7-blue.svg)]()
[![Build](https://img.shields.io/badge/windows-7%208%2010-blue.svg)]()
[![Build](https://img.shields.io/badge/Linux-Ubuntu%20Debian-orange.svg)]()
[![Build](https://img.shields.io/badge/arquiterura-64bits-blue.svg)]()<br>
  <h6 align="center">
   <img src="https://raw.githubusercontent.com/gorpo/Manicomio-Boot-Theme/master/manicomio/boot.png" width="55%"></img>
       <h2 align="center">Manicomio | OpenCV Python | Criando Haarcascade</h2>
  </h6>
  
  
  <p>Este material faz parte do tutorial Reconhecimento de Imagem | OpenCV Python do Zero | Criando Haarcascade postado no youtube para conhecimento do OpenCV do zero e criação de Haarcascades através de GUI. Abaixo disponibilizo outras fontes de estudo para criar Haarcascades de forma didatica.<br>
<a href="https://youtu.be/lAHMmsInBRI">Link para o tutorial</a><br></p>


<img src="https://raw.githubusercontent.com/gorpo/Python-Opencv-Criando-Haarcascade/master/images/banner.jpg" width="100%">

<h3> Programa de manipulação de imagens com OpenCV e Pillow e criação de Haarcascade.</h3>

<img src="https://raw.githubusercontent.com/gorpo/Python-Opencv-Criando-Haarcascade/master/images/example.jpg" width="100%"></img>




# Executando:
<p>- Importante:
- Datasets de imagens se comportam melhor na escala de cinza<br>
- Tente não usar imagens grandes.<br>
- Quanto mais imagens em seu dataset melhor sera o resultado de seu haarcascade.<br>
- Quanto maior a quantidade de vezes treinado("Number of Stages") melhor será o resultado, o aconselhavél é 30x.<br>
- Se tiver 8gb RAM ou mais mude as configurações de memoria para agilizar o processo.<br>
- Feche todo programa que consuma GPU durante a crição do haarcascade, afinal muitas imagens estão sendo processadas.<br>
- Feche todos programas pois seu processador vai suar.<br>
- Sim este sistema roda sem GPU porém é muitissimo mais lento.<br>
- Sim você pode adaptar este script para reconhecimento com camera, mas o processamento vai ficar mais lento ainda.<br>  
- Em breve tutorial de como fazer os reconhecimentos com a camera ou podem usar a base deste git para ver como usei a camera: <a href="https://github.com/gorpo/OpenCV-Thug-Life-Python">Veja como usar a camera</a>.<br>  
- Feche todos programas pois seu processador vai suar.<br>
- Tente manter no minimo 100 imagens na pasta de imagens positivas e negativas.<br>
- Quanto mais imagens inseridas nestas pastas melhor.<br>   
  </p><br>

  
# Requisitos:
- Python3.7 (não testado em outros)
- OpenCV
- Numpy
- Pyllow
- Haarcascade GUI (somente .exe, usa um wine no linux ai que vai)
- Opcional: Fatkun for Chrome

# Instalações previas das libs que cumprem os requisitos:
--> Pillow<br>
<code>pip install Pillow==6.1</code>
--> OpenCV<br>
<code>pip install opencv-python</code>
--> Numpy<br>
<code>pip install numpy</code>
--> Haarcascade GUI Creator<br>
<a href="https://amin-ahmadi.com/downloadfiles/cascadetrainergui/CascadeTrainerGUI_3.3.1_x64_Setup.exe">Cascade Trainer GUI 64Bits<a><br>
  <a href="https://amin-ahmadi.com/downloadfiles/cascadetrainergui/CascadeTrainerGUI_3.3.1_x86_Setup.exe">Cascade Trainer GUI 32Bits<a><br>
--> Opcional FatKun for Crome<br>
<a href="https://amin-ahmadi.com/downloadfiles/cascadetrainergui/CascadeTrainerGUI_3.3.1_x64_Setup.exe">FatKun Download<a><br>    
    
# Executando:
<p> Para criar nossos Haarcascades precisamos:
- Criar dentro da pasta do projeto uma pasta nomeada "p" para receber as imagens positivas<br>
- Criar dentro da pasta do projeto uma pasta nomeada "n" para receber as imagens negativas<br>
- Abrimos o programa Haarcasdade GUI  e indicamos o caminho da pasta do projeto que contem as duas pastas.<br>
- Setamos na aba "Common" o numero de vezes que ele vai passar em "Number of Stages".<br>
- Mudamos as propriedades de memoria caso nosso pc suporte.<br>
- Iniciamos o programa em "start" e após concluido nosso arquivo estará pronto dentro da pasta "classifier".</p><br>

  
# Links de estudo sem a GUI e uso via terminal ou cmd:
<a href="https://www.cs.auckland.ac.nz/~m.rezaei/Tutorials/Creating_a_Cascade_of_Haar-Like_Classifiers_Step_by_Step.pdf">Creating a Cascade of Haar-Like Classifiers: Step by Step<a><br>
<a href="https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/">Creating your own Haar Cascade OpenCV Python Tutorial<a><br>
<a href="http://amin-ahmadi.com/cascade-trainer-gui/">Cascade Trainer GUI<a><br>


