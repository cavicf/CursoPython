#conversão de tipos, coersão
#type convertion, typecasting, coercion
#é o ato de converter um tipo em outro 
#tipos imutáveis e primitivos:
#str, int, float, bool
print(1+1)
print('a'+'b')
#print('1'+ 1) isso não funciona pois os dados tem de ser do mesmo tipo
#fazendo as conversões com casting
print(int('1'), type(int('1')))
print(int('1')+1)
#o bool pode retornar true ou false, se for vazio é false e com algo é true
print(bool(''))
print(str(11) + 'b')