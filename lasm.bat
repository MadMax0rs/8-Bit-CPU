@echo off

IF "%~1"=="" (
	ECHO Syntax:
	ECHO lasm.bat ^<script name^>
	GOTO :End
)

python .\assembler\lasm.py /docs/examples/%1/%1.asm

:End