#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#
"""The weewx schema - an extension of the wview schema."""

# =============================================================================
# This is a list containing the default schema of the archive database.  It is
# only used for initialization --- afterwards, the schema is obtained
# dynamically from the database.  Although a type may be listed here, it may
# not necessarily be supported by your weather station hardware.
# =============================================================================
schema = [('dateTime',             'INTEGER NOT NULL UNIQUE PRIMARY KEY'),
          ('usUnits',              'INTEGER NOT NULL'),
          ('interval',             'INTEGER NOT NULL'),
          ('barometer',            'REAL'),
          ('pressure',             'REAL'),
          ('altimeter',            'REAL'),
          ('inTemp',               'REAL'),
          ('outTemp',              'REAL'),
          ('inHumidity',           'REAL'),
          ('outHumidity',          'REAL'),
          ('windSpeed',            'REAL'),
          ('windDir',              'REAL'),
          ('windGust',             'REAL'),
          ('windGustDir',          'REAL'),
          ('rainRate',             'REAL'),
          ('rain',                 'REAL'),
          ('hail',                 'REAL'),
          ('hailRate',             'REAL'),
          ('snow',                 'REAL'),
          ('snowRate',             'REAL'),
          ('dewpoint',             'REAL'),
          ('windchill',            'REAL'),
          ('heatindex',            'REAL'),
          ('ET',                   'REAL'),
          ('radiation',            'REAL'),
          ('UV',                   'REAL'),
          ('humidex',              'REAL'),
          ('appTemp',              'REAL'),
          ('maxSolarRad',          'REAL'),
          ('windrun',              'REAL'),
          ('cloudbase',            'REAL'),
          ('inDewpoint',           'REAL'),
          ('heatingTemp',          'REAL'),
          ('rxCheckPercent',       'REAL'),
          ('consBatteryVoltage',   'REAL'),
          ('heatingVoltage',       'REAL'),
          ('supplyVoltage',        'REAL'),
          ('referenceVoltage',     'REAL'),
          ('txBatteryStatus',      'REAL'),
          ('windBatteryStatus',    'REAL'),
          ('rainBatteryStatus',    'REAL'),
          ('hailBatteryStatus',    'REAL'),
          ('snowBatteryStatus',    'REAL'),
          ('outTempBatteryStatus', 'REAL'),
          ('inTempBatteryStatus',  'REAL'),
          ('uvBatteryStatus',      'REAL'),
          ('extraTemp1',           'REAL'),
          ('extraTemp2',           'REAL'),
          ('extraTemp3',           'REAL'),
          ('extraTemp4',           'REAL'),
          ('extraTemp5',           'REAL'),
          ('extraTemp6',           'REAL'),
          ('extraTemp7',           'REAL'),
          ('extraTemp8',           'REAL'),
          ('soilTemp1',            'REAL'),
          ('soilTemp2',            'REAL'),
          ('soilTemp3',            'REAL'),
          ('soilTemp4',            'REAL'),
          ('soilTemp5',            'REAL'),
          ('soilTemp6',            'REAL'),
          ('soilTemp7',            'REAL'),
          ('soilTemp8',            'REAL'),
          ('leafTemp1',            'REAL'),
          ('leafTemp2',            'REAL'),
          ('leafTemp3',            'REAL'),
          ('leafTemp4',            'REAL'),
          ('leafTemp5',            'REAL'),
          ('leafTemp6',            'REAL'),
          ('leafTemp7',            'REAL'),
          ('leafTemp8',            'REAL'),
          ('extraHumid1',          'REAL'),
          ('extraHumid2',          'REAL'),
          ('extraHumid3',          'REAL'),
          ('extraHumid4',          'REAL'),
          ('extraHumid5',          'REAL'),
          ('extraHumid6',          'REAL'),
          ('extraHumid7',          'REAL'),
          ('extraHumid8',          'REAL'),
          ('soilMoist1',           'REAL'),
          ('soilMoist2',           'REAL'),
          ('soilMoist3',           'REAL'),
          ('soilMoist4',           'REAL'),
          ('soilMoist5',           'REAL'),
          ('soilMoist6',           'REAL'),
          ('soilMoist7',           'REAL'),
          ('soilMoist8',           'REAL'),
          ('leafWet1',             'REAL'),
          ('leafWet2',             'REAL'),
          ('leafWet3',             'REAL'),
          ('leafWet4',             'REAL'),
          ('leafWet5',             'REAL'),
          ('leafWet6',             'REAL'),
          ('leafWet7',             'REAL'),
          ('leafWet8',             'REAL'),
          ('batteryStatus1',       'REAL'),
          ('batteryStatus2',       'REAL'),
          ('batteryStatus3',       'REAL'),
          ('batteryStatus4',       'REAL'),
          ('batteryStatus5',       'REAL'),
          ('batteryStatus6',       'REAL'),
          ('batteryStatus7',       'REAL'),
          ('batteryStatus8',       'REAL'),
          ('batteryVoltage1',      'REAL'),
          ('batteryVoltage2',      'REAL'),
          ('batteryVoltage3',      'REAL'),
          ('batteryVoltage4',      'REAL'),
          ('batteryVoltage5',      'REAL'),
          ('batteryVoltage6',      'REAL'),
          ('batteryVoltage7',      'REAL'),
          ('batteryVoltage8',      'REAL'),
          ('signal1',              'REAL'),
          ('signal2',              'REAL'),
          ('signal3',              'REAL'),
          ('signal4',              'REAL'),
          ('signal5',              'REAL'),
          ('signal6',              'REAL'),
          ('signal7',              'REAL'),
          ('signal8',              'REAL'),
          ]

# logger capacity?

# units
obs_group_dict['inTemp'] = 'group_temperature'
obs_group_dict['outTemp'] = 'group_temperature'
obs_group_dict['inHumidity'] = 'group_percent'
obs_group_dict['outHumidity'] = 'group_percent'
obs_group_dict['rxCheckPercent'] = 'group_percent'
obs_group_dict['batteryVoltage1'] = 'group_volt'
# FIXME: define units for these fields here

# accumulators
extract_dict['snow'] = Accum.sum_extract
extract_dict['hail'] = Accum.sum_extract
# FIXME: also day/month/year for these as last_extract?
