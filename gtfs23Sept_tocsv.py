import pandas as pd

FILES = [
    'data/gtfs23Sept/agency.txt',
    'data/gtfs23Sept/calendar.txt',
    'data/gtfs23Sept/shapes.txt',
    'data/gtfs23Sept/stops.txt',
    'data/gtfs23Sept/trips.txt',
    'data/gtfs23Sept/calendar_dates.txt',
    'data/gtfs23Sept/routes.txt',
    'data/gtfs23Sept/stop_times.txt',
    'data/gtfs23Sept/translations.txt'
]

for f in FILES:
    f_name = f.split('./')[-1].split('.txt')[0]
    print(f_name)    
    df = pd.read_fwf(f'{f_name}.txt')
    df.to_csv(f'{f_name}.csv')
