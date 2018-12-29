import csv
import codecs

with open('./csvData.csv','a') as f:
    # f.write(codecs.BOM_UTF8)
    writer = csv.writer(f)
    writer.writerow(['名字','显示名字','性别','身高','地点','签名','头像'])
f.close()
print("ok")