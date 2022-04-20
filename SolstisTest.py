# Import packages

# API Reference: https://pylablib.readthedocs.io/en/latest/.apidoc/pylablib.devices.M2.html
# Manual: http://ltj.otago.ac.nz:1300/quipfiles/attachments/2022/04/12/Solstis_3_TCP_JSON_protocol_V211.pdf
import pylablib.devices.M2
import csv
import datetime

# --------------------------------------------------------------------------------
# Connect to laser
# IP address and Port determined by Remote Connection on Webpage
laser = pylablib.devices.M2.solstis.Solstis("192.168.1.222", 39901)
# laser.connnect_wavemeter()

# Get the system status, useful for checking laser status?
print(laser.get_system_status())

# --------------------------------------------------------------------------------
# Set up and start writing to a data file

data_file = "DataFile_1.csv"
# Set the headers of the csv columns
headers = ["wavelength", "measurement"]

# Open the file and write the headers
file=open(data_file,"w",newline='',encoding='utf-8')
writer = csv.writer(file)
writer.writerow(headers)

# --------------------------------------------------------------------------------
# Example of sweeping wavelengths

WAVELENGTH_LOWER = 0
WAVELENGTH_UPPER = 1000
WAVELENGTH_STEP = 1

# For loop performs the sweep
for wavelength in range(WAVELENGTH_LOWER, WAVELENGTH_UPPER, WAVELENGTH_STEP):
    # Print the time stamp and wavelength - for logging if needed
    print(f"{datetime.datetime.now()}: {wavelength}")

    # Do a "measurement", this is the hard part later!
    measurement = wavelength**2

    # Write the row
    writer.writerow([wavelength, measurement])
    # Simulate an error occuring during the experiment
    if wavelength==400:
        raise ValueError()

# --------------------------------------------------------------------------------