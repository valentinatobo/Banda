# APLICACIÓN DE PRINCIPIOS SOLID AL PROGRAMA BANDA ALEATORIA 
----------------------------------------------------------------------------------------------------------------------------------------

La idea principal del programa es gestionar a los musicos e instrumentos de una banda de forma aleatoria, los cuales asistiran a una serenata para la cual fueron contratados, hay que tener en cuenta que por distintas razones personales no todos los musicos estaran disponibles para la presentación, así mismo cada musico tiene la disponibilidad de tocar cualquiera de los  5 instrumentos disponibles en la banda, en el momento que estos lleguen la banda se preparara y tocara. 

## ¿QUÉ SON LOS PRINCIPIOS SOLID?
----------------------------------------------------------------------------------------------------------------------------------------

SOLID es un acrónimo mnemónico introducido por Robert C. Martin a comienzos de la década del 2000 que representa cinco principios básicos de la programación orientada a objetos y el diseño.

![Principios Solid](https://github.com/valentinatobo/Banda/blob/master/img/solid.jpg)

## Aplicación de los Principios SOLID al Proyecto Banda Aleatoria
----------------------------------------------------------------------------------------------------------------

Este proyecto se dividira en dos fases, la primera sera la parte del diseño la cual estara encargada del diseño del diagrama de clases en el lenguaje unimicado de modelaje(uml) y el poder implementar en este diseño minimos tres principios SOLID, en su segunda parte ira dirigido a la implementación. 

## Diagrama de clases 
----------------------------------------------------------------------------------------------------------------

![Diagrama de clases](https://github.com/valentinatobo/Banda/blob/master/img/uml.JPG)

## ¿Qué principios usaremos en el proyecto?
----------------------------------------------------------------------------------------------------------------

### Principio de Inversión de Dependencias
**1. Definición:**
El principio establece:

* Los módulos de alto nivel no deberían depender de los módulos de bajo nivel. Ambos deberían depender de abstracciones (interfaces).
* Las abstracciones no deberían depender de los detalles. Los detalles (implementaciones concretas) deben depender de abstracciones.

**2. Aplicación en el Proyecto:**

Para este caso el principio se vera reflejado en la clase Instrumentos pues esta tiene una relación de herencia con la clase de cada instrumento teniendo como objetivo que cada instrumento dependa de esta clase y no la clase de los instrumentos permitiendo que sea flexible con fácil extensión.

### Open/Closed 

**1. Definición:**

Este principio tiene como fin que nuestra entidad (modulo/clase/funcion) debe estar abierta a la extensión pero cerrada a la modificación, se deben crear clases que tengan metodos que se usan de forma general pero con el desarrollo del programa no tenga que modificarse si no con cada clase nueva se integre esta.

**2. Aplicación en el Proyecto:**

Para este caso el principio se vera reflejado en la creación de la clase Intrumentos pues una vez que queramos agregar una nueva clase de tipo intrumento se podra hacer la extensión implementando el metodo y la herencia en esta nueva clase sin necesidad de modificar el codigo original logrando así la integración.

###  Responsabilidad Unica 

**1. Definición:**
La idea de este principio es fácil de entender, pero conforme un programa se va haciendo más grande, es más difícil de implementar. Lo que nos pide este principio es que cada clase debe tener una unica responsabilidad, por lo que si estamos programando una clase que se ocupa de diferentes cosas es conveniente partirla en 2 o más clases.

**2. Aplicación en el Proyecto:**

Para este caso el principio se vera reflejado en las clases instrumento, musico y banda pues cada uno tiene una responsabilidad diferente enfocada a lo que deben hacer respectivamente, en el caso del intrumento nos muestra cada instrumento, en la parte del musico le asignamos un intrumento el cual preparara para posterior mente tocarlo, en la clase de la banda lo que se hace es crear la banda con cada musico disponible, la prepara y toca la serenata.


### Sustitución de Liskov 

**1. Definición:**
Este principio nos dice que si en alguna parte de nuestro código estamos usando una clase, y esta clase es extendida, tenemos que poder utilizar cualquiera de las clases hijas y que el programa siga siendo válido. Esto nos obliga a asegurarnos de que cuando extendemos una clase no estamos alterando el comportamiento de la padre.

## Autores 
-Diana Valentina Uscategui Tobo 20172020063
-Edwin Andres Salinas Chaparro - 20172020087

## Información Adicional
