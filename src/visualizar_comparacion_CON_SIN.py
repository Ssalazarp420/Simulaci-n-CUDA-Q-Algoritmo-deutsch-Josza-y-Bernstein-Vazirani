import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
import numpy as np

# ============================================================================
# VISUALIZACIÓN COMPARATIVA: CON vs SIN QUBIT AUXILIAR
# ============================================================================

def create_comparison_deutsch_jozsa():
    """Crea comparación visual de Deutsch-Jozsa"""
    
    fig = plt.figure(figsize=(16, 10))
    
    # ========== VERSIÓN SIN AUXILIAR (ARRIBA) ==========
    ax1 = plt.subplot(2, 1, 1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(-0.5, 2.5)
    ax1.axis('off')
    
    # Título
    ax1.text(5, 2.8, 'Deutsch-Jozsa SIN Qubit Auxiliar (Optimizada)', 
            fontsize=16, ha='center', weight='bold', color='green')
    ax1.text(5, 2.4, 'Función balanceada: f(x) = x₀ ⊕ x₁', 
            fontsize=12, ha='center', style='italic')
    
    # Líneas de qubits
    for i in range(2):
        y = 1 - i
        ax1.plot([0.5, 9.5], [y, y], 'k-', linewidth=1.5)
        ax1.text(0.2, y, f'|q{i}⟩', fontsize=14, ha='right', va='center')
    
    # Estado inicial
    ax1.text(0.5, -0.5, '|00⟩', fontsize=12, ha='center', color='blue', style='italic')
    
    # Primera capa de Hadamard
    for i in range(2):
        y = 1 - i
        box = FancyBboxPatch((1.3, y - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                            edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax1.add_patch(box)
        ax1.text(1.5, y, 'H', fontsize=16, ha='center', va='center', weight='bold')
    
    # Barrera
    for i in range(2):
        y = 1 - i
        ax1.plot([2.5, 2.5], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax1.text(2.5, 2, 'Superposición', fontsize=10, ha='center', style='italic', color='gray')
    
    # Oráculo CZ
    ax1.plot([4, 4], [1, 0], 'purple', linewidth=2)
    circle1 = Circle((4, 1), 0.1, color='purple', zorder=10)
    ax1.add_patch(circle1)
    circle2 = Circle((4, 0), 0.1, color='purple', zorder=10)
    ax1.add_patch(circle2)
    ax1.text(4.4, 0.5, 'CZ', fontsize=11, color='purple', weight='bold')
    
    # Barrera
    for i in range(2):
        y = 1 - i
        ax1.plot([5.5, 5.5], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax1.text(5.5, 2, 'Oráculo', fontsize=10, ha='center', style='italic', color='gray')
    
    # Segunda capa de Hadamard
    for i in range(2):
        y = 1 - i
        box = FancyBboxPatch((6.8, y - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                            edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax1.add_patch(box)
        ax1.text(7, y, 'H', fontsize=16, ha='center', va='center', weight='bold')
    
    # Barrera
    for i in range(2):
        y = 1 - i
        ax1.plot([8, 8], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax1.text(8, 2, 'Interferencia', fontsize=10, ha='center', style='italic', color='gray')
    
    # Medición
    for i in range(2):
        y = 1 - i
        box = FancyBboxPatch((8.75, y - 0.3), 0.5, 0.6, boxstyle="round,pad=0.05", 
                            edgecolor='red', facecolor='lightyellow', linewidth=2)
        ax1.add_patch(box)
        arc = patches.Arc((9, y - 0.1), 0.3, 0.3, angle=0, theta1=0, theta2=180, 
                        color='red', linewidth=2)
        ax1.add_patch(arc)
        ax1.plot([9, 9.1], [y - 0.1, y + 0.2], 'r-', linewidth=2)
    
    # Recursos
    ax1.text(0.5, -0.9, '📊 Recursos: 2 qubits | 4H + 1CZ | Profundidad: 3', 
            fontsize=11, ha='left', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
    
    # ========== VERSIÓN CON AUXILIAR (ABAJO) ==========
    ax2 = plt.subplot(2, 1, 2)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(-0.5, 3.5)
    ax2.axis('off')
    
    # Título
    ax2.text(5, 3.8, 'Deutsch-Jozsa CON Qubit Auxiliar (Tradicional)', 
            fontsize=16, ha='center', weight='bold', color='blue')
    ax2.text(5, 3.4, 'Función balanceada: f(x) = x₀ ⊕ x₁', 
            fontsize=12, ha='center', style='italic')
    
    # Líneas de qubits
    for i in range(3):
        y = 2 - i
        ax2.plot([0.5, 9.5], [y, y], 'k-', linewidth=1.5)
        if i < 2:
            ax2.text(0.2, y, f'|q{i}⟩', fontsize=14, ha='right', va='center')
        else:
            ax2.text(0.2, y, '|aux⟩', fontsize=14, ha='right', va='center', color='orange')
    
    # Resaltar auxiliar
    rect = Rectangle((0.5, 0 - 0.35), 9, 0.7, facecolor='yellow', alpha=0.15, zorder=0)
    ax2.add_patch(rect)
    
    # Estado inicial
    ax2.text(0.5, -0.5, '|001⟩', fontsize=12, ha='center', color='blue', style='italic')
    
    # X en auxiliar
    box = FancyBboxPatch((0.8, 0 - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                        edgecolor='orange', facecolor='lightyellow', linewidth=2)
    ax2.add_patch(box)
    ax2.text(1, 0, 'X', fontsize=16, ha='center', va='center', weight='bold')
    
    # Primera capa de Hadamard
    for i in range(3):
        y = 2 - i
        box = FancyBboxPatch((1.8, y - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                            edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax2.add_patch(box)
        ax2.text(2, y, 'H', fontsize=16, ha='center', va='center', weight='bold')
    
    # Barrera
    for i in range(3):
        y = 2 - i
        ax2.plot([3, 3], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax2.text(3, 3.2, 'Superposición', fontsize=10, ha='center', style='italic', color='gray')
    
    # Oráculo: CNOT de q0 a aux
    ax2.plot([4.5, 4.5], [2, 0], 'b', linewidth=2)
    circle1 = Circle((4.5, 2), 0.1, color='blue', zorder=10)
    ax2.add_patch(circle1)
    circle2 = Circle((4.5, 0), 0.2, color='white', edgecolor='blue', linewidth=2, zorder=10)
    ax2.add_patch(circle2)
    ax2.plot([4.35, 4.65], [0, 0], 'b-', linewidth=2, zorder=11)
    ax2.plot([4.5, 4.5], [-0.15, 0.15], 'b-', linewidth=2, zorder=11)
    
    # CNOT de q1 a aux
    ax2.plot([5.5, 5.5], [1, 0], 'b', linewidth=2)
    circle3 = Circle((5.5, 1), 0.1, color='blue', zorder=10)
    ax2.add_patch(circle3)
    circle4 = Circle((5.5, 0), 0.2, color='white', edgecolor='blue', linewidth=2, zorder=10)
    ax2.add_patch(circle4)
    ax2.plot([5.35, 5.65], [0, 0], 'b-', linewidth=2, zorder=11)
    ax2.plot([5.5, 5.5], [-0.15, 0.15], 'b-', linewidth=2, zorder=11)
    
    # Barrera
    for i in range(3):
        y = 2 - i
        ax2.plot([6.5, 6.5], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax2.text(6.5, 3.2, 'Oráculo', fontsize=10, ha='center', style='italic', color='gray')
    
    # Segunda capa de Hadamard (solo trabajo)
    for i in range(2):
        y = 2 - i
        box = FancyBboxPatch((7.3, y - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                            edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax2.add_patch(box)
        ax2.text(7.5, y, 'H', fontsize=16, ha='center', va='center', weight='bold')
    
    # Barrera
    for i in range(3):
        y = 2 - i
        ax2.plot([8.3, 8.3], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax2.text(8.3, 3.2, 'Interferencia', fontsize=10, ha='center', style='italic', color='gray')
    
    # Medición (solo trabajo)
    for i in range(2):
        y = 2 - i
        box = FancyBboxPatch((9.05, y - 0.3), 0.5, 0.6, boxstyle="round,pad=0.05", 
                            edgecolor='red', facecolor='lightyellow', linewidth=2)
        ax2.add_patch(box)
        arc = patches.Arc((9.3, y - 0.1), 0.3, 0.3, angle=0, theta1=0, theta2=180, 
                        color='red', linewidth=2)
        ax2.add_patch(arc)
        ax2.plot([9.3, 9.4], [y - 0.1, y + 0.2], 'r-', linewidth=2)
    
    # Recursos
    ax2.text(0.5, -0.9, '📊 Recursos: 3 qubits | 1X + 6H + 2CNOT | Profundidad: 4', 
            fontsize=11, ha='left', bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('comparacion_deutsch_jozsa.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Comparación Deutsch-Jozsa guardada: comparacion_deutsch_jozsa.png")
    plt.close()


def create_comparison_bernstein_vazirani():
    """Crea comparación visual de Bernstein-Vazirani"""
    
    fig = plt.figure(figsize=(16, 10))
    
    # ========== VERSIÓN SIN AUXILIAR (ARRIBA) ==========
    ax1 = plt.subplot(2, 1, 1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(-0.5, 2.5)
    ax1.axis('off')
    
    # Título
    ax1.text(5, 2.8, 'Bernstein-Vazirani SIN Qubit Auxiliar (Optimizada)', 
            fontsize=16, ha='center', weight='bold', color='green')
    ax1.text(5, 2.4, 'Cadena secreta: s = "11"', 
            fontsize=12, ha='center', style='italic')
    
    # Líneas de qubits
    for i in range(2):
        y = 1 - i
        ax1.plot([0.5, 9.5], [y, y], 'k-', linewidth=1.5)
        ax1.text(0.2, y, f'|q{i}⟩', fontsize=14, ha='right', va='center')
    
    # Estado inicial
    ax1.text(0.5, -0.5, '|00⟩', fontsize=12, ha='center', color='blue', style='italic')
    
    # Primera capa de Hadamard
    for i in range(2):
        y = 1 - i
        box = FancyBboxPatch((1.3, y - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                            edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax1.add_patch(box)
        ax1.text(1.5, y, 'H', fontsize=16, ha='center', va='center', weight='bold')
    
    # Barrera
    for i in range(2):
        y = 1 - i
        ax1.plot([2.5, 2.5], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax1.text(2.5, 2, 'Superposición', fontsize=10, ha='center', style='italic', color='gray')
    
    # Oráculo: Z en q0 y q1
    for i in range(2):
        y = 1 - i
        box = FancyBboxPatch((3.8, y - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                            edgecolor='green', facecolor='lightgreen', linewidth=2)
        ax1.add_patch(box)
        ax1.text(4, y, 'Z', fontsize=16, ha='center', va='center', weight='bold')
    
    # Barrera
    for i in range(2):
        y = 1 - i
        ax1.plot([5.5, 5.5], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax1.text(5.5, 2, 'Oráculo', fontsize=10, ha='center', style='italic', color='gray')
    
    # Segunda capa de Hadamard
    for i in range(2):
        y = 1 - i
        box = FancyBboxPatch((6.8, y - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                            edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax1.add_patch(box)
        ax1.text(7, y, 'H', fontsize=16, ha='center', va='center', weight='bold')
    
    # Barrera
    for i in range(2):
        y = 1 - i
        ax1.plot([8, 8], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax1.text(8, 2, 'Interferencia', fontsize=10, ha='center', style='italic', color='gray')
    
    # Medición
    for i in range(2):
        y = 1 - i
        box = FancyBboxPatch((8.75, y - 0.3), 0.5, 0.6, boxstyle="round,pad=0.05", 
                            edgecolor='red', facecolor='lightyellow', linewidth=2)
        ax1.add_patch(box)
        arc = patches.Arc((9, y - 0.1), 0.3, 0.3, angle=0, theta1=0, theta2=180, 
                        color='red', linewidth=2)
        ax1.add_patch(arc)
        ax1.plot([9, 9.1], [y - 0.1, y + 0.2], 'r-', linewidth=2)
    
    # Resultado
    ax1.text(9.7, 0.5, '→ |11⟩', fontsize=14, ha='left', color='green', weight='bold')
    
    # Recursos
    ax1.text(0.5, -0.9, '📊 Recursos: 2 qubits | 4H + 2Z | Profundidad: 3', 
            fontsize=11, ha='left', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
    
    # ========== VERSIÓN CON AUXILIAR (ABAJO) ==========
    ax2 = plt.subplot(2, 1, 2)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(-0.5, 3.5)
    ax2.axis('off')
    
    # Título
    ax2.text(5, 3.8, 'Bernstein-Vazirani CON Qubit Auxiliar (Tradicional)', 
            fontsize=16, ha='center', weight='bold', color='blue')
    ax2.text(5, 3.4, 'Cadena secreta: s = "11"', 
            fontsize=12, ha='center', style='italic')
    
    # Líneas de qubits
    for i in range(3):
        y = 2 - i
        ax2.plot([0.5, 9.5], [y, y], 'k-', linewidth=1.5)
        if i < 2:
            ax2.text(0.2, y, f'|q{i}⟩', fontsize=14, ha='right', va='center')
        else:
            ax2.text(0.2, y, '|aux⟩', fontsize=14, ha='right', va='center', color='orange')
    
    # Resaltar auxiliar
    rect = Rectangle((0.5, 0 - 0.35), 9, 0.7, facecolor='yellow', alpha=0.15, zorder=0)
    ax2.add_patch(rect)
    
    # Estado inicial
    ax2.text(0.5, -0.5, '|001⟩', fontsize=12, ha='center', color='blue', style='italic')
    
    # X en auxiliar
    box = FancyBboxPatch((0.8, 0 - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                        edgecolor='orange', facecolor='lightyellow', linewidth=2)
    ax2.add_patch(box)
    ax2.text(1, 0, 'X', fontsize=16, ha='center', va='center', weight='bold')
    
    # Primera capa de Hadamard
    for i in range(3):
        y = 2 - i
        box = FancyBboxPatch((1.8, y - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                            edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax2.add_patch(box)
        ax2.text(2, y, 'H', fontsize=16, ha='center', va='center', weight='bold')
    
    # Barrera
    for i in range(3):
        y = 2 - i
        ax2.plot([3, 3], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax2.text(3, 3.2, 'Superposición', fontsize=10, ha='center', style='italic', color='gray')
    
    # Oráculo: CNOT de q0 a aux
    ax2.plot([4.5, 4.5], [2, 0], 'b', linewidth=2)
    circle1 = Circle((4.5, 2), 0.1, color='blue', zorder=10)
    ax2.add_patch(circle1)
    circle2 = Circle((4.5, 0), 0.2, color='white', edgecolor='blue', linewidth=2, zorder=10)
    ax2.add_patch(circle2)
    ax2.plot([4.35, 4.65], [0, 0], 'b-', linewidth=2, zorder=11)
    ax2.plot([4.5, 4.5], [-0.15, 0.15], 'b-', linewidth=2, zorder=11)
    
    # CNOT de q1 a aux
    ax2.plot([5.5, 5.5], [1, 0], 'b', linewidth=2)
    circle3 = Circle((5.5, 1), 0.1, color='blue', zorder=10)
    ax2.add_patch(circle3)
    circle4 = Circle((5.5, 0), 0.2, color='white', edgecolor='blue', linewidth=2, zorder=10)
    ax2.add_patch(circle4)
    ax2.plot([5.35, 5.65], [0, 0], 'b-', linewidth=2, zorder=11)
    ax2.plot([5.5, 5.5], [-0.15, 0.15], 'b-', linewidth=2, zorder=11)
    
    # Barrera
    for i in range(3):
        y = 2 - i
        ax2.plot([6.5, 6.5], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax2.text(6.5, 3.2, 'Oráculo', fontsize=10, ha='center', style='italic', color='gray')
    
    # Segunda capa de Hadamard (solo trabajo)
    for i in range(2):
        y = 2 - i
        box = FancyBboxPatch((7.3, y - 0.25), 0.4, 0.5, boxstyle="round,pad=0.05", 
                            edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax2.add_patch(box)
        ax2.text(7.5, y, 'H', fontsize=16, ha='center', va='center', weight='bold')
    
    # Barrera
    for i in range(3):
        y = 2 - i
        ax2.plot([8.3, 8.3], [y - 0.3, y + 0.3], 'gray', linewidth=3, linestyle='--', alpha=0.5)
    ax2.text(8.3, 3.2, 'Interferencia', fontsize=10, ha='center', style='italic', color='gray')
    
    # Medición (solo trabajo)
    for i in range(2):
        y = 2 - i
        box = FancyBboxPatch((9.05, y - 0.3), 0.5, 0.6, boxstyle="round,pad=0.05", 
                            edgecolor='red', facecolor='lightyellow', linewidth=2)
        ax2.add_patch(box)
        arc = patches.Arc((9.3, y - 0.1), 0.3, 0.3, angle=0, theta1=0, theta2=180, 
                        color='red', linewidth=2)
        ax2.add_patch(arc)
        ax2.plot([9.3, 9.4], [y - 0.1, y + 0.2], 'r-', linewidth=2)
    
    # Resultado
    ax2.text(9.7, 1, '→ |11⟩', fontsize=14, ha='left', color='blue', weight='bold')
    
    # Recursos
    ax2.text(0.5, -0.9, '📊 Recursos: 3 qubits | 1X + 6H + 2CNOT | Profundidad: 4', 
            fontsize=11, ha='left', bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('comparacion_bernstein_vazirani.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Comparación Bernstein-Vazirani guardada: comparacion_bernstein_vazirani.png")
    plt.close()


def create_resource_comparison_chart():
    """Crea gráfico comparativo de recursos"""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Datos
    n_qubits = np.array([2, 3, 4, 5, 6])
    
    # Gráfico 1: Número de qubits
    qubits_sin = n_qubits
    qubits_con = n_qubits + 1
    
    x = np.arange(len(n_qubits))
    width = 0.35
    
    ax1.bar(x - width/2, qubits_sin, width, label='Sin auxiliar', color='green', alpha=0.8)
    ax1.bar(x + width/2, qubits_con, width, label='Con auxiliar', color='blue', alpha=0.8)
    ax1.set_xlabel('n (qubits de trabajo)', fontsize=12)
    ax1.set_ylabel('Qubits totales requeridos', fontsize=12)
    ax1.set_title('Comparación: Número de Qubits', fontsize=14, weight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(n_qubits)
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Gráfico 2: Profundidad del circuito
    depth_sin = np.array([3, 3, 3, 3, 3])
    depth_con = np.array([4, 4, 4, 4, 4])
    
    ax2.bar(x - width/2, depth_sin, width, label='Sin auxiliar', color='green', alpha=0.8)
    ax2.bar(x + width/2, depth_con, width, label='Con auxiliar', color='blue', alpha=0.8)
    ax2.set_xlabel('n (qubits de trabajo)', fontsize=12)
    ax2.set_ylabel('Profundidad del circuito', fontsize=12)
    ax2.set_title('Comparación: Profundidad', fontsize=14, weight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(n_qubits)
    ax2.legend(fontsize=11)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Gráfico 3: Número de compuertas
    gates_sin = 2 * n_qubits + 1
    gates_con = 1 + 3 * n_qubits + n_qubits
    
    ax3.bar(x - width/2, gates_sin, width, label='Sin auxiliar', color='green', alpha=0.8)
    ax3.bar(x + width/2, gates_con, width, label='Con auxiliar', color='blue', alpha=0.8)
    ax3.set_xlabel('n (qubits de trabajo)', fontsize=12)
    ax3.set_ylabel('Número de compuertas', fontsize=12)
    ax3.set_title('Comparación: Complejidad Total', fontsize=14, weight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(n_qubits)
    ax3.legend(fontsize=11)
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Gráfico 4: Tabla resumen
    ax4.axis('off')
    
    table_data = [
        ['Aspecto', 'Sin Auxiliar', 'Con Auxiliar', 'Ventaja'],
        ['Qubits (n=2)', '2', '3', '✓ -33%'],
        ['Qubits (n=3)', '3', '4', '✓ -25%'],
        ['Profundidad', '3', '4', '✓ -25%'],
        ['Compuertas', 'Menos', 'Más', '✓ Mejor'],
        ['Tipo compuertas', 'Z, H', 'CNOT, H, X', '✓ Más simple'],
        ['Coherencia', 'Mayor', 'Menor', '✓ Mejor'],
        ['Implementación', 'Directa', 'Tradicional', '✓ Más eficiente']
    ]
    
    table = ax4.table(cellText=table_data, cellLoc='left', loc='center',
                     colWidths=[0.25, 0.25, 0.25, 0.25])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2.5)
    
    for i in range(4):
        table[(0, i)].set_facecolor('#4CAF50')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    for i in range(1, len(table_data)):
        for j in range(4):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#f0f0f0')
    
    ax4.set_title('Resumen Comparativo', fontsize=14, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('comparacion_recursos.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Gráfico de recursos guardado: comparacion_recursos.png")
    plt.close()


if __name__ == "__main__":
    print("\n" + "="*80)
    print("VISUALIZACIÓN COMPARATIVA: CON vs SIN QUBIT AUXILIAR")
    print("="*80)
    
    print("\nGenerando comparaciones visuales...")
    
    create_comparison_deutsch_jozsa()
    create_comparison_bernstein_vazirani()
    create_resource_comparison_chart()
    
    print("\n" + "="*80)
    print("✓ ¡Todas las comparaciones han sido generadas!")
    print("="*80)
    
    print("\nArchivos generados:")
    print("  1. comparacion_deutsch_jozsa.png")
    print("  2. comparacion_bernstein_vazirani.png")
    print("  3. comparacion_recursos.png")
    
    print("\n📊 CONCLUSIONES:")
    print("   • Versión sin auxiliar usa menos qubits")
    print("   • Versión sin auxiliar tiene menor profundidad")
    print("   • Versión sin auxiliar usa compuertas más simples")
    print("   • Ambas versiones producen resultados idénticos")
    
    print("\nAbrir imágenes: explorer.exe <archivo>.png")
    print("="*80 + "\n")