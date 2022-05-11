#Author: Robert Murphy
#Class: Python 307
#Assignment 8 geolocation
#date 5/10/22


import pygeoip
import ipaddress

#checks to see if an IP follows correct IP syntax standard
def ip_check(ip):
    try:
        ipaddress.ip_address(ip)
        return 0
    except ValueError as ve:
        print("Your IP is not a valid IP address")

#finds geolocation information about an IP address
def ip_geo_finder(ip):
    try:
        gi = pygeoip.GeoIP('GeoLiteCity.dat')
        print(gi.country_name_by_addr(ip))
        records = gi.record_by_addr(ip)
        print("City: ", records['city'])
        print("Postal code: ", records['postal_code'])

        #the commented below code would work if the ORG and ISP Geolite databases were not depricated
        #depricated Org database link
        #https://github.com/maxmind/geoip-api-php/blob/main/tests/data/GeoIPOrg.dat
        # orgdat = pygeoip.GeoIP('GeoIPOrg.dat')
        # org = orgdat.org_by_addr(ip)
        # print(org)

        #Depricated ISP database link
        # https://github.com/maxmind/geoip-api-php/blob/main/tests/data/GeoIPISP.dat
        #print("Organization name: ", org['organization'])
        # ISPdat = pygeoip.GeoIP('GeoIPISP.dat')
        # print(ISPdat)
    except pygeoip.GeoIPError as ge:
        print("unrecoverable GeoIP error. Exiting.")

if __name__ == '__main__':
    print("You must have the GeoLiteCity.dat file in this current directory for this program to work.\nVisit this site to download it")
    print("https://github.com/mbcc2006/GeoLiteCity-data/blob/master/GeoLiteCity.dat")
    ip = input("Please enter an IP: ")
    check = ip_check(ip)
    if check == 0:
        ip_geo_finder(ip)
    else:
        print("IP didn't work")
