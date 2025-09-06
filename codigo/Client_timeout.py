import xmlrpc_redes as xmlrpc
import datetime
import sys

if len(sys.argv) >= 2:
    sv1_port = int(sys.argv[1])
else:
    sv1_port = 5000
if len(sys.argv) >= 3:
    sv1_ip = str(sys.argv[2])
else:
    sv1_ip = '150.150.0.2'

conn1 = xmlrpc.Client.connect(sv1_ip, int(sv1_port))
print(f'Conexión establecida con {sv1_ip}:{sv1_port}')

resultado6 = conn1.timeout()
print(f'conn1.timeout() = {resultado6}')
assert resultado6 == True, f'Error en conn1.timeout: {resultado6} != True'