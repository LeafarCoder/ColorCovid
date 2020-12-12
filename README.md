# ColorCovid
A colaboration with the Faculty of Pharmacy from the University of Lisbon for a Covid-related project.
The task was: given a photo of an array of test samples for the Covid virus, determine which ones are the positive tests.

The idea was abandoned and the project did not continue.
This repository contains only the initial work for the project.

Project started in March 2020 (and abandoned shortly after).

## Requirements

Install [OpenCV](https://docs.opencv.org/master/index.html) library to access the camera and take photos of the samples:
```
pip install opencv-python
```

## Objectives

1. Allow the control of any camera connected to the computer.
2. Store snapshots of the samples in a light-controled environment.
3. Identify the portions of the image with the samples (and index each samples uniquely).
4. Extract the color characteristics of each sample.
5. Train a classifier based on a large dataset (classify outcome of the test based on color features).
6. Test on new data and assess performance.

## Results

Steps 1. to 4. where successfully accomplished.
There was never a response from the team in the lab with the dataset of samples and so steps 5. and 6. could not be implemented.

Steps 1. and 2. were easily accomplished with the Python library [OpenCV](https://docs.opencv.org/master/index.html).

For step 3., a couple of image processing techniques were used (click on the images to show zoomed version):

| | |
:----:|:------:
**0** Original screenshot<br><img src="/pre-processing/image_processing_0_original.PNG" width="350"/> | **1** First, detect the background <br> <img src="/pre-processing/image_processing_1_background_detection.PNG" width="350"/>
**2** Use a high saturation threshold to broadly detect the wells<br> <img src="/pre-processing/image_processing_2_high_saturation_threshold.PNG" width="350"/> | **3** Remove the background <br> <img src="/pre-processing/image_processing_3_background_removal.PNG" width="350"/>
**4** Use an Euclidean distance mask <br> <img src="/pre-processing/image_processing_4_euclidean_distance.PNG" width="350"/> | **5** Apply watershed and show markers <br> <img src="/pre-processing/image_processing_5_marker_by_watershedPNG.PNG" width="350"/>

With this, samples can be detected in a variety of array displays, well shapes and light conditions. Consider the following examples:

| original screenshot | Samples detected |
:----:|:------:
<img src="/tests/tests1.PNG" width="350"/> | <img src="/tests/results1.PNG" width="350"/>
<img src="/tests/tests2.PNG" width="350"/> | <img src="/tests/results2.PNG" width="350"/>
<img src="/tests/tests2.PNG" width="350"/> | <img src="/tests/results3.PNG" width="350"/>
<img src="/tests/tests3.PNG" width="350"/> | <img src="/tests/results4.PNG" width="350"/>


For step 4., all the samples were processed and the color features stored.
A visualization tool allowed to observe each individual sample, its color features and even order the samples by any given characteristic.




