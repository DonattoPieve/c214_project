import pandas as pd
from PySide6.QtWidgets import QApplication, QFileDialog

app = QApplication([])

arquivo_csv, _ = QFileDialog.getOpenFileName(None, "Selecionar arquivo CSV", "", "CSV Files (*.csv)")
if arquivo_csv:

    for encoding in ["utf-8", "ISO-8859-1", "latin1", "windows-1252"]:
        try:
            df = pd.read_csv(arquivo_csv, encoding=encoding, delimiter=";", on_bad_lines="skip")
            break  
        except UnicodeDecodeError:
            continue 

    arquivo_xlsx, _ = QFileDialog.getSaveFileName(None, "Salvar como Excel", "", "Excel Files (*.xlsx)")
    if arquivo_xlsx:
        df.to_excel(arquivo_xlsx, index=False)

app.quit()