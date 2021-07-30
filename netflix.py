from io import open
import pickle

class Pelicula:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)
        
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    
    peliculas = []
    
    # Constructor de clase
    def __init__(self):
        self.cargar()
        
        
    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()
        
    def mostrar(self):
        if len(self.peliculas)==0:
            print("el catalogo esta vacio ")
            return
        for p in self.peliculas:
            print(p)
    
    def cargar(self):
        #nombre del fichero fich
        fich=open('catalogo.pckl','ab+')#append binario con funciones de lectura
        fich.seek(0)
        try:
            self.peliculas=pickle.load(fich)
        except:
            print("el fichero esta vacio ")
        finally:   
            fich.close()
            del(fich) 
            print("se han cargado{} tantas pelicula".format(len(self.peliculas)))    
    def guardar(self):
        fich=open('catalogo.pckl','wb')
        pickle.dump(self.peliculas,fich)
        fich.close()
        del(fich)
       
    
    #destructor de  clase
    def __del__(self):

        self.guardar()#guardado automaticamente
        print("se ha  guardado el fichero ")
c=Catalogo()
c.agregar(Pelicula("daniluss 2",305,2001))
c.agregar(Pelicula("pueba",100,20))
