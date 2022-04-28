# Import packages

# API Reference: https://pylablib.readthedocs.io/en/latest/.apidoc/pylablib.devices.M2.html
# Manual: http://ltj.otago.ac.nz:1300/quipfiles/attachments/2022/04/12/Solstis_3_TCP_JSON_protocol_V211.pdf
import pylablib.devices.M2
import csv
import datetime
import os

# --------------------------------------------------------------------------------
# Accessing the wavemeter WS7 
from pylablib.devices import HighFinesse
import pylablib.devices.HighFinesse.wlm

app_folder = "C:\Program Files (x86)\HighFinesse\Wavelength Meter WS7 883"

dll_path = os.path.join(app_folder, "Projects","64")
app_path = os.path.join(app_folder,"wlm_ws7.exe")
wavemeter = pylablib.devices.HighFinesse.wlm.WLM(7, dll_path = dll_path, app_path = app_path)
# --------------------------------------------------------------------------------
# Connect to laser
# IP address and Port determined by Remote Connection on Webpage
laser = pylablib.devices.M2.solstis.Solstis("192.168.1.222", 39901)
pump = pylablib.devices.M2.solstis.Solstis("192.168.1.225",49946)
#laser.connect_wavemeter()

# Wavemeter connection, run through the Start Link Command in the JSON manual 
#{
#    "ConnectionWavemeter":
#    {
#        "transmission_id":[001],
#        "op":"start_link",
#        {
#            "ip_address": "192.168.1.10.39933"
#        }
#}

# Attempt to get the system 

# Get the system status, useful for checking laser status?
print(laser.get_system_status())
print(laser.get_full_fine_tuning_status())
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
# Example of sweeping wavelengths GHz 870 - 900 nm

WAVELENGTH_LOWER = 344589
WAVELENGTH_UPPER = 333102
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
# Wavemeter making sure there is a connection
wavemeter.open()
wavemeter.is_opened()
# Frequency range 800nm to 950 nm in Hz
FREQUENCY_LOWER = 374700000000000
FREQUENCY_UPPER = 315571000000000
FREQUENCY_STEP = 200000000000
# Sweep
# Wavemeter Data Aquisition - with time of aquisition
wavemeter.start_measurement
laser.setup_terascan("line",(374700000000000,315571000000000),"200000000000")
laser.start_terascan
for frequency in range(FREQUENCY_LOWER, FREQUENCY_UPPER, FREQUENCY_STEP):
    print(f"{datetime.datetime.now()}: {wavemeter.get_frequency(error_on_invalid = False)})
    if frequency==FREQUENCY_UPPER 
    wavemeter.stop_measurement
