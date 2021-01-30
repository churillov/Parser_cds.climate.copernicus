import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'grib',
        'variable': 'k_index',
        'year': '1979',
        'month': '01',
        'day': '01',
        'time': '07:00',
    },
    'download.grib')
