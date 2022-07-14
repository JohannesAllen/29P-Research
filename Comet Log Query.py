# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:56:40 2021

@author: johan
"""
# JPL Horizons Queries: https://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html#columns
# Horizons Class Astroquery information: https://astroquery.readthedocs.io/en/latest/api/astroquery.jplhorizons.HorizonsClass.html
# Astropy data tables: https://docs.astropy.org/en/stable/table/index.html

from astroquery.jplhorizons import Horizons
from astropy.table import Table

obj = Horizons(id='90000393', location='@HST', epochs = {'start':'2021-11-23', 'stop':'2021-12-8', 'step':'1d'})
eph = obj.ephemerides()
log = eph['datetime_str', 'RA', 'DEC','Tmag', 'r', 'delta', 'elong', 'elongFlag', 'alpha', 'sat_alpha']
log.rename_column('datetime_str','Date & Time')
log.rename_column('Tmag','TotalMag')
log.rename_column('r', 'Helio Dist')
log.rename_column('delta', 'Observer Dist')
log.rename_column('elongFlag', 'Trails/Leads Sun')
log.rename_column('alpha', 'Solar Phase Angle')
log.rename_column('sat_alpha', 'O-P-T')
print(log)
log.write('log2.html', overwrite=True)