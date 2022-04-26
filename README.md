# STARS Webscraper
The Sustainability Tracking, Assessment & Rating System (STARS) is a transparent, self-reporting framework for colleges and universities to measure their sustainability performance. The purpose of this webscraper is to help a startup called Breeze Box LLC by compiling relevant information on hundreds of potential clients.

## Sample Output
First 20/566 records.
|Institution                                    |Location               |Rating            |Score|Valid Through |Liaison           |Submitted     |Sustainability Rep|Reusable Keyword?|Number of Past Reports|
|-----------------------------------------------|-----------------------|------------------|-----|--------------|------------------|--------------|------------------|-----------------|----------------------|
|University of Alaska Anchorage                 |Anchorage, AK, US      |Reporter - expired|     |Aug. 11, 2018 |Ryan Buchholdt    |Aug. 12, 2015 |                  |FALSE            |0                     |
|University of Alaska Fairbanks                 |Fairbanks, AK, US      |Gold - expired    |65.51|Aug. 25, 2014 |Michele Hebert    |Aug. 26, 2011 |                  |FALSE            |0                     |
|University of Alaska Southeast                 |Juneau, AK, US         |Bronze - expired  |31.31|Jan. 9, 2017  |Keith Gerken      |Jan. 10, 2014 |                  |FALSE            |0                     |
|Auburn University                              |Auburn, AL, US         |Silver            |64.13|31-Mar-25     |Michael Kensler   |Feb. 4, 2022  |Glenn Loughridge  |TRUE             |4                     |
|University of Alabama at Birmingham            |Birmingham, AL, US     |Silver            |56.45|Feb. 6, 2023  |Bambi Ingram      |Feb. 7, 2020  |Julie Price       |TRUE             |2                     |
|University of Alabama in Huntsville            |Huntsville, AL, US     |Bronze - expired  |27.06|7-Mar-22      |Claire Jackson    |8-Mar-19      |Taylor Myers      |TRUE             |0                     |
|University of Montevallo                       |Montevallo, AL, US     |Bronze            |35.08|23-Jul-22     |Susan Caplow      |24-Jul-19     |Susan Caplow      |TRUE             |0                     |
|University of Arkansas                         |Fayetteville, AR, US   |Gold              |68.66|16-May-24     |Eric Boles        |5-Mar-21      |Kim Johnson       |TRUE             |5                     |
|University of Arkansas at Little Rock          |Little Rock, AR, US    |Bronze - expired  |35.82|Sept. 24, 2015|Jim Carr          |Sept. 24, 2012|                  |FALSE            |0                     |
|Arizona State University                       |TEMPE, AZ, US          |Platinum          |87.1 |5-Mar-23      |Alex Davis        |5-Mar-20      |Alex Davis        |TRUE             |5                     |
|Chandler-Gilbert Community College             |Chandler, AZ, US       |Bronze - expired  |37.67|Feb. 28, 2022 |Trina Larson      |1-Mar-19      |                  |FALSE            |0                     |
|Estrella Mountain Community College            |Avondale, AZ, US       |Bronze - expired  |35.3 |Feb. 9, 2017  |Nadine Johnson    |Feb. 10, 2014 |                  |FALSE            |2                     |
|Northern Arizona University                    |Flagstaff, AZ, US      |Gold              |66.48|Jan. 5, 2024  |Abraham (Avi) Henn|Sept. 28, 2020|Gabriela Galvan   |TRUE             |5                     |
|Prescott College                               |Prescott, AZ, US       |Silver            |48.02|27-Mar-25     |Zachary Czuprynski|Feb. 4, 2022  |Zachary Czuprynski|TRUE             |0                     |
|Rio Salado College                             |Tempe, AZ, US          |Silver - expired  |53.98|Aug. 11, 2014 |Alan Torvie       |Aug. 12, 2011 |                  |FALSE            |0                     |
|University of Arizona                          |Tucson, AZ, US         |Gold - expired    |66.35|Oct. 28, 2020 |Trevor Ledbetter  |2-May-17      |Benjamin Champion |TRUE             |2                     |
|Cal Poly Humboldt                              |Arcata, CA, US         |Gold              |72.07|7-May-23      |Katie Koscielak   |7-May-20      |Ron Rudebock      |TRUE             |3                     |
|California College of the Arts                 |Oakland, CA, US        |Reporter - expired|     |Aug. 28, 2021 |Dasha Ostrova     |2-Mar-18      |Jennifer Juras    |FALSE            |1                     |
|California Polytechnic State University        |San Luis Obispo, CA, US|Gold              |70.16|Sept. 18, 2022|Kylee Singh       |Sept. 19, 2019|Kaitlin Gibbons   |TRUE             |2                     |
|California State Polytechnic University, Pomona|Pomona, CA, US         |Silver            |58.15|15-May-23     |Monika Kamboures  |15-May-20     |Monika Kamboures  |TRUE             |4                     |



## Setup Instructions
### Virtual Environment
Create a virtual environment to store packages. Example:
```
conda create -n 'ENV-NAME'
conda activate 'ENV-NAME'
```
### Packages
Install packages in virtual environment with pip.
```
pip install -r requirements.txt
```
### Environment Variables
Create .env file to store csv output file path and chromedriver file path
### Execution
Run the script to produce the output csv file.
```
python main.py
```