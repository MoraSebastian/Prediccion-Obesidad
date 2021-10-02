from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
import joblib

#Cargar modelo
arbol = joblib.load("arbol_model.m")

window = Tk()

window.title("Formulario predicción nivel de obesidad")

window.geometry('500x500')

lbl_genero = Label(window, text="Genero: ")
lbl_genero.grid(column=10, row=10)

combo_genero = Combobox(window)
combo_genero['values'] = ('Mujer', 'Hombre')
combo_genero.current(1)
combo_genero.grid(column=11, row = 10)

lbl_edad = Label(window, text="Edad: ")
lbl_edad.grid(column=10, row=12)

spin_edad = Spinbox(window, from_=0, to=100, width = 5)
spin_edad.grid(column=11, row=12)

lbl_estatura = Label(window, text="Estatura (cm): ")
lbl_estatura.grid(column=10, row=14)

spin_estatura = Spinbox(window, from_=30, to=220, width = 5)
spin_estatura.grid(column=11, row=14)

lbl_peso = Label(window, text="Peso (kg): ")
lbl_peso.grid(column=10, row=16)

spin_peso = Spinbox(window, from_=10, to=330, width = 5)
spin_peso.grid(column=11, row=16)

lbl_familia = Label(window, text="familia con historial de obesidad: ")
lbl_familia.grid(column=10, row=18)

combo_familia = Combobox(window)
combo_familia['values'] = ('si', 'no')
combo_familia.current(1)
combo_familia.grid(column=11, row = 18)

lbl_favc = Label(window, text="Consume alimentos altos en calorias FAVC: ")
lbl_favc.grid(column=10, row=20)

combo_favc = Combobox(window)
combo_favc['values'] = ('si', 'no')
combo_favc.current(1)
combo_favc.grid(column=11, row = 20)

lbl_fcvc = Label(window, text="Por lo general, cuantas verduras consume en  sus comidas FCVC: ")
lbl_fcvc.grid(column=10, row=22)

spin_fcvc = Spinbox(window, values=(1,2,3), width = 5)
spin_fcvc.grid(column=11, row=22)

lbl_ncp = Label(window, text="Cuantas comidas tiene al dia NCP: ")
lbl_ncp.grid(column=10, row=24)

spin_ncp = Spinbox(window, values=(1,3,4), width = 5)
spin_ncp.grid(column=11, row=24)

lbl_caec = Label(window, text="Consume algun alimento entre comidas CAEC: ")
lbl_caec.grid(column=10, row=26)

combo_caec = Combobox(window)
combo_caec['values'] = ('No', 'Algunas veces', 'Frecuentemente', 'Siempre')
combo_caec.current(1)
combo_caec.grid(column=11, row = 26)

lbl_smoke = Label(window, text="Usted fuma? SMOKE: ")
lbl_smoke.grid(column=10, row=28)

combo_smoke = Combobox(window)
combo_smoke['values'] = ('si', 'no')
combo_smoke.current(1)
combo_smoke.grid(column=11, row = 28)

lbl_ch2o = Label(window, text="Que tanta agua consume al dia (litros) CH2O: ")
lbl_ch2o.grid(column=10, row=30)

spin_ch2o = Spinbox(window, values=(1,2,3), width = 5)
spin_ch2o.grid(column=11, row=30)

lbl_scc = Label(window, text="Monitorea las calorias que consume al dia? SCC: ")
lbl_scc.grid(column=10, row=32)

combo_scc = Combobox(window)
combo_scc['values'] = ('si', 'no')
combo_scc.current(1)
combo_scc.grid(column=11, row = 32)

lbl_faf = Label(window, text="Que tan amenudo practica actividad fisica (dias a la semana) FAF: ")
lbl_faf.grid(column=10, row=34)

spin_faf = Spinbox(window, values=(0,1,2,3,4,5), width = 5)
spin_faf.grid(column=11, row=34)

lbl_tue = Label(window, text="Que tanto tiempo usa dispositivos tecnologicos al dia (horas) TUE: ")
lbl_tue.grid(column=10, row=36)

spin_tue = Spinbox(window, values=(0,1,2,3,4,5), width = 5)
spin_tue.grid(column=11, row=36)

lbl_calc = Label(window, text="Que tan amenudo consume alcohol? CALC: ")
lbl_calc.grid(column=10, row=38)

combo_calc = Combobox(window)
combo_calc['values'] = ('No', 'Algunas veces', 'Frecuentemente')
combo_calc.current(1)
combo_calc.grid(column=11, row = 38)

lbl_transporte = Label(window, text="Medio de transporte que utiliza normalmente MTRANS: ")
lbl_transporte.grid(column=10, row=40)

combo_transporte = Combobox(window)
combo_transporte['values'] = ('Transporte publico', 'Caminar', 'Carro', 'Moto', 'Bicicleta')
combo_transporte.current(1)
combo_transporte.grid(column=11, row = 40)

lbl_resultado = Label(window, text='Presione el boton para obtener el resultado ...')
lbl_resultado.grid(column=10, row=44)

# Convertir los datos obtenidos por la gui al formato para realizar la prediccion
def convertirDatos(datos):    
    
    age = datos[1]
    height = datos[2]
    weight = datos[3]
    fcvc = datos[6]
    ncp = datos[7]
    ch2o = datos[10]
    faf = datos[12]
    tue = datos[13]
    gender_male = 0
    # Definir el valor de gender_male
    if datos[0] == 'Hombre':
        gender_male = 1
    else:
        gender_male = 0
        
    # Definir el valor de family_history_yes
    if datos[4] == 'si':        
        family_history_yes = 1
    else:
        family_history_yes = 0
    
    # Definir el valor de facv_yes
    if datos[5] == 'si':
        favc_yes = 1
    else:
        favc_yes = 0
        
    # Definir los valores de caec
    if datos[8] == 'Frecuentemente':    
        caec_frecuently = 1
        caec_sometimes = 0
        caec_no = 0
    elif datos[8] == 'Algunas veces':
        caec_frecuently = 0
        caec_sometimes = 1
        caec_no = 0
    elif datos[8] == 'no':
        caec_frecuently = 0
        caec_sometimes = 0
        caec_no = 1
    
    # Definir el valor de smoke_yes
    if datos[9] == 'yes':    
        smoke_yes = 1
    else:
        smoke_yes = 0
        
    # Definir el valor de scc_yes
    if datos[11] == 'yes':    
        scc_yes = 1
    else:
        scc_yes = 0
        
    # Definir el valor de calc
    if datos[14] == 'Frecuentemente':
        calc_frecuently = 1
        calc_sometimes = 0
        calc_no = 0
    elif datos[14] == 'Algunas veces':
        calc_frecuently = 0
        calc_sometimes = 1
        calc_no = 0
    elif datos[14] == 'no':
        calc_frecuently = 0
        calc_sometimes = 0
        calc_no = 1        
    
    # Definir el valor de mtrans
    if datos[15] == 'Bicicleta':       
        mtrans_bike = 1
        mtrans_motorbike = 0
        mtrans_public = 0
        mtrans_walk = 0
    elif datos[15] == 'Moto':
        mtrans_bike = 0
        mtrans_motorbike = 1
        mtrans_public = 0
        mtrans_walk = 0
    elif datos[15] == 'Transporte publico':
        mtrans_bike = 0
        mtrans_motorbike = 0
        mtrans_public = 1
        mtrans_walk = 0
    elif datos[15] == 'Caminar':
        mtrans_bike = 0
        mtrans_motorbike = 0
        mtrans_public = 0
        mtrans_walk = 1
    else:
        mtrans_bike = 0
        mtrans_motorbike = 0
        mtrans_public = 0
        mtrans_walk = 0
    
    return [age, height, weight, fcvc, ncp, ch2o, faf, tue, gender_male, family_history_yes, favc_yes,
            caec_frecuently, caec_sometimes, caec_no, smoke_yes, scc_yes, calc_frecuently, calc_sometimes,
            calc_no, mtrans_bike, mtrans_motorbike, mtrans_public, mtrans_walk]                       

def clicked():
    datos = [combo_genero.get(), spin_edad.get(), spin_estatura.get(), spin_peso.get(), combo_familia.get(),
             combo_favc.get(), spin_fcvc.get(), spin_ncp.get(), combo_caec.get(), combo_smoke.get(),
             spin_ch2o.get(), combo_scc.get(), spin_faf.get(), spin_tue.get(), combo_calc.get(), 
             combo_transporte.get()]
    #print('datos: ')
    #print(datos)
    
    datos_convertidos = convertirDatos(datos)
    prediction = arbol.predict([datos_convertidos])
    
    res = "El resultado es: " + prediction

    lbl_resultado.configure(text= res)

btn = Button(window, text="Obtener prediccion", command=clicked)

btn.grid(column=10, row=42)

window.mainloop()