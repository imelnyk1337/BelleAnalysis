from typing import List, Any
from modules.Histogramming import get_branches
import modules.CutsManager
import ROOT
import numpy as np
import numba



tracks_selection = {
    "something ...": [0, 0]
}

if __name__ == '__main__':
    filename = "evtgen_exp_53_Bs_Ds_KKpi_v6.root"
    branches = get_branches(filename, "h1")
    print(branches)
    print(len(branches))
