#!/usr/bin/env python3
import subprocess
import sys
import xml.dom.minidom

if len(sys.argv) >= 2:
    port = int(sys.argv[1])
else:
    port = 5000
if len(sys.argv) >= 3:
    host = str(sys.argv[2])
else:
    host = '127.0.0.1'

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
    f'http://{host}:{port}/RPC2'
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

curl_commands = []
#Protocolo no soportado: use HTTP/1.1
curl_command = [
    "curl",
    "--http1.0",
    "-X", "POST",
    "-H", "Content-Type: text/xml",
    "-H", "User-Agent: MiCliente/1.0",
    "-d", xml_body,
    f'http://{host}:{port}/RPC2'
]
curl_commands.append(curl_command)

#Método no permitido: use POST
curl_command2 = [
    "curl",
    "-X", "GET",
    "-H", "Content-Type: text/xml",
    "-H", "User-Agent: MiCliente/1.0",
    "-d", xml_body,
    f'http://{host}:{port}/RPC2'
]
curl_commands.append(curl_command2)

#Content-Type debe ser text/xml
curl_command3 = [
    "curl",
    "-X", "POST",
    "-H", "Content-Type: application/json",
    "-H", "User-Agent: MiCliente/1.0",
    "-d", xml_body,
    f'http://{host}:{port}/RPC2'
]
curl_commands.append(curl_command3)

#User-Agent requerido
curl_command4 = [
    "curl",
    "-X", "POST",
    "-H", "Content-Type: text/xml",
    "-H", "User-Agent: ",
    "-d", xml_body,
    f'http://{host}:{port}/RPC2'
]
curl_commands.append(curl_command4)

#Host incorrecto
curl_command5 = [
    "curl",
    "-X", "POST",
    "-H", "Host: 1234",
    "-H", "Content-Type: text/xml",
    "-H", "User-Agent: MiCliente/1.0",
    "-d", xml_body,
    f'http://{host}:{port}/RPC2'
]
curl_commands.append(curl_command5)

#Content-Length requerido
curl_command6 = [
    "curl",
    "-X", "POST",
    "-H", "Content-Length: ",
    "-H", "Content-Type: text/xml",
    "-H", "User-Agent: MiCliente/1.0",
    "-d", xml_body,
    f'http://{host}:{port}/RPC2'
]
curl_commands.append(curl_command6)

#Error parseo de XML: ...
xml_body_malo = """<?xml version="1.0"?>
<methodCall>
    </param>
  </params>
</methodCall>"""
curl_command6 = [
    "curl",
    "-X", "POST",
    "-H", "Content-Type: text/xml",
    "-H", "User-Agent: MiCliente/1.0",
    "-d", xml_body_malo,
    f'http://{host}:{port}/RPC2'
]
curl_commands.append(curl_command6)


for curl_command in curl_commands:
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