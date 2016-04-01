from django.test import TestCase
# Pruebas para la API coleccion y creacion
# curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/apiproducto/
# curl -H 'Accept: application/json; indent=4' -X POST http://127.0.0.1:8000/apiproducto/ -d '{"producto":"carro", "precio":"15000", "descripcion":"marca mattel"}'

# Pruebas para la API un elemento
# curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/apiproducto/2
