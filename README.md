# STARS Webscraper
The Sustainability Tracking, Assessment & Rating System (STARS) is a transparent, self-reporting framework for colleges and universities to measure their sustainability performance. The purpose of this webscraper is to help a startup called Breeze Box LLC by compiling relevant information on hundreds of potential clients.

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