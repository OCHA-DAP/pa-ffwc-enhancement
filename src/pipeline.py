from aatoolbox import (
    CodAB,
    GeoBoundingBox,
    GlofasReforecast,
    create_country_config,
)

country_config = create_country_config(iso3="bgd")
codab = CodAB(country_config=country_config)
codab.download()

admin0 = codab.load(admin_level=0)
geo_bounding_box = GeoBoundingBox.from_shape(admin0)

glofas_reforecast = GlofasReforecast(
    country_config=country_config,
    geo_bounding_box=geo_bounding_box,
    leadtime_max=15,
)
glofas_reforecast.download()
