import sys
import xmlrpc_redes as xmlrpc
import datetime
import time

def construirFloat(a, b):
    aux = f'{a}.{b}'
    return float(aux)

def divisionReales(a, b):
    return a/b

def fechaHora(d, m, a, hh, mm, ss):
    return datetime.datetime(a, m, d, hh, mm, ss)

def xor(a, b):
    return not ((a and b) or (not a and not b))

def dias(f1, f2):
    return abs((f1-f2).days)

def timeout():
    time.sleep(8)
    return True

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
    ip = '127.0.0.1'

server = xmlrpc.Server((ip, port))

server.add_method(construirFloat)
server.add_method(divisionReales)
server.add_method(fechaHora)
server.add_method(xor)
server.add_method(dias)
server.add_method(timeout)

server.serve()