# Car-Detection

## Setup:
Download and unzip train, supp and test sets into direct parent directory
Download and extract http://www.gti.ssr.upm.es/~jal/download.html to direct parent directory and rename to "GTI Car Detection Database"
mkdir classifier in direct parent directory
opencv folder located on desktop

./opencv_createsamples.exe -info ../../../../../UNSW/COMP9517/Project/Individual/benchmark_velocity_train/info.dat -num 42960 -w 64 -h 36 -vec ../../../../../UNSW/COMP9517/Project/Individual/benchmark_velocity_train/cars.vec

./opencv_traincascade.exe -data ../../../../../UNSW/COMP9517/Project/Individual/classifier -vec ../../../../../UNSW/COMP9517/Project/Individual/benchmark_velocity_train/cars.vec -bg ../../../../../UNSW/COMP9517/Project/Individual/GTI\ Car\ Detection\ Database/negatives.txt -numStages 1 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 5000 -numNeg 3900 -w 64 -h 36 -mode ALL -precalcValBufSize 1024 -precalcIdxBufSize 1024