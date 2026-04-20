# ColorCovid

A collaboration between [Faculty of Pharmacy](https://www.ulisboa.pt/en/unidade-organica/faculty-pharmacy) and [IST](http://tecnico.ulisboa.pt/), both from the [University of Lisbon](https://www.ulisboa.pt/).

Given a photograph of an array of COVID-19 test samples, ColorCovid automatically detects each sample well, extracts its color characteristics, and classifies which tests are positive.

<p align="center">
  <img src="pre-processing/overview.png" width="700"/>
</p>

## Features

- **Camera control** — connect any camera to the computer and capture snapshots directly from the GUI
- **Sample detection** — automatically locates and uniquely indexes each well in the plate, handling variable array layouts, well shapes, and lighting conditions
- **Color feature extraction** — computes HSV and RGB channel averages per sample and exports them to CSV
- **Classification** — classifies each sample as positive or negative based on its color features

## Requirements

```bash
pip install opencv-python numpy matplotlib scikit-image scipy pillow imutils easygui
```

## How It Works

The image processing pipeline detects and segments individual wells through five stages:

<details open>
  <summary><b>Processing steps</b></summary>
<br>

| | |
:----:|:------:
Original image<br><img src="pre-processing/image_processing_0_original.PNG" width="350"/> | **Step 1** Detect the background<br><img src="pre-processing/image_processing_1_background_detection.PNG" width="350"/>
**Step 2** High-saturation threshold to broadly locate the wells<br><img src="pre-processing/image_processing_2_high_saturation_threshold.PNG" width="350"/> | **Step 3** Remove the background<br><img src="pre-processing/image_processing_3_background_removal.PNG" width="350"/>
**Step 4** Euclidean distance mask<br><img src="pre-processing/image_processing_4_euclidean_distance.PNG" width="350"/> | **Step 5** Watershed algorithm — final sample markers<br><img src="pre-processing/image_processing_5_marker_by_watershedPNG.PNG" width="350"/>

</details>

Detection works across a range of plate formats and lighting conditions:

<details>
  <summary><b>Detection examples</b></summary>
<br>

| Original | Detected samples |
:----:|:------:
<img src="tests/tests1.PNG" width="350"/> | <img src="tests/results1.PNG" width="350"/>
<img src="tests/tests2.PNG" width="350"/> | <img src="tests/results2.PNG" width="350"/>
<img src="tests/tests3.PNG" width="350"/> | <img src="tests/results3.PNG" width="350"/>
<img src="tests/tests4.PNG" width="350"/> | <img src="tests/results4.PNG" width="350"/>

</details>

## Color Analysis

Each detected sample is uniquely indexed on the plate:

<p align="center">
  <img src="samples_visualization/case2_markers.PNG" width="580"/>
</p>

Color features (H, S, V, R, G, B averages) for all samples are exported to a CSV file:

<p align="center">
  <img src="samples_visualization/case2_CSV_file.PNG" width="450"/>
</p>

A built-in visualization tool lets you inspect each sample individually and browse all color data at a glance:

<p align="center">
  <img src="samples_visualization/case2_full_data.PNG" width="750"/>
</p>

Samples can be shown with their surrounding border or cropped tightly to the region of interest:

| With border | Cropped to ROI |
:----:|:------:
<img src="samples_visualization/case1_sorted_hue_value-broader_view_of_sample.PNG" width="375"/> | <img src="samples_visualization/case1_sorted_by_hue.PNG" width="375"/>

The list can be sorted by any parameter — color channel, test result, or sample index:

| By RGB value (red channel) | By test result | By sample index |
:----:|:------:|:----:
<img src="samples_visualization/case2_sorted_by_red_value.PNG" width="250"/> | <img src="samples_visualization/case2_sorted_by_result.PNG" width="250"/> | <img src="samples_visualization/case2_sorted_by_sample_index.PNG" width="250"/>

## Author

Rafael Correia — [LinkedIn](https://www.linkedin.com/in/joserafaelcorreia/)
