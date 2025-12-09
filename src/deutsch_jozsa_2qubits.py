import cudaq

# ============================================================================
# ALGORITMO DEUTSCH-JOZSA DE 2 QUBITS SIN QUBIT AUXILIAR
# ============================================================================

# Función constante: f(x) = 0
@cudaq.kernel
def deutsch_jozsa_constant_0():
    qubits = cudaq.qvector(2)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    
    # Oráculo: no hace nada (fase 0)
    # pass
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits)

# Función constante: f(x) = 1
@cudaq.kernel
def deutsch_jozsa_constant_1():
    qubits = cudaq.qvector(2)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    
    # Oráculo: aplica fase π a todos
    z(qubits[0])
    z(qubits[1])
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits)

# Función balanceada: f(x) = x₀
@cudaq.kernel
def deutsch_jozsa_balanced_x0():
    qubits = cudaq.qvector(2)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    
    # Oráculo: aplica Z cuando x₀ = 1
    z(qubits[0])
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits)

# Función balanceada: f(x) = x₁
@cudaq.kernel
def deutsch_jozsa_balanced_x1():
    qubits = cudaq.qvector(2)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    
    # Oráculo: aplica Z cuando x₁ = 1
    z(qubits[1])
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits)

# Función balanceada: f(x) = x₀ ⊕ x₁
@cudaq.kernel
def deutsch_jozsa_balanced_xor():
    qubits = cudaq.qvector(2)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    
    # Oráculo: CZ para XOR
    cz(qubits[0], qubits[1])
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits)

# Función balanceada: f(x) = NOT(x₀ ⊕ x₁)
@cudaq.kernel
def deutsch_jozsa_balanced_xnor():
    qubits = cudaq.qvector(2)
    
    # Hadamard inicial
    h(qubits[0])
    h(qubits[1])
    
    # Oráculo: fase para XNOR
    z(qubits[0])
    z(qubits[1])
    cz(qubits[0], qubits[1])
    
    # Hadamard final
    h(qubits[0])
    h(qubits[1])
    
    mz(qubits)


# ============================================================================
# FUNCIÓN PARA EJECUTAR Y ANALIZAR
# ============================================================================

def run_and_analyze(kernel_func, oracle_name, shots=1000):
    """Ejecuta el kernel y analiza los resultados"""
    
    print(f"\n{'='*70}")
    print(f"Ejecutando: {oracle_name}")
    print(f"{'='*70}")
    
    # Ejecutar el circuito
    result = cudaq.sample(kernel_func, shots_count=shots)
    
    # Mostrar resultados
    print(f"\nResultados de medición ({shots} shots):")
    print(result)
    
    # Analizar
    result_dict = {}
    for bits, count in result.items():
        result_dict[bits] = count
    
    prob_00 = result_dict.get('00', 0) / shots
    
    print(f"\nAnálisis:")
    print(f"Probabilidad de medir |00⟩: {prob_00:.4f}")
    
    if prob_00 > 0.9:
        print("✓ Conclusión: La función es CONSTANTE")
    else:
        print("✓ Conclusión: La función es BALANCEADA")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("IMPLEMENTACIÓN DEL ALGORITMO DEUTSCH-JOZSA EN CUDA-Q")
    print("Versión: 2 qubits sin qubit auxiliar")
    print("="*70)
    
    # Ejecutar cada función
    run_and_analyze(deutsch_jozsa_constant_0, "Constante f(x)=0")
    run_and_analyze(deutsch_jozsa_constant_1, "Constante f(x)=1")
    run_and_analyze(deutsch_jozsa_balanced_x0, "Balanceada f(x)=x₀")
    run_and_analyze(deutsch_jozsa_balanced_x1, "Balanceada f(x)=x₁")
    run_and_analyze(deutsch_jozsa_balanced_xor, "Balanceada f(x)=x₀⊕x₁")
    run_and_analyze(deutsch_jozsa_balanced_xnor, "Balanceada f(x)=NOT(x₀⊕x₁)")
    
    print("\n" + "="*70)
    print("¡Simulación completada!")
    print("="*70 + "\n")