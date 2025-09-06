#!/usr/bin/env python3
import subprocess
import xml.dom.minidom

xml_body = """<?xml version="1.0"?>
<methodCall>
  <methodName>construirFloat</methodName>
  <params>
    <param>
      <value><int>3</int></value>
    </param>
    <param>
      <value><int>14</int></value>
    </param>
  </params>
</methodCall>"""

curl_command = [
    "curl",
    "-X", "POST",
    "-H", "Content-Type: text/xml",
    "-H", "User-Agent: MiCliente/1.0",
    "-d", xml_body,
    "http://127.0.0.1:5000/RPC2"
]

try:
    result = subprocess.run(
        curl_command, capture_output=True, text=True, check=True
    )
    
    # Pretty print de la salida XML
    dom = xml.dom.minidom.parseString(result.stdout)
    pretty_xml = dom.toprettyxml(indent="  ")
    
    print("Salida del comando:")
    print(pretty_xml)    
    
except subprocess.CalledProcessError as e:
    print("El comando falló con código:", e.returncode)
    print("STDOUT:", e.stdout)
    print("STDERR:", e.stderr)

print("----------------------------------------------------------------------------")

#Protocolo no soportado: use HTTP/1.1
#Método no permitido: use POST
#Content-Type debe ser text/xml
#User-Agent requerido
#Host incorrecto
#Content-Length requerido
#Error parseo de XML: ...

xml_body2 = """<?xml version="1.0"?>
<methodCall>
  <methodName>construirFloat</methodName>
  <params>
    <param>
      <value><int>3</int></value>
    </param>
    <param>
      <value><int>14</int></value>
    </param>
  </params>
</methodCall>"""

curl_command2 = [
    "curl",
    "-X", "GET",
    "-H", "Content-Type: text/xml",
    "-H", "User-Agent: MiCliente/1.0",
    "-d", xml_body2,
    "http://127.0.0.1:5000/RPC2"
]

try:
    result = subprocess.run(
        curl_command2, capture_output=True, text=True, check=True
    )
    
    # Pretty print de la salida XML
    dom = xml.dom.minidom.parseString(result.stdout)
    pretty_xml = dom.toprettyxml(indent="  ")
    
    print("Salida del comando:")
    print(pretty_xml)    
    
except subprocess.CalledProcessError as e:
    print("El comando falló con código:", e.returncode)
    print("STDOUT:", e.stdout)
    print("STDERR:", e.stderr)