# 5 Даны два файла, в каждом из которых находится запись 
# многочлена. Задача - сформировать файл, содержащий сумму 
# многочленов.

data1 = open('1file5Task.txt', 'r')
adata = []
for line in data1:
    adata = str(line)
    adata1 = adata.split('+')
    adata2 = adata.split('-')
data2 = open('2file5Task.txt', 'r')
bdata  = []
for line in data2:
    bdata = str(line)
    bdata1 = bdata.split('+')
    bdata2 = bdata.split('-')

print(adata1)
print(adata2)
print(bdata1)
print(bdata2)
data1.close()
data2.close()

# Не осилил.