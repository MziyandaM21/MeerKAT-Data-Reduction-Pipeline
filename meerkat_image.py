field_0='/data/mziyanda/sarao/field_0/'
field_1='/data/mziyanda/sarao/field_1/'
field_2='/data/mziyanda/sarao/field_2/'
target='/data/mziyanda/sarao/target/'
msfile='el_gordo'


applycal(vis=msfile+'.ms',field='3',
        gaintable=[field_1+msfile+'.B0',
        field_1+msfile+'.fluxscale1',
        field_1+msfile+'.K0'],
        gainfield=['','J0024-4202',''],interp=['','linear',''],
        parang=False,calwt=False,applymode='calflag')

tclean(vis=msfile+'.ms',field='3',specmode='mfs',
	deconvolver='mtmfs',threshold='0mJy',
	gridder='wproject',imsize=[3888],nterms=2,
	cell=['4arcsec'],wprojplanes=-1,width=200,
	weighting='briggs',niter=0,interactive=False,
	imagename=target+'ElGordo-I-clean-mask-full',
	robust=0.8,pblimit=-0.01,pbcor=False,
	usemask='auto-multithresh',sidelobethreshold=2.0,
	noisethreshold=4.25,lownoisethreshold=1.5,
	minbeamfrac=0.3,growiterations=75,
	negativethreshold=15.0,verbose=True)

tclean(vis=msfile+'.ms',field='3',scan='4',antenna='m003',
	specmode='mfs',deconvolver='mtmfs',gridder='wproject',
	imsize=[2700],cell=['4arcsec'],weighting='briggs',
	threshold='0Jy',niter=1000,interactive=False,pbcor=True,
	imagename=target+'el_gordo-I-m003',robust=0.5,wprojplanes=-1)


tclean(vis=msfile+'.ms',field='3',scan='4',antenna='m003',
        specmode='mfs',deconvolver='hogbom',gridder='widefield',
        imsize=[2700],cell=['4arcsec'],weighting='briggs',
        threshold='0Jy',niter=100000,interactive=False,
        imagename=target+'el_gordo_masking',robust=0.5,wprojplanes=-1,
        usemask='auto-multithresh',sidelobethreshold=2.0,noisethreshold=4.25,
        lownoisethreshold=1.5,minbeamfrac=0.3,growiterations=75,
        negativethreshold=15.0,verbose=True)
