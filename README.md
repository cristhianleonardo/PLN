# Corrector de Concordancia de Género y Número en Español

**Proyecto Final — Procesamiento de Lenguaje Natural**  
Universidad del Valle · Ingeniería de Sistemas · Semestre 2026-1

**Integrante:** Cristhian Leonardo Albarracín Zapata · 1968253

---

## Descripción

Sistema en Python que recibe una frase en español, detecta errores de concordancia de género y número entre artículos, sustantivos y adjetivos, y sugiere la corrección. Construido completamente desde cero sin librerías de PLN externas.

**Ejemplos:**

| Entrada | Salida |
|---|---|
| `La niña alto corre` | Error: 'alto' debe ser 'alta' |
| `Los perro negro ladra` | Error: 'los' debe ser 'el' |
| `El gato gris duerme` | Frase válida ✓ |
| `La rosa grande corre` | Ambigüedad: 'rosa' puede ser N o Adj |

---

## Herramientas del curso implementadas

| Herramienta | Dónde se usa |
|---|---|
| Autómata Finito Determinista (DFA) | Tokenización carácter a carácter (clase `DFA`) |
| Gramática de Contexto Libre (CFG) | Estructura SN/SV como diccionario Python |
| Parser descendente recursivo | `parse_sn`, `parse_sv`, `parse_o` |
| DCG / Unificación con DAGs | `unificar()`, verificación de rasgos gen/num |
| Árbol de derivación | Clase `Nodo` + matplotlib (PNG) |
| Detección de ambigüedad | `lexico_ambiguo`, `detectar_ambiguedad()` |

---

## Requisitos

Solo necesita Python 3 y matplotlib:

```
pip install matplotlib
```

No se usa NLTK, spaCy ni ninguna librería de PLN.

---

## Cómo ejecutar

**Modo interactivo:**
```bash
python3 Corrector_concordancia.py
```

**Analizar una frase directamente:**
```bash
python3 Corrector_concordancia.py "La niña alto corre"
```

Al analizar una frase se genera automáticamente `arbol_derivacion.png` con el árbol de derivación visual.

---

## Descripción de componentes

**PARTE 1 — Léxico con DAGs**  
Diccionario con ~120 palabras (determinantes, sustantivos, adjetivos, verbos). Cada entrada es un DAG con rasgos `cat`, `gen`, `num`. Las palabras con ambigüedad léxica (rosa, joven, naranja, pobre) tienen entrada doble en `lexico_ambiguo`.

**PARTE 2 — Unificación**  
Función `unificar(dag1, dag2)` que combina dos DAGs de rasgos. Retorna el DAG fusionado o `None` si hay conflicto. Implementación idéntica a la vista en clase (Ejercicio_DCGs.py).

**PARTE 3 — DFA**  
Clase `DFA` con estados `q0/q1/q2` y función de transición `δ` implementada carácter a carácter. Emite tokens al transitar `q1→q2`.

**PARTE 4 — CFG**  
Gramática `O → SN SV | SN`, `SN → Det N | N`, `SV → V SN | V` representada como diccionario Python.

**PARTE 5 — Parser**  
Parser descendente recursivo que construye el árbol de derivación con clase `Nodo` (etiqueta + hijos).

**PARTE 6 — Verificación**  
Unificación de rasgos Det↔N y Adj↔N. Genera errores tipados (GÉNERO / NÚMERO) con sugerencia de corrección.

**PARTE 7 — Árbol visual**  
`dibujar_arbol()` con matplotlib. Nodos en error marcados en rojo, correctos en azul. Guarda PNG.

**PARTE 8 — Ambigüedad**  
`detectar_ambiguedad()` recorre los tokens contra `lexico_ambiguo` y reporta las interpretaciones posibles con la categoría que eligió el parser.

---

## Estructura del repositorio

```
├── Corrector_concordancia.py   # código fuente completo
├── README.md                   # este archivo
└── diagrama_sistema.png        # diagrama de flujo del sistema
```

