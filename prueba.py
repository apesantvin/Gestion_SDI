from urllib.request import urlopen
import json
def get_datos():
	api_url = 'https://api.exchangeratesapi.io/latest'
	response = urlopen(api_url)
	return  json.loads(response.read())

def convert(rates,cantidad, de):
	return cantidad/rates[de]

def escribir_datos(a,b,fecha):
    salida=open("Resultado_Banco",'w')
    salida.write('En fecha {} su saldo en la cuenta es: \n'.format(fecha))
    salida.write('\t{} euros \n'.format(a))
    if len(b)>0:
        salida.write('No hemos podido transformar los siguiente datos a la moneda deseada: \n')
        for fallos in b:
            salida.write("\t{0}:  {1}\n".format(fallos[0],fallos[1]))
    salida.close()
    
def leer_datos():
    fila = []
    with open ('ahorros') as file:
        for linea in file:
            fila.append(linea.strip().split(','))
    return fila
bbdd=get_datos()
monedas=bbdd['rates']
cantidad_total=0
datos=leer_datos()
base=bbdd['base']
errores=[]
for element in datos:
    if element[0] in monedas:
        cantidad_total = cantidad_total+convert(monedas,int(element[1]),element[0])
    else:
        if element[0]==base:
            cantidad_total = cantidad_total+int(element[1])
        else:
            errores.append(element)
escribir_datos(cantidad_total,errores,bbdd['date'])
