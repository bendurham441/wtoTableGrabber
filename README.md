# WTO Table Grabber
## Description
This script scrapes data from the WTO website by simulating browser interaction
using selenium. This data cannot be simply scraped using a typical web-scraping
package like BeautifulSoup because the relevant information is dynamically
generated and updated.

## Setup
Download the correct Chrome driver correlating with the version of Chrome you
are running from
[this site](https://sites.google.com/a/chromium.org/chromedriver/downloads).
Rename the driver file to chromedriver and place it in the directory with the
script. Then install selenium via `pip3 install selenium`. Run the script
as such: `python3 main.py`.
