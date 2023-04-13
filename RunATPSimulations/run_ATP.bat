@echo off
:: ####################################################
:: Move to ATPMINGW folder
:: ####################################################

C:
CD C:\ATP\atpmingw

:: ####################################################
:: Set variables
:: ####################################################

set arg1=%1

C:\ATP\atpmingw\tpbig.exe disk %arg1% s -r

echo ###########################################
echo ##			Envoila 
echo ##	Finish running simulation for :
echo ##	%arg1%
echo ###########################################
::pause