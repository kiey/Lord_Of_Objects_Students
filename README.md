# The Lord of Objects

Se quiere implementar un programa que gestione los diferentes habitantes de la Tierra Media.

Los diferentes habitantes de la Tierra Media son:

- Humanos
- Elfos
- Enanos
- Hobbits
- Magos

Los Enanos disponen de 100 puntos de salud cuando son creados. Un enano puede *Beber* para recuperar 20 puntos de salud. Además, los enanos disponen de 10 monedas (*dinero*) al ser creados. Pueden conseguir más dinero de dos formas:

- *Minar*: Aumenta el dinero en 1 punto.
- Usar su *Codicia*: Aumenta su dinero en 5 puntos a cambio de su salud que se reduce en 10 puntos.

Los Humanos disponen de 100 puntos de salud cuando son creados. Un humano puede *Beber* para recuperar 10 puntos de salud.  Además los humanos disponen de 10 monedas (*dinero*) al ser creados. Pueden conseguir más dinero solo con su *codicia*, Aumenta su dinero en 5 puntos a cambio de su salud que se reduce en 10 puntos. Los humanos también pueden luchar, para ello pueden *atacar* a otro habitante de la Tierra Media quitándole 10 puntos de salud.

Los Elfos disponen de 100 puntos de salud cuando son creados. Un Elfo puede *Beber* para recuperar 10 puntos de salud. Los elfos no disponen de dinero. Los elfos también pueden luchar, para ello pueden *disparar_flecha* dañando con 10 puntos de salud a su enemigo. Un elfo dispone de 10 flechas cuando es creado, y debe *recargar* antes de poder disparar una flecha. En caso de que se intente disparar una flecha con un elfo que no ha recargado se deberá lanzar una excepción *FlechaNoPreparada*.

Los Hobbits disponen 100 puntos de salud cuando son creados. Un hobbit puede *Beber* para recuperar 10 puntos de salud o puede comer para recuperar todos los puntos de salud perdidos.

Los Orcos disponen de 100 puntos de salud cuando son creados. Un Orco puede *Beber* para recuperar 10 puntos de salud. Los orcos también pueden luchar, para ello pueden *atacar* a otro habitante de la Tierra Media quitándole 10 puntos de salud.

Los Magos no son mortales por lo que no tienen puntos de salud. Un Mago puede *sanar* a otro habitante de la Tierra Media devolviéndole todos sus puntos de salud. Por otro lado, un mago puede crear una compañia. Para ello, primero debe añadir un hobbit a la compañia usando *anadir_miembro_compania*. En caso de que se intente crear una compañia sin un hobbit primero se deberá lanzar al excepción *CompaniaSinHobbit*. Una compania no puede tener orcos como miembros, si se intenta añadir un orco a la compañia se deberá lanzar la excepción *OrcoEnCompania*

Ningún mortal puede tener más de 100 puntos de salud.

Todos los atributos deben implementarse como propiedades privadas, y se deben usar @property para implementar sus getters y setters.

Cualquier parecido con la obra de J.R.R. Tolkien es pura coincidencia.

## Evaluación

La evaluación vendrá dada por el número de tests superados:

La nota de la actividad se desglosa de la siguiente forma:
    

- 6p Tests unitarios
  
- 2p Tests de integracion
  
- 2p Tests de excepciones



## Instalación en linux

Instalación de Visual Studio Code

```
snap install --classic code
```

Instalación de pytest

```
sudo apt-get install python3-pytest
```

Descarga del repositorio

```
git clone https://github.com/kiey/universidad_estudiantes
```

Abrir el repositorio

```
cd universidad_estudiantes
code .
```

Ejecutar los tests

```
pytest-3 test.py
```

Consultar la nota actual

```
python3 nota.py
```