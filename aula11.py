#Precedencia entre os operadores
#1. (n+n)
#2. **
#3. * / // %
#4. + -

conta_1 = 1 + 1 ** 5 + 5 #não vai dar 1024 por conta da precedencia
print(conta_1)

conta_2 = (1+1)**(5+5) #aqui ja da certo por conta da precedencia
print(conta_2)

#parenteses mais internos são executados primeiro
conta_3 = (1 + int(0.5 + 0.5))**(5+5)
print(conta_3)