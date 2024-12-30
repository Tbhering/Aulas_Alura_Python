import pandas as pd
import matplotlib.pyplot as plt

def grafico_vendas_por_mes(df, filename):
    # Verificar se as colunas 'Mês' e 'Vendas' estão presentes no DataFrame
    print(df.columns)  # Adicionar esta linha para verificar as colunas do DataFrame
    if 'Mês' not in df.columns or 'vendas' not in df.columns:
        raise KeyError("O DataFrame deve conter as colunas 'Mês' e 'vendas'.")

    # Área do Gráfico
    fig, ax = plt.subplots(figsize=(12, 6), dpi=85)

    ax.plot(df["Mês"], df["vendas"], lw=3, marker="o")

    ## Personalizando o gráfico
    ax.set_title('Total De Vendas Em 2023', fontsize=18, loc='center', color='black', pad=30, fontweight='bold', fontstyle='italic', fontname='times new roman')
    ax.set_xlabel('Mês', fontsize=15, labelpad=15, color='black', fontname='times new roman')
    ax.set_ylabel('Vendas (Em Milhares De Reais)', fontsize=15, color='black', fontname='times new roman')
    ax.set_frame_on(False,)
    ax.grid(True, color='grey', ls='--')

    # remover todos os ticks do eixo x e y
    ax.tick_params(axis='both', which='both', length=0)

    plt.ylim(0, df["vendas"].max() + 100)

    plt.savefig(filename, dpi=100, bbox_inches='tight', pad_inches=0)
    plt.show()

# Exemplo de uso
arquivo_saida_mes = 'C:\\Users\\thbg1\\OneDrive\\Área de Trabalho\\aula_alura\\tabela_financas_por_mes.txt'
df = pd.read_csv(arquivo_saida_mes, sep='\t')
grafico_vendas_por_mes(df, 'C:\\Users\\thbg1\\OneDrive\\Área de Trabalho\\aula_alura\\vendas_por_mes.pdf')