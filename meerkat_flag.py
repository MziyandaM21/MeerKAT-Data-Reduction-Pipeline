
#split(vis='/data/sarao/1530331251_sdp_l0.full_1284.full_pol.ms',datacolumn='data',outputvis='el_gordo.ms')
msfile='el_gordo.ms'

flagdata(vis=msfile,mode='unflag',field='0~2')
flagdata(vis=msfile,mode='manualflag',autocorr=True)

flagdata(vis=msfile,mode='manual',field='0~2',spw='0:0~164;379~496')
flagdata(vis=msfile,mode='manual',field='0~2',spw='0:3645~3690')

#flagdata(vis=msfile,mode='manual',field='1',scan='2',timerange='2018/06/30/04:11:30.644')


flagdata(vis=msfile,mode='manual',field='0~2',spw='0:1337~2140;1100~1140')
flagdata(vis=msfile,mode='manual',field='0~2',spw='0:2504~2521')
flagdata(vis=msfile,mode='manual',field='0~2',spw='0:3683~3685')
flagdata(vis=msfile,mode='manual',field='0~2',spw='0:2967~3613')
flagdata(vis=msfile,mode='manual',field='0~2',spw='0:3896~4095')

print('Quacking')
flagdata(vis=msfile, mode='quack', field='0~2',quackinterval=5.0, quackmode='beg', flagbackup=False)
print('TFCrop')

flagdata(vis=msfile, mode='clip', field='0~2',
	clipzeros=True, flagbackup=False,clipminmax=[0.0,60.0])

flagdata(vis=msfile, mode= 'tfcrop',field='0',
	correlation='XX,YY',datacolumn='data',
	action='apply',flagbackup=False,
	freqcutoff=5,timecutoff=5)

flagdata(vis=msfile, mode= 'tfcrop',field='0',
        correlation='XY,YX',datacolumn='data',
        action='apply',flagbackup=False,
        freqcutoff=5,timecutoff=5)

flagdata(vis=msfile, mode= 'tfcrop',field='1',
        correlation='XX,YY',datacolumn='data',
        action='apply',flagbackup=False,
        freqcutoff=5,timecutoff=5)

flagdata(vis=msfile, mode= 'tfcrop',field='1',
        correlation='XY,YX',datacolumn='data',
        action='apply',flagbackup=False,
        freqcutoff=5,timecutoff=5)

flagdata(vis=msfile, mode= 'tfcrop',field='2',
        correlation='XX,YY',datacolumn='data',
        action='apply',flagbackup=False,
        freqcutoff=5,timecutoff=5)

flagdata(vis=msfile, mode= 'tfcrop',field='2',
        correlation='XY,YX',datacolumn='data',
        action='apply',flagbackup=False,
        freqcutoff=5,timecutoff=5)

