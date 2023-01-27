# Face-detector-and-blink-couner

The Face and Eye Detector and Eye Blink Counter is a powerful tool created using Python and OpenCV. This tool can detect faces and eyes within an image or video stream and track the number of times a person blinks their eyes.

Using Python and OpenCV, the tool first detects faces within an image or video stream using Haar cascades. Once a face is detected, the tool then uses a similar process to detect eyes within the face using Haar cascades. The tool then uses a combination of image processing techniques, such as edge detection and thresholding, to determine if the person's eyes are open or closed.

The Eye Blink Counter then keeps track of the number of times a person blinks their eyes, which can be useful in a variety of applications. For example, in a video conferencing app, this feature can be used to detect when a user is paying attention and alert them if they seem to be drifting off. In a security system, this feature can be used to detect when a person's eyes are closed for an extended period, which could indicate that they are sleeping or unconscious.

to run:
`python main.py`

![image](https://user-images.githubusercontent.com/36006908/215068903-fc9f11fd-9bc8-4a4e-985f-a0fd521f29a7.png)
