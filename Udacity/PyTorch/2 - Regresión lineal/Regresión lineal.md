# Regresión lineal

La **regresión lineal** es una técnica de modelado estadístico que se utiliza para describir la relación entre una variable dependiente yyy y una o más variables independientes xxx. En la **regresión lineal simple**, tenemos una variable dependiente y una sola variable independiente.

La ecuación general de una línea recta es:
$$
y = w_1 \cdot x + w_2
$$
Donde:

- $y$ es la variable dependiente (el valor que queremos predecir).
- $x$ es la variable independiente (el valor que utilizamos para hacer la predicción).
- $w_1$ es la pendiente de la línea (indica cuánto cambia $y$ por cada cambio unitario en $x$).
- $w_2$ es la intersección en el eje $y$ (el valor de $y$ cuando $x = 0$).

El objetivo de la regresión lineal es encontrar los valores de $w_1$ y $w_2$ que minimicen la diferencia entre los valores observados $y$ y los valores predichos por la línea recta.



### Ejemplo de Regresión Lineal Simple

Vamos a realizar una regresión lineal simple usando un conjunto pequeño de datos que describe la relación entre el número de horas de estudio y la calificación obtenida en un examen. Los datos son los siguientes:

| Horas de Estudio ($x$) | Calificación ($y$) |
| ---------------------- | ------------------ |
| 1                      | 2                  |
| 2                      | 3                  |
| 3                      | 4                  |
| 4                      | 5                  |
| 5                      | 6                  |

En este caso:
- $x$ es el número de horas de estudio (variable independiente).
- $y$ es la calificación obtenida en el examen (variable dependiente).



#### Paso 1: Calcular la pendiente $w_1$ y la intersección $w_2$

La fórmula para calcular la pendiente $w_1$ es:


$$
w_1 = \dfrac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}
$$
Donde:
- $n$ es el número de puntos de datos.
- $\sum xy$ es la suma del producto de cada $x$ y $y$.
- $\sum x$ es la suma de los valores de $x$.
- $\sum y$ es la suma de los valores de $y$.
- $\sum x^2$ es la suma de los cuadrados de los valores de $x$.



Calculemos cada uno de estos valores:

- $\sum x = 1 + 2 + 3 + 4 + 5 = 15$
- $\sum y = 2 + 3 + 4 + 5 + 6 = 20$
- $\sum xy = (1 \cdot 2) + (2 \cdot 3) + (3 \cdot 4) + (4 \cdot 5) + (5 \cdot 6) = 70$
- $\sum x^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55$
- $n = 5$

Ahora sustituimos estos valores en la fórmula de $w_1$:

$w_1 = \dfrac{(5 \cdot 70) - (15 \cdot 20)}{(5  \cdot 55) - 15^2} = \dfrac{350 - 300}{275 - 225} = \dfrac{50}{50} = 1$

Por lo tanto, la pendiente $w_1 = 1$.



#### Paso 2: Calcular la intersección $w_2$

La fórmula para calcular la intersección $w_2$ es:

$$
w_2 = \dfrac{\sum y - w_1 \sum x}{n}
$$
Sustituyendo los valores que ya calculamos:

$w_2 = \dfrac{20 - (1 \cdot 15)}{5} = \dfrac{20 - 15}{5} = \dfrac{5}{5} = 1$

Por lo tanto, la intersección $w_2 = 1$.



#### Paso 3: Ecuación final de la recta

Sustituyendo los valores de $w_1$ y $w_2$ en la ecuación de la recta:

$$
y = 1x + 1 = x + 1
$$
Esta es la ecuación que describe la relación entre el número de horas de estudio y la calificación obtenida.



### Interpretación

La ecuación $y = 1x + 1$ nos dice que:
- Por cada hora adicional de estudio, la calificación aumenta en 1 punto.
- Si no se estudia $x = 0$, se espera que la calificación sea 1 (intersección).

Este es un ejemplo simple de cómo se puede calcular y aplicar una regresión lineal para predecir resultados a partir de datos.



## Gradiente Descendente para la Regresión Lineal (Truco Absoluto)

El **gradiente descendente** es un método de optimización utilizado para ajustar los parámetros de un modelo, en este caso, una línea de regresión lineal, con el objetivo de minimizar el error entre las predicciones y los datos observados. Este es un proceso iterativo en el que se modifican los parámetros de la recta (la pendiente $w_1$ y la intersección $w_2$) en pasos pequeños, determinados por una tasa de aprendizaje $\alpha$, hasta que la línea se ajuste lo mejor posible a los puntos de datos.



### Elementos iniciales

- Tenemos un **punto** con coordenadas $(p, q)$.
- Una **línea** que está representada por la ecuación general de una recta:

$$
y = w_1 \cdot x + w_2
$$

Donde:

- $w_1$ es la pendiente de la línea.
- $w_2$ es la intersección en el eje $y$.



El objetivo es ajustar la recta para que pase más cerca del punto $(p, q)$. Para lograr esto, el truco absoluto realiza dos ajustes:
1. **Mover la línea hacia arriba o hacia abajo** añadiendo un valor a la intersección con el eje $y$.
2. **Girar la línea** ajustando su pendiente para acercarla más al punto.



### Paso inicial (ajuste directo)

Imaginemos que para acercar la línea al punto $(p, q)$, simplemente sumamos 1 a la intersección con el eje $y$ y $p$ a la pendiente. Esto da lugar a la siguiente nueva ecuación para la línea:
$$
y = (w_1 + p) \cdot x + (w_2 + 1)
$$
Este ajuste hace que la línea se acerque rápidamente al punto, pero el problema es que el cambio es **demasiado grande**, lo que puede resultar en una sobrecorrección.

### Introducción de la tasa de aprendizaje $(\alpha)$

Para evitar grandes correcciones y mejorar el ajuste de la línea, introducimos un pequeño valor llamado **tasa de aprendizaje**, representado por $\alpha$. La tasa de aprendizaje nos permite hacer ajustes más graduales a los parámetros de la recta.

En lugar de sumar directamente 1 a la intersección y $p$ a la pendiente, ahora sumamos pequeñas fracciones de estos valores, multiplicándolos por $\alpha$.

La nueva ecuación de la recta con tasa de aprendizaje es:

$$
y = (w_1 + p \cdot \alpha) \cdot x + (w_2 + \alpha)
$$



#### Caso cuando el punto está por debajo de la línea

Si el punto $(p, q)$ está por **debajo** de la línea, necesitamos mover la línea hacia abajo. Esto se logra **restando** los términos en lugar de sumarlos. La ecuación para este caso es:

$$
y = (w_1 - p \cdot \alpha) \cdot x + (w_2 - \alpha)
$$


### Ejemplo

> Tenemos el punto $(5,15)$, la línea $𝑦=2𝑥+3$ y una tasa de aprendizaje de $0,1$.



#### Primer punto: $(5, 15)$ y la línea $y = 2x + 3$

1. **Ecuación inicial**:

   La línea que tenemos inicialmente es $y = 2x + 3$. 
   Aquí, $w_1 = 2$ es la pendiente y $w_2 = 3$ es la intersección con el eje $y$.

   

2. **Actualizar la pendiente**:

   Usamos el valor $p = 5$ (la coordenada $x$ del punto $(5, 15)$) para actualizar la pendiente $w_1$.

   Según el gradiente descendente, multiplicamos $p$ por la tasa de aprendizaje $\alpha = 0.1$:
   $$
   \text{Nuevo } w_1 = w_1 + p \cdot \alpha = 2 + 5 \cdot 0,1 = 2 + 0,5 = 2,5
   $$
   
3. **Actualizar la intersección**:

   Sumamos $\alpha = 0.1$ a la intersección $w_2$:

   $$
   \text{Nuevo } w_2 = w_2 + \alpha = 3 + 0,1 = 3,1
   $$
   
4. **Nueva ecuación de la recta**:

   La nueva ecuación, después de las actualizaciones, es:

   $$
   y = 2,5x + 3,1
   $$



#### Segundo punto: $(-5, 15)$

Ahora usamos el punto $(-5, 15)$ para actualizar la línea.

1. **Actualizar la pendiente**:

   Usamos el valor $p = -5$ (la coordenada $x$ del punto $(-5, 15)$). Multiplicamos $p$ por la tasa de aprendizaje $\alpha = 0.1$:

   $$
   \text{Nuevo } w_1 = w_1 + p \cdot \alpha = 2 + (-5) \cdot 0,1 = 2 - 0,5 = 1,5
   $$
   
2. **Actualizar la intersección**:

   Sumamos $\alpha = 0.1$ a la intersección $w_2$ para mover la línea hacia arriba:

   $$
   \text{Nuevo } w_2 = w_2 - \alpha = 3 - 0,1 = 2,9
   $$
   
3. **Nueva ecuación de la recta**:

   La nueva ecuación, después de estas actualizaciones, es:

   $$
   y = 1,5x + 2,9
   $$



## Optimización de mínimos cuadrados (Truco del cuadrado)

La **optimización de mínimos cuadrados** es un método utilizado para ajustar los parámetros de una línea (pendiente $w_1$ e intersección $w_2$) con el objetivo de minimizar la **suma de los errores al cuadrado** entre los puntos observados y los valores predichos por la línea. Este método tiene en cuenta no solo la dirección del ajuste, sino también la **magnitud de la diferencia** entre el punto y la línea, lo que permite un ajuste proporcional a la distancia del punto a la línea.



### Elementos iniciales:

- **Punto:** $(p, q)$
- **Línea:** Representada por la ecuación:

$$
y = w_1 \cdot x + w_2
$$



A diferencia del **truco absoluto**, que ajustaba la línea de manera uniforme sin importar la distancia del punto a la línea, el **truco del cuadrado** tiene en cuenta la distancia vertical entre el punto $(p, q)$ y la línea, que es:
$$
q - q'
$$

Donde $q'$ es el valor predicho por la línea para el punto $p$, es decir, $q' = w_1 \cdot p + w_2$.



### Regla de actualización

Para ajustar la línea, el **truco del cuadrado** sigue las siguientes reglas:

1. **Actualizar la intersección:** Añadimos $\alpha \cdot (q - q')$ a la intersección $w_2$.

2. **Actualizar la pendiente:** Añadimos $p \cdot \alpha \cdot (q - q')$ a la pendiente $w_1$.

Esto nos da la siguiente fórmula de actualización para la recta ajustada:

$$
y = (w_1 + p \cdot (q - q') \cdot \alpha) \cdot x + (w_2 + (q - q') \cdot \alpha)
$$

Esta regla es única y se puede aplicar tanto si el punto está por **encima** como si está por **debajo** de la línea, sin necesidad de diferentes fórmulas como en el truco absoluto.



### Ejemplo

> Digamos que tenemos el punto $(5,15)$, la línea $𝑦=2𝑥+3$ y una tasa de aprendizaje de 0,01. 

Observa que esta tasa de aprendizaje es menor que el ejemplo que usamos para el truco absoluto.

- El valor de $q'$ para $p = 5$ se calcula como:

$$
q' = 2 \cdot 5 + 3 = 13
$$



- La distancia entre el punto y la línea es:

$$
q - q' = 15 - 13 = 2
$$



1. **Actualizar la pendiente:** Usamos $p = 5$ y calculamos:

$$
\text{Nuevo } w_1 = w_1 + p \cdot (q - q') \cdot \alpha = 2 + 5 \cdot 2 \cdot 0,01 = 2 + 0,1 = 2,1
$$



2. **Actualizar la intersección:** Añadimos $\alpha \cdot (q - q')$ a $w_2$:

$$
\text{Nuevo } w_2 = w_2 + (q - q') \cdot \alpha = 3 + 2 \cdot 0,01 = 3 + 0,02 = 3,02
$$



3. **Nueva ecuación de la recta:**

$$
y = 2,1x + 3,02
$$



## Descenso de Gradiente 

El **descenso de gradiente** es un método de optimización utilizado para ajustar los parámetros de un modelo, en este caso, una línea de regresión, con el objetivo de minimizar el **error** entre las predicciones y los datos observados. En otras palabras, el algoritmo busca la mejor solución para una función ajustando gradualmente los parámetros (como la pendiente y la intersección de una recta) en pasos pequeños, llamados **tasa de aprendizaje** ($\alpha$), en la dirección que reduce el error.



### Proceso paso a paso 

1. **Dibuja una línea inicial aleatoria.**
2. **Calcula el error** entre la línea y los puntos observados. Este error es una medida de qué tan lejos están los puntos de la línea, como el **error cuadrático medio**:

$$
  L(w_1, w_2) = \frac{1}{2n} \sum_{i=1}^{n} (y_i - (w_1 \cdot x_i + w_2))^2
$$



3. **Ajusta los parámetros** de la línea moviendo la pendiente $w_1$ y la intersección $w_2$ en la dirección que reduce el error. Esto se hace usando las derivadas parciales del error:

   - **Actualización de la pendiente**:
     $$
        w_1 = w_1 - \alpha \cdot \frac{\partial L}{\partial w_1}
     $$

   - **Actualización de la intersección**:
     $$
     w_2 = w_2 - \alpha \cdot \frac{\partial L}{\partial w_2}
     $$

 

4. **Repite el proceso**: en cada iteración, los parámetros se ajustan de manera que se reduce el error hasta que no haya mejoras significativas.

 

### Ejemplo

Supongamos que tenemos los puntos $(1, 2), (2, 3), (3, 4)$ y una línea inicial aleatoria $y = 0.5x + 1$. Vamos a aplicar el descenso de gradiente:

1. **Calculamos el error inicial** usando la línea aleatoria y el error cuadrático medio.
2. **Ajustamos la pendiente $w_1$ y la intersección $w_2$**. Después de calcular el gradiente, determinamos que debemos aumentar la pendiente y reducir la intersección.
3. **Recalculamos el error** y seguimos ajustando, moviéndonos en la dirección que minimiza el error.
4. **Repetimos el proceso** hasta que la línea se ajuste a los puntos. El modelo final podría ser algo cercano a $y = 1x + 1$, que ajusta los puntos mejor.

 

### Aplicación del Algoritmo 

El descenso de gradiente permite encontrar la **mejor línea** que se ajusta a los datos mediante ajustes iterativos, reduciendo gradualmente el error en cada paso. Es un método fundamental en la optimización de modelos de aprendizaje automático.

 



## Error Absoluto Medio (EAM) 

El **error absoluto medio** (EAM) es una métrica utilizada en la regresión lineal para medir qué tan lejos están las predicciones de los valores reales. En lugar de considerar los errores al cuadrado (como en el error cuadrático medio), el EAM toma la **diferencia absoluta** entre las predicciones y los valores observados, y luego hace el promedio de estas diferencias.

 

### Fórmula del Error Absoluto Medio

Dado un conjunto de datos con puntos $(x_i, y_i)$ y una línea que representa las predicciones $\hat{y}$, el **error absoluto medio** se calcula de la siguiente forma:
$$
\text{Error absoluto medio} = \frac{1}{m} \sum_{i=1}^{m} | y_i - \hat{y}_i |
$$
 Donde:

- $y_i$ son los valores reales de los puntos.
- $\hat{y}_i$ son las predicciones de la línea.
- $m$ es el número total de puntos.



El **error absoluto medio** mide qué tan lejos están, en promedio, las predicciones de los valores reales. Al usar el valor absoluto, se asegura que las diferencias negativas no cancelen las positivas, lo que haría que la métrica no reflejara correctamente el error total.

 

### <strong style="color:green">Ventajas del Error Absoluto Medio</strong>

- **Fácil de interpretar**: Es intuitivo porque mide el error en las mismas unidades que los datos originales.
- **No penaliza los grandes errores de manera tan fuerte** como el error cuadrático medio, lo cual puede ser una ventaja cuando no queremos que los grandes errores tengan demasiado peso.

 

### Ejemplo

> Calcule el **error absoluto medio** para la siguiente línea y puntos:
>
> - **Línea**: $y=1,2𝑥+2$
> - **Puntos**: $(2, -2)$, $(5, 6)$, $(-4, -4)$, $(-7, 1)$, $(8, 14)$



#### Paso 1: Calcular las predicciones $ \hat{y} $

Para cada punto, vamos a calcular el valor de $ \hat{y} $ usando la ecuación de la recta $ y = 1,2x + 2 $.

1. Para el punto $ (2, -2) $:

   $ \hat{y} = 1,2 \cdot 2 + 2 = 2,4 + 2 = 4,4 $

2. Para el punto $ (5, 6) $:

   $ \hat{y} = 1,2 \cdot 5 + 2 = 6 + 2 = 8 $

3. Para el punto $ (-4, -4) $:

   $ \hat{y} = 1,2 \cdot (-4) + 2 = -4,8 + 2 = -2,8 $

4. Para el punto $ (-7, 1) $:

   $ \hat{y} = 1,2 \cdot (-7) + 2 = -8,4 + 2 = -6,4 $

5. Para el punto $ (8, 14) $:

   $ \hat{y} = 1,2 \cdot 8 + 2 = 9,6 + 2 = 11,6 $



#### Paso 2: Calcular los errores absolutos

Ahora calculamos el error absoluto entre los valores reales $ y $ y las predicciones $ \hat{y} $ para cada punto:

1. Para el punto $ (2, -2) $:

   $ | y - \hat{y} | = | -2 - 4,4 | = | -6,4 | = 6,4 $

2. Para el punto $ (5, 6) $:

   $ | y - \hat{y} | = | 6 - 8 | = | -2 | = 2 $

3. Para el punto $ (-4, -4) $:

   $ | y - \hat{y} | = | -4 - (-2,8) | = | -4 + 2,8 | = | -1,2 | = 1,2 $

4. Para el punto $ (-7, 1) $:

   $ | y - \hat{y} | = | 1 - (-6,4) | = | 1 + 6,4 | = | 7,4 | = 7,4 $

5. Para el punto $ (8, 14) $:

   $ | y - \hat{y} | = | 14 - 11,6 | = | 2,4 | = 2,4 $

 

#### Paso 3: Calcular el error absoluto medio (EAM)

El error absoluto medio se calcula promediando todos los errores absolutos:
$$
\text{EAM} = \dfrac{6,4 + 2 + 1,2 + 7,4 + 2,4}{5} = \dfrac{19,4}{5} = 3,88
$$


Este método de error es simple y efectivo, pero al no penalizar tanto los grandes errores como el error cuadrático medio, puede ser más adecuado para ciertos tipos de problemas en los que se busca un ajuste general más que uno extremadamente preciso.

 

## Error Cuadrático Medio (ECM) 

 El **error cuadrático medio** (ECM) es una métrica utilizada en la regresión lineal para medir qué tan lejos están las predicciones de los valores reales. A diferencia del **error absoluto medio**, el ECM toma la diferencia entre la predicción y el valor observado, la eleva al cuadrado y luego calcula el promedio de esos valores cuadrados.

 

### Fórmula del Error Cuadrático Medio

Dado un conjunto de datos con puntos $(x_i, y_i)$ y una línea que representa las predicciones $\hat{y}_i$, el error cuadrático medio se calcula de la siguiente manera:
$$
\text{Error\ cuadrático\ medio} = \frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2
$$
Donde:

- $y_i$ son los valores reales de los puntos.
- $\hat{y}_i$ son las predicciones de la línea.
- $m$ es el número total de puntos.

 

El **ECM** mide el error al cuadrado, lo que significa que **penaliza más los errores grandes**. Esta métrica es útil porque amplifica los errores grandes, ayudando a detectar desviaciones importantes en las predicciones. Como los errores se elevan al cuadrado, el ECM nunca será negativo y siempre será cero cuando las predicciones sean perfectas.



### Ejemplo

> Calcule el **error absoluto medio** para la siguiente línea y puntos:
>
> - **Línea**: $y=1,2𝑥+2$
> - **Puntos**: $(2, -2)$, $(5, 6)$, $(-4, -4)$, $(-7, 1)$, $(8, 14)$



#### Paso 1: Calcular las predicciones $ \hat{y} $

Para cada punto, vamos a calcular el valor de $ \hat{y} $ usando la ecuación de la recta $ y = 1,2x + 2 $.

1. Para el punto $ (2, -2) $:

   $ \hat{y} = 1,2 \cdot 2 + 2 = 2,4 + 2 = 4,4 $

2. Para el punto $ (5, 6) $:

   $ \hat{y} = 1,2 \cdot 5 + 2 = 6 + 2 = 8 $

3. Para el punto $ (-4, -4) $:

   $ \hat{y} = 1,2 \cdot (-4) + 2 = -4,8 + 2 = -2,8 $

4. Para el punto $ (-7, 1) $:

   $ \hat{y} = 1,2 \cdot (-7) + 2 = -8,4 + 2 = -6,4 $

5. Para el punto $ (8, 14) $:

   $ \hat{y} = 1,2 \cdot 8 + 2 = 9,6 + 2 = 11,6 $



#### Paso 2: Calcular los errores cuadrados

Ahora calculamos el error cuadrático entre los valores reales $ y $ y las predicciones $ \hat{y} $ para cada punto:

1. Para el punto $ (2, -2) $:

   $ (y - \hat{y})^2 = (-2 - 4,4)^2 = (-6,4)^2 = 40,96 $

2. Para el punto $ (5, 6) $:

   $ (y - \hat{y})^2 = (6 - 8)^2 = (-2)^2 = 4 $

3. Para el punto $ (-4, -4) $:

   $ (y - \hat{y})^2 = (-4 - (-2,8))^2 = (-1,2)^2 = 1,44 $

4. Para el punto $ (-7, 1) $:

   $ (y - \hat{y})^2 = (1 - (-6,4))^2 = (7,4)^2 = 54,76 $

5. Para el punto $ (8, 14) $:

   $ (y - \hat{y})^2 = (14 - 11,6)^2 = (2,4)^2 = 5,76 $

 

#### Paso 3: Calcular el error cuadrático medio (ECM)

El error cuadrático medio se calcula promediando todos los errores cuadrados:
$$
\text{ECM} = \dfrac{40,96 + 4 + 1,44 + 54,76 + 5,76}{5} = \dfrac{106,92}{5} = 21,384
$$


A diferencia del **error absoluto medio (EAM)**, que toma la distancia absoluta entre las predicciones y los valores reales, el ECM amplifica los errores más grandes, lo que puede ser útil cuando se desea penalizar más las predicciones erróneas.
