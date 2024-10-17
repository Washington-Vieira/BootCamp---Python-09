from src.interface.classes.csv_class import CsvProcessor
#import pandas as pd


arquivo_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'
arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(['estado', 'preço'], ['SP', '10,50']))


# arquivo_csv2 = './exemplo2.csv'
# filtro2 = 'estado'
# limite2 = 'PR'
# arquivo_CSV2 = CsvProcessor(arquivo_csv2)
# arquivo_CSV2.carregar_csv()
# print(arquivo_CSV2.filtrar_por(filtro2, limite2))
# print(arquivo_CSV2.sub_filtro('preço', '10,55'))