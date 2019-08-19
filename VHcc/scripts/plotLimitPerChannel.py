#!/usr/bin/env python

import CombineHarvester.CombineTools.plotting as plot
import ROOT
import argparse
import json

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(ROOT.kTRUE)
plot.ModTDRStyle()
ROOT.gStyle.SetTickLength(0., "Y")

parser = argparse.ArgumentParser()
parser.add_argument('--input','-i',help = 'input json file')
parser.add_argument('--output','-o', help = 'Output filename')
parser.add_argument('--extralabel', default='',help = 'Additional CMS label')

args = parser.parse_args()

with open(args.input) as jsonfile:
  js = json.load(jsonfile)

canv = ROOT.TCanvas(args.output,args.output)
pads = plot.OnePad()
pads[0].SetTicks(1,-1)
pads[0].SetLeftMargin(0.25)
pads[0].SetTicky(0)

#axis = ROOT.TH2F('axis', '',1,-2,2,7,0,7)
axis = ROOT.TH2F('axis', '',1,0,170,7,0,7)
plot.Set(axis.GetYaxis(), LabelSize=0)
plot.Set(axis.GetXaxis(), Title = 'Best fit #mu')
axis.Draw()


cmb_band = ROOT.TBox()
plot.Set(cmb_band, FillColor=ROOT.kGreen)
#plot.DrawVerticalBand(pads[0],cmb_band,js['r']['val']-js['r']['ErrLo'],js['r']['val']+js['r']['ErrHi'])

cmb_line = ROOT.TLine()
plot.Set(cmb_line,LineWidth=2,LineColor=ROOT.kRed)
#plot.DrawVerticalLine(pads[0],cmb_line,js['r']['val'])

horizontal_line = ROOT.TLine()
plot.Set(horizontal_line,LineWidth=2,LineStyle=2)
plot.DrawHorizontalLine(pads[0],horizontal_line,1.5)


gr2sigma = ROOT.TGraphAsymmErrors(5)
plot.Set(gr2sigma, LineWidth=20, LineColor=ROOT.kOrange)

gr1sigma = ROOT.TGraphAsymmErrors(5)
plot.Set(gr1sigma, LineWidth=20, LineColor=ROOT.kGreen+1)

y_pos = 4.5
#x_text = -3.0
x_text = -50
i=0
latex = ROOT.TLatex()
plot.Set(latex, TextAlign=12,TextSize=0.03)
latex.SetTextFont(62)
order = ['0L','1L','2L','cmb']
txt_dict = {
  '0L': '#splitline{0L}{#splitline{Exp.=%.0f#timesSM}{Obs.=%.0f#timesSM}}'%(js['0L']['Limit'],js['0L']['Observed']),
  '1L': '#splitline{1L}{#splitline{Exp.=%.0f#timesSM}{Obs.=%.0f#timesSM}}'%(js['1L']['Limit'],js['1L']['Observed']),
  '2L': '#splitline{2L}{#splitline{Exp.=%.0f#timesSM}{Obs.=%.0f#timesSM}}'%(js['2L']['Limit'],js['2L']['Observed']),
  'cmb':'#splitline{Combination}{#splitline{Exp.=%.0f#timesSM}{Obs.=%.0f#timesSM}}'%(js['cmb']['Limit'],js['cmb']['Observed'])
}

for stre in order:
  gr2sigma.SetPoint(i,js[stre]['Limit'],y_pos)
  gr2sigma.SetPointError(i,js[stre]['Limit']-js[stre]['TwoSigmaDown'],js[stre]['TwoSigmaUp']-js[stre]['Limit'],0,0)
  gr1sigma.SetPoint(i,js[stre]['Limit'],y_pos)
  gr1sigma.SetPointError(i,js[stre]['Limit']-js[stre]['OneSigmaDown'],js[stre]['OneSigmaUp']-js[stre]['Limit'],0,0)
  latex.DrawLatex(x_text,y_pos,txt_dict[stre])

  i+=1
  y_pos -= 1.15

gr2sigma.Draw("SAME EP")
gr1sigma.Draw("SAME EP")

pads[0].cd()
pads[0].GetFrame().Draw()
pads[0].RedrawAxis()

plot.DrawCMSLogo(pads[0],'CMS','%s'%args.extralabel,11,0.045,0.03,1.0,'',1.0)
#plot.DrawTitle(pads[0],'41.3 fb^{-1} (13 TeV)',3)
plot.DrawTitle(pads[0],'39,6 fb^{-1} (13 TeV)',3)

latex.SetTextFont(52)
latex.SetTextSize(0.04)
latex.SetTextColor(4)
#latex.DrawLatex(-0.82,6.1,"pp#rightarrow VH; H#rightarrow b#bar{b}")
#latex.DrawLatex(-0.82,5.7,"Combined #mu=%.1f#pm%.1f"%(js['r']['val'],js['r']['ErrHi']))
#latex.DrawLatex(-1.82,5.6,"pp#rightarrow VH; H#rightarrow b#bar{b}")
latex.DrawLatex(5,6.0,"pp#rightarrow VH(H#rightarrow c#bar{c})")
#latex.DrawLatex(5,5.6,"95% C.L. Exclusion Limits")

legend = plot.PositionedLegend(0.25,0.25,3,0.02,0.025)
#plot.Set(legend, NColumns=2)
legend.SetTextFont(52)
legend.SetTextSize(0.027)
legend.SetFillColor(0)
legend.SetHeader("95% CL upper limits")
legend.AddEntry(gr1sigma,"68% expected","l")
legend.AddEntry(gr2sigma,"95% expected","l")
legend.Draw("same")

#Luca latex.DrawLatex(-1.82,5.2,"#mu=%.2f#pm%.2f(stat.)#pm%.2f(syst.)"%(js['r']['val'],(js['r']['StatHi']+js['r']['StatLo'])/2.,(js['r']['SystHi']+js['r']['SystLo'])/2.))
#latex.DrawLatex(-69,5.2,"#mu=%.2f#pm%.2f(stat.+syst.)"%(js['r']['val'],(js['r']['ErrHi']+js['r']['ErrLo'])/2.))

canv.Print('.png')
canv.Print('.pdf')
