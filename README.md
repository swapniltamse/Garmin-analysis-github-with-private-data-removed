This is a quick and dirty visualization of my heart rate abnormalities during my last week's sick week.

Garmin's daily breakdowns become unclear when viewed in the weekly format, making it difficult to analyze trends effectively. Additionally, the platform does not support exporting heart rate data directly from the website.

This repository contains code for analyzing Garmin fitness data, specifically designed to process and extract insights from activity files. 
The project involves importing Garmin activity data, processing it, and generating valuable statistics and visualizations.

Using the Garmin API, this code will help us retrieve heart rate and other data. I have configured it for 7 days with 12-hour intervals. Please adjust it as necessary.

Garmin's screen:
![Garmin portal graph](https://github.com/user-attachments/assets/d1d89e99-ecfd-4091-b131-b390e952a12a)


Our chart:
![Garmin heart rate data](https://github.com/user-attachments/assets/98f32de6-485a-4c51-8542-b75efaa433a2)


## Features
- Import Garmin activity for daily historic heart rate data
- Data cleaning and preprocessing
- Analysis of key fitness metrics using granualar heart rate which is hard to do using most visualization tools
- Privacy considerations: All private data has been removed from this repository
- Split the code into 3 separate sections to use whichever part needed at different stages

## Requirements
- Python 3.x

### Required Python packages:
- pandas
- numpy
- matplotlib
- gpxpy

