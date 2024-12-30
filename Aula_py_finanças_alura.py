# importar_vendas.py
import pandas as pd

# Importando o Relatório de Vendas e Atualizando a Data de Pedido para o Tipo Data
def importar_vendas():
    vendas = pd.read_csv("https://raw.githubusercontent.com/afonsosr2/python-financas/main/Video_01/vendas.csv")
    vendas["data_pedido"] = pd.to_datetime(vendas["data_pedido"], format="%Y-%m-%d")
    
    # Caminho de saída para o arquivo
    arquivo_saida = 'C:\\Users\\thbg1\\OneDrive\\Área de Trabalho\\tabela_financas.txt'
    vendas.to_csv(arquivo_saida, sep='\t', index=False)
    
    print(f"Arquivo salvo em: {arquivo_saida}")
    return vendas

if __name__ == "__main__":
    vendas = importar_vendas()
    print(vendas)
