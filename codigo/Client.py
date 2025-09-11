import xmlrpc_redes as xmlrpc
import datetime
import sys

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
print(f'Estableciendo conexion con {sv1_ip}:{sv1_port}')

conn2 = xmlrpc.Client.connect(sv2_ip, int(sv2_port))
print(f'Estableciendo conexion con {sv2_ip}:{sv2_port}')
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
resultado7 = conn1.concatStringEntero(5, "cinco -> ")
print(f'conn1.concatStringEntero(5, "cinco -> ") = {resultado7}')
assert resultado7 == "cinco -> 5", f'Error en conn1.concatStringEntero: {resultado7} != "cinco = 5"'

#Implementar un método que recibe un string y devuelve el mismo string (echo)
texto_largo = """
Integer placerat iaculis elit et faucibus. Integer id ex ut tellus molestie euismod. Phasellus leo mauris, consectetur non dolor non, lacinia tincidunt arcu. Nunc sit amet scelerisque enim. Sed ultricies nunc eget augue porta accumsan. Maecenas mauris justo, congue a ante in, tempus vehicula felis. Sed et consequat nibh, in rutrum tortor. Nullam elementum pharetra orci eget pellentesque. Cras at venenatis tellus. Sed mollis, tortor sed sagittis malesuada, massa nisl elementum sem, cursus luctus urna velit nec ligula.

Nulla vehicula lacus sed velit posuere congue. Etiam id nibh dictum lectus finibus interdum. Vivamus sodales lobortis bibendum. Pellentesque gravida dolor at augue viverra tristique non eu est. Nullam aliquet eros nec libero efficitur, eget aliquam nunc sagittis. Donec enim sem, vestibulum sit amet mauris sagittis, dapibus rutrum neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent fermentum purus ut cursus euismod. Cras non egestas ante. In vel est tristique mauris aliquam gravida ac id augue.

Quisque rhoncus erat mi, eget tincidunt turpis consectetur ac. Morbi posuere placerat arcu, ut commodo dolor venenatis vel. Nullam rhoncus sed diam quis malesuada. Duis sed orci euismod, rhoncus diam id, rutrum eros. Vestibulum nec nisi sed quam hendrerit hendrerit. Vestibulum a ligula hendrerit, feugiat lacus nec, faucibus nibh. Ut vel ullamcorper purus. Nam efficitur velit at massa ultricies tempus. Phasellus tristique quam ligula, a fringilla sem dignissim id.

Pellentesque sodales nisi ullamcorper tortor pellentesque, eu fringilla sem rhoncus. Maecenas volutpat euismod nunc, id pulvinar nibh eleifend eu. Sed at quam porttitor, fringilla elit non, condimentum magna. Integer ut erat interdum, accumsan nisl non, hendrerit ligula. Donec sed nisl ut mi vulputate aliquet eu ac odio. Nunc egestas faucibus odio ac congue. Phasellus at blandit libero. Fusce nec feugiat libero, vitae tincidunt massa. Pellentesque nec lacus nisl. Suspendisse accumsan, dui eu tempus elementum, ante sem ultrices diam, vitae euismod lorem mauris vel orci. Suspendisse fringilla ornare justo ut accumsan.

Integer mattis, arcu vitae porttitor fermentum, nisl urna tristique augue, sed ultricies tellus odio ut nulla. Pellentesque vel pharetra tortor. Etiam mattis vestibulum sollicitudin. Aliquam nec ipsum arcu. Pellentesque id odio id massa interdum rutrum. Etiam venenatis id felis ac efficitur. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur magna arcu, auctor ac vulputate non, aliquet eu ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Nullam laoreet risus ac lacus porta suscipit. Fusce at lacinia sapien. Cras vel velit eget quam egestas lacinia quis non tortor. Fusce ut rhoncus odio, eu dignissim diam. Pellentesque tristique magna vel orci accumsan faucibus. Proin pellentesque ipsum ut urna dapibus tempor. Mauris non tellus erat. Vestibulum semper massa diam, et volutpat tellus rutrum a. Nam condimentum lacinia ex, vitae tempus odio tristique a. Donec placerat purus risus, eget consectetur turpis lacinia nec. Phasellus vulputate at dui ut varius. Duis in est mi.

Fusce tortor enim, egestas id nisi in, pretium ornare metus. Donec varius enim vel lacus tempor, in fermentum massa vehicula. Maecenas vitae rhoncus augue, id pellentesque.
"""
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