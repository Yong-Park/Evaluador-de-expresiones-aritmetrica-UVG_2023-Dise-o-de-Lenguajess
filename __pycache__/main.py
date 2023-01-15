# Yongbum Park 20117
# Universidad del Valle de Guatemala
# 4 año, primer ciclo
# Diseño de Lenguajes 

from evaluador import *

# problema = "5+3*2"
# problema = "10*(3+1)"
# problema = "10*((3+2)*5)"
# problema = "10*(3+2*5)"
problema = "10*(25/5)"

sol = Evaluador(problema)
total = sol.analizar()
print(total)