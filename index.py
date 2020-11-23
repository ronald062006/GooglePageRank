import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import operator

#creamos un grafo dirigido
graph=nx.gnp_random_graph(10,0.6,directed=True)

#dibujamos un grafo
nx.draw(graph,with_labels=True,font_color='black',font_size=10,node_color='red')

#trazar un gráfico
#plt.show()
plt.savefig('static/pics/nodos.png')

#numero de nodos
count=graph.number_of_nodes()
#grafos vecinos de un nodo
print(list(graph.neighbors(1)))

#Page Rank: cálculo de la puntuación de camino aleatoria

rank_dict={}
#tomamos un nodo aleatorio como nodo inicial
x=rd.randint(0,10)
for j in range(0,10):
  rank_dict[j]=0
rank_dict[x]=rank_dict[x]+1
for i in range(600000):
  list_n=list(graph.neighbors(x))
  if(len(list_n)==0):
    x=rd.randint(0,10)
    rank_dict[x]=rank_dict[x]+1
  else:
    x=rd.choice(list_n)
    rank_dict[x]=rank_dict[x]+1
  
print("Camino actualizado")

#normalizamos valores
for j in range(0,10):
  rank_dict[j]=rank_dict[j]/600000

#Page rank por biblioteca networkx
pagerank=nx.pagerank(graph)


#ordenar el rank_dict basado en valores
rank_dict_sorted=sorted(rank_dict.items(),key=lambda v:(v[1],v[0]),reverse=True)

rank_dict_sorted

#orenamos ambos diccionarios segun elementos
pagerank_sorted=sorted(pagerank.items(),key=lambda v:(v[1],v[0]),reverse=True)

pagerank_sorted

numeros={}
cont=0
print("El orden generado por nuestro algoritmo de implementación es \n")
for i in rank_dict_sorted:
  print(i[0],end=" ")
  numeros[cont] = i[0]
  cont=cont+1
print("\n \nEl orden generado por la biblioteca networkx es \n ")
for i in pagerank_sorted:
  print(i[0],end=" ")


from flask import Flask, render_template
import os
#from werkzeug import secure_filename #para subir los archivos al servidor}
picFolder = os.path.join('static','pics')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/imagen')
def imagen():
    pic1= os.path.join(app.config['UPLOAD_FOLDER'],'nodos.png')
    return render_template('imagen.html', user_image = pic1)

@app.route('/prueba')
def prueba():
  
  return render_template('prueba.html')

@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/terror')
def terror():
    numeros
    
    pelisTerror = ("SAW", "viernes 13", "dia de los muertos vivientes", "la casas del terror", "camino hacia el terror","la caceria", "Pet Sematary", "Midsomar", "Depredador","La niñera")
    return render_template('terror.html', pT=pelisTerror,num=numeros)

@app.route('/suspenso')
def suspenso():
    
    numeros
    pelisSuspenso = ("Parasitos", "Escape room", "escolta", "Perdida", "la llegada","Rogue", "el practicante  ", "Contratiempo", "Fragmentado","El hoyo")
    return render_template('suspenso.html', pS=pelisSuspenso, num= numeros)

@app.route('/accion')
def accion():
    
    numeros
    pic2= os.path.join(app.config['UPLOAD_FOLDER'],'nodos.png')
    pelisAccion = ("avengers", "Terminator", "Aves de presa", "Vennon", "spider-man","Rogue", "el practicante  ", "Contratiempo", "Fragmentado","El hoyo")
    return render_template('accion.html', pA= pelisAccion, num= numeros, img_user= pic2)

@app.route('/about')
def about():
    return render_template('about.html')

    

'''@app.route("/uploader", methods=['POST'])
def uploader():
  if request.method=="POST":
    f = request.files['archivo']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER', filename]))
    return "Archivo subido exitosamente"'''





if __name__=='__main__':
    app.run(debug=True)

