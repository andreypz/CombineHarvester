import os

CHN_DICT_SR = {
    "Wen": [
        ["vhcc_Wen_9_13TeV2016","1-lepton (e), W+c#bar{c}",-0.4,1.],
        ["vhcc_Wen_7_13TeV2016","1-lepton (e), t#bar{t}",-0.4,1.],
        ["vhcc_Wen_5_13TeV2016","1-lepton (e), W+b#bar{b}",-0.4,1.],
        ["vhcc_Wen_3_13TeV2016","1-lepton (e), W+udcsg",-0.4,1.]
        ],
    
    "Wmn": [
        ["vhcc_Wmn_9_13TeV2016","1-lepton (#mu), W+c#bar{c}",-0.4,1.],
        ["vhcc_Wmn_7_13TeV2016","1-lepton (#mu), t#bar{t}",-0.4,1.],
        ["vhcc_Wmn_5_13TeV2016","1-lepton (#mu), W+b#bar{b}",-0.4,1.],
        ["vhcc_Wmn_3_13TeV2016","1-lepton (#mu), W+udcsg",-0.4,1.]
        ],

    "Zee": [
        ["vhcc_Zee_3_13TeV2016","2-lepton (e), High V-p_{T}, Z+udcsg",-0.4,1.],
        ["vhcc_Zee_5_13TeV2016","2-lepton (e), High V-p_{T}, Z+b#bar{b}",-0.4,1.],
        ["vhcc_Zee_7_13TeV2016","2-lepton (e), High V-p_{T}, t#bar{t}",-0.4,1.],
        ["vhcc_Zee_9_13TeV2016","2-lepton (e), High V-p_{T}, Z+c#bar{c}",-0.4,1.],
        ["vhcc_Zee_4_13TeV2016","2-lepton (e), Low V-p_{T}, Z+udcsg",-0.4,1.],
        ["vhcc_Zee_6_13TeV2016","2-lepton (e), Low V-p_{T}, Z+b#bar{b}",-0.4,1.],
        ["vhcc_Zee_8_13TeV2016","2-lepton (e), Low V-p_{T}, t#bar{t}",-0.4,1.],
        ["vhcc_Zee_10_13TeV2016","2-lepton (e), Low V-p_{T}, Z+c#bar{c}",-0.4,1.]
        ],

    "Zmm": [
        ["vhcc_Zmm_3_13TeV2016","2-lepton (#mu), High V-p_{T}, Z+udcsg",-0.4,1.],
        ["vhcc_Zmm_5_13TeV2016","2-lepton (#mu), High V-p_{T}, Z+b#bar{b}",-0.4,1.],
        ["vhcc_Zmm_7_13TeV2016","2-lepton (#mu), High V-p_{T}, t#bar{t}",-0.4,1.],
        ["vhcc_Zmm_9_13TeV2016","2-lepton (#mu), High V-p_{T}, Z+c#bar{c}",-0.4,1.],
        ["vhcc_Zmm_4_13TeV2016","2-lepton (#mu), Low V-p_{T}, Z+udcsg",-0.4,1.],
        ["vhcc_Zmm_6_13TeV2016","2-lepton (#mu), Low V-p_{T}, Z+b#bar{b}",-0.4,1.],
        ["vhcc_Zmm_8_13TeV2016","2-lepton (#mu), Low V-p_{T}, t#bar{t}",-0.4,1.],
        ["vhcc_Zmm_10_13TeV2016","2-lepton (#mu), Low V-p_{T}, Z+c#bar{c}",-0.4,1.]
        ],

    "Znn": [
        ["vhcc_Znn_3_13TeV2016","0-lepton, Z+udcsg",-0.4,1.],
        ["vhcc_Znn_5_13TeV2016","0-lepton, Z+b#bar{b}",-0.4,1.],
        ["vhcc_Znn_7_13TeV2016","0-lepton, t#bar{t}",-0.4,1.],
        ["vhcc_Znn_9_13TeV2016","0-lepton, Z+c#bar{c}",-0.4,1.],
        ["vhcc_Wen_3_13TeV2016","1-lepton (e), W+udcsg",-0.4,1.],
        ["vhcc_Wen_5_13TeV2016","1-lepton (e), W+b#bar{b}",-0.4,1.],
        ["vhcc_Wen_7_13TeV2016","1-lepton (e), t#bar{t}",-0.4,1.],
        ["vhcc_Wen_9_13TeV2016","1-lepton (e), W+c#bar{c}",-0.4,1.],
        ["vhcc_Wmn_3_13TeV2016","1-lepton (#mu), W+udcsg",-0.4,1.],
        ["vhcc_Wmn_5_13TeV2016","1-lepton (#mu), W+b#bar{b}",-0.4,1.],
        ["vhcc_Wmn_7_13TeV2016","1-lepton (#mu), t#bar{t}",-0.4,1.],
        ["vhcc_Wmn_9_13TeV2016","1-lepton (#mu), W+c#bar{c}",-0.4,1.]
        ]
}


for MODE in ['prefit','postfit']:
#for MODE in ['prefit']:
    for CHN in ['Zee','Zmm','Wen','Wmn','Znn']:
    #for CHN in ['Zee']:
    #for CHN in ['Znn']:
        for i in range(0,len(CHN_DICT_SR[CHN])):
              LABEL = "%s" % CHN_DICT_SR[CHN][i][1]
              OUTNAME = "%s" % CHN_DICT_SR[CHN][i][0]
              XLOW = CHN_DICT_SR[CHN][i][2]
              XHIGH = CHN_DICT_SR[CHN][i][3]
              os.system(('./scripts/postFitPlot_vhcc.py' \
                  ' --file=shapes_VHincl_15May.root --ratio --extra_pad=0.53 --file_dir=%(OUTNAME)s --no_signal' \
                  ' --ratio_range 0.4,1.6 --empty_bin_error --channel=%(CHN)s --cr ' \
                  ' --outname %(OUTNAME)s --mode %(MODE)s --x_title="c-Tagger_{min}" --lumi="35.9 fb^{-1} (13 TeV)"'\
                  ' --x_axis_min %(XLOW)f --x_axis_max %(XHIGH)f --custom_x_range '\
                  ' --channel_label "%(LABEL)s"' % vars()))

#Luca for MODE in ['prefit','postfit']:
#Luca     for CHN in ['Wen','Wmn','Zee','Zmm','Znn']:
#Luca         for i in range(0,len(CHN_DICT_SR[CHN])):
#Luca               LABEL = "%s" % CHN_DICT_SR[CHN][i][1]
#Luca               OUTNAME = "%s" % CHN_DICT_SR[CHN][i][0]
#Luca               XLOW = CHN_DICT_SR[CHN][i][2]
#Luca               XHIGH = CHN_DICT_SR[CHN][i][3]
#Luca               os.system(('./scripts/postFitPlot.py' \
#Luca                   ' --file=shapes.root --ratio --extra_pad=0.53 --file_dir=%(OUTNAME)s --no_signal ' \
#Luca                   ' --ratio_range 0.4,1.6 --empty_bin_error --channel=%(CHN)s --cr ' \
#Luca                   ' --outname %(OUTNAME)s --mode %(MODE)s --x_title="CMVA_{min}" --lumi="35.9 fb^{-1} (13 TeV)" '\
#Luca                   ' --x_axis_min %(XLOW)f --x_axis_max %(XHIGH)f --custom_x_range '\
#Luca                   ' --channel_label "%(LABEL)s"' % vars()))
#Luca 
