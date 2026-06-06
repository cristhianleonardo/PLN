# ============================================================
# Corrector de Concordancia de Género y Número en Español
# Proyecto Final — Procesamiento de Lenguaje Natural
# Universidad del Valle · Semestre 2026-1
#
# Integrante : Cristhian Leonardo Albarracín Zapata
# Código     : 1968253
#
# COMMIT 1 — Léxico con DAGs + función unificar
# ============================================================

# ============================================================
# PARTE 1: Léxico con estructuras de rasgos (DAGs)
# ============================================================

lexico = {
    # ── Determinantes
    'el':       {'cat': 'det', 'gen': 'masc', 'num': 'sing'},
    'la':       {'cat': 'det', 'gen': 'fem',  'num': 'sing'},
    'los':      {'cat': 'det', 'gen': 'masc', 'num': 'plur'},
    'las':      {'cat': 'det', 'gen': 'fem',  'num': 'plur'},
    'un':       {'cat': 'det', 'gen': 'masc', 'num': 'sing'},
    'una':      {'cat': 'det', 'gen': 'fem',  'num': 'sing'},
    'unos':     {'cat': 'det', 'gen': 'masc', 'num': 'plur'},
    'unas':     {'cat': 'det', 'gen': 'fem',  'num': 'plur'},

    # ── Sustantivos masculinos singulares
    'gato':     {'cat': 'n', 'gen': 'masc', 'num': 'sing'},
    'perro':    {'cat': 'n', 'gen': 'masc', 'num': 'sing'},
    'niño':     {'cat': 'n', 'gen': 'masc', 'num': 'sing'},
    'hombre':   {'cat': 'n', 'gen': 'masc', 'num': 'sing'},
    'libro':    {'cat': 'n', 'gen': 'masc', 'num': 'sing'},
    'árbol':    {'cat': 'n', 'gen': 'masc', 'num': 'sing'},
    'pájaro':   {'cat': 'n', 'gen': 'masc', 'num': 'sing'},

    # ── Sustantivos femeninos singulares
    'gata':     {'cat': 'n', 'gen': 'fem', 'num': 'sing'},
    'perra':    {'cat': 'n', 'gen': 'fem', 'num': 'sing'},
    'niña':     {'cat': 'n', 'gen': 'fem', 'num': 'sing'},
    'mujer':    {'cat': 'n', 'gen': 'fem', 'num': 'sing'},
    'casa':     {'cat': 'n', 'gen': 'fem', 'num': 'sing'},
    'flor':     {'cat': 'n', 'gen': 'fem', 'num': 'sing'},
    'luna':     {'cat': 'n', 'gen': 'fem', 'num': 'sing'},
    'mesa':     {'cat': 'n', 'gen': 'fem', 'num': 'sing'},

    # ── Sustantivos masculinos plurales
    'gatos':    {'cat': 'n', 'gen': 'masc', 'num': 'plur'},
    'perros':   {'cat': 'n', 'gen': 'masc', 'num': 'plur'},
    'niños':    {'cat': 'n', 'gen': 'masc', 'num': 'plur'},
    'hombres':  {'cat': 'n', 'gen': 'masc', 'num': 'plur'},
    'libros':   {'cat': 'n', 'gen': 'masc', 'num': 'plur'},
    'pájaros':  {'cat': 'n', 'gen': 'masc', 'num': 'plur'},

    # ── Sustantivos femeninos plurales
    'gatas':    {'cat': 'n', 'gen': 'fem', 'num': 'plur'},
    'perras':   {'cat': 'n', 'gen': 'fem', 'num': 'plur'},
    'niñas':    {'cat': 'n', 'gen': 'fem', 'num': 'plur'},
    'mujeres':  {'cat': 'n', 'gen': 'fem', 'num': 'plur'},
    'casas':    {'cat': 'n', 'gen': 'fem', 'num': 'plur'},
    'flores':   {'cat': 'n', 'gen': 'fem', 'num': 'plur'},
    'mesas':    {'cat': 'n', 'gen': 'fem', 'num': 'plur'},

    # ── Adjetivos masculinos singulares
    'alto':     {'cat': 'adj', 'gen': 'masc', 'num': 'sing', 'base': 'alto'},
    'bajo':     {'cat': 'adj', 'gen': 'masc', 'num': 'sing', 'base': 'bajo'},
    'negro':    {'cat': 'adj', 'gen': 'masc', 'num': 'sing', 'base': 'negro'},
    'blanco':   {'cat': 'adj', 'gen': 'masc', 'num': 'sing', 'base': 'blanco'},
    'rojo':     {'cat': 'adj', 'gen': 'masc', 'num': 'sing', 'base': 'rojo'},
    'pequeño':  {'cat': 'adj', 'gen': 'masc', 'num': 'sing', 'base': 'pequeño'},
    'bonito':   {'cat': 'adj', 'gen': 'masc', 'num': 'sing', 'base': 'bonito'},
    'gordo':    {'cat': 'adj', 'gen': 'masc', 'num': 'sing', 'base': 'gordo'},

    # ── Adjetivos femeninos singulares
    'alta':     {'cat': 'adj', 'gen': 'fem', 'num': 'sing', 'base': 'alto'},
    'baja':     {'cat': 'adj', 'gen': 'fem', 'num': 'sing', 'base': 'bajo'},
    'negra':    {'cat': 'adj', 'gen': 'fem', 'num': 'sing', 'base': 'negro'},
    'blanca':   {'cat': 'adj', 'gen': 'fem', 'num': 'sing', 'base': 'blanco'},
    'roja':     {'cat': 'adj', 'gen': 'fem', 'num': 'sing', 'base': 'rojo'},
    'pequeña':  {'cat': 'adj', 'gen': 'fem', 'num': 'sing', 'base': 'pequeño'},
    'bonita':   {'cat': 'adj', 'gen': 'fem', 'num': 'sing', 'base': 'bonito'},
    'gorda':    {'cat': 'adj', 'gen': 'fem', 'num': 'sing', 'base': 'gordo'},

    # ── Adjetivos masculinos plurales
    'altos':    {'cat': 'adj', 'gen': 'masc', 'num': 'plur', 'base': 'alto'},
    'bajos':    {'cat': 'adj', 'gen': 'masc', 'num': 'plur', 'base': 'bajo'},
    'negros':   {'cat': 'adj', 'gen': 'masc', 'num': 'plur', 'base': 'negro'},
    'blancos':  {'cat': 'adj', 'gen': 'masc', 'num': 'plur', 'base': 'blanco'},
    'pequeños': {'cat': 'adj', 'gen': 'masc', 'num': 'plur', 'base': 'pequeño'},
    'bonitos':  {'cat': 'adj', 'gen': 'masc', 'num': 'plur', 'base': 'bonito'},

    # ── Adjetivos femeninos plurales
    'altas':    {'cat': 'adj', 'gen': 'fem', 'num': 'plur', 'base': 'alto'},
    'bajas':    {'cat': 'adj', 'gen': 'fem', 'num': 'plur', 'base': 'bajo'},
    'negras':   {'cat': 'adj', 'gen': 'fem', 'num': 'plur', 'base': 'negro'},
    'blancas':  {'cat': 'adj', 'gen': 'fem', 'num': 'plur', 'base': 'blanco'},
    'pequeñas': {'cat': 'adj', 'gen': 'fem', 'num': 'plur', 'base': 'pequeño'},
    'bonitas':  {'cat': 'adj', 'gen': 'fem', 'num': 'plur', 'base': 'bonito'},

    # ── Adjetivos invariables en género (neutros)
    'grande':   {'cat': 'adj', 'gen': 'neutro', 'num': 'sing', 'base': 'grande'},
    'grandes':  {'cat': 'adj', 'gen': 'neutro', 'num': 'plur', 'base': 'grande'},
    'feliz':    {'cat': 'adj', 'gen': 'neutro', 'num': 'sing', 'base': 'feliz'},
    'felices':  {'cat': 'adj', 'gen': 'neutro', 'num': 'plur', 'base': 'feliz'},
    'gris':     {'cat': 'adj', 'gen': 'neutro', 'num': 'sing', 'base': 'gris'},
    'grises':   {'cat': 'adj', 'gen': 'neutro', 'num': 'plur', 'base': 'gris'},
    'verde':    {'cat': 'adj', 'gen': 'neutro', 'num': 'sing', 'base': 'verde'},
    'verdes':   {'cat': 'adj', 'gen': 'neutro', 'num': 'plur', 'base': 'verde'},
    'azul':     {'cat': 'adj', 'gen': 'neutro', 'num': 'sing', 'base': 'azul'},
    'azules':   {'cat': 'adj', 'gen': 'neutro', 'num': 'plur', 'base': 'azul'},

    # ── Verbos
    'corre':    {'cat': 'v', 'num': 'sing', 'accion': 'correr'},
    'corren':   {'cat': 'v', 'num': 'plur', 'accion': 'correr'},
    'ladra':    {'cat': 'v', 'num': 'sing', 'accion': 'ladrar'},
    'ladran':   {'cat': 'v', 'num': 'plur', 'accion': 'ladrar'},
    'duerme':   {'cat': 'v', 'num': 'sing', 'accion': 'dormir'},
    'duermen':  {'cat': 'v', 'num': 'plur', 'accion': 'dormir'},
    'come':     {'cat': 'v', 'num': 'sing', 'accion': 'comer'},
    'comen':    {'cat': 'v', 'num': 'plur', 'accion': 'comer'},
    'juega':    {'cat': 'v', 'num': 'sing', 'accion': 'jugar'},
    'juegan':   {'cat': 'v', 'num': 'plur', 'accion': 'jugar'},
    'camina':   {'cat': 'v', 'num': 'sing', 'accion': 'caminar'},
    'caminan':  {'cat': 'v', 'num': 'plur', 'accion': 'caminar'},
    'salta':    {'cat': 'v', 'num': 'sing', 'accion': 'saltar'},
    'saltan':   {'cat': 'v', 'num': 'plur', 'accion': 'saltar'},
    'es':       {'cat': 'v', 'num': 'sing', 'accion': 'ser'},
    'son':      {'cat': 'v', 'num': 'plur', 'accion': 'ser'},
}

# Función de acceso al léxico (igual que cat() de la profe)
def rasgo(token):
    return lexico.get(token.lower(), None)


# ============================================================
# PARTE 2: Unificación de DAGs
# ============================================================

def unificar(dag1, dag2):
    """
    Unifica dos DAGs de rasgos.
    Retorna el DAG combinado, o None si hay conflicto.
    Mismo algoritmo que en Ejercicio_DCGs.py de la profe.
    """
    resultado = dict(dag1)
    for rasgo_k, valor in dag2.items():
        if rasgo_k in resultado:
            if isinstance(resultado[rasgo_k], dict) and isinstance(valor, dict):
                sub = unificar(resultado[rasgo_k], valor)
                if sub is None:
                    return None
                resultado[rasgo_k] = sub
            elif resultado[rasgo_k] != valor:
                return None      # ← conflicto, retornamos None
        else:
            resultado[rasgo_k] = valor
    return resultado


# ── Prueba básica ──────────────────────────────────────────
if __name__ == '__main__':
    print('=== Léxico — prueba de acceso ===')
    for palabra in ['la', 'niña', 'alto', 'gris', 'corre']:
        r = rasgo(palabra)
        print(f'  {palabra:<10} → {r}')

    print('\n=== Unificación — prueba básica ===')
    d1 = {'gen': 'fem', 'num': 'sing'}
    d2 = {'gen': 'fem', 'num': 'sing'}
    print(f'  fem/sing ↔ fem/sing  → {unificar(d1, d2)}')

    d3 = {'gen': 'masc', 'num': 'sing'}
    print(f'  masc/sing ↔ fem/sing → {unificar(d3, d2)}')
