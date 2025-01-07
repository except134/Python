import pandas as pd

def export_all_sheets_to_txt(output_file_name, out_excel_file):
    wb = pd.ExcelFile(out_excel_file)
    
    with open(output_file_name, 'w', encoding='utf-8') as file:
        # Проходим по всем вкладкам в excel
        for sheet_name in wb.sheet_names:
            # читаем все данные со вкладки
            df = wb.parse(sheet_name)
            # Проходим по всем ячейкам 
            for index, row in df.iterrows():
                for cell in row:
                    # пишем значение ячейки в выходной файл
                    file.write(str(cell) + '\n')
                file.write('\n')


