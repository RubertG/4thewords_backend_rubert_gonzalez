# Prueba técnica desarrollador fullstack

- Tiempo límite: 72 horas desde que se hace entrega de la prueba.

## Descripción

Para el puesto de desarrollador fullstack se necesita que el candidato demuestre un
conocimiento en el uso de los lenguajes de programación Python y Javascript, así
como tener bases en el uso de frameworks como FastAPI, Vue.js y/o React, a su vez
se estará evaluando sus conocimientos en base de datos con MySQL. Se tomará en
cuenta el uso de librerías CSS como Tailwind o Bootstrap y ORM como sqlmodel.
Tomando en cuenta lo anteriormente descrito, se le solicita al candidato que desarrolle
una solución para el caso planteado en este documento, utilizando las tecnologías
anteriormente mencionadas. Durante la entrevista, al candidato se le hará preguntas
sobre el código y deberá contestarlas lo más claro y conciso posible.

## Caso de desarrollo

Se necesita construir un libro virtual de leyendas costarricenses, este libro consta de
una lista de cada una de las leyendas típicas de Costa Rica. Cada una de las leyendas
debe incluir:

- Una imagen relativa a la leyenda
- Nombre
- Categoría
- Texto descriptivo
- Fecha de la leyenda
- Provincia, cantón y distrito
- Además de cualquier otro dato que el desarrollador considere adicionar.

A dicha lista se le debe poder agregar más leyendas mediante un formulario, así como
poder actualizar la información de cada una mediante un formulario que precarga la
información de la leyenda y permite su edición, además debe poder eliminar leyendas.

## Requerimientos

1. La imagen debe ser subida por medio de un input tipo file. Dicha imagen debe ser subida al proyecto creado por el candidato o a un host de imágenes externo y guardar la URL en la base de datos. La imagen debe ser recuperada para
cada una de las leyendas en la lista. 

2. La fecha de creación debe ser subida con formato de fecha y se debe recuperar para cada una de las leyendas en la lista como una fecha relativa.

3. Los formularios deben tener validaciones que eviten que la aplicación se caiga y que permitan que la experiencia de usuario sea agradable.

4. Es necesario que la lista de leyendas se pueda filtrar por nombre, categoría, fecha, provincia, cantón y distrito.

5. Para la eliminación de las leyendas se debe de pasar por una confirmación antes de eliminarla realmente.

6. Para la creación de la lista de leyendas, el formulario de creación y el formulario de edición se debe utilizar el framework de Vue.js 3 (preferiblemente) o React. El proyecto debe levantarse de forma local en el puerto 3000.

7. La aplicación debe tener cambio entre pantallas, esto quiere decir que se necesita una pantalla para la lista, una para el formulario de creación y una para el formulario de edición. Para esto se solicita usar vue-router para Vue o
react-router para React.

8. Es necesario la creación de componentes para maximizar la reutilización de código en las distintas pantallas. Ejemplos de componentes: Input, botones, dropdowns, date picker, modales, etc.

9. Para la creación del API se debe utilizar Python con el framework FastAPI. Para cada uno de los endpoints se tomará en cuenta el manejo de excepciones, el orden del código, documentación y la buena reutilización del código. El proyecto debe levantarse de forma local en el puerto 8080.

10. Las leyendas deben ser almacenadas en una base de datos MySQL. Se debe generar un archivo .sql que tenga el script necesario para la creación de la base de datos y deberá ser subido con el proyecto del backend. Dicha base de datos debe tener el nombre de 4thewords_prueba_nombre_apellido (siendo nombre y apellido los del candidato) y debe tener al menos 10 leyendas registradas con anterioridad.

11. El frontend debe comunicarse con el backend por medio de solicitudes HTTP (REST API) usando el formato JSON para la información que se envía o se solicita.

12. Los proyectos deben subirse a GitHub con el nombre de 4thewords_frontend_nombre_apellido y 4thewords_backend_nombre_apellido (siendo nombre y apellido los del candidato). Cada uno de los repositorios debe tener en un README.md con las instrucciones necesarias para levantar cada proyecto y se debe compartir el link de los repositorios al correo indicado.

13. Está prohibido el uso de cualquier IA (inteligencia artificial) para el desarrollo parcial o total del proyecto.
Aclaraciones y notas adicionales.

El diseño de la interfaz queda a criterio del desarrollador, sin embargo se evaluará el orden y buenas prácticas del HTML, CSS y Javascript, además de la capacidad responsiva que tenga la aplicación.

El objetivo fundamental de esta prueba es que usted demuestre que puede utilizar las tecnologías antes mencionadas para construir una pequeña aplicación, por favor: NO CONSIDERAR NINGUNA COMO OPCIONAL, la prueba debe reflejar que usted puede investigar, aprender, combinar tecnologías y entregar una solución básica compuesta por todas ellas.
Buena suerte y esperamos que obtenga los mejores resultados