#!/usr/bin/env python
import os,sys

from ROOT import *
gROOT.SetBatch()
gStyle.SetOptStat(0)

import argparse
parser =  argparse.ArgumentParser(description='Ploting my plots', usage=os.path.basename(__file__)+' ./inPath')
parser.add_argument("inPath", help="Input directory with root files.")
parser.add_argument("-o","--outDir", type=str, default="figs", help="Output directory for figures")
# parser.add_argument("-r",  dest="R", type=int, default=0, help="Not used")

opt = parser.parse_args()

#parser.print_help()
print opt

procs = ['ZH_hcc','WH_hcc','s_Top','TT','Zj_ll','Zj_blc','Zj_bbc','Zj_cc','Wj_ll','Wj_blc','Wj_bbc','Wj_cc']
#procs = ['ZH_hcc','ZH_hbb','ggZH_hbb','WH_hbb','s_Top','TT','Zj_ll','Zj_blc','Zj_bbc','Zj_cc','Wj_ll','Wj_blc','Wj_bbc','Wj_cc','VVLF','VVbb','VVcc']
#procs = ['Wj_ll']
categ = ['high_Zmm', 'high_Zee', 'low_Zmm', 'low_Zee', 'Wmunu', 'Wenu', 'Znn']
#categ = ['Wmunu', 'Wenu']

systs = ['CMS_scale_j_13TeV_2016', 'CMS_res_j_13TeV_2016', 'CMS_vhcc_puWeight_2016', 
         'CMS_LHE_weights_scale_muF_Wj_ll', 'CMS_LHE_weights_scale_muF_Wj_blc',
         'CMS_cTagWeight_PU']
#systs = ['CMS_scale_j_13TeV_2016']
#systs = ['CMS_vhcc_puWeight_2016']

CtoC = {'high_Zmm':'Zmm', 'high_Zee':'Zee', 'low_Zmm':'Zmm', 'low_Zee':'Zee', 'Wmunu':'Wmn', 'Wenu':'Wen', 'Znn':'Znn'}
regions = ['SR','ttbar',
           'Zcc', 'Wcc', 'Vcc',
           'Zlf', 'Wlf', 'Vlf',
           'Zhf', 'Whf', 'Vhf' ]
        
diffUp_vals = {}
diffDw_vals = {}
diffUD_vals = {}
hDiffUp = {}
hDiffDw = {}
hDiffUD = {}
hBits = {}

def createDir(myDir):
    print 'Creating a new directory: ', myDir
    if not os.path.exists(myDir):
        try: os.makedirs(myDir)
        except OSError:
            if os.path.isdir(myDir): pass
            else: raise
    else:
        print "\t OOps, it already exists"


for s in systs:
    hDiffUp[s] = TH1F('hDiffUp_'+s,'Nominal-Up difference for '+s, 100, -0.15, 0.15)
    hDiffDw[s] = TH1F('hDiffDw_'+s,'Nominal-Down difference for '+s, 100, -0.15, 0.15)
    hDiffUD[s] = TH1F('hDiffUD_'+s,'Up-Down difference for '+s, 100, -0.15, 0.15)
    hBits[s] = {}
    for r in regions:
        hBits[s][r] = TH1F('hBits_'+s+'/'+r,'++/+-/-+/-- for '+s+' in '+r, 4, 0, 4)

for s in systs:
    for r in regions:
        createDir(opt.outDir+'/'+s+'/'+r)


for c in categ:
    print "Open the corresponding root file for this category:", c
    fName = 'vhcc_'+CtoC[c]+'-2016.root'
    print fName
    f = TFile(opt.inPath+'/'+fName)
    f.ls()

    for r in regions:
        for p in procs:
            for s in systs:
                hName0 = "_".join(['BDT', r, c, p])
                h00 = f.Get(hName0)
                hName = hName0+"_"+s
                print hName
                hUp = f.Get(hName+"Up")
                hDw = f.Get(hName+"Down")
                if h00==None or hUp==None or hDw==None:
                    # Just skip those who dont exist
                    # print "I am None:", hName
                    continue

                # Calculate Chi2Test() between Up/Down and Nominal
                
                probChi2Up = h00.Chi2Test(hUp,"WW ")
                probChi2Dw = h00.Chi2Test(hDw,"WW ")
                # print probChi2Up, probChi2Dw

                # Calculate KolmogorovTest() between Up/Down and Nominal
                
                probKolmUp = h00.KolmogorovTest(hUp,"")
                probKolmDw = h00.KolmogorovTest(hDw,"")
                # print probKolmUp, probKolmDw

                # Compare the integrals
                intDiffUp, intDiffDw = 0, 0
                if h00.Integral() != 0:
                    intDiffUp = 1-hUp.Integral()/h00.Integral()
                    intDiffDw = 1-hDw.Integral()/h00.Integral()
                # print intDiffUp, intDiffDw

                
                # Now let's have a look at them
                # First set maximums for plotting 
                hmax = max([h00.GetMaximum(), hUp.GetMaximum(), hDw.GetMaximum()])
                # if 'puWe' in s:
                #     print "HMAX", hmax, [h00.GetMaximum(), hUp.GetMaximum(), hDw.GetMaximum()]

                h00.SetMaximum(hmax*1.4)

                # Now we are ready to plot
                hUp.SetLineColor(kGreen+2)
                hDw.SetLineColor(kRed+2)
                h00.Draw()
                hUp.Draw('same')
                hDw.Draw('same')
                if r == "SR":
                    xname = "BDT score"
                else:
                    xname = "C-tagger score"
                h00.SetTitle(' '.join([s, 'in', "("+', '.join([c,p,r])+")"]) +';'+xname)
                leg = TLegend(0.11,0.72,0.99,0.91)
                leg.AddEntry(h00, "Nominal", 'l')
                leg.AddEntry(hUp, "Syst. Up; P(#Chi^{2})=%.3f, P(Kolm)=%.3f, IntDiff=%.3f"%(probChi2Up, probKolmUp, intDiffUp), 'l')
                leg.AddEntry(hDw, "Syst. Dw; P(#Chi^{2})=%.3f, P(Kolm)=%.3f, IntDiff=%.3f"%(probChi2Dw, probKolmDw, intDiffDw), 'l')
                #leg.SetTextSize(0.25)
                leg.SetMargin(0.09)
                leg.Draw()
                c1.SaveAs(opt.outDir+"/"+s+"/"+r+"/fig_"+s+"_"+hName0+".png")

 
                # Save the integral difffs for plotting
                diffUp_vals[r,c,p,s], diffDw_vals[r,c,p,s], diffUD_vals[r,c,p,s] = -1, -1, -1
                diffUp_vals[r,c,p,s], diffDw_vals[r,c,p,s] = intDiffUp, intDiffDw

                hDiffUp[s].Fill(intDiffUp)
                hDiffDw[s].Fill(intDiffDw)

                if intDiffUp>=0 and intDiffDw>=0:
                    hBits[s][r].Fill(0)
                elif intDiffUp>=0 and intDiffDw<0:
                    hBits[s][r].Fill(1)
                elif intDiffUp<0 and intDiffDw>=0:
                    hBits[s][r].Fill(2)
                elif intDiffUp<0 and intDiffDw<0:
                    hBits[s][r].Fill(3)

                # Do Up - Down histogram
                hDiff = hUp.Clone()
                hDiff.Add(hUp, hDw, 1, -1)
                # hDiff.Print()
                if h00.Integral() != 0:
                    diffUD_vals[r,c,p,s] = hDiff.Integral()/h00.Integral()
                    hDiffUD[s].Fill(diffUD_vals[r,c,p,s])
        

"""
for i,n in enumerate([diffUp_vals, diffDw_vals, diffUD_vals]):
    for k,v in n.items():
        # print i, n 
        if abs(v)>0.08:
            print i, k, v
            print k[3]
        
"""

for s in systs:
    hDiffUp[s].Draw()
    hDiffUp[s].SetLineWidth(2)
    hDiffUp[s].SetLineColor(kBlue+1)
    hDiffUp[s].SetXTitle("Integral difference wrt Nominal")

    hDiffDw[s].Draw("same")
    hDiffDw[s].SetLineWidth(2)
    hDiffDw[s].SetLineColor(kRed+2)

    hDiffUp[s].SetMaximum(1.3*max([hDiffUp[s].GetMaximum(), hDiffDw[s].GetMaximum()]))
    leg = TLegend(0.33,0.78,0.99,0.91)
    leg.AddEntry(hDiffUp[s], "1 - Integral(Up)/Integral(Nominal)", 'l')
    leg.AddEntry(hDiffDw[s], "1 - Integral(Down)/Integral(Nominal)", 'l')
    leg.SetMargin(0.1)
    leg.Draw()
    c1.SaveAs(opt.outDir+"/"+s+"/fig_"+s+"_Diff.png")
    
    hDiffUD[s].Draw()
    hDiffUD[s].SetXTitle("(Integral(Up) - Integral(Down))/Integral(Nominal)")
    c1.SaveAs(opt.outDir+"/"+s+"/fig_"+s+"_DiffUD.png")

    for r in regions:
        hBits[s][r].Draw()
        c1.SaveAs(opt.outDir+"/"+s+"/fig_"+s+"_Bits_"+r+".png")
