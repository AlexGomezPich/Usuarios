def New_usuario():
    Nombre=input("introduce tu nombre: ")
    Apellido=input("introduce tu apellido: ")
    Edad=int(input(("introduce tu edad: ")))
    Sindicalizado=input("introduce Si/No eres sindicalizado: ")
    if Sindicalizado=="Si":
       Sindicalizado=True
    elif Sindicalizado=="No":
        Sindicalizado=False
    else:
         Sindicalizado="NA"
    Datos=[Nombre,Apellido,Edad,Sindicalizado]
    return Datos


def modificar_usuario():
 if usuario_modif in usuarios:
     print(f"""Se modificara este usario: {usuario_modif}

     ¿Que deseas modificar?
     Nombre---------> Opcion 0
     Apellido-------> Opcion 1
     Edad-----------> Opcion 2
     Sindicalizado--> Opcion 3
     """)
     lista_usa=usuarios[usuario_modif]
     opcion_cambio=int(input("Selecione una opcion: "))
     if opcion_cambio==0 :
         N=lista_usa[opcion_cambio]
         lista_usa[opcion_cambio]=input(f"se cambia el nombre de {N} por:  ")
         print(f" se cambio de nombre al usario {usuario_modif} de {N} a {lista_usa[opcion_cambio]}")
     elif opcion_cambio==1 :
         N=lista_usa[opcion_cambio]
         lista_usa[opcion_cambio]=input(f"se cambia el Apellido de {N} por:  ")
         print(f" se cambio de Apellido al usario {usuario_modif} de {N} a {lista_usa[opcion_cambio]}")   
     elif opcion_cambio==2 :
         N=lista_usa[opcion_cambio]
         lista_usa[opcion_cambio]=input(f"se cambia la edad de {N} por:  ")
         print(f" se cambio la edad al usario {usuario_modif} de {N} a {lista_usa[opcion_cambio]}")
     elif opcion_cambio==3 :
         N=lista_usa[opcion_cambio]
         lista_usa[opcion_cambio]= not lista_usa[opcion_cambio]
         print(f" se cambio sindicalizado al usario {usuario_modif} de {N} a {lista_usa[opcion_cambio]}")
     else:
         print(f"no se hace ningun cambio al usario: {usuario_modif}")
     return lista_usa  
def print_menu():
    print(f""" 
    ¿Que quieres hacer?
    Agregar un Usuario----------> Opcion A
    Editar un Usario------------> Opcion B
    Eliminar un Usarrio---------> Opcion C
    Ver Datos de un Usuario-----> Opcion D
    Salir de la APP-------------> Opcion E
    
    """)
print("hola")
if __name__=="__main__":
    usuarios={"JGPMEXFI":["Javier","Pichardo",34,False]}

    while usuarios:
        print(usuarios)
        print_menu()
        opcion=input("Selecione una opcion: ")
        opcion=opcion.capitalize()
        if opcion== "A":
            usuario=input("introduce un usuario: ")
            usuario=usuario.upper()
            Datos=New_usuario()
            usuarios [usuario]=Datos
            print(f"Se agrego el usuario {usuario}")
        elif opcion== "B":
            print("¿Que usuario quieres modificar? ")
            for usua in usuarios:
                print(f"{usua}")
            usuario_modif=input("escribe el usuario a modificar ")
            usuario_modif=usuario_modif.upper()
            list_nueva= modificar_usuario()
            if list_nueva != None: 
                usuarios[usuario_modif]=list_nueva
                print(f"Se modifico este usuario: {usuario_modif}")
            else:
                print(f"usuario {usuario_modif} No existe")   
        elif opcion== "C":
            print("¿Que usuario quieres eliminar? ")
            for usua in usuarios:
                print(f"{usua}")
            usuario_modif=input("escribe el usuario a Eliminar ")
            usuario_modif=usuario_modif.upper()
            if usuario_modif in usuarios:
                usuarios.pop(usuario_modif)
                print(f"Se elimino el usario: {usuario_modif}")
            else:
                print(f"usuario {usuario_modif} No existe")
        elif opcion== "D":
            print("¿Que usuario quieres Ver sus Datos? ")
            for usua in usuarios:
                print(f"{usua}")
            usuario_modif=input("escribe el usuario ")
            usuario_modif=usuario_modif.upper()
            if usuario_modif in usuarios:
                Datos=usuarios[usuario_modif]
                Nombre=Datos[0]
                Apellido=Datos[1]
                Edad=Datos[2]
                Sindicalizado=Datos[3]
                print(f"""Los Datos de este usario {usuario_modif} son:
                
                Nombre---------> {Nombre}
                Apellido-------> {Apellido}
                Edad-----------> {Edad}
                Sindicalizado--> {Sindicalizado}
                """) 
            else:
                print(f"usuario {usuario_modif} No existe")
        elif opcion== "E":
            break
        else:
            print("Opcion no disponible")
