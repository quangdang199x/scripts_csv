# Update database from csv - Single day

## Procedure
1.	Determine the lost date or time period 
2.	Download inverter csv file from webportal
3.	Calculate active energy of inverters at a single datapoints at every 15 minutes 
4.  Create new csv file with new data points for all inverters 
4.	Validate the site's summary active energy for the whole day 
5.	Import the new *.csv file to Solarmon database

# Requirements
## Input
-  Inverters' single day csv file from ABB/SMA webportal (15mins resolution)
-  Active energy value: 
    + lower bound: last Active energy
    + upper bound: last Active energy + day's active energy

## Output
- Active energy at every point in the day for every inverter
- Combined CSV file to import to Solarmon database

## Validation
- Site's summary active energy vs summary of all inverters' active energy in a single day