#! /bin/bash

curr_time=`date "+%Y-%m-%d"`
start_time=`date "+%s"`  # define time
echo $start_time
echo $curr_time
`[ -e /tmp/fd1 ] || mkfifo /tmp/fd1` # create named pip
exec 3<>/tmp/fd1                  # create file description and connect the PipFile with "<" ">"
rm -rf /tmp/fd1                   # it's time delete the file and keep the file description

for ((i=1; i<=10; i++))
do 
  echo >&3                        # &3 represent the file description, give a crsf in the pip
done

# for ((i=1; i<=1000; i++))
# do
  # read -u3                        # represent get one crsf
  # {
    # sleep 1
    # echo 'success'$i
    # echo >&3                        # put the crsf in the old pip
  # }&
# done
#
for file in `find ./files/ -name \*.m4a`
do 
  read -u3
  {
    temp=${file##*/}
    filename=${temp%.*}
    echo "文件名字:"$filename",正在转化成wav......"
    finalPath="./Wavfile/"$filename".wav"
    ffmpeg -i $file -acodec pcm_s16le -ac 2 -ar 44100  $finalPath
    echo $finalPath
    echo "转化成功"$filename
    echo >&3
  }&
done
wait

stop_time=`date "+%s"`           # define the end time 
echo $stop_time
echo "Time: `expr $stop_time - $start_time`"
exec 3<&-                         # close the read about the fileDescription exec 3>&-                         # close the wirte  about the fileDescription
exec 3>&-


