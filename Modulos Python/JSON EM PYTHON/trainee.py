#Aprendendo JSON em Python

from dados import dic_clientes
import json

json_dum = json.dumps(dic_clientes, indent=4)

print(json_dum)
