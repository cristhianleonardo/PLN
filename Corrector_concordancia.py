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


# ============================================================
# PARTE 3: Autómata Finito Determinista (DFA) — tokenización
#
# Estados: q0=INICIO  q1=EN_PALABRA  q2=SEPARADOR
# Transición δ(estado, caracter) definida en _delta()
# ============================================================

class DFA:
    """
    DFA que tokeniza una frase carácter a carácter.
    Cada vez que transita q1→q2 emite el token acumulado.
    """

    ESTADO_INICIAL = 'q0'

    def _es_letra(self, c):
        return c.isalpha() or c in 'áéíóúüñÁÉÍÓÚÜÑ'

    def _delta(self, estado, c):
        """Función de transición del DFA."""
        if estado == 'q0':
            return 'q1' if self._es_letra(c) else 'q2'
        if estado == 'q1':
            return 'q1' if self._es_letra(c) else 'q2'
        if estado == 'q2':
            return 'q1' if self._es_letra(c) else 'q2'
        return 'q2'

    def tokenizar(self, frase):
        estado  = self.ESTADO_INICIAL
        buffer  = ''
        tokens  = []

        for c in frase:
            nuevo = self._delta(estado, c)
            if estado == 'q1' and nuevo == 'q2':   # fin de palabra
                tokens.append(buffer.lower())
                buffer = ''
            if nuevo == 'q1':
                buffer += c
            estado = nuevo

        if buffer:                                  # último token
            tokens.append(buffer.lower())

        return tokens


# ============================================================
# PARTE 4: Gramática de Contexto Libre (CFG)
# ============================================================

gramatica = {
    'O':  [['SN', 'SV'], ['SN']],
    'SN': [['Det', 'N'], ['N']],
    'SV': [['V', 'SN'],  ['V']],
}

# El léxico actúa como reglas terminales de la CFG.
# Det, N, V, Adj son categorías; las palabras viven en `lexico`.


# ============================================================
# PARTE 5: Parser descendente recursivo  (commit 3)
#
# Clase Nodo igual a la de arbol_desde_cero.py de la profe.
# parse_sn / parse_sv / parse_o recorren los tokens buscando
# sintagmas válidos y construyen el árbol de derivación.
# ============================================================

class Nodo:
    """Nodo del árbol de derivación (igual que en arbol_desde_cero.py)."""
    def __init__(self, etiqueta, hijos=None, es_error=False):
        self.etiqueta = etiqueta
        self.hijos    = hijos if hijos else []
        self.es_error = es_error


def parse_sn(tokens, pos):
    """
    SN → Det N Adj*  |  N Adj*
    Retorna (nodo_SN, dag_concordancia, nueva_pos) o (None, None, pos).
    """
    if pos >= len(tokens):
        return None, None, pos

    nodo_sn   = Nodo('SN')
    dag_sn    = {}
    pos_act   = pos
    det_info  = None
    sust_info = None

    # ── Intento Det N ──────────────────────────────────────
    r = rasgo(tokens[pos_act])
    if r and r['cat'] == 'det':
        det_tok  = tokens[pos_act]
        det_info = r
        nodo_det = Nodo('Det')
        nodo_det.hijos.append(Nodo(f'"{det_tok}"'))
        pos_act += 1

        if pos_act < len(tokens):
            r2 = rasgo(tokens[pos_act])
            if r2 and r2['cat'] == 'n':
                sust_tok  = tokens[pos_act]
                sust_info = r2
                nodo_n    = Nodo('N')
                nodo_n.hijos.append(Nodo(f'"{sust_tok}"'))
                pos_act  += 1
                nodo_sn.hijos.extend([nodo_det, nodo_n])
                dag_sn = {'det': det_tok, 'n': sust_tok,
                          'gen': sust_info['gen'], 'num': sust_info['num']}

    # ── Intento N solo ──────────────────────────────────────
    if not dag_sn:
        pos_act = pos
        r = rasgo(tokens[pos_act])
        if r and r['cat'] == 'n':
            sust_tok  = tokens[pos_act]
            sust_info = r
            nodo_n    = Nodo('N')
            nodo_n.hijos.append(Nodo(f'"{sust_tok}"'))
            pos_act  += 1
            nodo_sn.hijos.append(nodo_n)
            dag_sn = {'n': sust_tok,
                      'gen': sust_info['gen'], 'num': sust_info['num']}

    if not dag_sn:
        return None, None, pos

    # ── Adjetivos opcionales ────────────────────────────────
    dag_sn['adjs'] = []
    while pos_act < len(tokens):
        r = rasgo(tokens[pos_act])
        if r and r['cat'] == 'adj':
            adj_tok = tokens[pos_act]
            dag_sn['adjs'].append({'palabra': adj_tok, 'rasgos': r})
            nodo_adj = Nodo('Adj')
            nodo_adj.hijos.append(Nodo(f'"{adj_tok}"'))
            nodo_sn.hijos.append(nodo_adj)
            pos_act += 1
        else:
            break

    dag_sn['det_info']  = det_info
    dag_sn['sust_info'] = sust_info
    return nodo_sn, dag_sn, pos_act


def parse_sv(tokens, pos):
    """SV → V SN | V"""
    if pos >= len(tokens):
        return None, None, pos

    r = rasgo(tokens[pos])
    if not r or r['cat'] != 'v':
        return None, None, pos

    v_tok   = tokens[pos]
    nodo_sv = Nodo('SV')
    nodo_v  = Nodo('V')
    nodo_v.hijos.append(Nodo(f'"{v_tok}"'))
    nodo_sv.hijos.append(nodo_v)
    dag_sv  = {'v': v_tok, 'num': r['num'], 'accion': r['accion']}
    pos_act = pos + 1

    nodo_sn_obj, dag_obj, pos2 = parse_sn(tokens, pos_act)
    if nodo_sn_obj:
        nodo_sv.hijos.append(nodo_sn_obj)
        dag_sv['objeto'] = dag_obj
        pos_act = pos2

    return nodo_sv, dag_sv, pos_act


def parse_o(tokens):
    """O → SN SV | SN"""
    nodo_o   = Nodo('O')
    nodo_sn, dag_sn, pos = parse_sn(tokens, 0)
    if not nodo_sn:
        return None, [], None

    nodo_sv, dag_sv, pos = parse_sv(tokens, pos)

    nodo_o.hijos.append(nodo_sn)
    sintagmas = [dag_sn]

    if nodo_sv:
        nodo_o.hijos.append(nodo_sv)
        if dag_sv and 'objeto' in dag_sv:
            sintagmas.append(dag_sv['objeto'])

    return nodo_o, sintagmas, dag_sv