# Author: Claire

import pandas as pd

time_periods = [("2020-03-01", "2020-04-30"),
                ("2020-12-01", "2021-01-31"),
                ("2021-12-01", "2022-01-31")]


def find_social_referral_frequency(start_date, end_date, source_cat):
    """
    Calculates the frequency of visits that were social referrals for a given
    traffic source. Examples of traffic sources with social referrals are:
    Facebook, Instagram, Twitter, Other .com, and Other .org.

    Inputs:
        start date of data already pulled (str)
        end date of data already pulled (str)
        source cat (str): must be the same exact str as source categories used
    
    Returns (float): frequency of visits that were social referrals for that source
    """
    filepath = f"happy_app/data/{start_date}_to_{end_date}_traffic-source.csv"
    
    traffic_source_data = pd.read_csv(filepath)
    
    # subset to only data within the source category provided
    traffic_source_data = traffic_source_data[traffic_source_data["source cat"] == source_cat]

    # find total number of visits from that source
    total = traffic_source_data["visits"].sum()

    # find number of visits that were social referrals from that source
    social_referrals = traffic_source_data[traffic_source_data["has_social_referral"] == "Yes"].sum()["visits"]

    # return the frequency of visits that were social referrals for that source
    return social_referrals/total

def get_social_referral_frequency(source_cat):
    """
    Find average across time periods pulled.
    """
    freq_total = 0
    for time_period in time_periods:
        start_date, end_date = time_period
        freq_total += find_social_referral_frequency(start_date, end_date, source_cat)
    
    return int(round(freq_total*100/len(time_periods), ndigits=0))