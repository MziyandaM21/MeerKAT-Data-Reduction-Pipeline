v_0 = '1.4GHz'
alpha = -1.2309337662992943
I= 15.19200487458442
beta = -0.40142548668427545    
gama = -0.4272505074440009
field_ = '/data/mziyanda/sarao/field_'
field_0 = '/data/mziyanda/sarao/field_0/'
field_1 = '/data/mziyanda/sarao/field_1/'
field_2 = '/data/mziyanda/sarao/field_2/'
msfile = 'el_gordo'
#clearcal(vis=msfile+'.ms',field='0~2')
fields = ['0','1']
field_n = ['1934-638','J0407-658']
'''
flagdata(vis=msfile,mode='manual',field='1',scan='2',timerange='2018/06/30/04:11:30.6444')

setjy(vis=msfile+'.ms',field='0',standard='Baars',usescratch=False,scalebychan=True)
setjy(vis=msfile+'.ms',field='1',standard='manual',fluxdensity=[I,0,0,0],spix=[alpha,beta],reffreq=v_0,usescratch=False,scalebychan=True)

	
gaincal(vis=msfile+'.ms', caltable=field_1+msfile+'.G0',
	field='1', refant='m003', spw='0:1.31~1.47GHz', calmode='p',
       	solint='int',minsnr=5,parang=True)


gaincal(vis=msfile+'.ms',caltable=field_1+msfile+'.K0',
	field='1',refant='m003',spw='0:300~3800',gaintype='K',
	solint='inf',combine='scan',minsnr=5,parang=True,
	gaintable=field_1+msfile+'.G0')

bandpass(vis=msfile+'.ms',caltable=field_1+msfile+'.B0',
	parang=True,field='1',refant='m003',combine='scan',
	solint='inf',bandtype='B',spw='0:300~3800',solnorm=True,
       	gaintable=[field_1+msfile+'.G0',field_1+msfile+'.K0'])


gaincal(vis=msfile+'.ms',caltable=field_1+msfile+'.G1',
	field='1',spw='0:300~3800',solint='2min',refant='m003',
	gaintype='G',calmode='ap',solnorm=False,
	gaintable=[field_1+msfile+'.K0',
	field_1+msfile+'.B0'],parang=True,
	interp=['linear','nearest'])

gaincal(vis=msfile+'.ms',caltable=field_1+msfile+'.G1',
        field='2',spw='0:300~3800',solint='2min',refant='m003',
        gaintype='G',calmode='ap',solnorm=False,
        gaintable=[field_1+msfile+'.K0',
	field_1+msfile+'.B0'],parang=True,
        append=True)

#pol

gaincal(vis=msfile+'.ms',caltable=field_1+msfile+'.Kcross',
	field='0',spw='0:300~3800',solint='inf',refant='m003',
	gaintype='KCROSS',parang=True,combine='scan',
	gaintable=[field_1+msfile+'.K0',field_1+msfile+'.B0',
	field_1+msfile+'.G1'],
	gainfield=['','','J0407-658']   )
'''
polcal(vis=msfile+'.ms',caltable=field_1+msfile+'.D0',
	refant='m003',field='0',spw='0:300~3800',
	gaintable=[field_1+msfile+'.K0',
        field_1+msfile+'.B0',
	field_1+msfile+'.G1',
	field_1+msfile+'.Kcross'],
	poltype='D',solint='inf',combine='scan',
	gainfield=['','','J0024-4202',''])
fluxscale(vis=msfile+'.ms',caltable=field_1+msfile+".G1",
	fluxtable=field_1+msfile+".fluxscale1",
	reference='J0407-658', 
        transfer='J0024-4202',
	incremental=False)

applycal(vis=msfile+'.ms',field='1',
	gaintable=[field_1+msfile+'.B0',
	field_1+msfile+'.fluxscale1',
	field_1+msfile+'.K0',
	field_1+msfile+'.Kcross',
	field_1+msfile+'.D0'],
	gainfield=['','J0407-658','','',''],
	interp=['','nearest','','',''],
	parang=True,calwt=False,applymode='calflag')


