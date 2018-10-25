#!/usr/bin/env python

from ROOT import *
import os,sys
import numpy as np
gROOT.SetBatch()


import argparse
parser = argparse.ArgumentParser(description='Limit plotting script')
parser.add_argument('-u','--unblind', dest="unblind", action="store_true", default=False,
                    help="Unblind the observed limits.")
parser.add_argument("--pdf", dest="pdf", action="store_true", default=False,
                    help="Make PDF plots along with PNGs.")
parser.add_argument("-v", dest="verb", type=int, default=0,
                    help="Verbosity level: 0 is minimal")

opt = parser.parse_args()


def getValuesFromFile(fname):
  f = TFile.Open(fname)
  if not f:
    print "This file does not exist.. Just skip this point!"
    return None

  if opt.verb>0:
    f.Print()

  res = []
  tree = f.Get("limit")
  if tree==None:
    if opt.verb>0:
      print "The limit tree in the file does not exist.. Just skip this point!"
    return None

  for i,l in enumerate(tree):
    # print i, l, l.limit
    if i==0: res.append(float(l.limit))
    if i==1: res.append(float(l.limit))
    if i==2: res.append(float(l.limit))
    if i==3: res.append(float(l.limit))
    if i==4: res.append(float(l.limit))
    if i==5: res.append(float(l.limit))

  f.Close()
  return res

if __name__ == "__main__":
  print "This is the __main__ part"

  Tag = 'Zll'
  #Tag = 'cmb'
  l_nom = getValuesFromFile('./output/2016_vhcc_Lumi35p9/'+Tag+'/higgsCombine.Test.AsymptoticLimits.mH125.root')
  l_150 = getValuesFromFile('./output/2016_vhcc_Lumi150/'+Tag+'/higgsCombine.Test.AsymptoticLimits.mH125.root')
  l_300 = getValuesFromFile('./output/2016_vhcc_Lumi300/'+Tag+'/higgsCombine.Test.AsymptoticLimits.mH125.root')
  l_3000 = getValuesFromFile('./output/2016_vhcc_Lumi3000/'+Tag+'/higgsCombine.Test.AsymptoticLimits.mH125.root')
 
  print l_nom
  print l_150
  print l_300
  print l_3000

  xAxis = [35.9, 150, 300, 3000]

  xErr  = []
  obs   = []
  expMean    = []
  exp1SigHi  = []
  exp1SigLow = []
  exp2SigHi  = []
  exp2SigLow = []


  for l in [l_nom, l_150, l_300, l_3000]:
      exp2SigLow.append(l[0])
      exp1SigLow.append(l[1])
      expMean.append(l[2])
      exp1SigHi.append(l[3])
      exp2SigHi.append(l[4])
      if opt.unblind:
        obs.append(l[5])
      else:
          obs.append(0)


  # Create the arrays for graphs
  zeros_Array = np.zeros(len(xAxis),dtype = float)
  xAxis_Array = np.array(xAxis)
  xErr_Array = zeros_Array


  exp_Array = np.array(expMean)
  exp2SigLowErr_Array = np.array([a-b for a,b in zip(expMean,exp2SigLow)])
  exp1SigLowErr_Array = np.array([a-b for a,b in zip(expMean,exp1SigLow)])
  exp1SigHiErr_Array  = np.array([b-a for a,b in zip(expMean,exp1SigHi)])
  exp2SigHiErr_Array  = np.array([b-a for a,b in zip(expMean,exp2SigHi)])

  if opt.unblind:
    obs_Array = np.array(obs)
  else:
    obs_Array = zeros_Array



  print "Exp(lumi)", exp_Array


  mg = TMultiGraph()
  mg.SetTitle('')

  nPoints  = len(xAxis)
  expected = TGraphAsymmErrors(nPoints,xAxis_Array,exp_Array,zeros_Array,zeros_Array,zeros_Array,zeros_Array)
  oneSigma = TGraphAsymmErrors(nPoints,xAxis_Array,exp_Array,xErr_Array,xErr_Array,exp1SigLowErr_Array,exp1SigHiErr_Array)
  twoSigma = TGraphAsymmErrors(nPoints,xAxis_Array,exp_Array,xErr_Array,xErr_Array,exp2SigLowErr_Array,exp2SigHiErr_Array)
  observed = TGraphAsymmErrors(nPoints,xAxis_Array,obs_Array,zeros_Array,zeros_Array,zeros_Array,zeros_Array)


  twoSigma.SetLineWidth(8)
  twoSigma.SetLineColor(kYellow)
  twoSigma.SetMarkerStyle(1)
  
  oneSigma.SetMarkerColor(kBlue+1)
  oneSigma.SetMarkerStyle(21)
  oneSigma.SetLineColor(kGreen+1)
  oneSigma.SetLineWidth(7)
  
  observed.SetMarkerStyle(20)
  
  mg.Add(twoSigma,'PZ')
  mg.Add(oneSigma, 'EPZ')

  #mg.Add(expected,'L')
  
  if opt.unblind:
      mg.Add(observed,'L')
      
  mg.Draw('A')
  mg.GetXaxis().SetTitle('Lumi, 1/fb')

  mg.SetMinimum(0)
  mg.SetMaximum(160)
  mg.GetXaxis().SetLimits(20, 3800)

  gPad.RedrawAxis()

  leg = TLegend(0.60,0.68,0.85,0.91)
  leg.SetTextFont(42)
  leg.SetTextSize(0.04)
  leg.SetFillStyle(0)
  leg.SetBorderSize(0)

  if opt.unblind:
      leg.AddEntry(observed,"Observed", "p")
  leg.AddEntry(oneSigma,"Expected", "p")
  leg.AddEntry(oneSigma,"Expected #pm 1#sigma", "l")
  leg.AddEntry(twoSigma,"Expected #pm 2#sigma", "l")

  leg.Draw()

  c1.SetLogx()

  ext = ['.png']
  if opt.pdf: ext.append('.pdf')
  for e in ext:
      c1.SaveAs('./limitPlot_'+Tag+e)
