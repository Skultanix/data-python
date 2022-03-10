# import plotly.express as px
import statistics

open_file = open('CupcakeInvoices.csv')

invoice_total = 0

chocolate_count = 0
strawberry_count = 0
vanilla_count = 0 

choco_rev = 0
strb_rev = 0
vanilla_rev = 0

choco_ages = []
strb_ages = []
vanilla_ages = []

for line in open_file:
    line = line.strip('\n').split(',')
    for value in line:
        invoice_cost = float(line[len(line) - 1])
        invoice_total = invoice_total + invoice_cost
        invoice_total_pretty = round(invoice_total, 2)
    
    for value in line:
        age = line[3]
        if value == 'Chocolate':
            chocolate_count +=1
            choco_rev = round((choco_rev + invoice_cost),2)
            choco_ages.append(int(age))
        elif value == "Strawberry":
            strawberry_count +=1
            strb_rev = round((strb_rev + invoice_cost),2)
            strb_ages.append(int(age))
        elif value == "Vanilla":
            vanilla_count +=1
            vanilla_rev = round((vanilla_rev + invoice_cost),2)
            vanilla_ages.append(int(age))
    

open_file.close()

choco_age_avg = round(statistics.mean(choco_ages),2)
strb_age_avg = round(statistics.mean(strb_ages),2)
vanilla_age_avg = round(statistics.mean(vanilla_ages),2)

choco_age_med = statistics.median(choco_ages)
strb_age_med = statistics.median(strb_ages)
vanilla_age_med = statistics.median(vanilla_ages)

print(invoice_total_pretty)
print()
print(chocolate_count, strawberry_count, vanilla_count)
print()
print(choco_rev, strb_rev, vanilla_rev)
print()
print(choco_ages, strb_ages, vanilla_ages)
print()
print(choco_age_med, strb_age_med, vanilla_age_med)
print()
print(choco_age_avg, strb_age_avg, vanilla_age_avg)