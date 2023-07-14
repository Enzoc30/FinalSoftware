# FinalSoftware

### Ejecuta el siguiente comando para iniciar la aplicación:

 ```
  set APP=main.py
  flask --app main.py run
 ```
  O también 

```
  py main.py
 ```


# Pregunta 3

Se implementaria una condicion y varias validaciones en varias partes del codigo, para que haya un limite de de transferencias por dia, validando el monto y el dia en el que se hace
Ademas de tener un mensaje definido de como avisarle al usuario de que ya no tiene que hacer mas transferencia por hoy
Y tambien tener como un aviso previo cuando el usuario este por llegar al maximo


Se cambiaria en la parte de operaciones porque se hace transacciones
Un metodo nuevo para la verificacion de transferencias por dia


Tambien de no ingresar montos negativos, o montos excesivos o montos minimos menores a un sol

Hay mucho riesgo de romper la aplicacion por el momento, porque se necesita muchas verificaciones y pruebas en las que se verifique la efectividad del codigo

Tambien se puede mejorar esa parte si es que el codigo se vuelve mucho mas consistente y se mejora mucho las buenas practicas (code smells)

Realizar cambios en el código siempre implica algún grado de riesgo, pero siguiendo buenas prácticas de desarrollo como realizar test, se puede reducir el riesgo y garantizar que el software funcione.

