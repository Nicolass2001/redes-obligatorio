import xmlrpc_redes as xmlrpc
import datetime
import sys
from lorem_text import lorem

if len(sys.argv) >= 2:
    sv1_port = int(sys.argv[1])
else:
    sv1_port = 5000
if len(sys.argv) >= 3:
    sv2_port = int(sys.argv[2])
else:
    sv2_port = 5001
if len(sys.argv) >= 4:
    sv1_ip = str(sys.argv[3])
else:
    sv1_ip = '150.150.0.2'
if len(sys.argv) >= 5:
    sv2_ip = str(sys.argv[4])
else:
    sv2_ip = '100.100.0.2'

conn1 = xmlrpc.Client.connect(sv1_ip, int(sv1_port))
print(f'Conexión establecida con {sv1_ip}:{sv1_port}')

conn2 = xmlrpc.Client.connect(sv2_ip, int(sv2_port))
print(f'Conexión establecida con {sv2_ip}:{sv2_port}')
print()

print('Funciones Servidor1: ')

resultado1 = conn1.construirFloat(3, 14)
print(f'conn1.construirFloat(3, 14) = {resultado1}')
assert resultado1 == 3.14, f'Error en conn1.construirFloat: {resultado1} != 3.14'

resultado2 = conn1.divisionReales(10, 3.14)
print(f'conn1.divisionReales(10, 3.14) = {resultado2}')
assert resultado2 == 10/3.14, f'Error en conn1.divisionReales: {resultado2} != {10/3.14}'

resultado3 = conn1.fechaHora(24, 9, 2025, 8, 30, 0)
print(f'conn1.fechaHora(24, 9, 2025, 8, 30, 0) = {resultado3}')
assert resultado3 == datetime.datetime(2025, 9, 24, 8, 30, 0), f'Error en conn1.fechaHora: {resultado3} != {datetime.datetime(2025, 9, 24, 8, 30, 0)}'

resultado4 = conn1.xor(True, True)
print(f'conn1.xor(True, True) = {resultado4}')
assert resultado4 == False, f'Error en conn1.xor: {resultado4} != False'

resultado5 = conn1.dias(datetime.datetime(2024, 1, 1), datetime.datetime(2025, 1, 1))
print(f'conn1.dias(datetime.datetime(2024, 1, 1), datetime.datetime(2025, 1, 1)) = {resultado5}')
assert resultado5 == 366, f'Error en conn1.dias: {resultado5} != 366'

#<---------------- Casos que pidieron los profes -------------->

#Un request a un método sin parámetros y que retorna un único valor
resultado6 = conn1.holaMundo()
print(f'conn1.holaMundo() = {resultado6}')
assert resultado6 == "Hola Mundo!", f'Error en conn1.holaMundo: {resultado6} != "Hola Mundo!"'

#Un request a un método con parámetros entero y string y que retorna un único valor
resultado7 = conn1.concatStringEntero(5, "cinco = ")
print(f'conn1.concatStringEntero(5, "cinco -> ") = {resultado7}')
assert resultado7 == "cinco = 5", f'Error en conn1.concatStringEntero: {resultado7} != "cinco = 5"'

#Implementar un método que recibe un string y devuelve el mismo string (echo)
texto_largo = lorem.words(20000)
resultado8 = conn1.echo(texto_largo)
if (texto_largo == resultado8):
    print('conn1.echo(texto_largo) -> se recibio el mismo string que texto_largo')
else:
    print('Error en conn1.echo -> no se recibio el mismo string que texto_largo')

#Implementar un método que tarde mas de 10 segundos en responder
print("<--- Ejecutando time.sleep! -->")
resultado9 = conn1.timeout(15)
print(f'conn1.timeout(15) = {resultado9}')
assert resultado9 == True, f'Error en conn1.timeout: {resultado9} != True'

print('--------------------------------')
print('ERRORES SERVER1:')
print('--------------------------------')
#Error No existe el método invocado

try:
    resultado_error1 = conn1.noExisteMetodo()
except Exception as e:
    print(e)

#Error en parámetros del método invocado
try:
    resultado_error2 = conn1.construirFloat()
except Exception as e:
    print(e)

try:
    resultado_error3 = conn1.construirFloat(1)
except Exception as e:
    print(e)

try:
    resultado_error4 = conn1.construirFloat(3, 3, 3)
except Exception as e:
    print(e)

try:
    resultado_error5 = conn1.construirFloat('abc', 'd')
except Exception as e:
    print(e)

#Error interno en la ejecución del método (Division por 0)
try:
    resultado_error6 = conn1.divisionReales(10, 0)
except Exception as e:
    print(e)

print('--------------------------------')

print()

print('Funciones Servidor2: ')

resultado6 = conn2.listsToMap(['a','b','c'],[1, 2]) # LAS CLAVES EN UN DICCIONARIO DE XLRPC DEBEN SER STRINGS
print(f'conn2.listsToMap([\'a\',\'b\',\'c\'],[1, 2]) = {resultado6}')
assert resultado6 == {'a': 1, 'b': 2}, f'Error en conn2.listsToMap: {resultado6} != {{"a": 1, "b": 2}}'

resultado7 = conn2.concatStrings('hello', 'world', '!', '!', '!')
print(f'conn2.concatStrings(\'hello\', \'world\', \'!\', \'!\', \'!\') = {resultado7}')
assert resultado7 == 'helloworld!!!', f'Error en conn2.concatStrings: {resultado7} != helloworld!!!'

resultado8 = conn2.existe([1, 2, 3, '4', 5, 'i'], 'j')
print(f'conn2.existe([1, 2, 3, \'4\', 5, \'i\'], \'j\') = {resultado8}')
assert resultado8 == False, f'Error en conn2.existe: {resultado8} != False'

resultado9 = conn2.agregarElemento({'a': 1, 'b': 2}, 'c', 3)
print(f'conn2.agregarElemento({{"a": 1, "b": 2}}, \'c\', 3) = {resultado9}')
assert resultado9 == {'a': 1, 'b': 2, 'c': 3}, f'Error en conn2.agregarElemento: {resultado9} != {{"a": 1, "b": 2, "c": 3}}'

resultado10 = conn2.construirListaEnteros(1, 10)
print(f'conn2.construirListaEnteros(1, 10) = {resultado10}')
assert resultado10 == [1,2,3,4,5,6,7,8,9,10], f'Error en conn2.construirListaEnteros: {resultado10} != [1,2,3,4,5,6,7,8,9,10]'

resultado11 = conn2.encode('Hello world!')
print(f'conn2.encode(\'Hello world!\') = {resultado11}')
assert resultado11 == b'SGVsbG8gd29ybGQh', f'Error en conn2.encode: {resultado11} != b\'SGVsbG8gd29ybGQh\''

resultado12 = conn2.decode(b'SG9sYSBtdW5kbyE=')
print(f'conn2.decode(b\'SG9sYSBtdW5kbyE=\') = {resultado12}')
assert resultado12 == 'Hola mundo!', f'Error en conn2.decode: {resultado12} != \'Hola mundo!\''