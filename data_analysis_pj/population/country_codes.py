from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据国家名字获得能被pygal使用的国别名（即两个字的国别名）"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
        # return None   #如果没找到指定国家就返回None

