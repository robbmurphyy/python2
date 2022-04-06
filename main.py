#Author: Robert Murphy
#Class: Python 307
#Assignment 6 webscraping
#date 4/7/22

from selenium import webdriver

#returns a new url that is acceptable by selenium
def create_url(site_to_visit):
    domain = "https://" + site_to_visit
    print("Opening: ", domain)
    return domain

#Asks the user for a site to visit
def ask_for_domain():
    site_to_visit = input("Enter a URL to visit in this format: www.<domain>.com\n")
    if "www." in site_to_visit and ".com" in site_to_visit: #check to see if www. and .com were entered
        new_url = create_url(site_to_visit)
        return new_url
    else:
        print("improper formatting of URL")
        return 1

#uses selenium to go to user's url
def visit_site(url):
    firefox = webdriver.Firefox()
    firefox.get(url)

if __name__ == "__main__":
    print("Requires geckodriver.exe to be in PATH")
    url = ask_for_domain()
    if url == 1:
        print("exiting")
    else:
        visit_site(url)
