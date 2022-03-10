open_file = open('CupcakeInvoices.csv','r')

invoice_total = 0

for line in open_file:
    line = line.strip('\n').split(',')
    for value in line:
        invoice_cost = float(line[len(line) - 1])
        invoice_total = invoice_total + invoice_cost
        invoice_total_pretty = round(invoice_total, 2)

open_file.close()
print(invoice_total_pretty)