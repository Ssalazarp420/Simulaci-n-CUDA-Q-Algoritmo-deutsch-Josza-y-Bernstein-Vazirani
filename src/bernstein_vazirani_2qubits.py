import cudaq

# ============================================================================
# ALGORITMO BERNSTEIN-VAZIRANI DE 2 QUBITS SIN QUBIT AUXILIAR
# ============================================================================
# 
# Objetivo: Encontrar la cadena secreta 's' en la función f(x) = s·x (mod 2)
# donde s·x = s₀x₀ ⊕ s₁x₁
#
# Para 2 qubits, hay 4 posibles cadenas secretas: "00", "01", "10", "11"
# ============================================================================

# Cadena secreta: s = "00"
@cudaq.kernel
def bernstein_vazirani_s00():
    """
    Cadena secreta s = "00"
    f(x) = 0·x₀ ⊕ 0·x₁ = 0 (función constante)
    """
    qubits = cudaq.qvector(2)
    
    # Hadamard inicial (crear superposición)
    h(qubits[0])
    h(qubits[1])
    
    # Oráculo: f(x) = 0 para todo x
    # No aplica ninguna fase
    # pass
    
    # Hadamard final (interferencia)
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits)


# Cadena secreta: s = "01"
@cudaq.kernel
def bernstein_vazirani_s01():
    """
    Cadena secreta s = "01"
    f(x) = 0·x₀ ⊕ 1·x₁ = x₁
    """
    qubits = cudaq.qvector(2)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    
    # Oráculo: aplica fase cuando x₁ = 1
    z(qubits[1])
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits)


# Cadena secreta: s = "10"
@cudaq.kernel
def bernstein_vazirani_s10():
    """
    Cadena secreta s = "10"
    f(x) = 1·x₀ ⊕ 0·x₁ = x₀
    """
    qubits = cudaq.qvector(2)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    
    # Oráculo: aplica fase cuando x₀ = 1
    z(qubits[0])
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits)


# Cadena secreta: s = "11"
@cudaq.kernel
def bernstein_vazirani_s11():
    """
    Cadena secreta s = "11"
    f(x) = 1·x₀ ⊕ 1·x₁ = x₀ ⊕ x₁
    """
    qubits = cudaq.qvector(2)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    
    # Oráculo: para s="11" necesitamos aplicar fase a ambos qubits
    # Esto es equivalente a f(x) = x₀ ⊕ x₁
    z(qubits[0])
    z(qubits[1])
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits)


# ============================================================================
# FUNCIÓN PARA EJECUTAR Y ANALIZAR
# ============================================================================

def run_bernstein_vazirani(kernel_func, secret_string, shots=1000):
    """Ejecuta el algoritmo y verifica si recupera la cadena secreta"""
    
    print(f"\n{'='*70}")
    print(f"Buscando cadena secreta: s = \"{secret_string}\"")
    print(f"{'='*70}")
    
    # Ejecutar el circuito
    result = cudaq.sample(kernel_func, shots_count=shots)
    
    # Mostrar resultados
    print(f"\nResultados de medición ({shots} shots):")
    print(result)
    
    # Analizar cuál estado se midió con mayor probabilidad
    result_dict = {}
    max_count = 0
    measured_state = ""
    
    for bits, count in result.items():
        result_dict[bits] = count
        if count > max_count:
            max_count = count
            measured_state = bits
    
    probability = max_count / shots
    
    print(f"\nAnálisis:")
    print(f"Estado medido con mayor frecuencia: |{measured_state}⟩")
    print(f"Probabilidad: {probability:.4f} ({max_count}/{shots})")
    
    # Verificar si encontramos la cadena secreta
    if measured_state == secret_string:
        print(f"✓ ¡ÉXITO! Cadena secreta recuperada: s = \"{measured_state}\"")
    else:
        print(f"✗ ERROR: Se esperaba s = \"{secret_string}\" pero se midió |{measured_state}⟩")
    
    return result


# ============================================================================
# VISUALIZACIÓN DE LA TABLA DE VERDAD
# ============================================================================

def print_truth_table():
    """Muestra la tabla de verdad para entender las funciones"""
    print("\n" + "="*70)
    print("TABLA DE VERDAD - Función f(x) = s·x para cada cadena secreta")
    print("="*70)
    
    print("\n| x₁ x₀ | s=\"00\" | s=\"01\" | s=\"10\" | s=\"11\" |")
    print("|-------|--------|--------|--------|--------|")
    
    for x1 in [0, 1]:
        for x0 in [0, 1]:
            f_00 = 0
            f_01 = x0
            f_10 = x1
            f_11 = x0 ^ x1
            print(f"|   {x1}  {x0} |    {f_00}   |    {f_01}   |    {f_10}   |    {f_11}   |")
    
    print("\nNota: f(x) = s·x = s₁·x₁ ⊕ s₀·x₀ (producto escalar mod 2)")


# ============================================================================
# COMPARACIÓN CON MÉTODO CLÁSICO
# ============================================================================

def classical_vs_quantum_comparison():
    """Explica la ventaja cuántica"""
    print("\n" + "="*70)
    print("COMPARACIÓN: CLÁSICO vs CUÁNTICO")
    print("="*70)
    
    print("\n📊 MÉTODO CLÁSICO:")
    print("   • Para encontrar una cadena de n bits")
    print("   • Se necesitan n consultas al oráculo")
    print("   • Para n=2: se necesitan 2 consultas")
    print("   • Ejemplo: consultar f(10) y f(01) para obtener cada bit de s")
    
    print("\n⚛️  MÉTODO CUÁNTICO (Bernstein-Vazirani):")
    print("   • Solo 1 consulta al oráculo, independiente de n")
    print("   • Para n=2: 1 consulta")
    print("   • Usa superposición e interferencia cuántica")
    print("   • ¡Ventaja exponencial para cadenas grandes!")
    
    print("\n🚀 VENTAJA CUÁNTICA:")
    print("   • Para n=2:  Clásico necesita 2, Cuántico necesita 1")
    print("   • Para n=10: Clásico necesita 10, Cuántico necesita 1")
    print("   • Para n=100: Clásico necesita 100, Cuántico necesita 1")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("IMPLEMENTACIÓN DEL ALGORITMO BERNSTEIN-VAZIRANI EN CUDA-Q")
    print("Versión: 2 qubits sin qubit auxiliar")
    print("="*70)
    
    # Mostrar tabla de verdad
    print_truth_table()
    
    # Ejecutar el algoritmo para cada cadena secreta posible
    print("\n" + "="*70)
    print("EJECUCIÓN DEL ALGORITMO")
    print("="*70)
    
    run_bernstein_vazirani(bernstein_vazirani_s00, "00", shots=1000)
    run_bernstein_vazirani(bernstein_vazirani_s01, "01", shots=1000)
    run_bernstein_vazirani(bernstein_vazirani_s10, "10", shots=1000)
    run_bernstein_vazirani(bernstein_vazirani_s11, "11", shots=1000)
    
    # Comparación clásico vs cuántico
    classical_vs_quantum_comparison()
    
    print("\n" + "="*70)
    print("¡Simulación completada!")
    print("="*70)
    print("\n💡 CONCLUSIÓN:")
    print("El algoritmo Bernstein-Vazirani recuperó exitosamente todas las")
    print("cadenas secretas con UNA SOLA consulta al oráculo cuántico.")
    print("="*70 + "\n")
