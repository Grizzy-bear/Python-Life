import csv

# csvFile = open('./csvData.txt','a')
# writer = csv.writer(csvFile)
# writer.writerow(['名字','显示名字','性别','身高','地点','签名','头像'])
# csvFile.close()

with open('./csvData.txt','a') as f:
    writer = csv.writer(f)
    writer.writerow(['名字','显示名字','性别','身高','地点','签名','头像'])

print("ok")