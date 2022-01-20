Dim fso: set fso = CreateObject("Scripting.FileSystemObject")
Dim path: path = fso.GetAbsolutePathName(".")
dim python_exe : python_exe = path & "\algo\Scripts\python.exe "
Dim script_python: script_python = "script.py"
Dim shell: set shell = WScript.CreateObject("Wscript.Shell")
shell.run Chr(34) & python_exe & Chr(34) & script_python, 0