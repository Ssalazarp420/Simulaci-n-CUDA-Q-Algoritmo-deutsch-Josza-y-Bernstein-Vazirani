import cudaq

# ============================================================================
# ALGORITMOS DEUTSCH-JOZSA Y BERNSTEIN-VAZIRANI DE 3 QUBITS
# ============================================================================

print("\n" + "="*80)
print("ALGORITMOS CUÁNTICOS CON 3 QUBITS")
print("="*80)

# ============================================================================
# PARTE 1: DEUTSCH-JOZSA DE 3 QUBITS
# ============================================================================

print("\n" + "="*80)
print("PARTE 1: ALGORITMO DEUTSCH-JOZSA (3 QUBITS)")
print("="*80)

# Funciones CONSTANTES

@cudaq.kernel
def dj3_constant_0():
    """DJ: f(x) = 0 para todo x"""
    qubits = cudaq.qvector(3)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: no hace nada (f(x) = 0)
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def dj3_constant_1():
    """DJ: f(x) = 1 para todo x"""
    qubits = cudaq.qvector(3)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Oráculo: aplica fase global π
    z(qubits[0])
    z(qubits[1])
    z(qubits[2])
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

# Funciones BALANCEADAS (ejemplos representativos)

@cudaq.kernel
def dj3_balanced_x0():
    """DJ: f(x) = x₀"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    z(qubits[0])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def dj3_balanced_x1():
    """DJ: f(x) = x₁"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    z(qubits[1])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def dj3_balanced_x2():
    """DJ: f(x) = x₂"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    z(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def dj3_balanced_xor_01():
    """DJ: f(x) = x₀ ⊕ x₁"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    cz(qubits[0], qubits[1])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def dj3_balanced_majority():
    """DJ: f(x) = majority(x₀, x₁, x₂) - función balanceada compleja"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # Implementación simplificada de majority
    # majority es 1 si al menos 2 de los 3 bits son 1
    cz(qubits[0], qubits[1])
    cz(qubits[1], qubits[2])
    cz(qubits[0], qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)


def run_deutsch_jozsa_3qubits(kernel_func, function_name, shots=1000):
    """Ejecuta y analiza Deutsch-Jozsa de 3 qubits"""
    
    print(f"\n{'='*80}")
    print(f"Función: {function_name}")
    print(f"{'='*80}")
    
    result = cudaq.sample(kernel_func, shots_count=shots)
    print(f"\nResultados ({shots} shots):")
    print(result)
    
    # Analizar
    result_dict = {}
    for bits, count in result.items():
        result_dict[bits] = count
    
    prob_000 = result_dict.get('000', 0) / shots
    
    print(f"\nProbabilidad de medir |000⟩: {prob_000:.4f}")
    
    if prob_000 > 0.9:
        print("✓ Conclusión: CONSTANTE")
    else:
        print("✓ Conclusión: BALANCEADA")


# ============================================================================
# PARTE 2: BERNSTEIN-VAZIRANI DE 3 QUBITS
# ============================================================================

print("\n\n" + "="*80)
print("PARTE 2: ALGORITMO BERNSTEIN-VAZIRANI (3 QUBITS)")
print("="*80)
print("\nCon 3 qubits hay 2³ = 8 cadenas secretas posibles")

# Implementar las 8 cadenas secretas posibles

@cudaq.kernel
def bv3_s000():
    """BV: s = "000" → f(x) = 0"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    # No aplica fase
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def bv3_s001():
    """BV: s = "001" → f(x) = x₂"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    z(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def bv3_s010():
    """BV: s = "010" → f(x) = x₁"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    z(qubits[1])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def bv3_s011():
    """BV: s = "011" → f(x) = x₁ ⊕ x₂"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    z(qubits[1])
    z(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def bv3_s100():
    """BV: s = "100" → f(x) = x₀"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    z(qubits[0])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def bv3_s101():
    """BV: s = "101" → f(x) = x₀ ⊕ x₂"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    z(qubits[0])
    z(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def bv3_s110():
    """BV: s = "110" → f(x) = x₀ ⊕ x₁"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    z(qubits[0])
    z(qubits[1])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)

@cudaq.kernel
def bv3_s111():
    """BV: s = "111" → f(x) = x₀ ⊕ x₁ ⊕ x₂"""
    qubits = cudaq.qvector(3)
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    z(qubits[0])
    z(qubits[1])
    z(qubits[2])
    
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    
    mz(qubits)


def run_bernstein_vazirani_3qubits(kernel_func, secret_string, shots=1000):
    """Ejecuta y analiza Bernstein-Vazirani de 3 qubits"""
    
    print(f"\n{'='*80}")
    print(f"Buscando cadena secreta: s = \"{secret_string}\"")
    print(f"{'='*80}")
    
    result = cudaq.sample(kernel_func, shots_count=shots)
    print(f"\nResultados ({shots} shots):")
    print(result)
    
    # Analizar
    result_dict = {}
    max_count = 0
    measured_state = ""
    
    for bits, count in result.items():
        result_dict[bits] = count
        if count > max_count:
            max_count = count
            measured_state = bits
    
    probability = max_count / shots
    
    print(f"\nEstado medido más frecuente: |{measured_state}⟩")
    print(f"Probabilidad: {probability:.4f} ({max_count}/{shots})")
    
    if measured_state == secret_string:
        print(f"✓ ¡ÉXITO! Cadena recuperada: s = \"{measured_state}\"")
    else:
        print(f"✗ ERROR: Esperaba \"{secret_string}\" pero midió \"{measured_state}\"")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    
    # EJECUTAR DEUTSCH-JOZSA
    print("\n" + "="*80)
    print("EJECUTANDO DEUTSCH-JOZSA DE 3 QUBITS")
    print("="*80)
    
    run_deutsch_jozsa_3qubits(dj3_constant_0, "Constante: f(x) = 0")
    run_deutsch_jozsa_3qubits(dj3_constant_1, "Constante: f(x) = 1")
    run_deutsch_jozsa_3qubits(dj3_balanced_x0, "Balanceada: f(x) = x₀")
    run_deutsch_jozsa_3qubits(dj3_balanced_x1, "Balanceada: f(x) = x₁")
    run_deutsch_jozsa_3qubits(dj3_balanced_x2, "Balanceada: f(x) = x₂")
    run_deutsch_jozsa_3qubits(dj3_balanced_xor_01, "Balanceada: f(x) = x₀⊕x₁")
    run_deutsch_jozsa_3qubits(dj3_balanced_majority, "Balanceada: f(x) = majority")
    
    # EJECUTAR BERNSTEIN-VAZIRANI
    print("\n\n" + "="*80)
    print("EJECUTANDO BERNSTEIN-VAZIRANI DE 3 QUBITS")
    print("="*80)
    
    run_bernstein_vazirani_3qubits(bv3_s000, "000")
    run_bernstein_vazirani_3qubits(bv3_s001, "001")
    run_bernstein_vazirani_3qubits(bv3_s010, "010")
    run_bernstein_vazirani_3qubits(bv3_s011, "011")
    run_bernstein_vazirani_3qubits(bv3_s100, "100")
    run_bernstein_vazirani_3qubits(bv3_s101, "101")
    run_bernstein_vazirani_3qubits(bv3_s110, "110")
    run_bernstein_vazirani_3qubits(bv3_s111, "111")
    
   # RESUMEN
    print("\n\n" + "="*80)
    print("COMPARACIÓN: 2 QUBITS vs 3 QUBITS")
    print("="*80)
    
    print("\n📊 DEUTSCH-JOZSA:")
    print("   2 qubits: 2² = 4 posibles entradas")
    print("   3 qubits: 2³ = 8 posibles entradas")
    print("   Clásico (peor caso): necesita 2^(n-1) + 1 consultas")
    print("   Cuántico: necesita 1 consulta")
    
    print("\n📊 BERNSTEIN-VAZIRANI:")
    print("   2 qubits: 4 cadenas secretas posibles")
    print("   3 qubits: 8 cadenas secretas posibles")
    print("   Clásico: necesita n consultas")
    print("   Cuántico: necesita 1 consulta")
    
    print("\n" + "="*80)
    print("🚀 VENTAJA CUÁNTICA DEMOSTRADA")
    print("="*80)
    
    print("\nPara 3 qubits:")
    print("  • Deutsch-Jozsa: 5x más rápido (1 consulta vs 5 clásicas)")
    print("  • Bernstein-Vazirani: 3x más rápido (1 consulta vs 3 clásicas)")
    
    print("\n" + "-"*80)
    print("Escalabilidad - Si usáramos más qubits:")
    print("-"*80)
    
    # Tabla formateada
    print("\n┌───────────┬────────────┬──────────────┬────────────┬──────────────┐")
    print("│ n qubits  │ DJ Clásico │ DJ Cuántico  │ BV Clásico │ BV Cuántico  │")
    print("├───────────┼────────────┼──────────────┼────────────┼──────────────┤")
    print("│     3     │      5     │       1      │      3     │       1      │")
    print("├───────────┼────────────┼──────────────┼────────────┼──────────────┤")
    print("│    10     │    513     │       1      │     10     │       1      │")
    print("├───────────┼────────────┼──────────────┼────────────┼──────────────┤")
    print("│   100     │   ~10³⁰    │       1      │    100     │       1      │")
    print("└───────────┴────────────┴──────────────┴────────────┴──────────────┘")
    
    print("\n💡 INTERPRETACIÓN:")
    print("   • DJ Clásico: 2^(n-1) + 1 consultas en el peor caso")
    print("   • BV Clásico: n consultas (una por cada bit de la cadena)")
    print("   • Cuántico: ¡Siempre 1 consulta, sin importar el tamaño!")
    
    print("\n🎯 CONCLUSIÓN CLAVE:")
    print("   A medida que n crece, la ventaja cuántica se vuelve exponencial.")
    print("   Para n=100, la diferencia es de ~10³⁰ consultas (clásico) vs 1 (cuántico).")
    print("   ¡Esto es más que el número de átomos en el universo observable!")
    
    print("\n" + "="*80)
    print("¡Simulación de 3 qubits completada!")
    print("="*80 + "\n")
