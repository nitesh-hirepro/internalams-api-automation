from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Font

def postprocess_resume_report(report_path):
    """
    Post-process the Excel report at report_path:
    - Set header row background to green
    - Set extracted columns text color (green/red) based on match with expected
    - Auto-resize columns
    """
    wb = load_workbook(report_path)
    ws = wb.active

    # 1. Set header row background to green
    header_fill = PatternFill(start_color='90EE90', end_color='90EE90', fill_type='solid')
    for cell in ws[1]:
        cell.fill = header_fill

    # 2. Set extracted columns text color (green/red)
    header = [cell.value for cell in ws[1]]
    extract_expected_pairs = [
        ('Expected Name', 'Extracted Name'),
        ('Expected Email', 'Extracted Email'),
        ('Expected Mobile', 'Extracted Mobile'),
        ('Expected Location', 'Extracted Location'),
        ('Expected Experience', 'Extracted Experience'),
        ('Expected Company', 'Extracted Company'),
    ]
    for exp_col, ext_col in extract_expected_pairs:
        if exp_col in header and ext_col in header:
            exp_idx = header.index(exp_col) + 1  # 1-based for openpyxl
            ext_idx = header.index(ext_col) + 1
            for row in range(2, ws.max_row + 1):
                exp_val = ws.cell(row=row, column=exp_idx).value
                ext_val = ws.cell(row=row, column=ext_idx).value
                if str(exp_val).strip().lower() == str(ext_val).strip().lower():
                    ws.cell(row=row, column=ext_idx).font = Font(color='008000')  # Green
                else:
                    ws.cell(row=row, column=ext_idx).font = Font(color='FF0000')  # Red

    # 3. Auto-resize columns
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Get the column name
        for cell in col:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width
    wb.save(report_path) 