import json
from pygal_maps_world.maps import World
from country_codes import get_country_code
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

cc_populations={}
for pop_dict in pop_data:
    if pop_dict['Year'] == "1960":
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        # print(country_name + ": "+ str(population))
        code=get_country_code(country_name)
        if code:
            cc_populations[code] = population
# print(cc_populations)
cc_pop_10yi,cc_pop_wan,cc_pop_less = {},{},{}
for cc,pop in cc_populations.items():
    if pop>100000000:
        cc_pop_10yi[cc] = pop
    elif pop<10000000:
        cc_pop_wan[cc] = pop
    else:
        cc_pop_less[cc] = pop


wm_style = LightColorizedStyle#RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'World Population in 2010,by Country'

wm.add('1亿',cc_pop_10yi)
wm.add('千万',cc_pop_wan)
wm.add('少于一千万',cc_pop_less)

wm.render_to_file('world_population.svg')

