import math
from os import rename
import sys

import requests


r = requests.get("https://coreyms.com")
print(r.status_code)
