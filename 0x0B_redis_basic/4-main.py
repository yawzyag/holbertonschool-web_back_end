#!/usr/bin/env python3
""" Main file """

get_page = __import__('web').get_page

for i in range(10):
    page = get_page("http://slowwly.robertomurray.co.uk")
    # print(page)
