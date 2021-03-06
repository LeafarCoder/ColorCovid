# ColorCovid
A colaboration between [Faculty of Pharmacy](https://www.ulisboa.pt/en/unidade-organica/faculty-pharmacy) and [IST](http://tecnico.ulisboa.pt/), both from the [University of Lisbon](https://www.ulisboa.pt/), for a Covid-related project.
The task was to, given a photo of an array of test samples for the Covid virus, determine which ones are the positive tests.

The idea was abandoned and the project did not continue.
This repository contains only the initial work for the project.

Project started in March 2020 (and abandoned shortly after).

<p align="center">
	<b>Overview of the project pipeline</b><br><br>
	<img align="center" src="/pre-processing/overview.png"/>
</p>
<br><br>

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

#### Summary

Objectives 1. to 4. where successfully accomplished.

There was never a response from the team in the lab with the dataset of samples and so the objectives 5. and 6. could not be implemented.


#### Detailed results

The objectives 1. and 2. were easily accomplished with the Python library [OpenCV](https://docs.opencv.org/master/index.html).

For the 3. objective, a couple of image processing techniques were used.

<details>
  <summary>Click to expand and see an example of the processing steps</summary>

Click on the images to see a zoomed version on a new page.

| | |
:----:|:------:
Original screenshot<br><img src="/pre-processing/image_processing_0_original.PNG" width="350"/> | **Step 1** First, detect the background <br> <img src="/pre-processing/image_processing_1_background_detection.PNG" width="350"/>
**Step 2** Use a high saturation threshold to broadly detect the wells<br> <img src="/pre-processing/image_processing_2_high_saturation_threshold.PNG" width="350"/> | **Step 3** Remove the background <br> <img src="/pre-processing/image_processing_3_background_removal.PNG" width="350"/>
**Step 4** Use an Euclidean distance mask <br> <img src="/pre-processing/image_processing_4_euclidean_distance.PNG" width="350"/> | **Step 5** Apply watershed and show markers <br> <img src="/pre-processing/image_processing_5_marker_by_watershedPNG.PNG" width="350"/>

</details>

With this pipeline, samples can be detected in a variety of array displays, well shapes and light conditions. Consider the following examples:

<details>
  <summary>Click to expand and see examples of detected samples</summary>

Click on the images to see a zoomed version on a new page.

| original screenshot | Samples detected |
:----:|:------:
<img src="/tests/tests1.PNG" width="350"/> | <img src="/tests/results1.PNG" width="350"/>
<img src="/tests/tests2.PNG" width="350"/> | <img src="/tests/results2.PNG" width="350"/>
<img src="/tests/tests3.PNG" width="350"/> | <img src="/tests/results3.PNG" width="350"/>
<img src="/tests/tests4.PNG" width="350"/> | <img src="/tests/results4.PNG" width="350"/>

</details>

For objective 4., all the samples were processed and the color features stored in a csv. file:

<p align="center">
	<img align="center" src="/samples_visualization/case2_CSV_file.PNG" width="450"/>
</p>

* A visualization tool allows to observe each individual sample and its color features.

<p align="center">
	<img align="center" src="/samples_visualization/case2_full_data.PNG" width="750"/>
</p>

* It also allows to choose a type of border to show

| Samples with border showing | Samples cropped to region of interest (ROI) |
:----:|:------:
<img align="center" src="/samples_visualization/case1_sorted_hue_value-broader_view_of_sample.PNG" width="375"/> | <img align="center" src="/samples_visualization/case1_sorted_by_hue.PNG" width="375"/>

 
* It also allows to order the list of samples by any given parameter

| **Order by RGB value**<br>(red channel, in this case) | **Order by test result**<br>(positive/negative) | **Order by sample index** |
:----:|:------:|:----:
<img align="center" src="/samples_visualization/case2_sorted_by_red_value.PNG" width="250"/> | <img align="center" src="/samples_visualization/case2_sorted_by_result.PNG" width="250"/> | <img align="center" src="/samples_visualization/case2_sorted_by_sample_index.PNG" width="250"/>

 
 ## Author
 
 Rafael Correia
 
* [LinkedIn](https://www.linkedin.com/in/joserafaelcorreia/)
* [Sourcerer](https://sourcerer.io/leafarcoder)
