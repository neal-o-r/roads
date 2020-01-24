import requests
import json

cts = {"C" : "County Cork",
"CE" : "County Clare",
"CN" : "County Cavan",
"CW" : "County Carlow",
"D" : "County Dublin",
"DL" : "County Donegal",
"G" : "County Galway",
"KE" : "County Kildare",
"KK" : "County Kilkenny",
"KY" : "County Kerry",
"L" : "County Limerick",
"LD" : "County Longford",
"LH" : "County Louth",
"LM" : "County Leitrim",
"LS" : "County Laois",
"MH" : "County Meath",
"MN" : "County Monaghan",
"MO" : "County Mayo",
"OY" : "County Offaly",
"RN" : "County Roscommon",
"SO" : "County Sligo",
"T" : "County Tipperary",
"W" : "County Waterford",
"WH" : "County Westmeath",
"WX" : "County Wexford",
"WW" : "County Wicklow",
"FM" : "County Fermanagh",
"AN" : "County Antrim",
"TY" : "County Tyrone",
"DW" : "County Down",
"AR" : "County Armagh",
"DR" : "County Derry"}


query = lambda x: f"""data=area[name="{x}"];
(._; )->.area;
(
way["highway"](area.area);
node(w);
);
out skel;"""

be = 'https://overpass.kumi.systems/api/interpreter'


for name, county in cts.items():
    print(county)
    js = requests.post(be, data=query(county)).text
    with open(f"data/{name}.osm", "w") as f:
        f.write(js)
