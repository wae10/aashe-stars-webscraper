# STARS Webscraper
The Sustainability Tracking, Assessment & Rating System (STARS) is a transparent, self-reporting framework for colleges and universities to measure their sustainability performance. The purpose of this webscraper is to help a startup called Breeze Box LLC by compiling relevant information on hundreds of potential clients.

## Output
First 10/566 records shown below. Full output file [here](/data.csv).
|Institution                          |Location            |Rating            |Score|Valid Through |Liaison        |Submitted     |Sustainability Rep|Reusable Keyword?|Number of Past Reports|
|-------------------------------------|--------------------|------------------|-----|--------------|---------------|--------------|------------------|-----------------|----------------------|
|University of Alaska Anchorage       |Anchorage, AK, US   |Reporter - expired|     |Aug. 11, 2018 |Ryan Buchholdt |Aug. 12, 2015 |                  |FALSE            |0                     |
|University of Alaska Fairbanks       |Fairbanks, AK, US   |Gold - expired    |65.51|Aug. 25, 2014 |Michele Hebert |Aug. 26, 2011 |                  |FALSE            |0                     |
|University of Alaska Southeast       |Juneau, AK, US      |Bronze - expired  |31.31|Jan. 9, 2017  |Keith Gerken   |Jan. 10, 2014 |                  |FALSE            |0                     |
|Auburn University                    |Auburn, AL, US      |Silver            |64.13|31-Mar-25     |Michael Kensler|Feb. 4, 2022  |Glenn Loughridge  |TRUE             |4                     |
|University of Alabama at Birmingham  |Birmingham, AL, US  |Silver            |56.45|Feb. 6, 2023  |Bambi Ingram   |Feb. 7, 2020  |Julie Price       |TRUE             |2                     |
|University of Alabama in Huntsville  |Huntsville, AL, US  |Bronze - expired  |27.06|7-Mar-22      |Claire Jackson |8-Mar-19      |Taylor Myers      |TRUE             |0                     |
|University of Montevallo             |Montevallo, AL, US  |Bronze            |35.08|23-Jul-22     |Susan Caplow   |24-Jul-19     |Susan Caplow      |TRUE             |0                     |
|University of Arkansas               |Fayetteville, AR, US|Gold              |68.66|16-May-24     |Eric Boles     |5-Mar-21      |Kim Johnson       |TRUE             |5                     |
|University of Arkansas at Little Rock|Little Rock, AR, US |Bronze - expired  |35.82|Sept. 24, 2015|Jim Carr       |Sept. 24, 2012|                  |FALSE            |0                     |
|Arizona State University             |TEMPE, AZ, US       |Platinum          |87.1 |5-Mar-23      |Alex Davis     |5-Mar-20      |Alex Davis        |TRUE             |5                     |



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