import matplotlib
import flask
import mplfinance as mpf
import pandas as pd
import requests
import asyncio
import aiohttp
from datetime import date
from PIL import Image
from moeximporter import *
def integral(i):
    data = {}
    data[0] = MoexCandlePeriods.Period1Min
    data[1] = MoexCandlePeriods.Period10Min
    data[2] = MoexCandlePeriods.Period1Hour
    data[3] = MoexCandlePeriods.Period1Day
    data[4] = MoexCandlePeriods.Period1Week
    data[5] = MoexCandlePeriods.Period1Month
    data[6] = MoexCandlePeriods.Period1Quarter
    return data[i]
def create_data(name_company, year_begin, month_begin, day_begin,year_end, month_end, day_end, inter):
    m1 = MoexImporter()
    sec = MoexSecurity(name_company, m1)
    is_exist = open('all companies.txt', 'r')
    df_candles = sec.getCandleQuotesAsDataFrame(date(year_begin, month_begin, day_begin), date(year_end, month_end, day_end), interval=integral(inter),  board=None)
    df_string =df_candles.to_string(header=False)
    s = name_company + ".txt"
    if name_company in is_exist.read():
        f = open(s, 'r+')
        f.truncate(0)
        f.close()
        my_file = open(s, "w")
        my_file.write(df_string)
        my_file.close()
    else:
        mf = open("all companies.txt", "a")
        mf.write(name_company+" ")
        mf.close()
        my_file = open(s, "w+")
        my_file.write(df_string)
        my_file.close()
    is_exist.close()
def main():
    m1 = MoexImporter()
    sec = MoexSecurity("DIOD", m1)
    candles_df = sec.getCandleQuotesAsDataFrame(date(2022, 2, 22), date(2023,12, 23), interval=MoexCandlePeriods.Period1Hour, board=None)
    mpf.plot(candles_df, type ="candle")
    s = input()
    create_data(s, 2022, 6, 22,2023,6,24, 1)
main()
