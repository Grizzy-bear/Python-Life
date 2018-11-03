# for dir in `ls ./m4aToMp3/ | tr ' ' '#'`
for dir in `ls ./m4aToMp3/ | tr ' ' '#'`
do
#  mv "`echo $dir | sed 's/#/ /g'`" "`echo $dir | sed 's/#//g'`"
  
  echo $dir
done
echo "finished!!!"
