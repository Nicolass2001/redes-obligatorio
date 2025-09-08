import sys
import xmlrpc_redes as xmlrpc
import datetime
import time

def construirFloat(unidades, decimales):
    aux = f'{unidades}.{decimales}'
    return float(aux)

def divisionReales(a, b):
    return a/b

def fechaHora(d, m, a, hh, mm, ss):
    return datetime.datetime(a, m, d, hh, mm, ss)

def xor(a, b):
    return not ((a and b) or (not a and not b))

def dias(f1, f2):
    return abs((f1-f2).days)

def timeout(t):
    time.sleep(t)
    return True

def holaMundo():
    return "Hola Mundo!"

def concatStringEntero(n, s):
    return s + str(n)

def echo(s):
    return s

# Pasar los argumentos por consola
# Primer argumento: puerto
# Segundo argumento: ip
if len(sys.argv) >= 2:
    port = int(sys.argv[1])
else:
    port = 5000

if len(sys.argv) >= 3:
    ip = str(sys.argv[2])
else:
    ip = '150.150.0.2'

server = xmlrpc.Server((ip, port))

server.add_method(construirFloat)
server.add_method(divisionReales)
server.add_method(fechaHora)
server.add_method(xor)
server.add_method(dias)
server.add_method(timeout)
server.add_method(holaMundo)
server.add_method(concatStringEntero)
server.add_method(echo)

server.serve()