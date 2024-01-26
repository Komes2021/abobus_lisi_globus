from moeximporter import MoexImporter, MoexSecurity, MoexCandlePeriods
from datetime import date
import mplfinance as mpf
def show_kostya_skill(name_company, file_name):
    m1 = MoexImporter()
    sec = MoexSecurity(name_company, m1)
    candles_df = sec.getCandleQuotesAsDataFrame(date(2023, 1, 1), date(2024, 1, 24), interval=MoexCandlePeriods.Period1Day, board=None)
    mpf.plot(candles_df, type='candle', style='yahoo', savefig=file_name)