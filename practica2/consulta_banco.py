from urllib.request import urlopen
import json
import fileinput

class ExchangeAPIClient:
    def get_datos(self):
        api_url = 'https://api.exchangeratesapi.io/latest'
        response = urlopen(api_url)
        return  json.loads(response.read())

    def convert(self,rates,cantidad, de):
        return cantidad/rates[de]

def escribir_datos(saldo,fecha):
    fila = []
    with open ('ahorros.txt') as file:
        for linea in file:
            fila.append(linea)
    salida=open("ahorros.txt",'w')
    for linea in fila:
        salida.write('{}'.format(linea))
    salida.write('{0} {1} \n'.format(fecha,saldo))
    salida.close()
    
def leer_datos():
    fila = []
    with open ('divisas.txt') as file:
        for linea in file:
            fila.append(linea.strip().split(','))
    return fila

if __name__== '__main__':
    bbdd_web=ExchangeAPIClient()
    bbdd=bbdd_web.get_datos()
    divisas=bbdd['rates']
    base=bbdd['base']
    cantidad_total=0
    datos=leer_datos()
    for element in datos:
        if element[0] in divisas:
            cantidad_total = cantidad_total+bbdd_web.convert(divisas,int(element[1]),element[0])
        elif element[0]==base:
                cantidad_total = cantidad_total+int(element[1])
    escribir_datos(cantidad_total,bbdd['date'])
