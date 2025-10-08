# Contexto del Negocio y Plan de Análisis

## 1. Tema

**Mercado IBM/Guayerd GRP3**: Una tienda minorista de abarrotes y productos de limpieza en Córdoba, Argentina. Ofrece tanto productos de consumo diario (bebidas, alimentos, productos de limpieza) como opciones gourmet locales. Vende en mostrador y también con reparto a domicilio en ciudades cercanas como Villa María y Alta Gracia.

## 2. Problema

La tienda carece de información analítica estructurada para responder preguntas comerciales básicas: ¿qué productos generan mayor volumen de ventas?, ¿quiénes son los clientes que compran con más frecuencia o gastan más? Sin estas respuestas, las decisiones sobre promociones, compras y gestión de stock son reactivas y poco focalizadas, lo que provoca oportunidades perdidas de aumentar la recompra, optimizar inventario y mejorar la rentabilidad.

Además, la información disponible está distribuida en varias tablas (clientes, ventas, detalle_ventas, productos) y no está integrada ni resumida de forma que permita identificar fácilmente top productos o top clientes. El objetivo es resolver esta falta de visibilidad mediante un análisis reproducible que identifique los productos más vendidos y los clientes con mayor contribución, para soportar estrategias de promoción y fidelización.

## 3. Solución

La tienda quiere identificar **qué productos son los más vendidos** y **quiénes son los clientes que más compran**, para diseñar promociones y descuentos que aumenten la recompra y la fidelización.

Propondremos un **script en Python** que siga estos pasos de manera sencilla:

1. Leer las bases de datos (`clientes`, `ventas`, `productos`, `detalle_ventas`).

2. Unir la información para relacionar clientes con sus compras y los productos adquiridos.

3. Contar cuántas veces se vendió cada producto y calcular el total de ingresos de cada cliente.

4. Generar dos listas: **top productos más vendidos** y **top clientes más compradores**.

5. Presentar los resultados en un formato fácil de usar para tomar decisiones comerciales.

## 4. Datos necesarios de las bases

- **Clientes**: `id_cliente`, `nombre_cliente`, `ciudad`

- **Ventas**: `id_venta`, `id_cliente`, `fecha`, `medio_pago`

- **Detalle_ventas**: `id_venta`, `id_producto`, `cantidad`, `precio_unitario`, `importe`

- **Productos**: `id_producto`, `nombre_producto`, `categoria`, `precio_unitario`

# Descripción Bases de Datos

## Archivo: clientes.xlsx
- **Número de filas:** 100
- **Número de columnas:** 5

### Estructura de columnas
| Columna | Tipo de dato | Escala | Ejemplos |
|---------|---------------|--------|----------|
| id_cliente | int | nominal | 1, 2, 3, 4, 5 |
| nombre_cliente | str | nominal | Mariana Lopez, Nicolas Rojas, Hernan Martinez, Uma Martinez, Agustina Flores |
| email | str | nominal | mariana.lopez@mail.com, nicolas.rojas@mail.com, hernan.martinez@mail.com, uma.martinez@mail.com, agustina.flores@mail.com |
| ciudad | str | nominal | Carlos Paz, Rio Cuarto, Cordoba, Villa Maria, Alta Gracia |
| fecha_alta | datetime | razón (temporal) | 2023-01-01T00:00:00.000000000, 2023-01-02T00:00:00.000000000, 2023-01-03T00:00:00.000000000, 2023-01-04T00:00:00.000000000, 2023-01-05T00:00:00.000000000 |

---

## Archivo: ventas.xlsx
- **Número de filas:** 120
- **Número de columnas:** 6

### Estructura de columnas
| Columna | Tipo de dato | Escala | Ejemplos |
|---------|---------------|--------|----------|
| id_venta | int | nominal | 1, 2, 3, 4, 5 |
| fecha | datetime | razón (temporal) | 2024-06-19T00:00:00.000000000, 2024-03-17T00:00:00.000000000, 2024-01-13T00:00:00.000000000, 2024-02-27T00:00:00.000000000, 2024-06-11T00:00:00.000000000 |
| id_cliente | int | nominal | 62, 49, 20, 36, 56 |
| nombre_cliente | str | nominal | Guadalupe Romero, Olivia Gomez, Tomas Acosta, Martina Molina, Bruno Diaz |
| email | str | nominal | guadalupe.romero@mail.com, olivia.gomez@mail.com, tomas.acosta@mail.com, martina.molina@mail.com, bruno.diaz@mail.com |
| medio_pago | str | nominal | tarjeta, qr, transferencia, efectivo |

---

## Archivo: productos.xlsx
- **Número de filas:** 100
- **Número de columnas:** 4

### Estructura de columnas
| Columna | Tipo de dato | Escala | Ejemplos |
|---------|---------------|--------|----------|
| id_producto | int | nominal | 1, 2, 3, 4, 5 |
| nombre_producto | str | nominal | Coca Cola 1.5L, Pepsi 1.5L, Sprite 1.5L, Fanta Naranja 1.5L, Agua Mineral 500ml |
| categoria | str | nominal | Alimentos, Limpieza |
| precio_unitario | int | razón | 2347, 4973, 4964, 2033, 4777 |

---

## Archivo: detalle_ventas.xlsx
- **Número de filas:** 343
- **Número de columnas:** 6

### Estructura de columnas
| Columna | Tipo de dato | Escala | Ejemplos |
|---------|---------------|--------|----------|
| id_venta | int | nominal | 1, 2, 3, 4, 5 |
| id_producto | int | nominal | 90, 82, 39, 70, 22 |
| nombre_producto | str | nominal | Toallas Húmedas x50, Aceitunas Negras 200g, Helado Vainilla 1L, Fernet 750ml, Medialunas de Manteca |
| cantidad | int | razón | 1, 5, 2, 4, 3 |
| precio_unitario | int | razón | 2902, 2394, 469, 4061, 2069 |
| importe | int | razón | 2902, 11970, 2345, 8122, 2069 |

---

## Relaciones entre Bases de Datos
- **clientes.xlsx ↔ ventas.xlsx**: `id_cliente` es la clave primaria en *clientes* y clave foránea en *ventas*.
- **ventas.xlsx ↔ detalle_ventas.xlsx**: `id_venta` es la clave primaria en *ventas* y clave foránea en *detalle_ventas*.
- **productos.xlsx ↔ detalle_ventas.xlsx**: `id_producto` es la clave primaria en *productos* y clave foránea en *detalle_ventas*.

// ...existing code...

## 5. Aporte de GitHub Copilot

GitHub Copilot asistió en la elaboración de esta documentación de manera práctica y reproducible:

- Leyó y sintetizó la estructura de las cuatro bases de datos (clientes, ventas, productos, detalle_ventas), identificando columnas, tipos de dato y ejemplos representativos.
- Describió las relaciones entre tablas y precisó los campos necesarios para el análisis (claves y columnas relevantes).
- Propuso el flujo de solución (lectura de archivos, uniones, agregaciones y generación de listas de top productos y top clientes).
- Recomendó validaciones y controles de calidad de datos (nulos, duplicados, verificación de importes) y métricas adicionales útiles (cantidad vendida, facturación, frecuencia y gasto total).
- Sugerencias prácticas para implementación: librerías (pandas, openpyxl), formatos de salida (CSV/Excel) y opciones de visualización para facilitar la toma de decisiones.

Este aporte fue empleado para estructurar y clarificar el problema, definir los pasos técnicos y dejar una guía clara para implementar el script en Python.