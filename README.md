
<h1 align="center">:dna: Face Mask Detection using R-Pi :dna:</h1>
<h3 align="center">A Low Cost Portable Raspberry-Pi Face Mask Detector with live feed</h3>

![Python](https://img.shields.io/badge/python-v3.7-blue)
![Flask](https://img.shields.io/badge/flask-v1.1.1-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-red)
![License](https://img.shields.io/badge/license-MIT-green)

## WebPage and Hardware

### Live feed Webpage
<img src="https://user-images.githubusercontent.com/57676220/132985159-4fe82376-fe11-4006-a6c7-b44e74831445.png" width=400> 


### Project Flowchart

<img src="https://user-images.githubusercontent.com/57676220/132984460-17296834-e5bb-4628-ace2-82ff80c52d97.png" width=500> 

### Neural Network Architecture
<img src = "https://user-images.githubusercontent.com/57676220/132985181-5b9d6250-68dd-43e3-9a32-cc819a3a3a23.png" width=400> 

<!-- GETTING STARTED -->
## Getting Started

**Hardware and basic setup guide.**

### Hardware Setup
  **List of Components**

  <img src="https://user-images.githubusercontent.com/57676220/132984661-7a960acd-5dfb-4e58-8107-9c99ca9db0b4.png" width=300> 
  <img src="https://user-images.githubusercontent.com/57676220/132984682-ac1c78d3-db0b-420f-98e6-be9598f65831.png" width=300> 

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Raspberry Pi OS
  ```sh
  > https://www.raspberrypi.org/software/operating-systems/
  ```
* Ethcer
  ```sh
  > https://www.balena.io/etcher/
  ```
* Tensorflow Lite
  ```sh
  > pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
  ```
* OpenCV Dependencies
  ```sh
  > sudo apt-get update && sudo apt-get upgrade
  > sudo apt-get install build-essential cmake unzip pkg-config
  > sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
  > sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
  > sudo apt-get install libxvidcore-dev libx264-dev
  > sudo apt-get install libgtk-3-dev
  > sudo apt-get install libcanberra-gtk*
  > sudo apt-get install libatlas-base-dev gfortran
  > sudo apt-get install python3-dev
  ```
* OpenCV 4
  ```sh
  > cd ~
  > wget -O opencv.zip https://github.com/opencv/opencv/archive/4.3.0.zip
  > wget -O opencv_contrib.zip
  > https://github.com/opencv/opencv_contrib/archive/4.3.0.zip unzip opencv.zip
  > unzip opencv_contrib.zip
  > mv opencv-4.0.0 opencv
  > mv opencv_contrib-4.0.0 opencv_contrib
  ```
* Numpy
  ```sh
  > pip3 install numpy
  ```
* CMake and compile OpenCV 4
  ```sh
  > cd ~/opencv
  > mkdir build
  > cd build
  > cmake -D CMAKE_BUILD_TYPE=RELEASE \-D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF ..
  > make -j4
  > sudo make install
  > sudo ldconfig 

### Installation

1. Clone the repo
   ```sh
   > git clone git@github.com:meetdoshi90/Face-Mask-Detector.git
   ```
2. Install Requirements
   ```sh
   > cd rpi_based_mask_detector_new
   > pip3 install -r requirements.txt
   ```

## Built With

- Python
- Flask
- Tensorflow
- OpenCV
- HTML
- CSS
- JavaScript

## Live Demo

[Live Demo Link](https://www.youtube.com/watch?v=nb4apwK3eP4)

## Authors

👤 **Meet Doshi**

- GitHub: [@githubhandle](https://github.com/meetdoshi90)
- LinkedIn: [LinkedIn](https://linkedin.com/in/meetdoshi90)

👤 **Shravani Dhote**


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!

## 📝 License

This project is [MIT](./MIT.md) licensed.
