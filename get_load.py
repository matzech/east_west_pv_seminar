import datetime
from datetime import time as settime

import numpy as np
from matplotlib import pyplot as plt

import demandlib.bdew as bdew
import demandlib.particular_profiles as profiles

def get_load(year=2017, demand_y=3000):
    import datetime
    from datetime import time as settime

    import numpy as np
    from matplotlib import pyplot as plt

    import demandlib.bdew as bdew
    import demandlib.particular_profiles as profiles

    holidays = { # exclusive, does not really matter for the simulation
        
    }

    ann_el_demand_per_sector = {
        "h0": demand_y,
    }


    # read standard load profiles
    e_slp = bdew.ElecSlp(year, holidays=holidays)

    # multiply given annual demand with timeseries
    elec_demand = e_slp.get_profile(ann_el_demand_per_sector)

    # Add the slp for the industrial group
    ilp = profiles.IndustrialLoadProfile(e_slp.date_time_index, holidays=holidays)


    # Resample 15-minute values to hourly values.
    elec_demand_resampled = elec_demand.resample("1h").mean()


    for key in ann_el_demand_per_sector:
        assert np.isclose(
            elec_demand[key].sum() / 4, ann_el_demand_per_sector[key]
        )
    return elec_demand_resampled

df = get_load(2013)