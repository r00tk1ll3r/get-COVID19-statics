#!/usr/bin/python3

import requests
import sys

banner_text = """

 ██████╗ ██████╗ ██╗   ██╗██╗██████╗        ██╗ █████╗     ██╗     ██╗██╗   ██╗███████╗    ███████╗████████╗ █████╗ ████████╗██╗ ██████╗███████╗
██╔════╝██╔═══██╗██║   ██║██║██╔══██╗      ███║██╔══██╗    ██║     ██║██║   ██║██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔════╝██╔════╝
██║     ██║   ██║██║   ██║██║██║  ██║█████╗╚██║╚██████║    ██║     ██║██║   ██║█████╗      ███████╗   ██║   ███████║   ██║   ██║██║     ███████╗
██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║╚════╝ ██║ ╚═══██║    ██║     ██║╚██╗ ██╔╝██╔══╝      ╚════██║   ██║   ██╔══██║   ██║   ██║██║     ╚════██║
╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝       ██║ █████╔╝    ███████╗██║ ╚████╔╝ ███████╗    ███████║   ██║   ██║  ██║   ██║   ██║╚██████╗███████║
 ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝        ╚═╝ ╚════╝     ╚══════╝╚═╝  ╚═══╝  ╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝╚══════╝                                                                                                                                                

 Script Written By r00tk1ll3r
"""
print(banner_text)

statistics = requests.get(
    "https://hpb.health.gov.lk/api/get-current-statistical"
).json()

update_date_time = statistics["data"]["update_date_time"]
local_new_cases = statistics["data"]["local_new_cases"]
local_total_cases = statistics["data"]["local_total_cases"]
local_total_number_of_individuals_in_hospitals = statistics["data"][
    "local_total_number_of_individuals_in_hospitals"
]
local_deaths = statistics["data"]["local_deaths"]
local_new_deaths = statistics["data"]["local_new_deaths"]
local_recovered = statistics["data"]["local_recovered"]
local_active_cases = statistics["data"]["local_active_cases"]
global_new_cases = statistics["data"]["global_new_cases"]
global_total_cases = statistics["data"]["global_total_cases"]
global_deaths = statistics["data"]["global_deaths"]
global_new_deaths = statistics["data"]["global_new_deaths"]
global_recovered = statistics["data"]["global_recovered"]
total_pcr_testing_count = statistics["data"]["total_pcr_testing_count"]

print("Local deaths             : " + str(local_deaths))
print("Local new deaths         : " + str(local_new_deaths))
print("Local recovered          : " + str(local_recovered))
print("Local active cases       : " + str(local_active_cases))
print("Global new cases         : " + str(global_new_cases))
print("Global total cases       : " + str(global_total_cases))
print("Global deaths            : " + str(global_deaths))
print("Global new deaths        : " + str(global_new_deaths))
print("Global recovered         : " + str(global_recovered))
print("Total pcr testing count  : " + str(total_pcr_testing_count))
