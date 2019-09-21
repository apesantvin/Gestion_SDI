from urllib.request import urlopen
import json
def get_rates():
	api_url = 'https://api.exchangeratesapi.io/latest'
	response = urlopen(api_url)
	rates = json.loads(response.read())
	return rates['rates']

def get_date():
    api_url = 'https://api.exchangeratesapi.io/latest'
    response = urlopen(api_url)
    rates = json.loads(response.read())
    return rates['date']

def get_base():
    api_url = 'https://api.exchangeratesapi.io/latest'
    response = urlopen(api_url)
    rates = json.loads(response.read())
    return rates['base']

def convert(cantidad, de):
	rates = get_rates()
	return cantidad/rates[de]

def escribir_datos(a,b):
    fecha=get_date()
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
monedas=get_rates()
cantidad_total=0
datos=leer_datos()
base=get_base()
errores=[]
for element in datos:
    if element[0] in monedas:
        cantidad_total = cantidad_total+convert(int(element[1]),element[0])
    else:
        if element[0]==base:
            cantidad_total = cantidad_total+int(element[1])
        else:
            errores.append(element)
escribir_datos(cantidad_total,errores)
