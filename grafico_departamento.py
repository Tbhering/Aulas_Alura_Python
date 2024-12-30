import pandas as pd
import matplotlib.pyplot as plt

def grafico_lucro_por_departamento(df, filename):
    # Verificar se as colunas 'departamento' e 'lucro' estão presentes no DataFrame
    print(df.columns)  # Adicionar esta linha para verificar as colunas do DataFrame
    if 'departamento' not in df.columns or 'lucro' not in df.columns:
        raise KeyError("O DataFrame deve conter as colunas 'departamento' e 'lucro'.")

    # Área do Gráfico
    fig, ax = plt.subplots(figsize=(12, 6), dpi=85)

    # Criar gráfico de barras horizontais com cor azul marinho
    bars = ax.barh(df["departamento"], df["lucro"], color='navy')

    ## Personalizando o gráfico
    ax.set_title('Total De Lucro Por Departamento Em 2023', fontsize=18, loc='center', color='black', pad=30, fontweight='bold', fontstyle='italic', fontname='times new roman')
    ax.set_xlabel('Lucro (Em Milhares De Reais)', fontsize=15, labelpad=15, color='black', fontname='times new roman')
    ax.set_ylabel('Departamento', fontsize=15, color='black', fontname='times new roman')
    ax.set_frame_on(False,)
    ax.grid(True, color='grey', ls='--')

    # Adicionar valores no final das barras
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontsize=12, color='red')

    # remover todos os ticks do eixo x e y
    ax.tick_params(axis='both', which='both', length=0)

    plt.xlim(0, df["lucro"].max() + 100)

    plt.savefig(filename, dpi=100, bbox_inches='tight', pad_inches=0)
    plt.show()

# Exemplo de uso
arquivo_saida_dpt = 'C:\\Users\\thbg1\\OneDrive\\Área de Trabalho\\aula_alura\\tabela_financas_por_departamento.txt'
df = pd.read_csv(arquivo_saida_dpt, sep='\t')
grafico_lucro_por_departamento(df, 'C:\\Users\\thbg1\\OneDrive\\Área de Trabalho\\aula_alura\\lucro_por_departamento.png')