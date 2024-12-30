import pandas as pd
from Aula_py_finanças_alura import importar_vendas

def organizar_lucro_por_departamento(vendas):
    # Selecionar as colunas 'departamento' e 'lucro'
    lucro_dpt = vendas[["departamento", "lucro"]]

    # Agrupar por 'departamento' e somar o lucro
    lucro_dpt = lucro_dpt.groupby("departamento").sum()
    lucro_dpt = lucro_dpt.reset_index()

    # Converter a coluna 'lucro' para milhares e arredondar para duas casas decimais
    lucro_dpt["lucro"] = (lucro_dpt["lucro"] / 1e3).round(2)

    # Caminho de saída para o arquivo
    arquivo_saida_dpt = 'C:\\Users\\thbg1\\OneDrive\\Área de Trabalho\\aula_alura\\tabela_financas_por_departamento.txt'
    lucro_dpt.to_csv(arquivo_saida_dpt, sep='\t', index=False)

    print(f"Arquivo salvo em: {arquivo_saida_dpt}")
    return lucro_dpt

if __name__ == "__main__":
    vendas = importar_vendas()
    lucro_por_departamento = organizar_lucro_por_departamento(vendas)
    print(lucro_por_departamento)