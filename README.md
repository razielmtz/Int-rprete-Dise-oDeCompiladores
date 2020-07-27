# Interprete-DisenoDeCompiladores

## Introduccion
Este es un proyecto escolar creado para poder entender mejor el funcionamiento de un compilador y hacer nuestro propio lenguaje aunque no sea practico usarlo. Por esos mismos motivos decidimos cambiar las palabras clave por simbolos.

## Uso
Para poder usar el programa hay que correr el archivo shell.py utilizando python3.

```bash
python3 shell.py
```

Una vez empezado, la consola permitira el uso del lenguaje mediante comandos de una linea en los cuales se puede simular un salto de linea utilizando el simbolo ';'.

Para correr un script completo se debe utilizar el comando RUN seguido del nombre del archivo de texto en el cual se hizo el programa.

```python3
RUN("test")
```

## Tabla de Simbolos
| Funcionalidad  | Simbolo  |
|----------------|----------|
|   IF           |    ?     |
|   ELSEIF       |    ??    |
|   ELSE         |    ???   |
|   AND          |    &     |
|   OR           |  &#124;  |
|   NOT          |    !     |
|   THEN         |    -->   |
|   WHILE        |    ---   |
|   FOR          |    +++   |
|   VAR          |    $     |
|   FUNCTION     |    @     |
|   END          |    @@    |
|   RETURN       |    >>>   |
