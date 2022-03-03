import sqlite3
import pandas as pd
import explore

def acquire_fires():
    '''
    This function returns a pandas dataframe of wildfire data from 1992-2018.
    '''
    # check for local csv
    import os
    if os.path.isfile('fires.csv'):
        fires = pd.read_csv('fires.csv', index_col=0)
    # if no local csv, get data from database
    else:
        # create connection
        cnx = sqlite3.connect('FPA_FOD_20210617.sqlite')
        # get data
        fires = pd.read_sql_query("SELECT * FROM Fires", cnx)
        # cache data to csv
        fires.to_csv('fires.csv')
    return fires

def prep_fires(fires):
    '''
    This function takes in the fires dataframe and prepares it for our MVP
    exploration.
    '''
    # drop columns due to null values
    fires.drop(columns=['LOCAL_FIRE_REPORT_ID',
                   'LOCAL_INCIDENT_ID',
                   'FIRE_CODE',
                   'FIRE_NAME',
                   'ICS_209_PLUS_INCIDENT_JOIN_ID',
                   'ICS_209_PLUS_COMPLEX_JOIN_ID',
                   'MTBS_ID',
                   'MTBS_FIRE_NAME',
                   'COMPLEX_NAME',
                   'DISCOVERY_TIME',
                   'NWCG_CAUSE_AGE_CATEGORY',
                   'CONT_TIME',
                   'COUNTY',
                   'FIPS_CODE',
                   'FIPS_NAME'], inplace=True)
    # drop columns we don't need for MVP
    fires.drop(columns=['FOD_ID',
                   'FPA_ID',
                   'SOURCE_SYSTEM_TYPE',
                   'SOURCE_SYSTEM',
                   'NWCG_REPORTING_AGENCY',
                   'NWCG_REPORTING_UNIT_ID',
                   'NWCG_REPORTING_UNIT_NAME',
                   'SOURCE_REPORTING_UNIT',
                   'SOURCE_REPORTING_UNIT_NAME',
                   'FIRE_SIZE_CLASS',
                   'NWCG_CAUSE_CLASSIFICATION',
                   'CONT_DOY',
                   'DISCOVERY_DOY',
                   'OWNER_DESCR'], inplace=True)
    # convert columns to datetime
    fires['DISCOVERY_DATE'] = pd.to_datetime(fires['DISCOVERY_DATE'])
    fires.CONT_DATE = pd.to_datetime(fires.CONT_DATE, errors='coerce')
    # lowercase column names
    fires.columns = fires.columns.str.lower()
    # rename column name
    fires.rename(columns={'nwcg_general_cause':'general_cause', 'cont_date':'containment_date'}, inplace=True)
    fires = explore.label_regions(fires)
    fires['fire_size_cat'] = np.where(fires.fire_size < 5000, 'small', 'large')
    return fires

def wrangle_fires():
    '''
    This function acquires and prepares wildfire data from 1992-2018 for our MVP.
    '''
    return prep_fires(acquire_fires())