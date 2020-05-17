"""
Urllib - GET Requests || Python Tutorial || Learn Python Programming
ref: https://www.youtube.com/watch?v=LosIGgon_KM&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=33
"""

# Package: urllib
# 5 modules
# request: open URLs
# response: (used internally by request module)
# error: contains several error classes for use by request module
# parse: has a variety of functions to break url into meaningful pieces
# robotparser: robots.txt files

# # Example 1: request
# from urllib import request
#
# resp = request.urlopen("https://www.wikipedia.org") # this function returns a "response" object
#
# print("Print all the objects (directory) of 'response'\n", dir(resp), "\n")
# print("Print the HTTP status code of 'response'\n", resp.code, "\n")
# # HTTP status codes:
# # 200: okay
# # 400: Bad Request
# # 403: Forbidden
# # 404: Not Found
#
# print("Print the length of 'response'\n", resp.length, "\n") # the size of the response in Bytes
# print("Take a quick peek of the 'response'\n", resp.peek, "\n")
#
# data = resp.read()
# print("Print the type of 'data'\n", type(data), "\n") # it is <class 'bytes'>
# print("Print the length of 'data'\n", len(data), "\n") # 76776
#
# html = data.decode("UTF-8")
# print("Print the type of 'data'\n", type(html), "\n")
# print("Display the whole 'html' used for the webpage: \n", html, "\n")



# Example 2: parse
from urllib import parse
from urllib import request
# Example youtube video to parse:
# https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s

params = {"v": "EuC-yVzHhMI",
          "t": "5m56s"}

querystring = parse.urlencode(params)

url = "https://www.youtube.com/watch" + "?" + querystring
resp = request.urlopen(url)

