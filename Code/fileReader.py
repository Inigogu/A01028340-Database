

import csv
import numpy as np
paisesGEI = [""]
paisesPoblados = [""]
numeros = [0]

with open("TextFiles/populationbycountry19802010millions.csv") as csvPopulation:
     reader = csv.reader(csvPopulation)
     for row in reader:
          if row[30] > numeros[0]:
               numeros.insert(0,row[30])
               paisesPoblados.insert(0,row[0])
          elif row[30] > numeros[1]:
               numeros.insert(1,row[30])
               paisesPoblados.insert(1,row[0])
          elif row[30] > numeros[2]:
               numeros.insert(2,row[30])
               paisesPoblados.insert(2,row[0])
          elif row[30] > numeros[3]:
               numeros.insert(3,row[30])
               paisesPoblados.insert(3,row[0])
          elif row[30] > numeros[4]:
               numeros.insert(4,row[30])
               paisesPoblados.insert(4,row[0])



for i in range(0,5):
      print(paisesPoblados[i])



numeros = [0, 0, 0, 0, 0]
with open("TextFiles/greenhouse_gas_inventory_data_data.csv") as csvGHG:
     reader = csv.reader(csvGHG)
     for row in reader:
          if row[1] == "2010":
               if row[2] > numeros[0]:
                    numeros.insert(0,row[2])
                    paisesGEI.insert(0,row[0])
               elif row[2] > numeros[1]:
                    numeros.insert(1,row[2])
                    paisesGEI.insert(1,row[0])
               elif row[2] > numeros[2]:
                    numeros.insert(2,row[2])
                    paisesGEI.insert(2,row[0])
               elif row[2] > numeros[3]:
                    numeros.insert(3,row[2])
                    paisesGEI.insert(3,row[0])
               elif row[2] > numeros[4]:
                    numeros.insert(4,row[2])
                    paisesGEI.insert(4,row[0])
     
for i in range(0,5):
     print(paisesGEI[i])



    