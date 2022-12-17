# Iconic-Gesture-Application
1. This is an Software application that detects the hand through webcam and perform actions like controlling ppt, video player, audio player 
2. This application is build in python 


# Requirements
1) **Web Camera** - This application uses a web camera to capture gestures by the user and then perform basic operations based on the input and execute the control over the media player and ppt. With OpenCV, we can capture a video from the camera. It lets you create a video capture object which is helpful to capture videos through a webcam and then you may perform desired operations on that video.
2) **Libraries** - To implement this code you need to install this required libraries (tutorial for install libraries are on internet)
  1. Cv2 (for video Capture)
  2. Numpy (for calculation)
  3. Shutil (different operations on files)
  4. cvzone.HandTracking module (For tracking hand and fingers)
  5. Subprocess (to run different files)
  6. Tkinter (GUI part)
  7. Time (for the delay)
  8. Pdf2image (converting pdf to an image)
  9. Win32com.client (converting ppt to pdf)
 10. Pyautogui (automatically control keyboard)
 11. os (For detecting/choosing the file)
 
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
 # NOTE :- 1. Only change the path of newpathofoutput variable before running in ppt_to_image.py
           2. Try to run code in VScode because to when it is running on pycharm somehow it gives error in Win32com.client library
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Implementation
Firstly welcome window will start then after clicking next button the camera detection part process will start and if camera is not detected then it will exit from the application and if camera is detected then choice window will open in that there are various choices are given such as ppt, video and audio.

1. If the user selects the ppt option then the sign convention or Instruction for ppt window will open. After clicking on next in Instruction of ppt the user should    select the ppt file and after that, the ppt presentation will start if a user wants to exit from the application then the user should press the ‘ESC’ button from the keyboard.

2. If the user selects the video option then the sign convention or Instruction for the video window will open. After clicking on next in the Instruction of video, the user should select the video file and after that default video player with a camera window for controlling the video player will start if the user wants to exit from the application then the user should press the ‘ESC’ button form the keyboard.

3. If the user selects the audio option then the sign convention or Instruction for the audio window will open. After clicking on next in Instruction of audio, the user should select the audio file and after that default, the audio player with a camera window for controlling the audio player will start if the user wants to exit from the application then the user should press the ‘ESC’ button from the keyboard.

Hope you like the application


