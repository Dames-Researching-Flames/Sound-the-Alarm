import pandas as pd
import numpy as np

# label states by regions
west = ['WA', 'OR', 'CA', 'NV', 'UT', 'CO', 'WY', 'ID', 'MT', 'AK', 'HI']
southwest = ['AZ', 'NM', 'OK', 'TX']
midwest = ['ND', 'SD', 'NE', 'KS', 'MO', 'IA', 'IL', 'MN', 'WI', 'IN', 'OH', 'MI']
southeast = ['MD', 'AR', 'LA', 'MS', 'AL', 'TN', 'KY', 'FL', 'PR', 'GA', 'SC', 'NC', 'VA', 'DC', 'WV', 'DE']
northeast = ['PA', 'NJ', 'CT', 'RI', 'MA', 'NH', 'ME', 'VT', 'NY']

def label_regions(fires):
    '''
    This function takes in the fires dataframe and labels each state by which US region it is in.
    It then adds the size of each region by summing the sizes of each state in that region.
    '''
    # get state size data
    states = pd.read_csv('state_acres.csv', index_col=0)
    states.rename(columns={'State Acres':'state_size'}, inplace=True)
    # add onto df
    fires1 = pd.merge(fires, states, left_on=fires.state, right_index=True).drop(columns='key_0')
    fires['state_size'] = fires1.state_size.str.replace(',','')
    # change dtype
    fires = fires.astype({'state_size':'float64'})
    # add labels to dataframe
    fires['region'] = np.where(fires.state.isin(west), 'west', 'region')
    fires['region'] = np.where(fires.state.isin(southwest), 'southwest', fires.region)
    fires['region'] = np.where(fires.state.isin(midwest), 'midwest', fires.region)
    fires['region'] = np.where(fires.state.isin(southeast), 'southeast', fires.region)
    fires['region'] = np.where(fires.state.isin(northeast), 'northeast', fires.region)
    # calculate each region's size
    west_size = sum([fires[fires.state == state].state_size.max() for state in west])
    southwest_size = sum([fires[fires.state == state].state_size.max() for state in southwest])
    southeast_size = sum([fires[fires.state == state].state_size.max() for state in southeast])
    midwest_size = sum([fires[fires.state == state].state_size.max() for state in midwest])
    northeast_size = sum([fires[fires.state == state].state_size.max() for state in northeast])
    # add region_size to dataframe
    fires['region_size'] = np.where(fires.region == 'west', west_size, 0)
    fires['region_size'] = np.where(fires.region == 'southwest', southwest_size, fires.region_size)
    fires['region_size'] = np.where(fires.region == 'midwest', midwest_size, fires.region_size)
    fires['region_size'] = np.where(fires.region == 'southeast', southeast_size, fires.region_size)
    fires['region_size'] = np.where(fires.region == 'northeast', northeast_size, fires.region_size)
    return fires

def fire_size_region(fires):
    '''
    This function takes in the fires dataframe and creates a new dataframe of total fire size
    by region for each year during 1992-2018.
    '''
    # get sum of fire sizes for each year
    year_sums = fires.groupby('fire_year').fire_size.sum()
    # turn into dataframe
    year_totals = pd.DataFrame(year_sums)
    year_totals.columns = ['total_acres_burned']
    # do the same for each region
    west_sums = fires[fires.region == 'west'].groupby('fire_year').fire_size.sum()
    year_totals['west'] = west_sums
    southwest_sums = fires[fires.region == 'southwest'].groupby('fire_year').fire_size.sum()
    year_totals['southwest'] = southwest_sums
    midwest_sums = fires[fires.region == 'midwest'].groupby('fire_year').fire_size.sum()
    year_totals['midwest'] = midwest_sums
    southeast_sums = fires[fires.region == 'southeast'].groupby('fire_year').fire_size.sum()
    year_totals['southeast'] = southeast_sums
    northeast_sums = fires[fires.region == 'northeast'].groupby('fire_year').fire_size.sum()
    year_totals['northeast'] = northeast_sums
    return year_totals

def num_region(fires):
    '''
    This function takes in the fires dataframe and creates a new dataframe of total number of fires
    by region for each year during 1992-2018.    
    '''
    # number of fires by size, region
    year_fires = fires.groupby('fire_year').fire_size.count()
    total_fires = pd.DataFrame(year_fires)
    total_fires.columns = ['total_fires']
    west_fires = fires[fires.region == 'west'].groupby('fire_year').fire_size.count()
    total_fires['west'] = west_fires
    southwest_fires = fires[fires.region == 'southwest'].groupby('fire_year').fire_size.count()
    total_fires['southwest'] = southwest_fires
    midwest_fires = fires[fires.region == 'midwest'].groupby('fire_year').fire_size.count()
    total_fires['midwest'] = midwest_fires
    southeast_fires = fires[fires.region == 'southeast'].groupby('fire_year').fire_size.count()
    total_fires['southeast'] = southeast_fires
    northeast_fires = fires[fires.region == 'northeast'].groupby('fire_year').fire_size.count()
    total_fires['northeast'] = northeast_fires
    return total_fires

def mean_region(fires):
    '''
    This function takes in the fires dataframe and creates a new dataframe of mean fire size
    by region for each year during 1992-2018.    
    '''
    # mean fire size by year, region
    year_mean = fires.groupby('fire_year').fire_size.mean()
    mean_fire_size = pd.DataFrame(year_mean)
    mean_fire_size.columns = ['overall_mean']
    west_mean = fires[fires.region == 'west'].groupby('fire_year').fire_size.mean()
    mean_fire_size['west'] = west_mean
    southwest_mean = fires[fires.region == 'southwest'].groupby('fire_year').fire_size.mean()
    mean_fire_size['southwest'] = southwest_mean
    midwest_mean = fires[fires.region == 'midwest'].groupby('fire_year').fire_size.mean()
    mean_fire_size['midwest'] = midwest_mean
    southeast_mean = fires[fires.region == 'southeast'].groupby('fire_year').fire_size.mean()
    mean_fire_size['southeast'] = southeast_mean
    northeast_mean = fires[fires.region == 'northeast'].groupby('fire_year').fire_size.mean()
    mean_fire_size['northeast'] = northeast_mean
    return mean_fire_size

def median_region(fires):
    '''
    This function takes in the fires dataframe and creates a new dataframe of median fire size
    by region for each year during 1992-2018.    
    '''
    # median fire size by year, region
    year_median = fires.groupby('fire_year').fire_size.median()
    median_fire_size = pd.DataFrame(year_median)
    median_fire_size.columns = ['overall_median']
    west_median = fires[fires.region == 'west'].groupby('fire_year').fire_size.median()
    median_fire_size['west'] = west_median
    southwest_median = fires[fires.region == 'southwest'].groupby('fire_year').fire_size.median()
    median_fire_size['southwest'] = southwest_median
    midwest_median = fires[fires.region == 'midwest'].groupby('fire_year').fire_size.median()
    median_fire_size['midwest'] = midwest_median
    southeast_median = fires[fires.region == 'southeast'].groupby('fire_year').fire_size.median()
    median_fire_size['southeast'] = southeast_median
    northeast_median = fires[fires.region == 'northeast'].groupby('fire_year').fire_size.median()
    median_fire_size['northeast'] = northeast_median
    return median_fire_size