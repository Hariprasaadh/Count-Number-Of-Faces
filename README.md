**Face Detection with Dlib and OpenCV**

This repository contains a simple Python script for detecting faces in real-time using your webcam. The script utilizes the Dlib library for face detection and OpenCV for capturing video and displaying the results.

The core libraries used in the script are OpenCV, NumPy, and Dlib. The webcam is accessed using cv2.VideoCapture(0), and frames are converted to grayscale for face detection. The detected faces are drawn using cv2.rectangle, and the number of faces is displayed using cv2.putText. Finally, the webcam is released and all OpenCV windows are closed with cap.release() and cv2.destroyAllWindows().
