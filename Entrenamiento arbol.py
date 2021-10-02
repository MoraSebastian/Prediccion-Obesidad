import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

#para graficar el arbol de decision
from sklearn.tree import export_graphviz
import graphviz
from graphviz import Source
import matplotlib.pyplot as plt
import numpy as np

import joblib

#cargamos los datos desde el csv usando la libreria pandas
data = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')

#se limpian los datos nulos que se puedan encontrar en el cvs
data = data.dropna()

#Para comprobar que se ha leido bien, se listan las variables en el fichero
#print(data.dtypes)

#y se obtienen los estadisticos principales
#print(data.describe())

#Imprimir el head de los datos originales leidos
#print(data.head())

data = pd.get_dummies(data, columns= ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS'], drop_first=True)
#print(data.dtypes)
# Imprimir en head luego de aplicar onehotEncoder
#print(data.head())
#Incidamos las variables predictoras y debajo la variable objetivo.
#Se busca predecir la especie de la planta segun ciertos parametros
predictors = data[['Age', 'Height', 'Weight', 'FCVC',
					'NCP', 'CH2O', 'FAF', 'TUE',
                    'Gender_Male', 'family_history_with_overweight_yes', 'FAVC_yes', 'CAEC_Frequently',
                    'CAEC_Sometimes', 'CAEC_no', 'SMOKE_yes',
                    'SCC_yes', 'CALC_Frequently', 'CALC_Sometimes', 'CALC_no', 'MTRANS_Bike',
                    'MTRANS_Motorbike', 'MTRANS_Public_Transportation', 'MTRANS_Walking']]
targets = data.NObeyesdad
#print(targets)

predictors_labels = ['Age', 'Height', 'Weight', 'FCVC',
					'NCP', 'CH2O', 'FAF', 'TUE',
                    'Gender_Male', 'family_history_with_overweight_yes', 'FAVC_yes', 'CAEC_Frequently',
                    'CAEC_Sometimes', 'CAEC_no', 'SMOKE_yes',
                    'SCC_yes', 'CALC_Frequently', 'CALC_Sometimes', 'CALC_no', 'MTRANS_Bike',
                    'MTRANS_Motorbike', 'MTRANS_Public_Transportation', 'MTRANS_Walking']
target_labels = ['Insufficient_Weight', 'Normal_Weight', 'Overweight_Level_I', 'Overweight_Level_II',   
                    'Obesity_Type_I', 'Obesity_Type_II', 'Obesity_Type_III']

#crean las variables para el entrenamiento del arbol y las variables para las pruebas
X_entrenamiento, X_test, y_entrenamiento, y_test = train_test_split(predictors, targets)

#construimos el arbol con los datos de entrenamiento
arbol = DecisionTreeClassifier()
arbol.fit(X_entrenamiento, y_entrenamiento)

#Se verifica la probabilidad de prediccion del arbol con los datos de prueba

print("PROBABILIDAD DE PREDICCION, DATOS DE PRUEBA" , arbol.score(X_test, y_test))

#Se verifica la probabilidad de prediccion del arbol con los datos de entrenamiento 
print("PROBABILIDAD DE PREDICCION, DATOS DE ENTRENAMIENTO", arbol.score(X_entrenamiento, y_entrenamiento))

# Se genera la grafica del arbol para visualizarlo
export_graphviz(arbol, out_file='arbol.dot', class_names=target_labels,
				feature_names=predictors_labels, impurity=False, filled=True)
				
with open('arbol.dot') as f:
	dot_graph = f.read()
graphviz.Source(dot_graph)

#para ver la importancia de las caracteristicas para ayudar a definir
caract=23
plt.barh(range(caract), arbol.feature_importances_)
plt.yticks(np.arange(caract), predictors_labels)
plt.xlabel('Importancia de las caracteristicas')
plt.ylabel('Caracteristicas')
plt.show()

# se visualiza la profundidad actual del arbol de decision creado con los datos
arbol.tree_.max_depth

# se crea un nuevo arbol evitando el sobre-ajuste limitando su profundidad
arbol = DecisionTreeClassifier(max_depth = 4)

# se vuelve a entrenar el arbol de decision
arbol.fit(X_entrenamiento, y_entrenamiento)

# se visualiza la nueva precision de prediccion con los datos de pruebas
arbol.score(X_test, y_test)

#se visualiza la nueva precision de prediccion con los datos de entrenamiento
arbol.score(X_entrenamiento, y_entrenamiento)

# se genera la grafica del arbol para visualizarlo
export_graphviz(arbol, out_file='arbol.dot', class_names=target_labels,
				feature_names=predictors_labels, impurity=False, filled=True)


with open('arbol.dot') as f:
	dot_graph = f.read()
graphviz.Source(dot_graph)

#Guardar el modelo
joblib.dump(arbol, "arbol_model.m")

# EJEMPLO DE PREDICCION
datos_ejemplo = ['Female', 21, 1.62, 64, 'yes', 'no', 2,3, 'Sometimes', 'no', 2, 'no', 0,1,'no', 'Public_Transportation']
datos_ejemplo = [21, 162, 64, 2, 3, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
prediction = arbol.predict([datos_ejemplo])
print(prediction)

