#! /bin/bash


# files = "/home/lamplight/Documents/programmer/practice/python/dailyPro/Python-Life/NeedForLife/ximalaya/test/m4aToMp3"

# for file in ./m4aToMp3/*.mp3


for file in `find ./m4aToMp3/ -name \*.m4a`
do
  temp=${file##*/}
#  echo "temp:"$temp
 # newTemp=`echo $temp | tr ' ' '#'`
  fileEnd=${file##*.}
# echo "file:"$newTemp
  filename=${temp%.*}
  echo -e "文件名:"$filename
  ffmpeg -i $file -acodec pcm_s16le -ac 2 -ar 44100 $filename.wav

done

