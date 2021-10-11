import pyarrow.parquet as pq
import pandas as pd

#Abrir o 1º parquet
df = pq.read_table(source=r'C:\Users\barateir\Documents\sharedfolder\workspace\test_automation\parquet_test\21-04-29_16-48-58-240-CM1623667295.parquet').to_pandas()

html = df.to_html()
print(html)

text_file = open("index.html", "w")
text_file.write(html)
text_file.close()
#Abrir o 2º parquet
#df2 = pq.read_table(source=r'C:\Users\barateir\Documents\sharedfolder\workspace\test_automation\parquet_test\21-04-29_16-48-58-240-CM1623667308.parquet').to_pandas()

#Fazer o merge de dois parquets
##result = df.append(df2)

#Criar um novo parquet a partir do merge dos outros 2
#result.to_parquet('parquets_merged.parquet')


#df = pd.DataFrame(list(resultRow["parquetlist"].items()),columns = ['customer','use_case','system','datatype','source1','source2','source3','layer','processor','description','filename_in','filename_out','filesize_in','filesize_out','status','date_begin','date_end','cur_type','cur_rule','error_level','error_message','other'])

