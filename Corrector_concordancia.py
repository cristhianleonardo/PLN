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

import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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

    # ── Palabras con ambigüedad léxica (uso principal: N)
    'rosa':    {'cat': 'n', 'gen': 'fem',  'num': 'sing'},
    'naranja': {'cat': 'n', 'gen': 'fem',  'num': 'sing'},
    'pobre':   {'cat': 'n', 'gen': 'masc', 'num': 'sing'},
    'joven':   {'cat': 'n', 'gen': 'masc', 'num': 'sing'},

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

    # ── Verbos (num para concordancia sujeto-verbo, accion para semántica)
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

# Tabla de formas correctas para construir sugerencias
formas_adj = {
    'alto':    {'masc': {'sing': 'alto',    'plur': 'altos'},
                'fem':  {'sing': 'alta',    'plur': 'altas'}},
    'bajo':    {'masc': {'sing': 'bajo',    'plur': 'bajos'},
                'fem':  {'sing': 'baja',    'plur': 'bajas'}},
    'negro':   {'masc': {'sing': 'negro',   'plur': 'negros'},
                'fem':  {'sing': 'negra',   'plur': 'negras'}},
    'blanco':  {'masc': {'sing': 'blanco',  'plur': 'blancos'},
                'fem':  {'sing': 'blanca',  'plur': 'blancas'}},
    'rojo':    {'masc': {'sing': 'rojo',    'plur': 'rojos'},
                'fem':  {'sing': 'roja',    'plur': 'rojas'}},
    'pequeño': {'masc': {'sing': 'pequeño', 'plur': 'pequeños'},
                'fem':  {'sing': 'pequeña', 'plur': 'pequeñas'}},
    'bonito':  {'masc': {'sing': 'bonito',  'plur': 'bonitos'},
                'fem':  {'sing': 'bonita',  'plur': 'bonitas'}},
    'gordo':   {'masc': {'sing': 'gordo',   'plur': 'gordos'},
                'fem':  {'sing': 'gorda',   'plur': 'gordas'}},
    'grande':  {'masc': {'sing': 'grande',  'plur': 'grandes'},
                'fem':  {'sing': 'grande',  'plur': 'grandes'}},
    'feliz':   {'masc': {'sing': 'feliz',   'plur': 'felices'},
                'fem':  {'sing': 'feliz',   'plur': 'felices'}},
    'gris':    {'masc': {'sing': 'gris',    'plur': 'grises'},
                'fem':  {'sing': 'gris',    'plur': 'grises'}},
    'verde':   {'masc': {'sing': 'verde',   'plur': 'verdes'},
                'fem':  {'sing': 'verde',   'plur': 'verdes'}},
    'azul':    {'masc': {'sing': 'azul',    'plur': 'azules'},
                'fem':  {'sing': 'azul',    'plur': 'azules'}},
}

formas_det = {
    'masc': {'sing': 'el',  'plur': 'los'},
    'fem':  {'sing': 'la',  'plur': 'las'},
}

# Función de acceso al léxico (igual que cat() de la profe)
def rasgo(token):
    return lexico.get(token.lower(), None)

lexico_ambiguo = {
    'rosa':    [{'cat': 'n', 'gen': 'fem', 'num': 'sing'}, {'cat': 'adj', 'gen': 'neutro', 'num': 'sing', 'base': 'rosa'}],
    'naranja': [{'cat': 'n', 'gen': 'fem', 'num': 'sing'}, {'cat': 'adj', 'gen': 'neutro', 'num': 'sing', 'base': 'naranja'}],
    'pobre':   [{'cat': 'n', 'gen': 'masc', 'num': 'sing'}, {'cat': 'adj', 'gen': 'neutro', 'num': 'sing', 'base': 'pobre'}],
    'joven':   [{'cat': 'n', 'gen': 'masc', 'num': 'sing'}, {'cat': 'adj', 'gen': 'neutro', 'num': 'sing', 'base': 'joven'}],
}

def rasgo_ambiguo(token):
    return lexico_ambiguo.get(token.lower(), None)



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

# ============================================================
# PARTE 6: Verificación de errores + sugerencias  
# ============================================================

def sugerir_det(gen_sust, num_sust):
    g = gen_sust if gen_sust != 'neutro' else 'masc'
    return formas_det.get(g, {}).get(num_sust, '?')

def sugerir_adj(base, gen_sust, num_sust):
    g = gen_sust if gen_sust != 'neutro' else 'masc'
    return formas_adj.get(base, {}).get(g, {}).get(num_sust, f'{base}(?)')


def concordancia_det_n(det_info, sust_info):
    dag_det  = {'gen': det_info['gen'], 'num': det_info['num']}
    dag_sust = {'gen': sust_info['gen'], 'num': sust_info['num']}
    if dag_det['gen'] == 'neutro':   dag_det['gen']  = dag_sust['gen']
    if dag_sust['gen'] == 'neutro':  dag_sust['gen'] = dag_det['gen']
    return unificar(dag_det, dag_sust)


def concordancia_adj_n(adj_info, sust_info):
    dag_adj  = {'gen': adj_info['gen'], 'num': adj_info['num']}
    dag_sust = {'gen': sust_info['gen'], 'num': sust_info['num']}
    if dag_adj['gen'] == 'neutro':   dag_adj['gen']  = dag_sust['gen']
    if dag_sust['gen'] == 'neutro':  dag_sust['gen'] = dag_adj['gen']
    return unificar(dag_adj, dag_sust)


def verificar_sintagma(dag_sn):
    errores       = []
    unificaciones = []
    sust_info = dag_sn.get('sust_info')
    det_info  = dag_sn.get('det_info')
    adjs      = dag_sn.get('adjs', [])

    if not sust_info:
        return errores, unificaciones

    # Det ↔ N
    if det_info:
        resultado = concordancia_det_n(det_info, sust_info)
        gen_ok = (det_info['gen'] == sust_info['gen']
                  or 'neutro' in (det_info['gen'], sust_info['gen']))
        num_ok = (det_info['num'] == sust_info['num'])
        unificaciones.append({
            'par':    f"{dag_sn.get('det','?')} ↔ {dag_sn.get('n','?')}",
            'tipo':   'Det–N',
            'dag1':   {'gen': det_info['gen'],  'num': det_info['num']},
            'dag2':   {'gen': sust_info['gen'], 'num': sust_info['num']},
            'gen_ok': gen_ok, 'num_ok': num_ok,
            'unifica': resultado is not None,
        })
        if resultado is None:
            if not gen_ok:
                correcto = sugerir_det(sust_info['gen'], sust_info['num'])
                errores.append({
                    'tipo': 'GÉNERO', 'token': dag_sn.get('det', '?'),
                    'desc': (f"'{dag_sn['det']}' es {det_info['gen']} "
                             f"pero '{dag_sn['n']}' es {sust_info['gen']}"),
                    'sug':  f"Cambiar '{dag_sn['det']}' → '{correcto}'",
                })
            if not num_ok:
                correcto = sugerir_det(sust_info['gen'], sust_info['num'])
                errores.append({
                    'tipo': 'NÚMERO', 'token': dag_sn.get('det', '?'),
                    'desc': (f"'{dag_sn['det']}' es {det_info['num']} "
                             f"pero '{dag_sn['n']}' es {sust_info['num']}"),
                    'sug':  f"Cambiar '{dag_sn['det']}' → '{correcto}'",
                })

    # Adj ↔ N
    for adj_entry in adjs:
        adj_tok  = adj_entry['palabra']
        adj_info = adj_entry['rasgos']
        resultado = concordancia_adj_n(adj_info, sust_info)
        gen_ok = (adj_info['gen'] == sust_info['gen']
                  or 'neutro' in (adj_info['gen'], sust_info['gen']))
        num_ok = (adj_info['num'] == sust_info['num'])
        unificaciones.append({
            'par':    f"{adj_tok} ↔ {dag_sn.get('n','?')}",
            'tipo':   'Adj–N',
            'dag1':   {'gen': adj_info['gen'],  'num': adj_info['num']},
            'dag2':   {'gen': sust_info['gen'], 'num': sust_info['num']},
            'gen_ok': gen_ok, 'num_ok': num_ok,
            'unifica': resultado is not None,
        })
        if resultado is None:
            base = adj_info.get('base', adj_tok)
            if not gen_ok:
                correcto = sugerir_adj(base, sust_info['gen'], sust_info['num'])
                errores.append({
                    'tipo': 'GÉNERO', 'token': adj_tok,
                    'desc': (f"'{adj_tok}' es {adj_info['gen']} "
                             f"pero '{dag_sn['n']}' es {sust_info['gen']}"),
                    'sug':  f"Cambiar '{adj_tok}' → '{correcto}'",
                })
            if not num_ok:
                correcto = sugerir_adj(base, sust_info['gen'], sust_info['num'])
                errores.append({
                    'tipo': 'NÚMERO', 'token': adj_tok,
                    'desc': (f"'{adj_tok}' es {adj_info['num']} "
                             f"pero '{dag_sn['n']}' es {sust_info['num']}"),
                    'sug':  f"Cambiar '{adj_tok}' → '{correcto}'",
                })

    return errores, unificaciones


# ============================================================
# PARTE 7: Árbol de derivación con matplotlib 
# ============================================================

def _medir_ancho(nodo):
    if not nodo.hijos:
        return 1
    return sum(_medir_ancho(h) for h in nodo.hijos)


def dibujar_arbol(nodo, ax, x, y, ancho):
    if not isinstance(nodo, Nodo):
        ax.text(x, y, str(nodo), ha='center', va='center', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9))
        return
    color = '#ffaaaa' if nodo.es_error else 'lightblue'
    ax.text(x, y, nodo.etiqueta, ha='center', va='center', fontsize=10,
            fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=color, alpha=0.9, edgecolor='gray'))
    if not nodo.hijos:
        return
    n     = len(nodo.hijos)
    x_ini = x - ancho / 2
    for hijo in nodo.hijos:
        ancho_hijo = ancho / n
        x_hijo     = x_ini + ancho_hijo / 2
        y_hijo     = y - 1.2
        ax.plot([x, x_hijo], [y - 0.2, y_hijo + 0.2], 'k-', lw=1.2)
        dibujar_arbol(hijo, ax, x_hijo, y_hijo, ancho_hijo)
        x_ini += ancho_hijo


def marcar_errores_arbol(nodo, tokens_error):
    for hijo in nodo.hijos:
        marcar_errores_arbol(hijo, tokens_error)
    etiq = nodo.etiqueta.strip('"')
    if etiq in tokens_error:
        nodo.es_error = True
    if any(h.es_error for h in nodo.hijos):
        nodo.es_error = True


def guardar_arbol(nodo_raiz, frase, nombre_archivo='arbol_derivacion.png'):
    ancho_total = max(_medir_ancho(nodo_raiz) * 1.5, 6)
    fig, ax = plt.subplots(figsize=(ancho_total + 2, 6))
    ax.set_xlim(0, ancho_total)
    ax.set_ylim(0, 6)
    ax.axis('off')
    dibujar_arbol(nodo_raiz, ax, ancho_total / 2, 5.5, ancho_total)
    parche_ok  = mpatches.Patch(color='lightblue', label='Correcto')
    parche_err = mpatches.Patch(color='#ffaaaa',   label='Error de concordancia')
    ax.legend(handles=[parche_ok, parche_err], loc='lower right', fontsize=8)
    plt.title(f'Árbol de Derivación — "{frase}"', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=120, bbox_inches='tight')
    plt.close()
    return nombre_archivo


# ============================================================
# PARTE 8: Detección de ambigüedad léxica  (commit 5)
#
# Una palabra es ambigua cuando puede funcionar como N o Adj
# según el contexto. El sistema la detecta, reporta las
# interpretaciones posibles y señala cuál usó el parser.
# ============================================================

def detectar_ambiguedad(tokens):
    """
    Recorre los tokens y reporta los que tienen más de una
    interpretación en el léxico (lexico_ambiguo).
    Retorna lista de dicts con la palabra y sus lecturas.
    """
    ambiguos = []
    for tok in tokens:
        interpretaciones = rasgo_ambiguo(tok)
        if interpretaciones:
            ambiguos.append({
                'palabra':         tok,
                'interpretaciones': interpretaciones,
            })
    return ambiguos


def reportar_ambiguedad(tokens):
    """
    Imprime el reporte de ambigüedad para los tokens de la frase.
    Si no hay palabras ambiguas lo indica también.
    """
    ambiguos = detectar_ambiguedad(tokens)
    if not ambiguos:
        print('  Sin ambigüedad léxica detectada.')
        return

    for a in ambiguos:
        print(f"  ⚠  '{a['palabra']}' es ambigua — {len(a['interpretaciones'])} lecturas posibles:")
        for i, interp in enumerate(a['interpretaciones'], 1):
            cat  = interp['cat']
            gen  = interp.get('gen', '—')
            num  = interp.get('num', '—')
            rol  = 'sustantivo' if cat == 'n' else 'adjetivo' if cat == 'adj' else cat
            print(f"      {i}. cat={cat} ({rol})  gen={gen}  num={num}")
        print(f"     → El parser la usó como: "
              f"{'sustantivo' if rasgo(a['palabra']) and rasgo(a['palabra'])['cat']=='n' else 'adjetivo (o desconocida en léxico principal)'}")


# ============================================================
# PARTE 9: Función principal de análisis
# ============================================================

def analizar(frase, guardar_img=True):
    sep  = '=' * 60
    sep2 = '-' * 60

    print(f'\n{sep}')
    print(f'  CORRECTOR DE CONCORDANCIA — PLN 2026-1')
    print(sep)
    print(f'  Frase: "{frase}"')
    print(sep2)

    # ── 1. DFA: tokenización ─────────────────────────────
    print('\n[1] TOKENIZACIÓN (DFA)')
    print(sep2)
    dfa    = DFA()
    tokens = dfa.tokenizar(frase)

    desconocidos = []
    for tok in tokens:
        r = rasgo(tok)
        if r:
            print(f'  {tok:<12}  →  cat={r["cat"]}', end='')
            if 'gen' in r: print(f'  gen={r["gen"]}', end='')
            if 'num' in r: print(f'  num={r["num"]}', end='')
            print()
        else:
            # puede ser ambigua
            interps = rasgo_ambiguo(tok)
            if interps:
                cats = '/'.join(set(i['cat'] for i in interps))
                print(f'  {tok:<12}  →  cat={cats} (AMBIGUA)')
            else:
                print(f'  {tok:<12}  →  DESCONOCIDO')
                desconocidos.append(tok)

    if desconocidos:
        print(f'\n  ⚠  No reconocidas: {", ".join(desconocidos)}')

    # ── 2. CFG + Parser: sintagmas nominales ─────────────
    print(f'\n[2] PARSER — SINTAGMAS NOMINALES (CFG)')
    print(sep2)
    nodo_raiz, sintagmas, dag_sv = parse_o(tokens)

    if not sintagmas:
        print('  No se detectaron sintagmas nominales reconocibles.')
        return

    for i, sn in enumerate(sintagmas, 1):
        partes = []
        if sn.get('det'):   partes.append(f"Det:'{sn['det']}'")
        if sn.get('n'):     partes.append(f"N:'{sn['n']}'")
        for a in sn.get('adjs', []):
            partes.append(f"Adj:'{a['palabra']}'")
        print(f'  SN{i}: [ {" | ".join(partes)} ]')

    # ── 3. DCG / Unificación ─────────────────────────────
    print(f'\n[3] UNIFICACIÓN DE RASGOS (DCG / DAGs)')
    print(sep2)
    print(f'  {"Par":<22} {"Tipo":<10} {"DAG1":<22} {"DAG2":<22} {"Gen":>5} {"Num":>5} {"Estado"}')
    print(f'  {"-"*22} {"-"*10} {"-"*22} {"-"*22} {"-"*5} {"-"*5} {"-"*8}')

    todos_errores = []
    todas_unifs   = []
    tokens_error  = set()

    for sn in sintagmas:
        errores, unifs = verificar_sintagma(sn)
        todos_errores.extend(errores)
        todas_unifs.extend(unifs)
        for e in errores:
            tokens_error.add(e['token'])

    for u in todas_unifs:
        gen_s  = '✓' if u['gen_ok'] else '✗'
        num_s  = '✓' if u['num_ok'] else '✗'
        estado = 'OK' if u['unifica'] else 'FALLA'
        dag1_s = str(u['dag1'])
        dag2_s = str(u['dag2'])
        print(f'  {u["par"]:<22} {u["tipo"]:<10} {dag1_s:<22} {dag2_s:<22} {gen_s:>5} {num_s:>5} {estado}')

    # ── 4. Ambigüedad léxica ──────────────────────────────
    print(f'\n[4] AMBIGÜEDAD LÉXICA')
    print(sep2)
    reportar_ambiguedad(tokens)

    # ── 5. Árbol de derivación ────────────────────────────
    if nodo_raiz:
        print(f'\n[5] ÁRBOL DE DERIVACIÓN (matplotlib)')
        print(sep2)
        marcar_errores_arbol(nodo_raiz, tokens_error)

        if guardar_img:
            archivo = guardar_arbol(nodo_raiz, frase)
            print(f'  Árbol guardado en: {archivo}')

        def ascii_arbol(nodo, prefijo='', es_ult=True):
            conn  = '└── ' if es_ult else '├── '
            marca = ' ← ERROR' if nodo.es_error else ''
            print(prefijo + (conn if prefijo else '') + nodo.etiqueta + marca)
            nuevo = prefijo + ('    ' if es_ult else '│   ')
            for i, h in enumerate(nodo.hijos):
                ascii_arbol(h, nuevo, i == len(nodo.hijos) - 1)

        ascii_arbol(nodo_raiz)

    # ── 6. Resultado final ────────────────────────────────
    print(f'\n[6] RESULTADO')
    print(sep2)

    if not todos_errores:
        print('  ✓  Frase válida — concordancia correcta en género y número.')
        if dag_sv and dag_sv.get('accion'):
            sn_suj = sintagmas[0]
            sujeto = ' '.join(filter(None, [sn_suj.get('det'), sn_suj.get('n')]))
            print(f'  → Sujeto: "{sujeto}"  |  Acción: "{dag_sv["accion"]}"')
    else:
        n = len(todos_errores)
        print(f'  ✗  {n} error{"es" if n > 1 else ""} detectado{"s" if n > 1 else ""}:\n')
        for i, err in enumerate(todos_errores, 1):
            print(f'  Error {i} [{err["tipo"]}]')
            print(f'    → {err["desc"]}')
            print(f'    ✦ Sugerencia: {err["sug"]}')
            if i < len(todos_errores):
                print()

    print(f'\n{sep}\n')
    return todos_errores


# ============================================================
# PARTE 10: Interfaz interactiva
# ============================================================

EJEMPLOS = [
    ('La niña alto corre',        'del proyecto — error de género'),
    ('Los perro negro ladra',      'del proyecto — error de número'),
    ('El gato gris duerme',        'del proyecto — concordancia correcta'),
    ('Una casa bonita',            'SN simple correcto'),
    ('Los niños felices juegan',   'plural correcto'),
    ('La mujer alto come',         'error de género en adjetivo'),
    ('Un flor rojo',               'error de género en det y adj'),
    ('Los gato negro corre',       'múltiples errores'),
    ('La rosa grande corre',       'AMBIGÜEDAD: rosa = N o Adj'),
    ('El joven alto camina',       'AMBIGÜEDAD: joven = N o Adj'),
]

def menu():
    print("""
╔══════════════════════════════════════════════════════════════╗
║   CORRECTOR DE CONCORDANCIA DE GÉNERO Y NÚMERO EN ESPAÑOL   ║
║   Procesamiento de Lenguaje Natural — Univ. del Valle 2026-1║
║   Cristhian Leonardo Albarracín Zapata · 1968253            ║
╚══════════════════════════════════════════════════════════════╝

Herramientas: DFA · CFG · Parser recursivo · DCG/Unificación · Árbol · Ambigüedad

Comandos:
  [e] Ver ejemplos predefinidos
  [s] Salir
  O escriba directamente una frase.
""")

    while True:
        try:
            entrada = input('  Frase > ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\n  Saliendo...')
            break

        if not entrada:
            continue
        if entrada.lower() == 's':
            print('  ¡Hasta luego!')
            break
        if entrada.lower() == 'e':
            print('\n  Ejemplos:')
            for i, (ej, desc) in enumerate(EJEMPLOS, 1):
                print(f'    {i:>2}. "{ej}"  ({desc})')
            try:
                op = input('\n  Número (o Enter para cancelar): ').strip()
                if op.isdigit() and 1 <= int(op) <= len(EJEMPLOS):
                    analizar(EJEMPLOS[int(op)-1][0])
            except (EOFError, KeyboardInterrupt):
                pass
            continue

        analizar(entrada)


# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        frase = ' '.join(sys.argv[1:])
        analizar(frase)
    else:
        menu()
