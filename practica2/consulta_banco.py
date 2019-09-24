from urllib.request import urlopen
import json
import fileinput

"""Esta clase implementa la conexión a la pagina web, además de transformar la moneda. """
class ExchangeAPIClient:
    def  __init__(self):
        self.bbdd=[]
    def get_datos(self):
        api_url = 'https://api.exchangeratesapi.io/latest'
        response = urlopen(api_url)
        return  json.loads(response.read())

    def convert(self,cantidad, de):
        return cantidad/self.bbdd['rates'][de]

def escribir_datos(saldo,fecha):
    salida=open("ahorros.txt",'a+')
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
    bbdd_web.bbdd=bbdd_web.get_datos()
    cantidad_total=0
    datos=leer_datos()
    for element in datos:
        if element[0] in bbdd_web.bbdd['rates']:
            cantidad_total = cantidad_total+bbdd_web.convert(int(element[1]),element[0])
        elif element[0]==bbdd_web.bbdd['base']:
                cantidad_total = cantidad_total+int(element[1])
    escribir_datos(cantidad_total,bbdd_web.bbdd['date'])
