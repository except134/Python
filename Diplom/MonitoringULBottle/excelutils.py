import pandas as pd

def export_all_sheets_to_txt(output_file_name, out_excel_file):
    wb = pd.ExcelFile(out_excel_file)
    
    with open(output_file_name, 'w', encoding='utf-8') as file:
        # �������� �� ���� �������� � excel
        for sheet_name in wb.sheet_names:
            # ������ ��� ������ �� �������
            df = wb.parse(sheet_name)
            # �������� �� ���� ������� 
            for index, row in df.iterrows():
                for cell in row:
                    # ����� �������� ������ � �������� ����
                    file.write(str(cell) + '\n')
                file.write('\n')


