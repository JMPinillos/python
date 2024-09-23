# Formulas para aproximaciones a puntos

## Truco absoluto

El truco absoluto funciona empezando por un punto y una línea.

- Un punto con coordenadas $(p,q)$.
- Una línea representada por $y=w_1 \cdot x+w_2$.

Para acercar la línea al punto $(p,q)$ El truco absoluto tiene dos pasos:

- Añade a la intersección con el eje $Y$ y para que la línea se mueva hacia arriba.
- Añade a la pendiente para hacer que la línea gire en la dirección del punto.

El primer paso posible es agregar 1 a la intersección con el eje $y$ y $p$ a la pendiente, dándonos la ecuación $y=(w_1+p)𝑥+(w_2+1)$.

Esto termina siendo un paso demasiado grande, y hemos corregido en exceso nuestra línea. En su lugar, utilizaremos un pequeño número llamado **tasa de aprendizaje**, conocido como alfa ($\alpha$), para dar pasos más pequeños.

Añadiremos ($1 \alpha$) a la intersección con el eje $Y$, y ($p \alpha$) a la pendiente. Esto nos da la ecuación:


$$
y = (w_1 + p \alpha) \cdot x + (w_2 + \alpha)
$$
Esto funciona cuando el punto $(p,q)$ está por encima de la línea, pero cuando el punto está por debajo de la línea, necesitamos **restar** para mover la línea correctamente.
$$
y = (w_1 - p \alpha) \cdot x + (w_2 - \alpha)
$$


### Ejemplo

Digamos que tenemos el punto $(5,15)$ y la línea $𝑦=2𝑥+3$ y una tasa de aprendizaje de $0,1$.

- **Actualizar la pendiente**: Tomamos $5$, lo multiplicamos por $0,1$ y lo añadimos a la pendiente existente, lo que nos da una nueva pendiente de $2,5$.
- Actualizamos la intersección con el eje y añadiendo $0,1$, lo que nos da una nueva intersección con el eje y de $3,1$.

Esto significa que nuestra nueva ecuación es $𝑦=2,5𝑥+3,1$.

Si nuestro punto fuera ($−5,15$), añadiríamos $0,1$ a la intersección con el eje $y$ para mover la línea hacia arriba, pero actualizamos la pendiente multiplicando $-5 \cdot 0,1$. Esto significa que nuestra nueva ecuación va a ser $𝑦=1,5𝑥+2,9$.



## Optimización de mínimos cuadrados

Si tenemos un punto que está cerca de una línea, entonces la distancia es pequeña y queremos mover la línea muy poco. Si el punto está lejos de la línea, quieren mover la línea mucho más. El truco absoluto no tiene en cuenta la distancia a la que se encuentra el punto de la línea.

El truco del cuadrado aborda esto.

Veamos esta distancia vertical entre el punto y la línea. El punto sobre la línea tiene coordenadas $(p,q)$ y el punto correspondiente de la recta es $(p,q′)$.

La distancia entre el punto y la línea es ($𝑞−𝑞′$).

Tomamos esta distancia y la multiplicamos por lo que añadimos tanto a la intersección con el eje y como a la pendiente.

- Actualice la intersección con el eje y agregando $\alpha \cdot(q−q′)$.
- Actualice la pendiente agregando $p \cdot\alpha \cdot(q−q′)$.

Esto nos da la ecuación
$$
y = ( w_1 + p (q − q') \cdot \alpha) \cdot x + (w_2 + (q − q′) \cdot α)
$$
Este truco se encarga automáticamente de los puntos que están por debajo de la línea y no necesitamos dos reglas como teníamos en el truco absoluto. Simplemente tenemos la misma regla para ambos.



### Ejemplo

Digamos que tenemos el punto $(5,15)$ y la línea $𝑦=2𝑥+3$ (lo que nos da $𝑞′= 2 \cdot 5 + 313$) y una tasa de aprendizaje de 0,01. Observa que esta tasa de aprendizaje es menor que el ejemplo que usamos para el truco absoluto.

- **Actualiza la pendiente**: Tomamos $5$ y lo multiplicamos por $0,01$, y luego multiplicamos este valor por $2$ antes de agregar el resultado a la pendiente existente, lo que nos da una nueva pendiente de $2,1$.
- Actualice la intersección con el eje y agregando $0,012$, lo que nos da una nueva intersección con el eje y de $3,02$

Esto significa que nuestra nueva ecuación es $𝑦=2,1𝑥+3,02$.
