#RequireAdmin
#include <File.au3>
AutoItSetOption("MustDeclareVars",1)

while 1>0
   WinWait("Confirm file replace")  ;可能弹出一个
   If WinExists("Confirm file replace") Then
	  ControlClick("Confirm file replace","","[CLASS:Button;INSTANCE:2]")
   EndIf
WEnd