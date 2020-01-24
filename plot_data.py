import matplotlib.pyplot as plt
import geopandas as gpd
import glob


def plot(f):
    print(f)
    df = gpd.read_file(f)
    name = f.split('/')[-1].split('.')[0]
    df.plot(lw=0.05, color='k')
    plt.axis('off')
    plt.savefig(f"img/{name}.svg")
    plt.clf()

fs = glob.glob("data/*.geojson")

for f in fs:
    plot(f)



