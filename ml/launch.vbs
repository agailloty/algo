Dim fso: set fso = CreateObject("Scripting.FileSystemObject")
Dim path: path = fso.GetAbsolutePathName(".")
dim python_exe = path 
Dim script_python: script_python = "app.py"
Dim shell: set shell = WScript.CreateObject("Wscript.Shell")
Msgbox path
shell.run path & "\" & script_python

oShell.run currentCommand,1,True