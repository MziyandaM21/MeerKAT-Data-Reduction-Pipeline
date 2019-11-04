# MeerKAT-Data-Reduction-Pipeline
For flaggin known FRI bands and autoflagging, Standard Interferometry Calibration and Imaging
The flagger deals with Radio Frequency Inteference (RFI). The flagdata commands manually removes the frequency channels that are highly affected by RFI. This is about 45% of the original observations. The flagdata commands can be mofified to suit any measurement set. The reference antenna also used here can be changed. These frequncy range can be obtained online and the known RFI bands: 944-947MHz, 1160-1310MHz, 1476-1611MHz, 1670-1700MHz

The next step involves automatic flagging, a stage whereby we invoke casa's clip and tfcrop modes to remove data according to given thresholds. This is done for all correlations individually to avoid averaging through correlations for different sources. The RFI is reletively the same through out the scans, however the obseravations done to test this pipeline had time-dependent RFI which at this point has not been identified.

The calibrations procedure follows the standard inteferometry calibration that is available on the NRAO website. The site contains various calibration and imaging tutorials for continuum and spectral line imaging.

