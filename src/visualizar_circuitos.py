import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np

# ============================================================================
# VISUALIZACIÓN DE CIRCUITOS CUÁNTICOS
# ============================================================================

class QuantumCircuitDrawer:
    """Clase para dibujar circuitos cuánticos de manera visual"""
    
    def __init__(self, num_qubits, figsize=(14, 8)):
        self.num_qubits = num_qubits
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(-0.5, num_qubits + 0.5)
        self.ax.axis('off')
        
        # Dibujar líneas de qubits
        for i in range(num_qubits):
            y = num_qubits - 1 - i
            self.ax.plot([0.5, 9.5], [y, y], 'k-', linewidth=1.5)
            self.ax.text(0.2, y, f'|q{i}⟩', fontsize=14, ha='right', va='center')
    
    def add_gate(self, gate_type, qubit, position, label=''):
        """Añade una compuerta al circuito"""
        y = self.num_qubits - 1 - qubit
        
        if gate_type == 'H':
            # Compuerta Hadamard (cuadrado azul)
            box = FancyBboxPatch((position - 0.2, y - 0.25), 0.4, 0.5,
                                boxstyle="round,pad=0.05", 
                                edgecolor='blue', facecolor='lightblue', linewidth=2)
            self.ax.add_patch(box)
            self.ax.text(position, y, 'H', fontsize=16, ha='center', va='center', weight='bold')
        
        elif gate_type == 'Z':
            # Compuerta Z (cuadrado verde)
            box = FancyBboxPatch((position - 0.2, y - 0.25), 0.4, 0.5,
                                boxstyle="round,pad=0.05", 
                                edgecolor='green', facecolor='lightgreen', linewidth=2)
            self.ax.add_patch(box)
            self.ax.text(position, y, 'Z', fontsize=16, ha='center', va='center', weight='bold')
        
        elif gate_type == 'M':
            # Medición (símbolo de medidor)
            box = FancyBboxPatch((position - 0.25, y - 0.3), 0.5, 0.6,
                                boxstyle="round,pad=0.05", 
                                edgecolor='red', facecolor='lightyellow', linewidth=2)
            self.ax.add_patch(box)
            # Dibujar símbolo de medidor
            arc = patches.Arc((position, y - 0.1), 0.3, 0.3, angle=0, theta1=0, theta2=180, 
                            color='red', linewidth=2)
            self.ax.add_patch(arc)
            self.ax.plot([position, position + 0.1], [y - 0.1, y + 0.2], 'r-', linewidth=2)
        
        elif gate_type == 'X':
            # Compuerta X (cuadrado naranja)
            box = FancyBboxPatch((position - 0.2, y - 0.25), 0.4, 0.5,
                                boxstyle="round,pad=0.05", 
                                edgecolor='orange', facecolor='lightyellow', linewidth=2)
            self.ax.add_patch(box)
            self.ax.text(position, y, 'X', fontsize=16, ha='center', va='center', weight='bold')
    
    def add_cz(self, control_qubit, target_qubit, position):
        """Añade una compuerta CZ (Controlled-Z)"""
        y_control = self.num_qubits - 1 - control_qubit
        y_target = self.num_qubits - 1 - target_qubit
        
        # Dibujar línea vertical conectando los qubits
        self.ax.plot([position, position], [y_control, y_target], 'purple', linewidth=2)
        
        # Círculo de control (filled)
        circle_control = Circle((position, y_control), 0.1, color='purple', zorder=10)
        self.ax.add_patch(circle_control)
        
        # Círculo de target (filled)
        circle_target = Circle((position, y_target), 0.1, color='purple', zorder=10)
        self.ax.add_patch(circle_target)
        
        # Etiqueta CZ
        mid_y = (y_control + y_target) / 2
        self.ax.text(position + 0.4, mid_y, 'CZ', fontsize=12, color='purple', weight='bold')
    
    def add_barrier(self, position, label=''):
        """Añade una barrera visual (separador)"""
        for i in range(self.num_qubits):
            y = self.num_qubits - 1 - i
            self.ax.plot([position, position], [y - 0.3, y + 0.3], 'gray', 
                        linewidth=3, linestyle='--', alpha=0.5)
        if label:
            self.ax.text(position, self.num_qubits + 0.3, label, 
                        fontsize=11, ha='center', style='italic', color='gray')
    
    def add_label(self, position, y_offset, text, fontsize=10):
        """Añade una etiqueta descriptiva"""
        self.ax.text(position, -0.7 + y_offset, text, 
                    fontsize=fontsize, ha='center', style='italic', color='blue')
    
    def set_title(self, title):
        """Establece el título del circuito"""
        self.ax.text(5, self.num_qubits + 0.8, title, 
                    fontsize=18, ha='center', weight='bold')
    
    def save(self, filename):
        """Guarda la figura"""
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✓ Circuito guardado en: {filename}")
    
    def show(self):
        """Muestra la figura"""
        plt.tight_layout()
        plt.show()


# ============================================================================
# FUNCIÓN PARA CREAR CIRCUITOS ESPECÍFICOS
# ============================================================================

def draw_deutsch_jozsa_2qubits():
    """Dibuja el circuito de Deutsch-Jozsa para 2 qubits"""
    
    drawer = QuantumCircuitDrawer(num_qubits=2, figsize=(14, 6))
    drawer.set_title('Algoritmo Deutsch-Jozsa (2 qubits) - Sin qubit auxiliar')
    
    # Estado inicial
    drawer.add_label(0.5, 0, '|00⟩', fontsize=12)
    
    # Primera capa de Hadamard
    drawer.add_gate('H', 0, 1.5)
    drawer.add_gate('H', 1, 1.5)
    drawer.add_barrier(2.3, 'Superposición')
    
    # Oráculo (ejemplo: función balanceada f(x) = x₀)
    drawer.add_gate('Z', 0, 4)
    drawer.add_barrier(5, 'Oráculo')
    drawer.add_label(4, 0, 'Uf', fontsize=12)
    
    # Segunda capa de Hadamard
    drawer.add_gate('H', 0, 6.5)
    drawer.add_gate('H', 1, 6.5)
    drawer.add_barrier(7.3, 'Interferencia')
    
    # Medición
    drawer.add_gate('M', 0, 8.5)
    drawer.add_gate('M', 1, 8.5)
    
    drawer.save('deutsch_jozsa_2qubits.png')
    return drawer


def draw_deutsch_jozsa_3qubits():
    """Dibuja el circuito de Deutsch-Jozsa para 3 qubits"""
    
    drawer = QuantumCircuitDrawer(num_qubits=3, figsize=(14, 7))
    drawer.set_title('Algoritmo Deutsch-Jozsa (3 qubits) - Sin qubit auxiliar')
    
    # Estado inicial
    drawer.add_label(0.5, 0, '|000⟩', fontsize=12)
    
    # Primera capa de Hadamard
    drawer.add_gate('H', 0, 1.5)
    drawer.add_gate('H', 1, 1.5)
    drawer.add_gate('H', 2, 1.5)
    drawer.add_barrier(2.3, 'Superposición')
    
    # Oráculo (ejemplo: función balanceada f(x) = x₀ ⊕ x₁)
    drawer.add_cz(0, 1, 4)
    drawer.add_barrier(5, 'Oráculo')
    drawer.add_label(4, 0, 'Uf', fontsize=12)
    
    # Segunda capa de Hadamard
    drawer.add_gate('H', 0, 6.5)
    drawer.add_gate('H', 1, 6.5)
    drawer.add_gate('H', 2, 6.5)
    drawer.add_barrier(7.3, 'Interferencia')
    
    # Medición
    drawer.add_gate('M', 0, 8.5)
    drawer.add_gate('M', 1, 8.5)
    drawer.add_gate('M', 2, 8.5)
    
    drawer.save('deutsch_jozsa_3qubits.png')
    return drawer


def draw_bernstein_vazirani_2qubits():
    """Dibuja el circuito de Bernstein-Vazirani para 2 qubits"""
    
    drawer = QuantumCircuitDrawer(num_qubits=2, figsize=(14, 6))
    drawer.set_title('Algoritmo Bernstein-Vazirani (2 qubits) - Cadena s = "11"')
    
    # Estado inicial
    drawer.add_label(0.5, 0, '|00⟩', fontsize=12)
    
    # Primera capa de Hadamard
    drawer.add_gate('H', 0, 1.5)
    drawer.add_gate('H', 1, 1.5)
    drawer.add_barrier(2.3, 'Superposición')
    
    # Oráculo (cadena secreta s = "11")
    drawer.add_gate('Z', 0, 4)
    drawer.add_gate('Z', 1, 4)
    drawer.add_barrier(5, 'Oráculo')
    drawer.add_label(4, 0, 'Uf (s="11")', fontsize=12)
    
    # Segunda capa de Hadamard
    drawer.add_gate('H', 0, 6.5)
    drawer.add_gate('H', 1, 6.5)
    drawer.add_barrier(7.3, 'Interferencia')
    
    # Medición
    drawer.add_gate('M', 0, 8.5)
    drawer.add_gate('M', 1, 8.5)
    
    drawer.add_label(9.2, 0, '→ |11⟩', fontsize=12)
    
    drawer.save('bernstein_vazirani_2qubits.png')
    return drawer


def draw_bernstein_vazirani_3qubits():
    """Dibuja el circuito de Bernstein-Vazirani para 3 qubits"""
    
    drawer = QuantumCircuitDrawer(num_qubits=3, figsize=(14, 7))
    drawer.set_title('Algoritmo Bernstein-Vazirani (3 qubits) - Cadena s = "101"')
    
    # Estado inicial
    drawer.add_label(0.5, 0, '|000⟩', fontsize=12)
    
    # Primera capa de Hadamard
    drawer.add_gate('H', 0, 1.5)
    drawer.add_gate('H', 1, 1.5)
    drawer.add_gate('H', 2, 1.5)
    drawer.add_barrier(2.3, 'Superposición')
    
    # Oráculo (cadena secreta s = "101")
    drawer.add_gate('Z', 0, 4)
    drawer.add_gate('Z', 2, 4)
    drawer.add_barrier(5, 'Oráculo')
    drawer.add_label(4, 0, 'Uf (s="101")', fontsize=12)
    
    # Segunda capa de Hadamard
    drawer.add_gate('H', 0, 6.5)
    drawer.add_gate('H', 1, 6.5)
    drawer.add_gate('H', 2, 6.5)
    drawer.add_barrier(7.3, 'Interferencia')
    
    # Medición
    drawer.add_gate('M', 0, 8.5)
    drawer.add_gate('M', 1, 8.5)
    drawer.add_gate('M', 2, 8.5)
    
    drawer.add_label(9.2, 0, '→ |101⟩', fontsize=12)
    
    drawer.save('bernstein_vazirani_3qubits.png')
    return drawer


def draw_comparison_diagram():
    """Dibuja un diagrama comparativo de complejidad"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Gráfico 1: Deutsch-Jozsa
    n_values = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])
    classical_dj = 2**(n_values - 1) + 1
    quantum_dj = np.ones_like(n_values)
    
    ax1.plot(n_values, classical_dj, 'ro-', linewidth=2, markersize=8, label='Clásico: 2^(n-1)+1')
    ax1.plot(n_values, quantum_dj, 'b^-', linewidth=2, markersize=8, label='Cuántico: 1')
    ax1.set_xlabel('Número de qubits (n)', fontsize=14)
    ax1.set_ylabel('Número de consultas', fontsize=14)
    ax1.set_title('Deutsch-Jozsa: Complejidad de Consultas', fontsize=16, weight='bold')
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    ax1.set_ylim(0.5, 1000)
    
    # Gráfico 2: Bernstein-Vazirani
    classical_bv = n_values
    quantum_bv = np.ones_like(n_values)
    
    ax2.plot(n_values, classical_bv, 'ro-', linewidth=2, markersize=8, label='Clásico: n')
    ax2.plot(n_values, quantum_bv, 'b^-', linewidth=2, markersize=8, label='Cuántico: 1')
    ax2.set_xlabel('Número de qubits (n)', fontsize=14)
    ax2.set_ylabel('Número de consultas', fontsize=14)
    ax2.set_title('Bernstein-Vazirani: Complejidad de Consultas', fontsize=16, weight='bold')
    ax2.legend(fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 12)
    
    plt.tight_layout()
    plt.savefig('comparacion_complejidad.png', dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✓ Gráfico de comparación guardado en: comparacion_complejidad.png")
    plt.close()


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("VISUALIZACIÓN DE CIRCUITOS CUÁNTICOS")
    print("="*80)
    
    print("\nGenerando diagramas de circuitos...")
    
    # Crear todos los circuitos
    draw_deutsch_jozsa_2qubits()
    draw_deutsch_jozsa_3qubits()
    draw_bernstein_vazirani_2qubits()
    draw_bernstein_vazirani_3qubits()
    draw_comparison_diagram()
    
    print("\n" + "="*80)
    print("✓ ¡Todas las visualizaciones han sido generadas exitosamente!")
    print("="*80)
    
    print("\nArchivos generados:")
    print("  1. deutsch_jozsa_2qubits.png")
    print("  2. deutsch_jozsa_3qubits.png")
    print("  3. bernstein_vazirani_2qubits.png")
    print("  4. bernstein_vazirani_3qubits.png")
    print("  5. comparacion_complejidad.png")
    
    print("\nPuedes abrir estas imágenes con cualquier visualizador de imágenes.")
    print("En WSL2, puedes usar: explorer.exe <nombre_archivo>.png")
    print("="*80 + "\n")