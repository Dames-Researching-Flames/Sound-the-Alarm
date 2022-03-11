
<div align="center">

<img width= "300" src="https://cdn.discordapp.com/attachments/392490318798389248/945695517004951633/jeanettes_fireart.png" alt="US Fires Logo">

# README

### by Lori Ainslie, Jeanette Schulz, Kristine Cabanela, and Sophia Stewart 

</div align="center">
    
<hr style="border:2px solid blue"> </hr>

## Project Goals

With over 2.16 million recorded wildfires and over 164 million acres burned, human intervention is needed to reduce the devastation and destruction caused by wildfires. Our overall goal is to see how US wildfires have changed over the years to promote active solutions to reduce the prevalence of wildfires.

## Project Description

A wildfire is an unplanned fire that burns in a natural area such as a forest, grassland, or prairie.  Wildfires typically spread quickly over woodland or brush and can lead to negative effects such as the deterioration of air quality, loss of property, crops, resources, animals and people.  In an effort to aid in the reduction of destruction and detriments of this phenomena, we've investigated key drivers of wildfires and hope to share our findings to encourage human intervention to alleviate the number of wildfires in the future. We acquired a database from a US Department of Agriculture publication of over two milliion wildfires that had occurred in the U.S. between 1992 and 2018. We transformed the data and conducted extensive exploratory analysis to identify the key drivers of wildfires.


## The Plan

**Plan - Acquire - Prepare - Explore - Deliver**

- Wrangle
    - Acquire data by downloading dataset from [U.S. DEPARTMENT OF AGRICULTURE](https://www.fs.usda.gov/rds/archive/Catalog/RDS-2013-0009.5) and saving CSV file locally.
    - Prepare data by dropping unneeded columns, converting columns to datetime, renaming columns for clarity.
    - Create a function that we can reference later to acquire and prepare the data by storing the function in a file named wrangle.py
- Explore
    - Create visualizations that pinpoint driving forces of wildfires and support findings of initial exploration questions
    - Apply statistical tests to support visual findings 
- Delivery
    - README with project details
    - Python modules with acquire and prepare functions
    - Final Report as a Jupyter Notebook
    - Presentation using Canva

 
## Initial Questions

- What locations are the most and least fire-prone? 
- Does fire size vary by location?
- Are wildfires becoming more prevalent over time?
- Does the number of wildfires vary by season?
- Are wildfires more destructive now than they were in the past? 
- What are the most common causes of wildfires? Is there anything that can be done to prevent that?
- Is it taking longer to contain and/or extinguish fires than it did in the past?


##  Steps to Reproduce
- Read this README
- Unzip fires.csv file  or
     - Create a fresh CSV using the 'Fires' table within the sqlite database found at: [U.S. DEPARTMENT OF AGRICULTURE](https://www.fs.usda.gov/rds/archive/Catalog/RDS-2013-0009.5)  
- Clone this repo (including the wrangle.py) 
- Ensure "*.csv" is included in gitignore to prevent issues with github
- Run Final_Report.ipynb


## Data Dictionary

| Variable          | Description                                                  |Data types|
| ----------------- | -----------------------------------------------------------  |----------|
| fire_year         | Calendar year in which the fire was discovered or confirmed to exist. |   int64        |
| discovery_date    | Date on which the fire was discovered or confirmed to exist. |   datetime64           |
| general_cause     | Description of the (statistical) cause of the fire.          |   object         |
| containment_date  | Date on which the fire was declared contained or otherwise controlled. | datetime64         |
| fire_size         | Estimate of acres within the final perimeter of the fire.    |   float64         |
| latitude          | Latitude (NAD83) for point location of the fire (decimal degrees). |  float64         |
| longitude         | Longitude (NAD83) for point location of the fire (decimal degrees). | float64         |
| state             | The state in which the fire burned (or originated), based on the nominal designation in the fire report. |   object         |
| state_size        | The state size in acres |   float64         |
| year             | Calendar year in which the fire was discovered or confirmed to exist. |   object         |
| region            | The region in which the fire burned (or originated), based on the nominal designation in the fire report. |   object         |
| region_size      | The region size in acres |   float64         |
| fire_size_cat    | The fire size category ('large': 5,000 acres or larger (NWCG Class G), 'small': less than 5,000 acres) |  object         |

                
## Exploration Findings
- The months of July, March, and April have the largest number of wildfires that occur.
- The number of wildfires from 1992 - 2018 shows a slight upward trend but the area burned by those wildfires shows a significant upward trend.
- Large wildfires are increasing more so than small wildfires and are a major component of global warming.
- The number one cause for overall number of wildfires is from human activity while the number one cause for large wildfires is from natural causes
- California, Georgia, and Texas are the top three states for number of wildfires while Alaska, California, and Idaho are the top three for total area burned by wildfires.
- The largest fire in the dataset, named the Starbuck fire, occurred in 2017 in the state of Oklahoma and was 55,755 acres more than the previously recorded largest fire that occurred in Arkansas in 1997.


# Conclusion

## Key Takeaways:
-  The number of wildfires has stayed pretty steady over the years but the amount of destruction caused by wildfires has increased and is continuing on an upward trend.
- The western region of the U.S. has the most destruction from wildfires and the southeastern region has the largest number of wildfires.
- Most wildfires are caused by humans through debris and open burning and are preventable.


## Recommendations:
Considering human involvement is the number one cause for wildfires in the US, possible recommendations include:
- Awareness: Spreading education on safe open burning practices with pamphlets/brouchures
- Action: Implementing safe open burning procedures or limit open burning
    - Reduction in trash/waste by recycling
    - Extinguishing campfires, BBQ pits/grills, fireplaces
    - Don't leave fires unattended
    - Open burn during months less prone to wildfires

## Next Steps:
- Analyze and include additional data that includes weather reports on precipitation levels, dryness, wind.
