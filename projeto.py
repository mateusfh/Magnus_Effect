
import numpy as np
import math
import matplotlib.pyplot as plt


rho = 1.224 	    # Densidade do ar em Kg/m³
D = 22e-2 			# Diâmetro da bola em metros
r = D/2 			# Raio da bola
A = math.pi*r*r; 	# Área da bola
CM = 1; 			# Coeficiente de Magnus para bola
v = [65, 30, 20] 	# Velocidade linear definida com módulo de 74,3 Km/h
omega = [0, -20, 0] # Velocidade angular definida com modulo de 200 RPM

dkb = 'darkblue' #Definindo atalho para cor azul escuro
dkor = 'darkorange' #Definindo atalho para cor laranja escuro

for_Magnus= 0.5*CM*rho*A*r*np.cross(omega,v) #Equação para a força de Magnus
fr= math.sqrt(math.pow(for_Magnus[0],2) \
+ math.pow(for_Magnus[1],2) \
+ math.pow(for_Magnus[2],2) ) #Cálculo da Força Resultante

#Os códigos abaixo irão exibir as forças Fx, Fy, Fz e Fr com 3 casas decimais, simultaneamente
print("O valor da força de Magnus no eixo X = ", "{:.3f}".format(for_Magnus[0]),"N") 
#print("O valor da força de Magnus no eixo X = ", for_Magnus[0],"N")
print("O valor da força de Magnus no eixo Y = ", "{:.3f}".format(for_Magnus[1]),"N") 
print("O valor da força de Magnus no eixo Z = ", "{:.3f}".format(for_Magnus[2]),"N") 
print("O valor da força resultante de Magnus = ", "{:.3f}".format(fr),"N") 


fig = plt.figure()
ax = plt.axes(projection="3d") #Comando que seleciona uma projeção 3D da figura
#ax.set_xlim3d(1,-3) #Escala do eixo X
#ax.set_ylim3d(-1,round(1)) #Escala do eixo y
#ax.set_zlim3d(-0,4) #Escala do eixo z

ax.set_xlim([1,-3])
ax.set_ylim([-1,1])
ax.set_zlim([-0,4])

x= [0, 0, 0] # Vetor para definir o início dos vetores

ax.plot3D([x[0]],[x[1]],[x[2]], 'ok') #Cria a esfera localizada na origem do gráfico
ax.text3D(x[0]-0.3,x[1]-0.3,x[2],'o',color='k') #Identificador do vetor Fx com a cor vermelha

# Vetor da força de magnus no eixo X
ax.quiver(x[0], x[1], x[2],for_Magnus[0], 0, 0, color='r') #Imagem do vetor Fx na cor vermelha
ax.text3D(for_Magnus[0],x[1]-0.3,x[2],\
'Fx',color='r') #Identificador do vetor Fx com a cor vermelha

# Vetor da força de magnus no eixo Y
ax.quiver(x[0],x[1],x[2],0,for_Magnus[1],0,color='lime') #Imagem do vetor Fy na cor verde limão
ax.text3D(x[0]+0.3,for_Magnus[1]-0.3,x[2],'Fy',color='lime') #Identificador do vetor Fy com a cor verde limão

# Vetor da força de magnus no eixo Z
ax.quiver(x[0],x[1],x[2],0,0,for_Magnus[2],color=dkor) #Imagem do vetor Fz na cor laranja escuro
ax.text3D(x[0]+0.5,x[1],for_Magnus[2],'Fz',color=dkor) #Identificador do vetor Fz com a cor laranja escuro

# Vetor resultante da força de magnus
ax.quiver(x[0],x[1],x[2],for_Magnus[0],for_Magnus[1],for_Magnus[2],color=dkb) #Imagem do vetor Fr na cor azul escuro
ax.text3D(for_Magnus[0]-0.3,for_Magnus[1],for_Magnus[2],'Fr',color=dkb) #Identificador do vetor Fr na cor azul escuro

plt.show()