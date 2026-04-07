#Ejercicio 1 "Caja del Kiosco"
nombre_cliente= input("Ingrese su nombre (solo letras): ").strip()

while nombre_cliente == "" or not nombre_cliente.isalpha():
   print ("Error, ingresa un nombre no vacio y solo con letras")
   nombre_cliente= input("Ingrese su nombre (solo letras): ").strip()

productos_a_comprar_str= input("Ingrese la cantidad de productos a comprar (solo digitos): ") .strip()

while not productos_a_comprar_str.isdigit() or int(productos_a_comprar_str) == 0:
   print ("Error, ingrese solo digitos enteros positivos")
   productos_a_comprar_str=  input("Ingrese la cantidad de productos a comprar (solo digitos): ").strip()
productos_a_comprar_int= int(productos_a_comprar_str)

total_sin_descuento= 0
total_con_descuento= 0
for c in range (1, productos_a_comprar_int+1):
   precio_str = input(f"Producto {c} - Precio: ").strip()
   while not precio_str.isdigit() or int(precio_str) == 0:
       print ("Error, ingrese solo digitos enteros positivos")
       precio_str=input(f"Producto {c} - Precio: ").strip()
   precio_int= int(precio_str)
   desc= input("Descuento (S/N): ").strip().lower()
   while desc != "s" and desc != "n":
       print("Error, ingrese S para si o N para no")
       desc= input("Descuento (S/N): ").strip().lower()

   total_sin_descuento+=precio_int

   if desc == "s":
       precio_final= precio_int * 0.9
   else:
       precio_final = precio_int
    
   total_con_descuento+= precio_final
ahorro= total_sin_descuento - total_con_descuento
promedio= total_con_descuento/productos_a_comprar_int
print(f"El total sin descuento es: ${total_sin_descuento:.2f}")
print(f"EL total con descuento es: ${total_con_descuento:.2f}")
print(f"El total de ahorro es: ${ahorro:.2f}")
print (f"El promedio por producto es: ${promedio:.2f}")

#Ejercicio 2 "Acceso al Campus y Menu Seguro"
usuario_correcto= "admin"
clave_correcta= "python123"
contador= 0
ingreso_permitido = False
while True:
   usuario= input("Ingrese su usuario: ").strip()
   clave= input("Ingrese su clave: ").strip()
   if usuario == usuario_correcto and clave == clave_correcta:
       print ("Bienvenido/a")
       ingreso_permitido= True
       break
   else:
       contador+=1
       if contador < 3 :
           print(f"Datos incorrectos, utilizaste {contador} intentos tienes 3")
       else:
           print ("Cuenta bloqueada, superaste los intetos permitidos")
           break
if ingreso_permitido == True:
   while True:
       print ("1)Estado de inscripcion 2)Cambiar clave 3)Mensaje 4)Salir")
       opcion= input("Elija una opcion (1,2,3 o 4): ")
       if opcion.isdigit():
           opcion=int(opcion)
           if opcion == 1:
               print ("Estas inscripto")
           elif opcion == 2:
               clave_nueva= input("Ingrese clave nueva: ").strip()
               if len(clave_nueva)< 6:  
                   print("La contraseña debe tener al menos 6 caracteres")
               else:
                   confirmacion= input("Confirme su clave nueva: ").strip()
                   if clave_nueva == confirmacion:
                       print ("Las contraseñas coinciden")
                       clave_correcta = clave_nueva
                   else:
                       print("Intente nuevamente, las contraseñas no coinciden")
                
           elif opcion == 3:
               print ("Segui practicando programacion, vas por buen camino")
           elif opcion == 4:
               break
       else:
           print ("Ingrese un numero entre uno y cuatro")

#Ejercicio 3 "Agenda de turnos con nombres (sin listas)"
lunes1=""
lunes2=""
lunes3=""
lunes4=""
martes1=""
martes2=""
martes3=""
operador= input("Ingrese el nombre del operador: ").strip()
while not operador.isalpha():
    print ("Error, ingrese solo letras")
    operador= input("Ingrese el nombre del operador: ").strip()
print(f"Bienvenido/a {operador}")
while True:
    print ("Menu")
    print ("1. Reservar turno")
    print ("2. Cancelar turno (por nombre)")
    print ("3. Ver agenda del dia")
    print ("4. Ver resumen general")
    print ("5. Cerrar sistema")
    opcion=input("\nElija una opcion: ")
    if opcion == "1":
        dia= input("Elija un dia: 1 (Lunes) o 2 (Martes): ")
        while  dia != "1" and dia !="2":
            print ("Error, elija la opcion 1 o 2")
            dia= input("Elija un dia: 1(Lunes) o 2(Martes): ")
        nombre_paciente= input("Ingrese nombre del paciente: ").strip()
        while nombre_paciente == "" or not nombre_paciente.isalpha():
            print ("Error, ingrese solo letras")
            nombre_paciente= input("Ingrese nombre del paciente: ").strip()
        if dia == "1":
            if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente ==lunes4:
                print (f"Error.{nombre_paciente} ya tiene turno este dia")
            elif lunes1== "":
                lunes1=nombre_paciente
                print ("Registrado en turno 1")
            elif lunes2=="":
                lunes2 = nombre_paciente
                print ("Registrado en turno 2")
            elif lunes3=="":
                lunes3 = nombre_paciente
                print ("Registrado en turno3")
            elif lunes4=="":
                lunes4= nombre_paciente
                print ("Registrado en turno 4")
            else:
                print ("No hay mas turnos disponibles")
        if dia == "2":
            if nombre_paciente ==martes1 or nombre_paciente == martes2 or nombre_paciente== martes3:
                print (f"Error, {nombre_paciente} ya tiene turno ese dia")
            elif martes1=="":
                martes1=nombre_paciente
                print ("Registrado en turno 1")
            elif martes2=="":
                martes2=nombre_paciente
                print ("Registrado en turno 2")
            elif martes3=="":
                martes3=nombre_paciente
                print ("Registrado en turno 3")
            else:
                print("No hay turnos disponibles")
    elif opcion == "2":
        dia_elegido=input("Elija un dia(lunes o martes): ").strip().lower()
        if dia_elegido == "lunes" or dia_elegido=="martes":
            nombre_paciente=input("ingrese nombre del paciente: ").strip()
            while nombre_paciente== "" or not nombre_paciente.isalpha():
                print ("El nombre solo debe contener solo letras")
                nombre_paciente=input("ingrese nombre del paciente: ").strip()
            if dia_elegido == "lunes":  
                if nombre_paciente==lunes1:
                    print ("Cancelamos el turno")
                    lunes1=""
                elif nombre_paciente ==lunes2:
                    print ("Cancelamos el turno")
                    lunes2=""
                elif nombre_paciente ==lunes3:
                    print ("Cancelamos el turno")
                    lunes3=""
                elif nombre_paciente ==lunes4:
                    print ("Cancelamos el turno")
                    lunes4=""
                else:
                    print ("No se encontro paciente el dia lunes")
            elif dia_elegido == "martes":
                if nombre_paciente==martes1:
                    print("Cancelamos el turno")
                    martes1=""
                elif nombre_paciente ==martes2:
                    print("Cancelamos el turno")
                    martes2=""
                elif nombre_paciente == martes3:
                    print("Cancelamos el turno")
                    martes3=""
                else:
                    print("El paciente no tiene turno el dia martes")
        else:
            print ("Solo hay turnos los dias lunes y martes")
    elif opcion == "3":
        agenda= input("elija el dia para ver la agenda (lunes o martes): ").strip().lower()
        if agenda == "lunes":
            print("AGENDA DEL DIA LUNES")
            if lunes1=="":
                print("Turno1. Libre")
            else:
                print (f"{lunes1} tiene el turno 1")
            if lunes2=="":
                print("Turno2. Libre")
            else:
                print (f"{lunes2} tiene el turno 2")
            if lunes3=="":
                print("Turno3. Libre")
            else:
                print (f"{lunes3} tiene el turno 3")
            if lunes4=="":
                print("Turno4. Libre")
            else:
                print (f"{lunes4} tiene el turno 4")
        elif agenda == "martes":
            print("AGENDA DEL DIA MARTES")
            if martes1=="":
                print("Turno 1. Libre")
            else:
                print (f"{martes1} tiene el turno 1")
            if martes2=="":
                print("Turno 2. Libre")
            else:
                print (f"{martes2} tiene el turno 2")
            if martes3=="":
                print ("Turno 3. Libre")
            else:
                print (f"{martes3} tiene el turno 3")
    elif opcion == "4":
        lunes_libre= 0
        lunes_ocupado=0
        martes_libre=0
        martes_ocupado=0
        if lunes1 =="":
            lunes_libre+=1
        else:
            lunes_ocupado+=1
        if lunes2 =="":
            lunes_libre+=1
        else:
            lunes_ocupado+=1
        if lunes3=="":
            lunes_libre+=1
        else:
            lunes_ocupado+=1
        if lunes4=="":
            lunes_libre+=1
        else:
            lunes_ocupado+=1
        if martes1=="":
            martes_libre+=1
        else:
            martes_ocupado+=1
        if martes2=="":
            martes_libre+=1
        else:
            martes_ocupado+=1
        if  martes3=="":
            martes_libre+=1
        else:
            martes_ocupado+=1
        print(f"El dia lunes cuenta con {lunes_libre} turnos libres y {lunes_ocupado} turnos ocupados")
        print (f"El dia martes cuenta con {martes_libre} turnos libres y {martes_ocupado} turnos ocupados")
        if lunes_ocupado > martes_ocupado:
            print ("El dia lunes tiene mas turnos ocupados")
        elif martes_ocupado > lunes_ocupado:
            print ("El martes tiene mas turnos ocupados ")
        else:
            print ("Ambos tienen la misma cantidad de turnos ocupados")
        
    elif opcion == "5":
        break
    else:
        print ("\nError, elija una opcion entre 1 y 5\n")
        input("presiones ENTER para continuar\n")

#Ejercicio 4 "Escape Room: La Bóveda"
energia=100
tiempo=12
cerraduras_abiertas=0
alarma=False
codigo_parcial=""
racha_forzar=0
nombre_agente=input("Ingrese el nombre del agente: ").strip()
while nombre_agente=="" or not nombre_agente.isalpha():
    print ("El nombre solo debe contener letras")
    nombre_agente=input("Ingrese el nombre del agente: ").strip()
while True:
    if cerraduras_abiertas==3:
        print ("Lograste abrir las 3 cerraduras")
        break
    if energia <=0 or tiempo<=0:
        print ("Te quedaste sin tiempo y/o energia")
        break
    if alarma==True and tiempo<=3:
        print("Se bloqueo el sistema")
        break
    print (f"El/la Agente {nombre_agente} tiene {energia} de energia y {tiempo} de tiempo\n")
    print("Opciones del Menu")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    print("4. Salir\n")
    opcion=input ("Elija una opcion (solo numeros): \n").strip()
    while opcion=="" or not opcion.isdigit():
        print("Error, elija una opcion numerica")
        opcion=input("Elija una opcion (solo numeros): \n").strip()
    if opcion =="1":
        energia-=20
        tiempo-=2
        racha_forzar+=1
        if  racha_forzar==3:
            alarma=True
            print ("Se activo la alarma porque la cerradura se trabo")
        if energia <40 and not alarma:
            print ("Riesgo de alarma, energia baja")
            intento=input("Elija un numero entre 1 y 3: ").strip()
            while intento=="" or not intento.isdigit():
                print("Intenta de nuevamente, tiene que ser una opcion numerica")
                intento=input("Elija un numero entre 1 y 3: ").strip()
            if intento=="3":
                print("Se activo la alarma por cansancio")
                alarma=True
            else:
                print("No se activo la alarma")
        if not alarma and cerraduras_abiertas<3:
                cerraduras_abiertas+=1
                print ("Abriste una cerradura \n")
            
    elif opcion =="2":
        racha_forzar=0
        energia-=10
        tiempo-=3
        for i in range (4):
            codigo_parcial+= "x"
            print (f"Hackeando...Proceso {codigo_parcial}\n")
        if len(codigo_parcial) >= 8:
            cerraduras_abiertas+=1
            print("Hackeo exitoso. Se abrio una cerradura \n")
            codigo_parcial=""
        else:
            print ("Codigo incompleto")
    elif opcion =="3":
        racha_forzar=0
        energia+=15
        tiempo-=1
        if energia>100:
            energia=100
        if alarma==True:
            energia-=10
    elif opcion=="4":
        break
    else:
        print ("Por favor elija una opcion entre 1 y 4 \n")

#Ejercicio 5 "Escape room: La arena del Gladiador"
vida_gladiador = 100
vida_enemigo = 100
pociones_de_vida = 3
daño_base_ataque_pesado = 15
daño_base_enemigo= 12
turno_gladiador= True
print("-----BIENVENIDO A LA ARENA-----")
nombre_gladiador=input("Nombre del gladiador: ").strip()
while nombre_gladiador=="" or not nombre_gladiador.isalpha():
    print("Error: solo se permiten letras")
    nombre_gladiador=input("Ingrese nombre del gladiador: ").strip()
while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"La vida actual del gladiador es {vida_gladiador} HP y la del enemigo es {vida_enemigo} HP")
    print (f"Las pociones restantes son {pociones_de_vida}")
    print ("----- MENU -----")
    print ("1. Ataque pesado")
    print ("2. Rafaga veloz")
    print ("3. Curar")
    opcion= input("Seleccione una opcion del menu: ").strip()
    while opcion == "" or not opcion.isdigit():
        print ("Error, debe ingresar un numero")
        opcion= input("Seleccione una opcion del menu: ").strip()
    if opcion =="1":
        if vida_enemigo<20:
            print("El enemigo tiene poca vida, realizaste un golpe critico")
            golpe_critico=daño_base_ataque_pesado * 1.5
            print(f"Atacaste al enemigo por {golpe_critico} puntos de daño")
            vida_enemigo-=golpe_critico
            print (f"La vida actual del enemigo es {vida_enemigo} HP")
        else:
            vida_enemigo-=daño_base_ataque_pesado
            print (f"Atacaste al enemigo por {daño_base_ataque_pesado} puntos de daño")
            print (f"La vida actual del enemigo es {vida_enemigo}")
    elif opcion =="2":
        for i in range (3):
             vida_enemigo-=5
             print ("Golpe conectado por 5 de daño")
        print (f"Golpe realizado, la vida actual del enemigo es {vida_enemigo} HP")
    elif opcion == "3":
        if pociones_de_vida>0:
             vida_gladiador+=30
             pociones_de_vida-=1
             print (f"Te curas 30 HP, te quedan {pociones_de_vida} pociones")
             if vida_gladiador>100:
                  vida_gladiador=100
                  print (f"La vida actual del gladiador es {vida_gladiador} HP")
        else:
             print("No te quedan pociones, pierdes el turno")
    else:
        print("Error, ingrese un numero entre 1 y 3")

    if vida_enemigo>0:
            vida_gladiador-=daño_base_enemigo
            print (f"El enemigo te ataco por {daño_base_enemigo} puntos de daño")
            print (f"La vida actual del gladiador es {vida_gladiador} HP")
    else:
            print("El enemigo no tiene puntos de vida")
if vida_gladiador>0:
    print ("GANASTE LA BATALLA")
else:
     print("PERDISTE LA BATALLA")
        


