from google import google, images
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)


def setup_options():
    options = images.ImageOptions()
    options.size_category = "large"

    return options


def search(query="", options={}):
    results = google.search_images(query, options)
    print(results[1])


options = setup_options()
search(query="cats", options=options)
