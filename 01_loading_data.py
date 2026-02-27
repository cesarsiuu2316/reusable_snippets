import pandas as pd
from pathlib import Path
import urllib.request
import tarfile

# csv paths
datapath = Path() / "datasets" / "lifesat"
datapath.mkdir(parents=True, exist_ok=True)
csv_url = "https://github.com/ageron/data/raw/main/"

# tar paths
tarball_path = Path("datasets/housing.tgz")
Path("datasets").mkdir(parents=True, exist_ok=True)
tar_url = "https://github.com/ageron/data/raw/main/housing.tgz"


def loading_csv_from_request(datapath, csv_url):
    for filename in ("oecd_bli.csv", "gdp_per_capita.csv"):
        # if the file is not already downloaded, download it
        if not (datapath / filename).is_file():
            print("Downloading", filename)
            url = csv_url + "lifesat/" + filename
            urllib.request.urlretrieve(url, datapath / filename)

    oecd_bli = pd.read_csv(datapath / "oecd_bli.csv") # ECD better life index
    gdp_per_capita = pd.read_csv(datapath / "gdp_per_capita.csv") # GDP per capita in US dollars
    return oecd_bli, gdp_per_capita


def loading_tar_from_request(tarball_path, tar_url):
    if not tarball_path.is_file():
        urllib.request.urlretrieve(tar_url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets", filter="data")
    return pd.read_csv(Path("datasets/housing/housing.csv"))
