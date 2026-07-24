from pathlib import Path
path = Path('index.html')
text = path.read_text(encoding='utf-8')
header_old = 'let html = `<div style="text-align:center; overflow-x:auto;"><table class="consejeras-table" style="margin:0 auto; min-width:900px;">\n<thead><tr><th>LINEA</th><th>CONSULTA</th><th>DIAGNOSTICO</th><th>%</th><th>ORDEN</th><th>%</th><th>PRESUPUESTO</th><th>%</th><th>VENTA</th><th>VENTA/PRESUPUESTO</th><th>VENTA/ORDEN</th><th>VENTA/CONSULTA</th></tr></thead><tbody>\n`;'
header_new = 'let html = `<div style="text-align:center; overflow-x:auto;"><table class="consejeras-table" style="margin:0 auto; min-width:900px;">\n<thead><tr><th>LINEA</th><th>CONSULTA</th><th>DIAGNOSTICO</th><th>%</th><th>ORDEN</th><th>%</th><th>PRESUPUESTO</th><th>%</th><th>VENTA</th><th>VENTA/PRESUPUESTO</th><th>VENTA/ORDEN</th>${showConversionRate ? '<th>VENTA/CONSULTA</th>' : ''}</tr></thead><tbody>\n`;'
row_old = '<td style="text-align:center;">${r.ventaPresupuesto}</td>\n<td style="text-align:center;">${r.ventaOrden}</td>\n<td style="text-align:center;">${r.consulta ? pct(r.venta, r.consulta) : \'0.00%\'}</td>\n</tr>\n`;'
row_new = '<td style="text-align:center;">${r.ventaPresupuesto}</td>\n<td style="text-align:center;">${r.ventaOrden}</td>' + (showConversionRate ? '\n<td style="text-align:center;">${r.consulta ? pct(r.venta, r.consulta) : \'0.00%\'}</td>' : '') + '\n</tr>\n`;'
print('header found', header_old in text)
print('row found', row_old in text)
