# Yongbum Park 20117
# Universidad del Valle de Guatemala
# 4 año, primer ciclo
# Diseño de Lenguajes 
import re

class Evaluador:
    
    def __init__(self,expresion):
        self.expresion = expresion
        self.array = []
        self.valor = ""
        self.total = 0.0
        
    def analizar(self):
        for var in self.expresion:
            if var.isnumeric():
                self.valor += var
            else:
                if self.valor != "":
                    self.array.append(self.valor)
                    self.valor = ""
                self.array.append(var)
        if self.valor != "":
            self.array.append(self.valor)
        self.postfix()
        return self.total
        
    def postfix(self):
        temporal = []
        pila = []
        for exp in self.array:
            if exp.isnumeric():
                temporal.append(exp)
            else: 
                if pila != []:
                    largo = len(pila) - 1
                    if exp == ")":
                        pila.append(exp)
                        pila.reverse()
                        number_pop = 0
                        for val in pila:
                            if val == ")":
                                number_pop += 1
                            elif val == "(":
                                number_pop +=1
                                break
                            else:
                                temporal.append(val)
                                number_pop+=1
                        for i in range(number_pop):
                            pila.pop(0)
                        pila.reverse()

                    elif exp == "-":
                        if "+" == pila[largo] or "/" == pila[largo] or "*" == pila[largo]:
                            temporal.append(pila[largo])
                            pila.pop(largo)
                        pila.append(exp)
                    elif exp == "+":
                        if "/" == pila[largo] or "*" == pila[largo]:
                            temporal.append(pila[largo])
                            pila.pop(largo)
                        pila.append(exp)
                            
                    elif exp == "/":
                        if "*" == pila[largo]:
                            temporal.append(pila[largo])
                            pila.pop(largo)
                        pila.append(exp)
                    else:
                        pila.append(exp)
                else:
                    pila.append(exp)
        if pila:
            pila.reverse()
            for val in pila:
                temporal.append(val)
        # print(temporal)
        # print(pila)
        self.calcular(temporal)
        
    def calcular(self,temporal):
        # print(temporal)
        largo = len(temporal)
        # print(largo)
      
        for pos in range(largo):
            if temporal[pos] == "+":
                self.total = float(temporal[pos-1]) + float(temporal[pos-2])
                temporal.pop(pos-1)
                temporal.pop(pos-1)
                temporal[pos-2] = self.total
                self.calcular(temporal)
                break
            elif temporal[pos] == "-":
                self.total = float(temporal[pos-1]) - float(temporal[pos-2]) 
                temporal.pop(pos-1)
                temporal.pop(pos-1)
                temporal[pos-2] = self.total
                self.calcular(temporal)
                break
            elif temporal[pos] == "*":
                self.total = float(temporal[pos-1]) * float(temporal[pos-2])
                temporal.pop(pos-1)
                temporal.pop(pos-1)
                temporal[pos-2] = self.total
                self.calcular(temporal)
                break
            elif temporal[pos] == "/": 
                self.total = float(temporal[pos-2]) / float(temporal[pos-1])
                temporal.pop(pos-1)
                temporal.pop(pos-1)
                temporal[pos-2] = self.total
                self.calcular(temporal)
                break
   
                    
            
            
        
        

            
            
    
    