# Proyecto Final CoderHouse MatiasDamiani

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

# Superusuario:
username:admin
contraseña:admin

## Instrucciones para entrar al panel aministrativo de Django
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```
+ En consola, si deseas cambiar el superuser, con un nuevo username y contraseña:
```
python manage.py createsuperuser
```
# Unit Test Perfiles:
para ejecutar el test se debe utilizar el comando
```
python manage.py test perfiles
```
El UnitTest realizará dos test, la creación de un usuario exitoso y un usuario rechazado.


