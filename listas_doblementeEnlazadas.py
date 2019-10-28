class NodoDoble():
    def __init__(self,dato):
    self.dato = dato
    self.siguiente = None
    self.anterior = None

class listasDoblementeEnlazadas():

    def __init__ (self):
        self.size = 0
        self.primero= None
        self.ultimo= None
        
    def get_size(self):
        return self.size
        
    def is_empty(self):
        return self.primero == None

    def insert( self ,value ): 
        if self.vacia():
            self.primero = self.ultimo = NodoDoble(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoDoble(dato)
            self.ultimo.anterior = aux
        self.size += 1
            
    def find_from_tail(self, value ):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False
        
    def find_from_head(self, value ):
        aux = self.ultimo
        while aux:
            if aux.dato == dato:
                return True
            else:
                aux = aux.anterior
                if aux == self.ultimo:
                    return False
    
    def remove_from_head(self):
        if self.vacia():
            print ("Esta vacia")
        elif self.primero.siguiente == None:
            self.primero=self.ultimo=None
            self.size=0
        else:
            self.primero=self.primero.siguiente
            self.primero.anterior = None
            self.size -=1
            
    def remove_from_tail( value ):
        if self.vacia():
            print ("Esta vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -=1
    
    def insert_between(  value , predecesor ,sucesor):
        if self.size == 0:
            nuevo = NodoDoble(value, self.ultimo, self.primero)
            self.primero.siguiente=nuevo
            self.ultimo.anterior=nuevo
        else:
            nuevo = NodoDoble(value, self.ultimo, self.ultimo.anterior)
            self.ultimo.anterior.siguiente=nuevo
            self.ultimo.anterior=nuevo
        self.size += 1
            
    def transversal(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux=aux.siguiente
        
    def reverse_transversal(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux=aux.anterior
