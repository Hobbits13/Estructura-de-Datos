from nodo import Nodo
from listaSimple import ListaSimple
from listaDoble import ListaDoble
from listaDobleCircular import ListaDobleCircular
from pila import Pila
from cola import Cola 
from pilaEstatica import PilaEstatica
from colaCircular import ColaCircular
from colaDoble import ColaDoble
from colaER import ColaER
from colaSR import ColaSR
from colaPA import ColaPA
from colaPD import ColaPD
from listaCircular import ListaCircular




def mostrar_menu_principal():
    print("--------------------------------------------------------------------")
    print("Portafolio de Estructura de Datos")
    print("--------------------------------------------------------------------")
    print("1.- Listas")
    print("2.- Pilas")
    print("3.- Colas")
    print("0.- Salir")

def mostrar_submenu_listas():
    print("--------------------------------------------------------------------")
    print("1.- Lista Simple")
    print("2.- Lista Doble")
    print("3.- Lista Doble Circular")
    print("4.- Lista Simple Circular")
    print("5.- Regresar al menú principal")

def mostrar_submenu_pilas():
    print("--------------------------------------------------------------------")
    print("1.- Pila Dinámica.")
    print("2.- Pila Estática.")
    print("3.- Regresar al menú principal")

def mostrar_submenu_colas():
    print("--------------------------------------------------------------------")
    print("1.- Cola Simple")
    print("2.- Cola Doble")
    print("3.- Cola Circular")
    print("4.- Cola Entrada Restringida")
    print("5.- Cola Salida Restringida")
    print("6.- Cola Prioridad Ascendete")
    print("7.- Cola Prioridad Descendente")
    print("8.- Regresar al menú principal")

def submenu_lista_simple():
    lista = ListaSimple()  # Crear una nueva lista simple
    while True:
        print("\nMenu Lista Simple")
        print("--------------------------------------------------------------------")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar lista")
        print("4. Buscar elemento")
        print("5. Eliminar el último elemento")
        print("6. Regresar")
        print("0. Definición")

        opcion_ls = input("Seleccione una opción: ")

        if opcion_ls == "1":
            elemento = input("Ingrese el valor a agregar: ")
            lista.agregar(elemento)
            print("Elemento agregado.")

        elif opcion_ls == "2":
            elemento = input("Ingrese el valor a eliminar: ")
            eliminado = lista.eliminar(elemento)
            if eliminado:
                print("Elemento eliminado.")
            else:
                print("Elemento no encontrado.")

        elif opcion_ls == "3":
            print("Elementos de la lista:")
            lista.recorrer()

        elif opcion_ls == "4":
            elemento = input("Ingrese el valor a buscar: ")
            encontrado = lista.buscar(elemento)
            if encontrado:
                print("Elemento encontrado.")
            else:
                print("Elemento no encontrado.")

        elif opcion_ls == "5":
            eliminado = lista.eliminar_final()
            if eliminado:
                print("Último elemento eliminado.")
            else:
                print("Lista ya está vacía.")
        elif opcion_ls == "0":
            print('''La Lista Simple es una estructura de datos que organiza elementos de manera secuencial, 
             donde cada elemento está conectado únicamente al siguiente. Es fácil de implementar y 
             usar para colecciones de datos lineales.''')

        elif opcion_ls == "6":
            print("--------------------------------------------------------------")

            break
        else:
            print("Opción no válida.")

def sub_menu_lista_doble():
    lista = ListaDoble()
    while True:
        print("\nMenu Lista Doble")
        print("--------------------------------------------------------------------")
        print("1. Agregar elemento al final")
        print("2. Agregar elemento al inicio")
        print("3. Eliminar elemento del final")
        print("4. Eliminar elemento del inicio")
        print("5. Eliminar elemento")
        print("6. Mostrar lista desde el inicio")
        print("7. Mostrar lista desde el final")
        print("8. Buscar elemento")
        print("9. Regresar")
        print("0. Definición")

        opcion_ld = input("Seleccione una opción: ")

        if opcion_ld == "1":
            elemento = input("Ingrese el valor a agregar: ")
            lista.agregar_final(elemento)
            print("Elemento agregado.")

        elif opcion_ld == "2":
            elemento = input("Ingrese el valor a agregar: ")
            lista.agregar_inicio(elemento)
            print("Elemento agregado.")

        elif opcion_ld == "3":
            eliminado = lista.eliminar_final()
            if eliminado:
                print("Último elemento eliminado.")
            else:
                print("Lista ya está vacía.")


        elif opcion_ld == "4":
             eliminado=lista.eliminar_inicio()
             if eliminado:
                 print("Primer elemento eliminado")
             else:
                 print("La lista ya está vacía.")

        elif opcion_ld == "5":
            elemento = input("Ingrese el valor a eliminar: ")
            eliminado = lista.eliminar(elemento)
            if eliminado:
                print("Elemento eliminado.")
            else:
                print("Elemento no encontrado.")
                
        elif opcion_ld == "6":
            print("Elementos de la lista desde el inicio:")
            lista.recorrer_inicio()
            
        elif opcion_ld == "7":
            print("Elementos de la lista desde el final:")
            lista.recorrer_fin()
            
        elif opcion_ld == "8":
            elemento = input("Ingrese el valor a buscar: ")
            encontrado = lista.buscar(elemento)
            if encontrado:
                print("Elemento encontrado.")
            else:
                print("Elemento no encontrado.")
        elif opcion_ld == "0":
            print('''La Lista Doble es similar a la lista simple pero cada nodo tiene dos enlaces: uno hacia el 
             próximo nodo y otro hacia el anterior. Esto facilita recorrer la lista en ambas direcciones, 
             mejorando la flexibilidad para operaciones de inserción y eliminación.''')        
            
        elif opcion_ld == "9":
            print("--------------------------------------------------------------")

            break
        else:
            print("Opción no válida")
   
def submenu_listaDobleCircular():

    lista = ListaDobleCircular()
    while True:
        print("\nMenu Lista Doble Circular")
        print("--------------------------------------------------------------------")
        print("1. Agregar elemento al final")
        print("2. Agregar elemento al inicio")
        print("3. Eliminar elemento del final")
        print("4. Eliminar elemento del inicio")
        print("5. Eliminar elemento")
        print("6. Mostrar lista desde el inicio")
        print("7. Mostrar lista desde el final")
        print("8. Buscar elemento")
        print("9. Regresar")
        print("0. Definición")

        opcion_ldc = input("Seleccione una opción: ")

        if opcion_ldc == "1":
            elemento = input("Ingrese el valor a agregar: ")
            lista.agregar_final(elemento)
            print("Elemento agregado.")

        elif opcion_ldc == "2":
            elemento = input("Ingrese el valor a agregar: ")
            lista.agregar_inicio(elemento)
            print("Elemento agregado.")

        elif opcion_ldc == "3":
            eliminado = lista.eliminar_final()
            if eliminado:
                print("Elemento eliminado.")
            else:
                print("Lista ya está vacía.")


        elif opcion_ldc == "4":
            eliminado=lista.eliminar_inicio()
            if eliminado:
                print("Elemento eliminado.")
            else: 
                print("La lista ya está vacía")

        elif opcion_ldc == "5":
            elemento = input("Ingrese la posición del valor a eliminar: ")
            eliminado = lista.eliminar(elemento)
            if eliminado:
                print("Elemento eliminado.")
            else:
                print("Elemento no encontrado.")
                
        elif opcion_ldc == "6":
            print("Elementos de la lista desde el inicio:")
            lista.recorrer_inicio()
            
        elif opcion_ldc == "7":
            print("Elementos de la lista desde el final:")
            lista.recorrer_fin()
            
        elif opcion_ldc == "8":
            elemento = input("Ingrese el valor a buscar: ")
            encontrado = lista.buscar(elemento)
            if encontrado:
                print("Elemento encontrado.")
            else:
                print("Elemento no encontrado.")
        elif opcion_ldc == "0":
            print('''La Lista Doble Circular es una variante de las listas dobles en la que el último elemento está 
             conectado al primero, formando un círculo. Esto permite un recorrido continuo de la lista y mejora 
             la eficiencia de ciertas operaciones.''')        
            
        elif opcion_ldc == "9":
            print("--------------------------------------------------------------")

            break
        else:
            print("Opción no válida") 

def submenu_listaSimpleCircular():
    lista= ListaCircular()
    while True:
        print("\nMenu Lista Simple Circular")
        print("--------------------------------------------------------------------")
        print("1. Agregar elemento al final")
        print("2. Agregar elemento al inicio")
        print("3. Eliminar elemento del final")
        print("4. Eliminar elemento del inicio")
        print("5. Eliminar elemento")
        print("6. Mostrar lista desde el inicio")
        print("7. Mostrar lista desde el final")
        print("8. Buscar elemento")
        print("9. Regresar")
        print("0. Definición")

        opcion_lsc = input("Seleccione una opción: ")

        if opcion_lsc == "1":
            elemento = input("Ingrese el valor a agregar: ")
            lista.agregar_final(elemento)
            print("Elemento agregado.")

        elif opcion_lsc == "2":
            elemento = input("Ingrese el valor a agregar: ")
            lista.agregar_inicio(elemento)
            print("Elemento agregado.")

        elif opcion_lsc == "3":
            eliminado = lista.eliminar_final()
            if eliminado:
                print("Elemento eliminado.")
            else:
                print("Lista ya está vacía.")


        elif opcion_lsc == "4":
            eliminado=lista.eliminar_inicio()
            if eliminado:
                print("Elemento eliminado.")
            else: 
                print("La lista ya está vacía")

        elif opcion_lsc == "5":
            elemento = input("Ingrese la posición del valor a eliminar: ")
            
            if elemento.isdigit():
                posicion= int(elemento)
                eliminado = lista.eliminar(posicion)
                if eliminado:
                    print("Elemento eliminado.")
                else:
                    print("Elemento no encontrado.")
            else: print("Por favor, ingrese un número válido para la posicion")  
             
        elif opcion_lsc == "6":
            print("Elementos de la lista desde el inicio:")
            lista.recorrer_adelante()
            
        elif opcion_lsc == "7":
            print("Elementos de la lista desde el final:")
            lista.recorrer_atras()
            
        elif opcion_lsc == "8":
            elemento = input("Ingrese el valor a buscar: ")
            encontrado = lista.buscar(elemento)
            if encontrado:
                print("Elemento encontrado.")
            else:
                print("Elemento no encontrado.")
        elif opcion_lsc == "0":
            print('''La Lista Simple Circular es una lista en la que el último nodo está conectado al primero, 
             creando un bucle circular. Esto es útil para aplicaciones que necesitan un reciclaje continuo de 
             los datos.''')        
            
        elif opcion_lsc == "9":
            print("--------------------------------------------------------------")

            break
        else:
            print("Opción no válida") 
    
def submenu_pila():
    pilaD=Pila()
    while True:
        print("\nSubmemu Pila Dinámica")
        print("--------------------------------------------------------------------")  
        print("1. Apilar")
        print("2. Desapilar")
        print("3. Consultar")
        print("4. Obtener el tamaño de la pila")
        print("5. Verificar si la pila está vacía")
        print("6. Regresar")
        print("0. Definición")

        opcion_pd=(input("Ingrese una opción: "))
        
        if opcion_pd=="1":
            elemento=input("Ingrese el elemento a apilar: ")
            pilaD.apilar(elemento)
            print("Elemento agregado a la Pila.") 
        elif opcion_pd=="2":
            if not pilaD.esta_vacia():
                pilaD.desapilar()
                print("Elemento eliminado de la Pila.")
            else:
                print("La pila actual ya está vacía.")
        elif opcion_pd=="3":
            elemento=pilaD.consultar()
            if elemento is not None:
                print(f"El elemento en la cima es:", pilaD.consultar())
            else:
                print("La pila está vacía.")
                
        elif opcion_pd=="4":
            print("El tamaño de la Pila actual es: "+ str(pilaD.size()))
            
        elif opcion_pd=="5":
            if pilaD.esta_vacia():
                print("La pila está vacía.")
            else: 
                print("La pila no está vacía")
        
        elif opcion_pd == "0":
            print('''La Pila es una estructura de datos del tipo LIFO (Last In, First Out), donde el último elemento 
             añadido es el primero en ser retirado. Es ampliamente usada en situaciones que requieren una 
             gestión inversa temporal de los datos.''')
        elif opcion_pd=="6":
            print("--------------------------------------------------------------")
            break
        else:
            print("Opción no válida")       
                
def submenu_pilaE():
    pilae=PilaEstatica()
    while True:
        print("\nMenu Pila Estática con 5 espacios.") 
        print("--------------------------------------------------------------------") 
        print("1. Apilar")
        print("2. Desapilar")
        print("3. Consultar")
        print("4. Obtener el tamaño de la pila")
        print("5. Verificar si la pila está vacía")
        print("6. Regresar")
        print("0. Definición")

        opcion_pe=(input("Ingrese una opción: "))
        
        if opcion_pe=="1":
            
            elemento=input("Ingrese el elemento a apilar: ")
            pilae.apilar(elemento)
            print("Elemento agregado a la Pila.") 
            
        elif opcion_pe=="2":
            if not pilae.esta_vacia():
                pilae.desapilar()
                print("Elemento eliminado de la Pila.")
            else:
                print("La pila actual ya está vacía.")
        elif opcion_pe=="3":
            elemento=pilae.consultar()
            if elemento is not None:
                print(f"El elemento en la cima es:", pilae.consultar())
            else:
                print("La pila está vacía.")
                
        elif opcion_pe=="4":
            print("La capacidad de la pila es de 5 Elementos.")
            print("Y contiene "+ str(pilae.tamanio()) + " Elemento/s.")
            
        elif opcion_pe=="5":
            if pilae.esta_vacia():
                print("La pila está vacía.")
            else: 
                print("La pila no está vacía")
        elif opcion_pe == "0":
            print('''La Pila Estática es una pila con un tamaño fijo. Una vez que se llena, no se pueden añadir más 
             elementos a menos que se libere espacio. Esto puede limitar su uso pero garantiza un control sobre 
             el consumo de memoria.''')

        
        elif opcion_pe=="6":   
                print("--------------------------------------------------------------")
                break
        else: 
            print("Opción no válida")
 
def submenu_cola():
    cola_s= Cola()
    while True:
    
        print("\nMenu Cola")
        print("--------------------------------------------------------------------")
        print("1. Encolar")
        print("2. Desencolar")  
        print("3. Consultar")
        print("4. Verificar si la cola está vacía")
        print("5. Tamaño de la cola")
        print("6. Regresar")
        print("0. Definición")

        opcion_cola=input("Ingrese una opción: ")
        if opcion_cola == "1":
            elemento = input("Ingrese el elemento a encolar: ")
            cola_s.encolar(elemento)
            print("Elemento agregado a la cola")
        elif opcion_cola== "2":
                if not cola_s.esta_vacia():
                    cola_s.desencolar()
                    print("Elemento desencolado.")
                else:
                    print("La cola está vacía.")
        elif opcion_cola== "3":
            if cola_s.esta_vacia():
                print("La cola está vacía")
            else:
                print("El próximo valor de la cola en salir es: ", cola_s.consultar())
            
        elif opcion_cola == "4":
            if not cola_s.esta_vacia():
                print("La no cola está vacía.")  
            else:
                print("La cola está vacía") 
        elif opcion_cola == "5":
            print("El tamaño de la cola es: ", cola_s.size(), " Elemento/s")
        
        elif opcion_cola == "0":
            print('''La Cola es una estructura de datos del tipo FIFO (First In, First Out), donde el primer elemento 
             en ser añadido es el primero en ser retirado. Es ideal para procesos de planificación y gestión de 
             tareas en secuencia.''')
        elif opcion_cola== "6":   
                print("--------------------------------------------------------------")
                break
        else: 
            print("Opción no válida")    
            
def submenu_colaDoble():
    colaD=ColaDoble()

    while True:
        print("\nMenu Cola Doble")
        print("--------------------------------------------------------------------")
        print("1. Encolar al inicio: ")
        print("2. Encolar al final: ")  
        print("3. Desencolar del inicio")
        print("4. Desencolar del final")
        print("5. Verificar si la cola está vacía")
        print("6. Recorrer desde el inicio.")
        print("7. Recorrer desde el final.")
        print("8. Tamaño de la Cola.")
        print("9. Regresar")
        print("0. Definición")
    
        
        opcion_cd= input("Ingresa una opción: ")        
        if opcion_cd == "1":
            elemento=input("Ingrese el elemento a encolar: ")
            colaD.encolar_inicio(elemento)
            print("Elemento encolado al inicio.")
        elif opcion_cd == "2":
            elemento= input("Ingrese el elemento a encolar: ")
            colaD.encolar_final(elemento)
            print("Elemento encolado al final.")
        elif opcion_cd == "3":
            if not colaD.esta_vacia():
                colaD.desencolar_inicio()
                print("Elemento desencolado.")
            else: 
                print("La cola está vacía")
        elif opcion_cd == "4":
            if not colaD.esta_vacia():
                colaD.desencolar_final()
                print("Elemento desencolado")
            else:
                print("La cola está vacía.")
        elif opcion_cd== "5":
            if colaD.esta_vacia():
                print("La cola está vacía.")
            else:
                print("La cola no está vacía")
        elif opcion_cd == "6":
            colaD.recorrer_inicio()
        elif opcion_cd == "7": 
            colaD.recorrer_fin()
        elif opcion_cd == "8":
            print("El tamaño de la cola es de: ", colaD.size(), "Elementos.")
        elif opcion_cd == "0":
            print('''La Cola Doble permite inserciones y eliminaciones en ambos extremos. Combina las características 
             de una pila y una cola, haciéndola muy versátil para ciertos tipos de procesamientos de datos.''')

        
        elif opcion_cd=="9":   
                print("--------------------------------------------------------------")
                break
        else: 
            print("Opción no válida") 
                       
def submenu_colaCircular():
    colaC= ColaCircular()
    while True:
        print("Submenu de Cola Circular.")
        print("--------------------------------------------------------------------")
        print("1. Encolar un elemento al inicio.")
        print("2. Desencolar el primer elemento ingresado.")
        print("3. Consultar el próximo elemento a salir.")
        print("4. Verificar si la cola está vacía.")
        print("5. Recorrer desde el inicio.")
        print("6. Recorrer desde el final.")
        print("7. Elementos de la cola.")
        print("8. Regresar")
        print("0. Definición")

        opcion_colaC= input("Ingresa una opción: ")
        if opcion_colaC == "1":
            elemento=input("Ingresa el elemento a encolar: ")
            colaC.encolar(elemento)
            print("Elemento encolado.")
        elif opcion_colaC == "2":
            if not colaC.esta_vacia():
                colaC.desencolar()
                print("Elemento desencolado.")
            else: 
                print("La cola está vacía")
        elif opcion_colaC== "3":
            if not colaC.esta_vacia():
                print("Próximo valor a desencolar:", colaC.consultar())
                
            else:
                print("La cola está vacía.")
        elif opcion_colaC == "4":
            if colaC.esta_vacia:
                print("La cola está vacía")
            else:
                print("La cola no está vacía")
        elif opcion_colaC == "5":
            colaC.recorrer_inicio()
        elif opcion_colaC =="6":
            colaC.recorrer_final()
        elif opcion_colaC == "7":
            print("La cola contiene ", colaC.size()," Elemento/s")
        elif opcion_colaC == "0":
            print('''La Cola Circular es una variante de la cola donde los extremos están conectados formando un 
             círculo. Esto optimiza el uso del espacio permitiendo reutilizar las posiciones liberadas de manera 
             continua y eficiente.''')

        
        
        elif opcion_colaC=="8":   
                print("--------------------------------------------------------------")
                break
        else: 
            print("Opción no válida")    
        
def submenu_colaRestringida():
    colaR=ColaER()
    while True:
        print("\nMenu Cola de Entrada Restringida")
        print("--------------------------------------------------------------------")
        print("1. Encolar al inicio: ")
        print("2. Desencolar del final. ")
        print("3. Consultar el frente.")
        print("4. Consultar el final.")
        print("5. Verificar si la cola está vacía")
        print("6. Recorrer.")
        print("7. Tamaño de la Cola.")
        print("8. Regresar")
        print("0. Definición")

        opcion_colaR = input("Ingresa una opción: ")

        if opcion_colaR =="1":
            elemento=input("Ingrese el elemento a encolar: ")
            colaR.encolar_inicio(elemento)
            print("Elemento agregado.")
        elif opcion_colaR == "2":
            colaR.desencolar_final()
            print("Elemento eliminado de la cola.")
        elif opcion_colaR == "3":
            print("Primer elemento de la cola: ",colaR.consultar())
        elif opcion_colaR == "4":
            print("Último elemento de la cola: ",colaR.consultar_final())
        elif opcion_colaR == "5":
            if colaR.esta_vacia():
                print("La cola está vacía.")
            else: 
                print("La cola no está vacía.")
        elif opcion_colaR =="6":
            colaR.recorrer_inicio()
        elif opcion_colaR == "7":
            print("La cola contiene ",colaR.size(), "Elemento/s.")
        
        elif opcion_colaR == "0":
            print('''La Cola de Entrada Restringida solo permite añadir elementos por un extremo. Esto puede ser útil 
             para controlar cómo se añaden los datos y gestionar de manera precisa el flujo de entrada en 
             entornos controlados.''')
        
        elif opcion_colaR == "8":
            print("--------------------------------------------------------------")
            break
        else: 
            print("Opción no válida")
            
def submenu_colaSR():
    cola_sr=ColaSR()
    while True:
        print("\nMenu Cola de Entrada Restringida")
        print("--------------------------------------------------------------------")
        print("1. Encolar al inicio: ")
        print("2. Desencolar del final. ")
        print("3. Consultar el frente.")
        print("4. Consultar el final.")
        print("5. Verificar si la cola está vacía")
        print("6. Recorrer.")
        print("7. Tamaño de la Cola.")
        print("8. Regresar")
        print("0. Definición")

        opcion_colasr=input("Ingresa una opción: ")
        
        if opcion_colasr =="1":
            elemento=input("Ingrese el elemento a encolar: ")
            cola_sr.agregar_inicio(elemento)
            print("Elemento agregado.")
        elif opcion_colasr == "2":
            if cola_sr.esta_vacia():
                print("La cola está vacía.")
            else:
                cola_sr.desencolar_final()
                print("Elemento eliminado de la cola.")
        elif opcion_colasr == "3":
            print("Primer elemento de la cola: ",cola_sr.consultar_frente())
        elif opcion_colasr == "4":
            print("Último elemento de la cola: ",cola_sr.consultar_final())
        elif opcion_colasr == "5":
            if cola_sr.esta_vacia():
                print("La cola está vacía.")
            else: 
                print("La cola no está vacía.")
        elif opcion_colasr =="6":
            cola_sr.recorrer_inicio()
        elif opcion_colasr == "7":
            print("La cola contiene ",cola_sr.size(), "Elemento/s.")
        
        elif opcion_colasr == "0":
            print('''La Cola de Salida Restringida es una estructura de datos donde sólo se puede eliminar el primer 
             elemento encolado, es decir, sólo se permite desencolar por un extremo. Esto es útil para casos 
             donde se necesita mantener un control estricto sobre el orden de salida de los elementos, garantizando 
             que el proceso siga un orden estrictamente FIFO (First In, First Out).''')
        elif opcion_colasr == "8":
            print("--------------------------------------------------------------")
            break
        else: 
            print("Opción no válida")
          
def submenu_colaPA():
    cola_pa=ColaPA()
    while True:
        print("\nMenu Cola de Prioridad Ascendente")
        print("--------------------------------------------------------------------")
        print("1. Encolar: ")
        print("2. Eliminar elemento menor prioritario. ")
        print("3. Consultar elemento de menor prioridad.")
        print("4. Verificar si la cola está vacía")
        print("5. Tamaño de la Cola.")
        print("6. Regresar")
        print("0. Definición")

        opcion_colapa=input("Ingresa una opción: ")
        
        if opcion_colapa =="1":
            elemento = input("Ingrese el elemento a encolar: ")
            prioridad = input("Ingrese la prioridad del elemento (con número entero): ")
            if prioridad.isdigit():
                cola_pa.encolar(elemento, int(prioridad))
                print("Elemento agregado.")
            else:
                print("Por favor, ingrese un número entero como prioridad.")

        elif opcion_colapa == "2": 
            if cola_pa.esta_vacia():
                print("La cola está vacía.")
            else:
                cola_pa.menos_p()
                print("Desencolar elemento de menor prioridad.")
        elif opcion_colapa == "3":
            if cola_pa.esta_vacia():
                print("La cola está vacía.")
            else:
                elemento=cola_pa.consultar_min()
                print("Elemento de menor priodad: ", elemento)
        elif opcion_colapa == "4":
            if cola_pa.esta_vacia():
                print("La cola está vacía.")
            else:  
                print("La cola no está vacía")
        elif opcion_colapa == "5":
            print("La cola contiene:",cola_pa.size(), "Elemento/s.")
        elif opcion_colapa == "0":
            print('''Las Colas de Prioridad gestionan elementos según su prioridad en lugar de el orden de llegada. 
             En la versión Ascendente, los elementos con menor valor de prioridad salen primero, mientras que 
             en la versión Descendente, los de mayor prioridad salen primero.''')

        elif opcion_colapa == "6":
            print("--------------------------------------------------------------------")
            break
        else: 
            print("Opción no válida")        

def submenu_colaPD():
    cola_pd=ColaPD()
    while True:
        print("\nMenu Cola de Prioridad Descendente")
        print("--------------------------------------------------------------------")
        print("1. Encolar: ")
        print("2. Eliminar elemento de mayor prioridad. ")
        print("3. Consultar elemento de mayor prioridad.")
        print("4. Verificar si la cola está vacía")
        print("5. Tamaño de la Cola.")
        print("6. Regresar")
        print("0. Definición")

        opcion_colapd=input("Ingresa una opción: ")
        
        if opcion_colapd =="1":
            elemento = input("Ingrese el elemento a encolar: ")
            prioridad = input("Ingrese la prioridad del elemento (con número entero): ")
            if prioridad.isdigit():
                cola_pd.encolar(int (prioridad), elemento)
                print("Elemento agregado.")
            else:
                print("Por favor, ingrese un número entero como prioridad.")

        elif opcion_colapd == "2": 
            if cola_pd.esta_vacia():
                print("La cola está vacía.")
            else:
                cola_pd.menos_p()
                print("Desencolar elemento de mayor prioridad.")
        elif opcion_colapd == "3":
            if cola_pd.esta_vacia():
                print("La cola está vacía.")
            else:
                elemento=cola_pd.consultar_max()
                print("Elemento de mayor priodad: ", elemento)
        elif opcion_colapd == "4":
            if cola_pd.esta_vacia():
                print("La cola está vacía.")
            else:  
                print("La cola no está vacía")
        elif opcion_colapd == "5":
            print("La cola contiene:",cola_pd.size(), "Elemento/s.")
        elif opcion_colapd == "0":
            print('''Las Colas de Prioridad gestionan elementos según su prioridad en lugar de el orden de llegada. 
             En la versión Ascendente, los elementos con menor valor de prioridad salen primero, mientras que 
             en la versión Descendente, los de mayor prioridad salen primero.''')
        elif opcion_colapd == "6":
            print("--------------------------------------------------------------------")
            break
        else: 
            print("Opción no válida")     
       
def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                mostrar_submenu_listas()
                opcion_lista = input("Seleccione una opción de lista: ")
                if opcion_lista == "1":
                    submenu_lista_simple()
                    pass
                elif opcion_lista == "2":
                    sub_menu_lista_doble()
                    pass
                elif opcion_lista == "3":
                    submenu_listaDobleCircular()
                    pass
                elif opcion_lista == "4":
                    submenu_listaSimpleCircular()
                    pass
                elif opcion_lista == "5":
                    print("-------------------------------------------------------")
                    
                    break
                
                else:
                    print("Opción no válida.")

        elif opcion == "2":
            while True:
                mostrar_submenu_pilas()
                opcion_pila = input("Seleccione una opción de pila: ")
                if opcion_pila == "1":
                    submenu_pila()
                    pass
                elif opcion_pila == "2":
                    submenu_pilaE()
                    pass
                elif opcion_pila == "3":
                    print("-------------------------------------------------------")
                    break
                else:
                    print("Opción no válida.")

        elif opcion == "3":
            while True:
                mostrar_submenu_colas()
                opcion_cola = input("Seleccione una opción de cola: ")
                if opcion_cola == "1":
                    submenu_cola()
                    pass
                elif opcion_cola == "2":
                    submenu_colaDoble()
                    pass
                elif opcion_cola == "3":
                    submenu_colaCircular()
                    pass
                elif opcion_cola == "4":
                    submenu_colaRestringida()
                    pass
                elif opcion_cola == "5":
                    submenu_colaSR()
                    pass
                elif opcion_cola == "6":
                    submenu_colaPA()
                    pass
                elif opcion_cola == "7":
                    submenu_colaPD()
                    pass
                elif opcion_cola == "8":
                    print("-------------------------------------------------------")
                    break
                
                else:
                    print("Opción no válida.")

        elif opcion == "0":
            print("Gracias por utilizar el portafolio de estructuras de datos.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
