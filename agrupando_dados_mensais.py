# organizar_vendas.py
import pandas as pd
from Aula_py_finanças_alura import importar_vendas

def organizar_vendas(vendas):
    # Organizando Arquivo
    vendas_por_mes = vendas[["data_pedido", "vendas"]]
    
    # Agrupar por Mês e Somar as Vendas
    vendas_por_mes.set_index("data_pedido", inplace=True)
    vendas_por_mes = vendas_por_mes.resample("M").sum()
    
    # Renomear o Índice para "Mês" e Redefinir o Índice
    vendas_por_mes = vendas_por_mes.rename_axis("Mês").reset_index()
    
    # Formatando a Coluna "Mês" para exibir apenas o nome do mês
    vendas_por_mes["Mês"] = vendas_por_mes["Mês"].dt.strftime("%b")
    
    # Convertendo a coluna "vendas" para mil e arredondando para duas casas decimais
    vendas_por_mes["vendas"] = (vendas_por_mes["vendas"]/1e3).round(2)
    
    # Caminho de saída para o arquivo
    arquivo_saida_mes = 'C:\\Users\\thbg1\\OneDrive\\Área de Trabalho\\aula_alura\\tabela_financas_por_mes.txt'
    vendas_por_mes.to_csv(arquivo_saida_mes, sep='\t', index=False)
    
    print(f"Arquivo salvo em: {arquivo_saida_mes}")
    return vendas_por_mes

if __name__ == "__main__":
    vendas = importar_vendas()
    vendas_por_mes = organizar_vendas(vendas)
    print(vendas_por_mes)


