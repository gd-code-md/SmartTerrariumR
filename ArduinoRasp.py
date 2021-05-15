try:
    import os, time, serial, Metodos
except ImportError as error:
    print(f"\n\n\t\t\t\tOcurrió el ERROR: {error}")

def Core():
    metos= Metodos.ColeccionMetodos()
    #os.system("clear")#Para linux.
    os.system("cls")#Para windows.
    print("\n\n\t\t\t\tIniciando comunicacion con arduino")

    # Abrimos la conexión con Arduino
    try:
        #arduino = serial.Serial('/dev/ttyACM0', 9600)#Escucha en puerto serial linux mio.
        arduino = serial.Serial('COM6', 9600)#Para windows mio
        bande= 0
        time.sleep(2)
    except Exception as e:
        print(f"\n\n\t\t\t\tOcurrió el ERROR: {e}")
        bande= 1
    finally:
        if bande== 0:
            with arduino:
                while True:
                    try:
                        metos.Arduino(arduino)
                        #ApagarBuzzer()#Para mandar por el puerto serial que se presiono el botón y apagar el buzzer.
                    except KeyboardInterrupt:
                        print("\n\n\t\t\t\tTermino del programa por Ctrl+c presionado")
                        arduino.close()
                        break
                    except Exception as e:
                        print(f"\n\n\t\t\t\tOcurrió el ERROR: {e}")
                        arduino.close()
                        break
        else:
            print("\n\n\t\t\t\tNo se puede ejecutar el resto del programa debido al/los errores anteriores.")
            print("\n\n\t\t\t\tFinalizando programa.")

if __name__== "__main__":
    Core()