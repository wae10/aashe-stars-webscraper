# STARS Webscraper
The Sustainability Tracking, Assessment & Rating System (STARS) is a transparent, self-reporting framework for colleges and universities to measure their sustainability performance. The purpose of this webscraper is to help a startup called Breeze Box LLC by compiling relevant information on hundreds of potential clients.

## Sample Output
First 20/566 records.
|Institution| Location| Rating| Score| Valid Through| Liaison| Submitted| Sustainability Rep| Reusable Keyword?| Number of Past Reports| Dates of Past Reports|
|---|---|---|---|---|---|---|---|---|---|---|
|University of Alaska Anchorage|"Anchorage| AK| US"|Reporter - expired||"Aug. 11| 2018"|Ryan Buchholdt|"Aug. 12| 2015"||False|0||
|University of Alaska Fairbanks|"Fairbanks| AK| US"|Gold - expired|65.51|"Aug. 25| 2014"|Michele Hebert|"Aug. 26| 2011"||False|0||
|University of Alaska Southeast|"Juneau| AK| US"|Bronze - expired|31.31|"Jan. 9| 2017"|Keith Gerken|"Jan. 10| 2014"||False|0||
|Auburn University|"Auburn| AL| US"|Silver|64.13|"March 31| 2025"|Michael Kensler|"Feb. 4| 2022"|Glenn Loughridge|True|4|"Feb. 4| 2022 - March 31| 2025| Jan. 23| 2019 - Jan. 22| 2022| Jan. 11| 2016 - Jan. 10| 2019| Jan. 15| 2013 - Jan. 15| 2016"|
|University of Alabama at Birmingham|"Birmingham| AL| US"|Silver|56.45|"Feb. 6| 2023"|Bambi Ingram|"Feb. 7| 2020"|Julie Price|True|2|"Feb. 7| 2020 - Feb. 6| 2023| July 29| 2016 - July 29| 2019"|
|University of Alabama in Huntsville|"Huntsville| AL| US"|Bronze - expired|27.06|"March 7| 2022"|Claire Jackson|"March 8| 2019"|Taylor Myers|True|0||
|University of Montevallo|"Montevallo| AL| US"|Bronze|35.08|"July 23| 2022"|Susan Caplow|"July 24| 2019"|Susan Caplow|True|0||
|University of Arkansas|"Fayetteville| AR| US"|Gold|68.66|"May 16| 2024"|Eric Boles|"March 5| 2021"|Kim Johnson|True|5|"March 5| 2021 - May 16| 2024| March 8| 2017 - Sept. 3| 2020| Feb. 12| 2015 - Feb. 11| 2018| Feb. 14| 2014 - Feb. 13| 2017| Feb. 15| 2011 - Feb. 14| 2014"|
|University of Arkansas at Little Rock|"Little Rock| AR| US"|Bronze - expired|35.82|"Sept. 24| 2015"|Jim Carr|"Sept. 24| 2012"||False|0||
|Arizona State University|"TEMPE| AZ| US"|Platinum|87.10|"March 5| 2023"|Alex Davis|"March 5| 2020"|Alex Davis|True|5|"March 5| 2020 - March 5| 2023| March 1| 2018 - Aug. 27| 2021| Feb. 27| 2017 - Feb. 27| 2020| Feb. 28| 2014 - Feb. 27| 2017| July 29| 2011 - July 28| 2014"|
|Chandler-Gilbert Community College|"Chandler| AZ| US"|Bronze - expired|37.67|"Feb. 28| 2022"|Trina Larson|"March 1| 2019"||False|0||
|Estrella Mountain Community College|"Avondale| AZ| US"|Bronze - expired|35.30|"Feb. 9| 2017"|Nadine Johnson|"Feb. 10| 2014"||False|2|"Feb. 10| 2014 - Feb. 9| 2017| Jan. 18| 2011 - Jan. 17| 2014"|
|Northern Arizona University|"Flagstaff| AZ| US"|Gold|66.48|"Jan. 5| 2024"|Abraham (Avi) Henn|"Sept. 28| 2020"|Gabriela Galvan|True|5|"Sept. 28| 2020 - Jan. 5| 2024| March 3| 2017 - Aug. 29| 2020| May 1| 2014 - April 30| 2017| Oct. 8| 2012 - Oct. 8| 2015| Aug. 2| 2011 - Aug. 1| 2014"|
|Prescott College|"Prescott| AZ| US"|Silver|48.02|"March 27| 2025"|Zachary Czuprynski|"Feb. 4| 2022"|Zachary Czuprynski|True|0||
|Rio Salado College|"Tempe| AZ| US"|Silver - expired|53.98|"Aug. 11| 2014"|Alan Torvie|"Aug. 12| 2011"||False|0||
|University of Arizona|"Tucson| AZ| US"|Gold - expired|66.35|"Oct. 28| 2020"|Trevor Ledbetter|"May 2| 2017"|Benjamin Champion|True|2|"May 2| 2017 - Oct. 28| 2020| Feb. 10| 2012 - Feb. 9| 2015"|
|Cal Poly Humboldt|"Arcata| CA| US"|Gold|72.07|"May 7| 2023"|Katie Koscielak|"May 7| 2020"|Ron Rudebock|True|3|"May 7| 2020 - May 7| 2023| April 21| 2017 - Oct. 17| 2020| May 8| 2013 - May 7| 2016"|
|California College of the Arts|"Oakland| CA| US"|Reporter - expired||"Aug. 28| 2021"|Dasha Ostrova|"March 2| 2018"|Jennifer Juras|False|1|" - Aug. 28| 2021"|
|California Polytechnic State University|"San Luis Obispo| CA| US"|Gold|70.16|"Sept. 18| 2022"|Kylee Singh|"Sept. 19| 2019"|Kaitlin Gibbons|True|2|"Sept. 19| 2019 - Sept. 18| 2022| Feb. 16| 2017 - Feb. 16| 2020"|
|"California State Polytechnic University| Pomona"|"Pomona| CA| US"|Silver|58.15|"May 15| 2023"|Monika Kamboures|"May 15| 2020"|Monika Kamboures|True|4|"May 15| 2020 - May 15| 2023| May 30| 2017 - Nov. 25| 2020| April 10| 2014 - April 9| 2017| May 4| 2011 - May 3| 2014"|


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