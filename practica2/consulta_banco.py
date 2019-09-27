from urllib.request import urlopen
import json
class ExchangeAPIClient:

    def __init__(self):
        self.datos_web=[]
        
    def get_datos(self):
        api_url = 'https://api.exchangeratesapi.io/latest'
        response = urlopen(api_url)
        self.datos_web=json.loads(response.read())
        
    def convert(self,cantidad, de):
        return cantidad/self.datos_web['rates'][de]
    def get_rates(self):
        return self.datos_web['rates']
    def get_date(self):
        return self.datos_web['date']
    def get_base(self):
        return self.datos_web['base']

def escribir_datos(saldo,fecha):
    salida=open("ahorros.txt",'a+')
    salida.write('{}, {} \n'.format(fecha,int(saldo)))
    salida.close()
    
def leer_datos():
    fila = []
    with open ('divisas.txt') as file:
        for linea in file:
            fila.append(linea.strip().split(','))
    return fila

if __name__== '__main__':
    bbdd_web=ExchangeAPIClient()
    bbdd_web.get_datos()
    divisas=bbdd_web.get_rates()
    base=bbdd_web.get_base()
    cantidad_total=0
    datos=leer_datos()
    for element in datos:
        if element[0] in divisas:
            cantidad_total = cantidad_total+bbdd_web.convert(int(element[1]),element[0])
        elif element[0]==base:
                cantidad_total = cantidad_total+int(element[1])
    escribir_datos(cantidad_total,bbdd_web.get_date())
