import cudaq

# ============================================================================
# ALGORITMOS DEUTSCH-JOZSA Y BERNSTEIN-VAZIRANI CON QUBIT AUXILIAR
# ============================================================================

print("\n" + "="*80)
print("ALGORITMOS CUÁNTICOS CON QUBIT AUXILIAR (Versión Tradicional)")
print("="*80)

# ============================================================================
# PARTE 1: DEUTSCH-JOZSA CON QUBIT AUXILIAR (2 QUBITS DE TRABAJO + 1 AUXILIAR)
# ============================================================================

print("\n" + "="*80)
print("PARTE 1: ALGORITMO DEUTSCH-JOZSA CON QUBIT AUXILIAR")
print("="*80)
print("\nEsquema: 2 qubits de trabajo + 1 qubit auxiliar = 3 qubits totales")

# Funciones CONSTANTES

@cudaq.kernel
def dj_aux_constant_0():
    """DJ con auxiliar: f(x) = 0 para todo x"""
    qubits = cudaq.qvector(3)  # 2 trabajo + 1 auxiliar
    
    # Preparar auxiliar en |1⟩
    x(qubits[2])
    
    # Hadamard en todos los qubits
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])  # Auxiliar: (|0⟩ - |1⟩)/√2
    
    # Oráculo: f(x) = 0 → no hace nada
    # No aplicamos ninguna operación
    
    # Hadamard en qubits de trabajo
    h(qubits[0])
    h(qubits[1])
    
    # Medir solo los qubits de trabajo
    mz(qubits[0])
    mz(qubits[1])


@cudaq.kernel
def dj_aux_constant_1():
    """DJ con auxiliar: f(x) = 1 para todo x"""
    qubits = cudaq.qvector(3)
    
    # Preparar auxiliar en |1⟩
    x(qubits[2])
    
    # Hadamard en todos
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: f(x) = 1 → aplicar X al auxiliar para todo x
    # Esto equivale a aplicar CNOT desde cada qubit de trabajo
    # Pero como f(x)=1 siempre, aplicamos X directo
    x(qubits[2])
    
    # Hadamard en qubits de trabajo
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits[0])
    mz(qubits[1])


# Funciones BALANCEADAS

@cudaq.kernel
def dj_aux_balanced_x0():
    """DJ con auxiliar: f(x) = x₀"""
    qubits = cudaq.qvector(3)
    
    x(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: f(x) = x₀ → CNOT de q0 a auxiliar
    cx(qubits[0], qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits[0])
    mz(qubits[1])


@cudaq.kernel
def dj_aux_balanced_x1():
    """DJ con auxiliar: f(x) = x₁"""
    qubits = cudaq.qvector(3)
    
    x(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: f(x) = x₁ → CNOT de q1 a auxiliar
    cx(qubits[1], qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits[0])
    mz(qubits[1])


@cudaq.kernel
def dj_aux_balanced_xor():
    """DJ con auxiliar: f(x) = x₀ ⊕ x₁"""
    qubits = cudaq.qvector(3)
    
    x(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: f(x) = x₀ ⊕ x₁ → CNOT de q0 y q1 a auxiliar
    cx(qubits[0], qubits[2])
    cx(qubits[1], qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits[0])
    mz(qubits[1])


@cudaq.kernel
def dj_aux_balanced_xnor():
    """DJ con auxiliar: f(x) = NOT(x₀ ⊕ x₁)"""
    qubits = cudaq.qvector(3)
    
    x(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: f(x) = NOT(x₀ ⊕ x₁)
    # Primero calculamos x₀ ⊕ x₁
    cx(qubits[0], qubits[2])
    cx(qubits[1], qubits[2])
    # Luego negamos el resultado
    x(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits[0])
    mz(qubits[1])


def run_deutsch_jozsa_auxiliar(kernel_func, function_name, shots=1000):
    """Ejecuta y analiza Deutsch-Jozsa CON qubit auxiliar"""
    
    print(f"\n{'='*80}")
    print(f"Función: {function_name}")
    print(f"{'='*80}")
    
    result = cudaq.sample(kernel_func, shots_count=shots)
    print(f"\nResultados ({shots} shots):")
    print(result)
    
    # Analizar (solo miramos los primeros 2 bits, ignoramos el auxiliar)
    result_dict = {}
    for bits, count in result.items():
        # Extraer solo los 2 primeros bits (qubits de trabajo)
        work_bits = bits[:2] if len(bits) >= 2 else bits
        result_dict[work_bits] = result_dict.get(work_bits, 0) + count
    
    prob_00 = result_dict.get('00', 0) / shots
    
    print(f"\nProbabilidad de medir |00⟩ (qubits de trabajo): {prob_00:.4f}")
    
    if prob_00 > 0.9:
        print("✓ Conclusión: CONSTANTE")
    else:
        print("✓ Conclusión: BALANCEADA")


# ============================================================================
# PARTE 2: BERNSTEIN-VAZIRANI CON QUBIT AUXILIAR
# ============================================================================

print("\n\n" + "="*80)
print("PARTE 2: ALGORITMO BERNSTEIN-VAZIRANI CON QUBIT AUXILIAR")
print("="*80)
print("\nEsquema: 2 qubits de trabajo + 1 qubit auxiliar = 3 qubits totales")

# Las 4 cadenas secretas posibles para 2 qubits

@cudaq.kernel
def bv_aux_s00():
    """BV con auxiliar: s = "00" → f(x) = 0"""
    qubits = cudaq.qvector(3)
    
    # Preparar auxiliar en |1⟩
    x(qubits[2])
    
    # Hadamard en todos
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: f(x) = 0 (no hace nada)
    
    # Hadamard en qubits de trabajo
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits[0])
    mz(qubits[1])


@cudaq.kernel
def bv_aux_s01():
    """BV con auxiliar: s = "01" → f(x) = x₁"""
    qubits = cudaq.qvector(3)
    
    x(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: s₁ = 1 → CNOT de q1 a auxiliar
    cx(qubits[1], qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits[0])
    mz(qubits[1])


@cudaq.kernel
def bv_aux_s10():
    """BV con auxiliar: s = "10" → f(x) = x₀"""
    qubits = cudaq.qvector(3)
    
    x(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: s₀ = 1 → CNOT de q0 a auxiliar
    cx(qubits[0], qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits[0])
    mz(qubits[1])


@cudaq.kernel
def bv_aux_s11():
    """BV con auxiliar: s = "11" → f(x) = x₀ ⊕ x₁"""
    qubits = cudaq.qvector(3)
    
    x(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: s₀ = 1 y s₁ = 1 → CNOT de ambos a auxiliar
    cx(qubits[0], qubits[2])
    cx(qubits[1], qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits[0])
    mz(qubits[1])


def run_bernstein_vazirani_auxiliar(kernel_func, secret_string, shots=1000):
    """Ejecuta y analiza Bernstein-Vazirani CON qubit auxiliar"""
    
    print(f"\n{'='*80}")
    print(f"Buscando cadena secreta: s = \"{secret_string}\"")
    print(f"{'='*80}")
    
    result = cudaq.sample(kernel_func, shots_count=shots)
    print(f"\nResultados ({shots} shots):")
    print(result)
    
    # Analizar (solo los 2 primeros bits)
    result_dict = {}
    max_count = 0
    measured_state = ""
    
    for bits, count in result.items():
        work_bits = bits[:2] if len(bits) >= 2 else bits
        result_dict[work_bits] = result_dict.get(work_bits, 0) + count
        if result_dict[work_bits] > max_count:
            max_count = result_dict[work_bits]
            measured_state = work_bits
    
    probability = max_count / shots
    
    print(f"\nEstado medido más frecuente (qubits de trabajo): |{measured_state}⟩")
    print(f"Probabilidad: {probability:.4f} ({max_count}/{shots})")
    
    if measured_state == secret_string:
        print(f"✓ ¡ÉXITO! Cadena recuperada: s = \"{measured_state}\"")
    else:
        print(f"✗ ERROR: Esperaba \"{secret_string}\" pero midió \"{measured_state}\"")


# ============================================================================
# COMPARACIÓN: CON vs SIN QUBIT AUXILIAR
# ============================================================================

def print_comparison_table():
    """Imprime tabla comparativa de recursos"""
    
    print("\n" + "="*80)
    print("COMPARACIÓN: CON QUBIT AUXILIAR vs SIN QUBIT AUXILIAR")
    print("="*80)
    
    print("\n┌─────────────────────┬──────────────────┬──────────────────┬─────────────┐")
    print("│ Aspecto             │ CON Auxiliar     │ SIN Auxiliar     │ Mejora      │")
    print("├─────────────────────┼──────────────────┼──────────────────┼─────────────┤")
    print("│ Qubits (n=2)        │        3         │        2         │   -33%      │")
    print("├─────────────────────┼──────────────────┼──────────────────┼─────────────┤")
    print("│ Qubits (n=3)        │        4         │        3         │   -25%      │")
    print("├─────────────────────┼──────────────────┼──────────────────┼─────────────┤")
    print("│ Compuertas típicas  │    CNOT, H, X    │      Z, H        │  Más simple │")
    print("├─────────────────────┼──────────────────┼──────────────────┼─────────────┤")
    print("│ Complejidad oráculo │    Mayor         │     Menor        │    Mejor    │")
    print("├─────────────────────┼──────────────────┼──────────────────┼─────────────┤")
    print("│ Preparación inicial │    X en aux      │     Ninguna      │    Mejor    │")
    print("├─────────────────────┼──────────────────┼──────────────────┼─────────────┤")
    print("│ Resultado           │    Idéntico      │    Idéntico      │   Empate    │")
    print("└─────────────────────┴──────────────────┴──────────────────┴─────────────┘")
    
    print("\n💡 VENTAJAS DE LA VERSIÓN SIN QUBIT AUXILIAR:")
    print("   ✓ Menos qubits físicos requeridos")
    print("   ✓ Compuertas más simples (Z vs CNOT)")
    print("   ✓ Menor profundidad de circuito")
    print("   ✓ Más eficiente para sistemas con recursos limitados")
    print("   ✓ Mejor para implementación fotónica (como en tu documento)")
    
    print("\n💡 VENTAJAS DE LA VERSIÓN CON QUBIT AUXILIAR:")
    print("   ✓ Esquema más tradicional y didáctico")
    print("   ✓ Más fácil de entender conceptualmente")
    print("   ✓ Separación clara entre entrada y salida de f(x)")
    print("   ✓ Mejor para debugging y verificación")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    
    # EJECUTAR DEUTSCH-JOZSA CON AUXILIAR
    print("\n" + "="*80)
    print("EJECUTANDO DEUTSCH-JOZSA CON QUBIT AUXILIAR")
    print("="*80)
    
    run_deutsch_jozsa_auxiliar(dj_aux_constant_0, "Constante: f(x) = 0")
    run_deutsch_jozsa_auxiliar(dj_aux_constant_1, "Constante: f(x) = 1")
    run_deutsch_jozsa_auxiliar(dj_aux_balanced_x0, "Balanceada: f(x) = x₀")
    run_deutsch_jozsa_auxiliar(dj_aux_balanced_x1, "Balanceada: f(x) = x₁")
    run_deutsch_jozsa_auxiliar(dj_aux_balanced_xor, "Balanceada: f(x) = x₀⊕x₁")
    run_deutsch_jozsa_auxiliar(dj_aux_balanced_xnor, "Balanceada: f(x) = NOT(x₀⊕x₁)")
    
    # EJECUTAR BERNSTEIN-VAZIRANI CON AUXILIAR
    print("\n\n" + "="*80)
    print("EJECUTANDO BERNSTEIN-VAZIRANI CON QUBIT AUXILIAR")
    print("="*80)
    
    run_bernstein_vazirani_auxiliar(bv_aux_s00, "00")
    run_bernstein_vazirani_auxiliar(bv_aux_s01, "01")
    run_bernstein_vazirani_auxiliar(bv_aux_s10, "10")
    run_bernstein_vazirani_auxiliar(bv_aux_s11, "11")
    
    # TABLA COMPARATIVA
    print_comparison_table()
    
    print("\n" + "="*80)
    print("¡Simulación con qubit auxiliar completada!")
    print("="*80)
    
    print("\n📚 RESUMEN:")
    print("   Has implementado ambas versiones de los algoritmos:")
    print("   • Versión TRADICIONAL (con qubit auxiliar) ✓")
    print("   • Versión OPTIMIZADA (sin qubit auxiliar) ✓")
    print("\n   Ambas producen los mismos resultados, pero la versión")
    print("   sin auxiliar es más eficiente en recursos.")
    print("="*80 + "\n")