# Self Driving Car Trajectory Planning
This project plans a real-time trajectory of a self-driving car using onboard cameras.

## List of contents
- [Install Requirements](#install-requirements)
- [General Functions](#general-functions)
    - [Capture an Image](#capture-an-image)
    - [Car Acceleration](#car-acceleration)
    - [Release Control of Car](#release-control-of-car)
- [Software Information](#software-information)

## Install Requirements
```shell
sudo pip3 install requirements.txt
sudo apt-get install scrot
```

## General Functions

### Capture an Image
```python
selfdrive.capture(number_of_images, delay_between_captures)
```
If no parameters are specified, the function captures one image instantaneously.
**number_of_images**: Positive integer specifying the number of frames to be captured.
**delay_between_captures**: Positive integer value in seconds, specifying the delay between each frame capture.

### Car Acceleration
Start accelerating
```python
selfdrive.accelerate()
```
Stop accelerating
```python
selfdrive.stop_accelerate()
```

### Release Control of Car
Release all control from the car
```python
selfdrive.release_control()
```

## Software Information
Tested on  

Ubuntu 16.04 LTS  
Python 3.5.2  
PyAutoGUI 0.9.36