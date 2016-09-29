import urllib
import re

SELO_BLOG_URL = 'https://selo77.github.io'

fp = urllib.urlopen(SELO_BLOG_URL)
html = fp.read()
