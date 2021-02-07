import cdsapi
import os


processed_data = 'processed data'     # Папка для хранения обработанных данных
if os.path.exists(processed_data):    # Проверка наличия папки
    print('Папка уже существует')
else:
    os.mkdir(processed_data)          # Создает папку processed data

c = cdsapi.Client()

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
months = ['04', '05', '06', '07', '08']
days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
times = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']

for year in years:
    if os.path.exists("{}/{}".format(processed_data, year)):  # Проверка наличия папки
        print('Папка уже существует')
    else:
        os.mkdir("{}/{}".format(processed_data, year))
    for month in months:
        if os.path.exists("{}/{}/{}".format(processed_data, year, month)):
            print('Папка уже существует')   # Проверка наличия папки
        else:
            os.mkdir("{}/{}/{}".format(processed_data, year, month))
        if int(months[0]) % 2 == 0:
            for day in days[:30]:
                if os.path.exists("{}/{}/{}/{}".format(processed_data, year, month, day)):  # Проверка наличия папки
                    print('Папка уже существует')
                else:
                    os.mkdir(
                        "{}/{}/{}/{}".format(processed_data, year, month, day))
                for time in times:
                    c.retrieve(
                        'reanalysis-era5-single-levels',
                        {
                            'product_type': 'reanalysis',
                            'format': 'netcdf',
                            'variable': 'k_index',
                            'year': '{}'.format(year),
                            'month': '{}'.format(month),
                            'day': '{}'.format(day),
                            'time': '{}'.format(time),
                        },
                        '{}/{}/{}/{}/KI_{}.{}.{}_{}.nc'.format(processed_data, year, month, day, day, month, year, time[:2]))

        elif int(months[0]) % 2 == 1:
            for day in days:
                if os.path.exists("{}/{}/{}/{}".format(processed_data, year, month, day)):  # Проверка наличия папки
                    print('Папка уже существует')
                else:
                    os.mkdir(
                        "{}/{}/{}/{}".format(processed_data, year, month, day))
                for time in times:
                    c.retrieve(
                        'reanalysis-era5-single-levels',
                        {
                            'product_type': 'reanalysis',
                            'format': 'netcdf',
                            'variable': 'k_index',
                            'year': '{}'.format(year),
                            'month': '{}'.format(month),
                            'day': '{}'.format(day),
                            'time': '{}'.format(time),
                        },
                        '{}/{}/{}/{}/KI_{}.{}.{}_{}.nc'.format(processed_data, year, month, day, day, month, year, time[:2]))
