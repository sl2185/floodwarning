from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
import datetime

def test_polyfit():
    # Mock dates and water levels
    mock_dates = [datetime.datetime(2023, 1, 1), datetime.datetime(2023, 1, 2), datetime.datetime(2023, 1, 3)]
    mock_levels = [1.5, 2.0, 2.5]

    poly, coeff = polyfit( mock_dates,mock_levels,3)

    assert poly.order == 3

    assert coeff == poly[0]