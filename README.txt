(A/C Professor Marcos):
" Before reading the documentation please read the NOTE.TXT file!

"


Hello everyone!

This is the OPENCV_CASCADE documentation. The following steps below, 
introduce the project structure and how to execute the software. 

Project structure:

-> OPENCV_CASCADE
--> handFiles
----> negatives
----> positives
----> training
--> peopleFiles
----> negatives
----> positives
----> training
--> truckFiles
----> negatives
----> positives
----> training
buildListNegative.py
exec.py
pictureDetector.py
renamefiles.py
videoDetector.py
README.TXT


#-- First steps:

Before running exec.py, you need to fill the folders with images to train the model. 
Folders named "negatives", you need to save images without the object you want to detect. 
For example, in the negatives folder, inside the handFiles folder, just include images when no hands are seen.
You do the opposite in positives files, just save images with the object you want to detect to train the model. 


#-- Download and configure OpenCV library:

The next step is to download the OpenCV library to train a machine learning model in order to use in this project.
Download OpenCV in https://opencv.org/, select the option releases and choose the version 3.4.12 (recommended for python version 3.6.1)  
After doing it, the download is about to start. When the download is finished, unzip the OpenCV folder downloaded and save in another directory.

To use the OpenCV functions, save the following path in environment variables: 
C:\Users\{your user}\{your folder}\opencv\build\x64\vc14\bin

Now you are able to use all OpenCV functions located inside the bin folder. 
This project use these following functions: opencv_annotation, opencv_createsamples and opencv_traincascade.


#-- Running side functions:

In this project, you'll find side functions named buildListNegative.py and renamefiles.py. 
buildListNegative.py needs to be run to create a text file with all the negative images. This file you use in the training algorithm process.
renamefiles.py is a side function that helps us to rename the all images in both negatives and positives folders. 


#-- Execute opencv_annotation:

Open the Command Prompt in your operation system and navigate to the pictures folders (handFiles for example). 
inside the selected folder, write down te instruction: opencv_annotation --annotations={your exit filename}.txt --images={the positives images folders}/

The next step is to indentify the object you want to detect to train the model. To do this, just follow these simple steps:
- Drawn a rectangle around the object. 
- Press C to confirm 
- Press N to go to the next image. 

The result are going to be saved in the exit filename with all the coordinates of all images.


#-- Execute opencv_createsamples:

inside the same selected folder, write down te instruction: 
opencv_createsamples -info {your exit filename}.txt -bg {your negatives filename}.txt -vec {your vector filename}.vec -w {width} -h {height}
EX: opencv_createsamples -info exit.txt -bg negatives.txt -vec vector.vec -w 24 -h 24


#-- Execute opencv_traincascade:

inside the same selected folder, write down te instruction: 
opencv_traincascade -data {your exit filename} -vec {your vector filename}.vec -bg {your negatives filename}.txt 
-numPos {number of positives images} -numNeg {number of negatives images} -w {width} -h {height} -precalcValBufSize 1024 -precalcIdxBufSize 1024 
-numStages {number of trainig stages} -acceptanceRatioBreakValue {value of acceptance of learning}
EX: opencv_traincascade -data training -vec vector.vec -bg negatives.txt -numPos 100 -numNeg 200 -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages 30 -acceptanceRatioBreakValue 1.0e-5


#-- Running the exec.py:

After doing all steps mentioned above, run the exec.py to execute the main program. 
There is a First menu when you select if you want to detect a hand, a truck or poeple in pictures. 
After that, another menu is shown to select whether you want to upload an image or use your camera.
Make sure to use the right training method for your picture!

Enjoy it and feel free to make all the changes you find important to improve this code!


