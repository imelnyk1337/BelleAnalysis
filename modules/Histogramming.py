import ROOT
import sys
import numpy as np
import numba
from typing import List, Dict, Any


def get_branches(filename_: str, treename_: str) -> List[Any]:
    file = ROOT.TFile.Open(filename_)
    if file.IsZombie():
        print(f"Error: couldn't open file {filename_}")
        return []
    tree = file.Get(treename_)  # replace with the name of your tree
    branches_ = [br.GetName() for br in tree.GetListOfBranches()]
    file.Close()
    return branches_


class HistogramManager:
    """
    Use of lambda calculus approach.
     Full functional-style code
     """
    ROOT.EnableImplicitMT(10)
    ROOT.EnableThreadSafety()
    preselection_cuts = ''

    def __init__(self) -> None:
        self._to_draw = ''

    @staticmethod
    def preselect(self, file_: str, tree_: str,
                  preselection_cut: str):
        rdf = ROOT.RDataFrame(tree_, file_)
        preselection_cuts_ = preselection_cut
        rdf2 = (rdf
                .Filter(f"{preselection_cuts_}")
                )
        return rdf2

    def get_stats(self): ...

    def histogram(self, target: str) -> None:
        self._to_draw = target


if __name__ == '__main__':
    ...
