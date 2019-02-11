#!/usr/bin/env python

import CombineHarvester.CombineTools.ch as ch
import argparse
# import CombineHarvester.CombineTools.pdgRounding as pdgRounding
import ROOT

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(ROOT.kTRUE)

ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')

parser = argparse.ArgumentParser()
parser.add_argument('--workspace', '-w',help='Input workspace')
parser.add_argument('--fit_file', '-f',help='Input workspace')

args = parser.parse_args()

fin = ROOT.TFile(args.workspace)
wsp = fin.Get('w')

cmb = ch.CombineHarvester()
cmb.SetFlag("workspaces-use-clone", True)
ch.ParseCombineWorkspace(cmb, wsp, 'ModelConfig', 'data_obs', False)


mlf = ROOT.TFile(args.fit_file)
rfr = mlf.Get('fit_s')


def PrintTables(cmb, uargs):
    c_znn = cmb.cp().bin(['vhcc_Znn_1_13TeV2016'])
    c_wmn = cmb.cp().bin(['vhcc_Wmn_1_13TeV2016'])
    c_wen = cmb.cp().bin(['vhcc_Wen_1_13TeV2016'])
    c_zeelow = cmb.cp().bin(['vhcc_Zee_2_13TeV2016'])
    c_zmmlow = cmb.cp().bin(['vhcc_Zmm_2_13TeV2016'])
    c_zeehi = cmb.cp().bin(['vhcc_Zee_1_13TeV2016'])
    c_zmmhi = cmb.cp().bin(['vhcc_Zmm_1_13TeV2016'])

    print r"""
\begin{tabular}{|l|r@{$ \,\,\pm\,\, $}lr@{$ \,\,\pm\,\, $}l|}
\hline
Process & \multicolumn{2}{c}{1-lepton(e)} & \multicolumn{2}{c|}{1-lepton($\mu$)} \\
\hline
\hline"""
    print r'Wcc                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['Wj_cc']).GetRate(), c_wen.cp().process(['Wj_cc']).GetUncertainty(*uargs),
        c_wmn.cp().process(['Wj_cc']).GetRate(), c_wmn.cp().process(['Wj_cc']).GetUncertainty(*uargs))
    print r'Wbb/bc                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['Wj_bbc']).GetRate(), c_wen.cp().process(['Wj_bbc']).GetUncertainty(*uargs),
        c_wmn.cp().process(['Wj_bbc']).GetRate(), c_wmn.cp().process(['Wj_bbc']).GetUncertainty(*uargs))
    print r'Wbl/cl                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['Wj_blc']).GetRate(), c_wen.cp().process(['Wj_blc']).GetUncertainty(*uargs),
        c_wmn.cp().process(['Wj_blc']).GetRate(), c_wmn.cp().process(['Wj_blc']).GetUncertainty(*uargs))
    print r'W+udsg                                       & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['Wj_ll']).GetRate(), c_wen.cp().process(['Wj_ll']).GetUncertainty(*uargs),
        c_wmn.cp().process(['Wj_ll']).GetRate(), c_wmn.cp().process(['Wj_ll']).GetUncertainty(*uargs))
    print r'Zcc                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['Zj_cc']).GetRate(), c_wen.cp().process(['Zj_cc']).GetUncertainty(*uargs),
        c_wmn.cp().process(['Zj_cc']).GetRate(), c_wmn.cp().process(['Zj_cc']).GetUncertainty(*uargs))
    print r'Zbb/bc                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['Zj_bbc']).GetRate(), c_wen.cp().process(['Zj_bbc']).GetUncertainty(*uargs),
        c_wmn.cp().process(['Zj_bbc']).GetRate(), c_wmn.cp().process(['Zj_bbc']).GetUncertainty(*uargs))
    print r'Zbl/cl                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['Zj_blc']).GetRate(), c_wen.cp().process(['Zj_blc']).GetUncertainty(*uargs),
        c_wmn.cp().process(['Zj_blc']).GetRate(), c_wmn.cp().process(['Zj_blc']).GetUncertainty(*uargs))
    print r'Z+udsg                                       & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['Zj_ll']).GetRate(), c_wen.cp().process(['Zj_ll']).GetUncertainty(*uargs),
        c_wmn.cp().process(['Zj_ll']).GetRate(), c_wmn.cp().process(['Zj_ll']).GetUncertainty(*uargs))
    print r'\ttbar                                       & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['TT']).GetRate(), c_wen.cp().process(['TT']).GetUncertainty(*uargs),
        c_wmn.cp().process(['TT']).GetRate(), c_wmn.cp().process(['TT']).GetUncertainty(*uargs))
    print r'Single top quark                              & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['s_Top']).GetRate(), c_wen.cp().process(['s_Top']).GetUncertainty(*uargs),
        c_wmn.cp().process(['s_Top']).GetRate(), c_wmn.cp().process(['s_Top']).GetUncertainty(*uargs))
    print r'VV(udsg)                                      & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['VVLF']).GetRate(), c_wen.cp().process(['VVLF']).GetUncertainty(*uargs),
        c_wmn.cp().process(['VVLF']).GetRate(), c_wmn.cp().process(['VVLF']).GetUncertainty(*uargs))
    print r'VV(bb)                                      & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['VVbb']).GetRate(), c_wen.cp().process(['VVbb']).GetUncertainty(*uargs),
        c_wmn.cp().process(['VVbb']).GetRate(), c_wmn.cp().process(['VVbb']).GetUncertainty(*uargs))
    print r'VZ(cc)                                      & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_wen.cp().process(['VVcc']).GetRate(), c_wen.cp().process(['VVcc']).GetUncertainty(*uargs),
        c_wmn.cp().process(['VVcc']).GetRate(), c_wmn.cp().process(['VVcc']).GetUncertainty(*uargs))
    print r'\hline'
    print r'Total expected background                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\ ' % (
        c_wen.cp().backgrounds().GetRate(), c_wen.cp().backgrounds().GetUncertainty(*uargs),
        c_wmn.cp().backgrounds().GetRate(), c_wmn.cp().backgrounds().GetUncertainty(*uargs))
    print r'VH                               & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\ ' % (
        c_wen.cp().signals().GetRate(), c_wen.cp().signals().GetUncertainty(*uargs),
        c_wmn.cp().signals().GetRate(), c_wmn.cp().signals().GetUncertainty(*uargs))
    print r'\hline'
    print r'Observed data                                    & \multicolumn{2}{c}{$%g$} & \multicolumn{2}{c|}{$%g$} \\' % (
        c_wen.cp().GetObservedRate(), c_wmn.cp().GetObservedRate())
    print r"""\hline
\end{tabular}"""

    print r"""
\begin{tabular}{|l|r@{$ \,\,\pm\,\, $}lr@{$ \,\,\pm\,\, $}l|}
\hline
Process & \multicolumn{2}{c}{Zee low \pT} & \multicolumn{2}{c|}{Zee high \pT} \\
\hline
\hline"""
    print r'Zcc                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zeelow.cp().process(['Zj_cc']).GetRate(), c_zeelow.cp().process(['Zj_cc']).GetUncertainty(*uargs),
        c_zeehi.cp().process(['Zj_cc']).GetRate(), c_zeehi.cp().process(['Zj_cc']).GetUncertainty(*uargs))
    print r'Zbb/bc                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zeelow.cp().process(['Zj_bbc']).GetRate(), c_zeelow.cp().process(['Zj_bbc']).GetUncertainty(*uargs),
        c_zeehi.cp().process(['Zj_bbc']).GetRate(), c_zeehi.cp().process(['Zj_bbc']).GetUncertainty(*uargs))
    print r'Zbl/cl                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zeelow.cp().process(['Zj_blc']).GetRate(), c_zeelow.cp().process(['Zj_blc']).GetUncertainty(*uargs),
        c_zeehi.cp().process(['Zj_blc']).GetRate(), c_zeehi.cp().process(['Zj_blc']).GetUncertainty(*uargs))
    print r'Z+udsg                                       & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zeelow.cp().process(['Zj_ll']).GetRate(), c_zeelow.cp().process(['Zj_ll']).GetUncertainty(*uargs),
        c_zeehi.cp().process(['Zj_ll']).GetRate(), c_zeehi.cp().process(['Zj_ll']).GetUncertainty(*uargs))
    print r'\ttbar                                       & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zeelow.cp().process(['TT']).GetRate(), c_zeelow.cp().process(['TT']).GetUncertainty(*uargs),
        c_zeehi.cp().process(['TT']).GetRate(), c_zeehi.cp().process(['TT']).GetUncertainty(*uargs))
    print r'Single top quark                              & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zeelow.cp().process(['s_Top']).GetRate(), c_zeelow.cp().process(['s_Top']).GetUncertainty(*uargs),
        c_zeehi.cp().process(['s_Top']).GetRate(), c_zeehi.cp().process(['s_Top']).GetUncertainty(*uargs))
    print r'VV(udsg)                                      & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zeelow.cp().process(['VVLF']).GetRate(), c_zeelow.cp().process(['VVLF']).GetUncertainty(*uargs),
        c_zeehi.cp().process(['VVLF']).GetRate(), c_zeehi.cp().process(['VVLF']).GetUncertainty(*uargs))
    print r'VZ(bb)                                      & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zeelow.cp().process(['VVbb']).GetRate(), c_zeelow.cp().process(['VVbb']).GetUncertainty(*uargs),
        c_zeehi.cp().process(['VVbb']).GetRate(), c_zeehi.cp().process(['VVbb']).GetUncertainty(*uargs))
    print r'VZ(cc)                                      & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zeelow.cp().process(['VVcc']).GetRate(), c_zeelow.cp().process(['VVcc']).GetUncertainty(*uargs),
        c_zeehi.cp().process(['VVcc']).GetRate(), c_zeehi.cp().process(['VVcc']).GetUncertainty(*uargs))
    print r'\hline'
    print r'Total expected background                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\ ' % (
        c_zeelow.cp().backgrounds().GetRate(), c_zeelow.cp().backgrounds().GetUncertainty(*uargs),
        c_zeehi.cp().backgrounds().GetRate(), c_zeehi.cp().backgrounds().GetUncertainty(*uargs))
    print r'VH                               & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\ ' % (
        c_zeelow.cp().signals().GetRate(), c_zeelow.cp().signals().GetUncertainty(*uargs),
        c_zeehi.cp().signals().GetRate(), c_zeehi.cp().signals().GetUncertainty(*uargs))
    print r'\hline'
    print r'Observed data                                    & \multicolumn{2}{c}{$%g$} & \multicolumn{2}{c|}{$%g$} \\' % (
        c_zeelow.cp().GetObservedRate(), c_zeehi.cp().GetObservedRate())
    print r"""\hline
\end{tabular}"""

    print r"""
\begin{tabular}{|l|r@{$ \,\,\pm\,\, $}lr@{$ \,\,\pm\,\, $}l|}
\hline
Process & \multicolumn{2}{c}{Z$\mu\mu$ low \pT} & \multicolumn{2}{c|}{Z$\mu\mu$ high \pT} \\
\hline
\hline"""
    print r'Zcc                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zmmlow.cp().process(['Zj_cc']).GetRate(), c_zmmlow.cp().process(['Zj_cc']).GetUncertainty(*uargs),
        c_zmmhi.cp().process(['Zj_cc']).GetRate(), c_zmmhi.cp().process(['Zj_cc']).GetUncertainty(*uargs))
    print r'Zbb                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zmmlow.cp().process(['Zj_bbc']).GetRate(), c_zmmlow.cp().process(['Zj_bbc']).GetUncertainty(*uargs),
        c_zmmhi.cp().process(['Zj_bbc']).GetRate(), c_zmmhi.cp().process(['Zj_bbc']).GetUncertainty(*uargs))
    print r'Zbl/cl                                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zmmlow.cp().process(['Zj_blc']).GetRate(), c_zmmlow.cp().process(['Zj_blc']).GetUncertainty(*uargs),
        c_zmmhi.cp().process(['Zj_blc']).GetRate(), c_zmmhi.cp().process(['Zj_blc']).GetUncertainty(*uargs))
    print r'Z+udsg                                       & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zmmlow.cp().process(['Zj_ll']).GetRate(), c_zmmlow.cp().process(['Zj_ll']).GetUncertainty(*uargs),
        c_zmmhi.cp().process(['Zj_ll']).GetRate(), c_zmmhi.cp().process(['Zj_ll']).GetUncertainty(*uargs))
    print r'\ttbar                                       & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zmmlow.cp().process(['TT']).GetRate(), c_zmmlow.cp().process(['TT']).GetUncertainty(*uargs),
        c_zmmhi.cp().process(['TT']).GetRate(), c_zmmhi.cp().process(['TT']).GetUncertainty(*uargs))
    print r'Single top quark                              & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zmmlow.cp().process(['s_Top']).GetRate(), c_zmmlow.cp().process(['s_Top']).GetUncertainty(*uargs),
        c_zmmhi.cp().process(['s_Top']).GetRate(), c_zmmhi.cp().process(['s_Top']).GetUncertainty(*uargs))
    print r'VV(udsg)                                      & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zmmlow.cp().process(['VVLF']).GetRate(), c_zmmlow.cp().process(['VVLF']).GetUncertainty(*uargs),
        c_zmmhi.cp().process(['VVLF']).GetRate(), c_zmmhi.cp().process(['VVLF']).GetUncertainty(*uargs))
    print r'VZ(bb)                                      & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zmmlow.cp().process(['VVbb']).GetRate(), c_zmmlow.cp().process(['VVbb']).GetUncertainty(*uargs),
        c_zmmhi.cp().process(['VVbb']).GetRate(), c_zmmhi.cp().process(['VVbb']).GetUncertainty(*uargs))
    print r'VZ(cc)                                      & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\' % (
        c_zmmlow.cp().process(['VVcc']).GetRate(), c_zmmlow.cp().process(['VVcc']).GetUncertainty(*uargs),
        c_zmmhi.cp().process(['VVcc']).GetRate(), c_zmmhi.cp().process(['VVcc']).GetUncertainty(*uargs))
    print r'\hline'
    print r'Total expected background                        & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\ ' % (
        c_zmmlow.cp().backgrounds().GetRate(), c_zmmlow.cp().backgrounds().GetUncertainty(*uargs),
        c_zmmhi.cp().backgrounds().GetRate(), c_zmmhi.cp().backgrounds().GetUncertainty(*uargs))
    print r'VH                               & $%.2f$ & $%.2f$ & $%.2f$ & $%.2f$ \\ ' % (
        c_zmmlow.cp().signals().GetRate(), c_zmmlow.cp().signals().GetUncertainty(*uargs),
        c_zmmhi.cp().signals().GetRate(), c_zmmhi.cp().signals().GetUncertainty(*uargs))
    print r'\hline'
    print r'Observed data                                    & \multicolumn{2}{c}{$%g$} & \multicolumn{2}{c|}{$%g$} \\' % (
        c_zmmlow.cp().GetObservedRate(), c_zmmhi.cp().GetObservedRate())
    print r"""\hline
\end{tabular}"""

    print r"""
\begin{tabular}{|l|r@{$ \,\,\pm\,\, $}l|}
\hline
Process & \multicolumn{2}{c}{Z$\nu\nu$} \\
\hline
\hline"""
    print r'Wcc                                        & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['Wj_cc']).GetRate(), c_znn.cp().process(['Wj_cc']).GetUncertainty(*uargs))
    print r'Wbb/bc                                        & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['Wj_bbc']).GetRate(), c_znn.cp().process(['Wj_bbc']).GetUncertainty(*uargs))
    print r'Wbl/cl                                        & $%.2f$ & $%.2f$  \\' % (
        c_znn.cp().process(['Wj_blc']).GetRate(), c_znn.cp().process(['Wj_blc']).GetUncertainty(*uargs))
    print r'W+udsg                                       & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['Wj_ll']).GetRate(), c_znn.cp().process(['Wj_ll']).GetUncertainty(*uargs))
    print r'Zcc                                        & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['Zj_cc']).GetRate(), c_znn.cp().process(['Zj_cc']).GetUncertainty(*uargs))
    print r'Zbb/bc                                        & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['Zj_bbc']).GetRate(), c_znn.cp().process(['Zj_bbc']).GetUncertainty(*uargs))
    print r'Zbl/cl                                        & $%.2f$ & $%.2f$  \\' % (
        c_znn.cp().process(['Zj_blc']).GetRate(), c_znn.cp().process(['Zj_blc']).GetUncertainty(*uargs))
    print r'Z+udsg                                       & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['Zj_ll']).GetRate(), c_znn.cp().process(['Zj_ll']).GetUncertainty(*uargs))
    print r'\ttbar                                       & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['TT']).GetRate(), c_znn.cp().process(['TT']).GetUncertainty(*uargs))
    print r'QCD                                       & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['QCD']).GetRate(), c_znn.cp().process(['QCD']).GetUncertainty(*uargs))
    print r'Single top quark                              & $%.2f$ & $%.2f$  \\' % (
        c_znn.cp().process(['s_Top']).GetRate(), c_znn.cp().process(['s_Top']).GetUncertainty(*uargs))
    print r'VV(udsg)                                      & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['VVLF']).GetRate(), c_znn.cp().process(['VVLF']).GetUncertainty(*uargs))
    print r'VZ(bb)                                      & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['VVbb']).GetRate(), c_znn.cp().process(['VVbb']).GetUncertainty(*uargs))
    print r'VZ(cc)                                      & $%.2f$ & $%.2f$ \\' % (
        c_znn.cp().process(['VVcc']).GetRate(), c_znn.cp().process(['VVcc']).GetUncertainty(*uargs))
    print r'\hline'
    print r'Total expected background                        & $%.2f$ & $%.2f$ \\ ' % (
        c_znn.cp().backgrounds().GetRate(), c_znn.cp().backgrounds().GetUncertainty(*uargs))
    print r'VH                               & $%.2f$ & $%.2f$  \\ ' % (
        c_znn.cp().signals().GetRate(), c_znn.cp().signals().GetUncertainty(*uargs))
    print r'\hline'
    print r'Observed data                                    & \multicolumn{2}{c}{$%g$} \\' % (
        c_znn.cp().GetObservedRate())
    print r"""\hline
\end{tabular}"""




print 'Pre-fit tables:'
PrintTables(cmb, tuple())

cmb.UpdateParameters(rfr)

print 'Post-fit tables:\n\n'
PrintTables(cmb, (rfr, 500))
