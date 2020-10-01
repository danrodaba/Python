codigo2 = input('Introduce el codigo: ')
texto = input('Introduce el texto cifrado: ')
codigo=[]
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',' ']
for i in range(len(alfabeto)):
    codigo.append(codigo2[2*i]+codigo2[2*i+1])
print(codigo2)

for i in range(len(codigo)):
    texto=texto.replace(codigo[i],alfabeto[i])

diccionario=dict(zip(alfabeto,codigo))
print(diccionario)

print('Tu texto es: ')
print(texto)