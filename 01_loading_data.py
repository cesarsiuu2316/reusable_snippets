import pandas as pd
from pathlib import Path
import urllib.request

datapath = Path() / "datasets" / "lifesat"
datapath.mkdir(parents=True, exist_ok=True)
data_root = "https://github.com/ageron/data/raw/main/"

def loading_from_request(datapath, data_root):
    for filename in ("oecd_bli.csv", "gdp_per_capita.csv"):
        # if the file is not already downloaded, download it
        if not (datapath / filename).is_file():
            print("Downloading", filename)
            url = data_root + "lifesat/" + filename
            urllib.request.urlretrieve(url, datapath / filename)

    oecd_bli = pd.read_csv(datapath / "oecd_bli.csv") # ECD better life index
    gdp_per_capita = pd.read_csv(datapath / "gdp_per_capita.csv") # GDP per capita in US dollars
    return oecd_bli, gdp_per_capita


