    Download SNAP7 library for example: snap7-full-1.2.1
    wget http://sourceforge.net/projects/snap7/files/1.2.1/snap7-full-1.2.1.tar.gz/download
    
    Unzip downloaded file
    in Pi command line:
    tar -zxvf snap7-full-1.2.1.tar.gz
    
    Compile library for raspberry (arm_v6_linux.mk is used for RPI 1. For RPI 2 use arm_v7_linux.mk)
    in Pi command line:
    cd snap7-full-1.2.1/build/unix && sudo make -f arm_v6_linux.mk all
    
    Copy compiled library to lib directories
    in Pi command line:
    sudo cp ../bin/arm_v6-linux/libsnap7.so /usr/lib/libsnap7.so
    sudo cp ../bin/arm_v6-linux/libsnap7.so /usr/local/lib/libsnap7.so
    
    (optional) Install python pip if you don't have it
    in Pi command line:
    sudo apt-get install python-pip
    
    Install python wrapper for SNAP7 lib
    in Pi command line:
    sudo pip install python-snap7
