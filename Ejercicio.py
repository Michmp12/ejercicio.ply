#Un estudiante debe realizar su proceso de matricula teniendo en cuenta lo siguiente:

cons_totalcredito1 = 15 * 28000
cons_totalcredito2 = 10 * 35000
cons_totalcredito3 = 12 * 40000
cons_totalcredito4 = 11 * 45000
cons_totalcredito5 = 16 * 55000
cons_totalcredito6 = 17 * 60000
cons_totalcredito7 = 9 * 75000
cons_totalcredito8 = 18 * 80000
cons_totalcredito9 = 12 * 95000
cons_totalcredito10 = 17 * 110000



print ('Bienvenido a nuestra pagina de registros de la Universidad')
semestre = int(input('Ingrese el semestre para la matricula'))

if semestre == 1: 
    cantidadCreditos = 15
    valorCredito = 28000

if semestre == 2:
    cantidadCreditos = 10
    valorCredito = 35000

if semestre == 3:
    cantidadCreditos = 12
    valorCredito = 40000

if  semestre == 4:
    cantidadCreditos = 11
    valorCredito = 45000

if semestre == 5:
    cantidadCreditos = 16
    valorCredito = 55000

if semestre == 6:
    cantidadCreditos = 17
    valorCredito = 60000

if semestre == 7:
    cantidadCreditos = 9
    valorCredito = 75000

if semestre == 8:
    cantidadCreditos = 18
    valorCredito = 80000

if semestre == 9:
    cantidadCreditos = 12
    valorCredito = 95000

if semestre == 10:
    cantidadCreditos = 17
    valorCredito = 110000


print ("Para el semestre ", semestre)
print ("La cantidad de creditos es de: ", cantidadCreditos)
print ("El valor de cada credito es de: $", cantidadCreditos * valorCredito)

dinero_actual = float(input('Cuanto dinero tienes en efectivo? '))
dinero_en_cuenta = float(input('Cuanto dinero tienes en tu cuenta bancaria?'))

total_dinero = dinero_actual + dinero_en_cuenta 
print ('Tienes un total de $' + str(total_dinero))

print('Recuerda que para matricular debes de tener el suficiente dinero de lo contrario no podras matricularte')

print('Si desea saber si puede realizar el proceso de matricula ingrese los siguientes datos')

costo_credito = float(input('Ingrese el costo del credito solicitado:'))
print('El costo del credito solcilitado es: $' + str(costo_credito))

def matricularse(dinero_actual, costo_credito):
    if dinero_actual >= costo_credito:
        dinero_restante = dinero_actual - costo_credito
        return True, dinero_restante
    else:
        return False, dinero_actual 
    
dinero_actual = float(input('Ingrese nuevamente el dinero que tiene actualmente para la matricula'))
costo_credito = float (input('¿Cual es el costo del credito que quiere matricular?'))

exito,dinero_restante = matricularse(dinero_actual, costo_credito)

if exito:
    print('Si tu dinero es el suficiente entonces tienes una ¡Matricula exitosa! de lo contrario lo siento, no tienes suficiente dinero para la matricula, te quedan $' + str(dinero_restante) +' disponibles.')

