import pandas as pd

url = "https://www.bi.go.id/id/statistik/informasi-kurs/jisdor/Default.aspx"

tables = pd.read_html(url)

print(f"Jumlah tabel: {len(tables)}")

for i, table in enumerate(tables):
    print(f"\n===== TABLE {i} =====")
    print(table.head())
