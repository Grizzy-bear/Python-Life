cd ~/Desktop/test/file/
rename -v 's/./trytest/' *.txt
# try --> trytesttry
# 可是.txt --> trytest可是.txt
# 会自动添加到前缀，不会自动删除文件名
ls 
cd - 