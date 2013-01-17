;���طֱ�����

#RequireAdmin
#include <File.au3>
AutoItSetOption("MustDeclareVars",1)
main()

Func main()
   Dim $dataPath="D:\data\���ڹ�Ʊ�շֱ�����"
   Dim $jztPath="D:\Weisoft Stock"
   Dim $loadStartYear=2012 ;��ʼ��
   Dim $loadStartMonth=2  ;��ʼ�·�
   Dim $howManyMonth=11 ;���ض��ٸ���
   Dim $monthIndex=$loadStartMonth
   Dim $month
   Dim $year
   FileChangeDir($jztPath)
   For $i = 1 to $howManyMonth
	  if $monthIndex > 12 Then
		 $year=$loadStartYear + Floor($monthIndex/12)
		 $month=Mod($monthIndex/12)
	  Else
		 $year=$loadStartYear
		 $month=$monthIndex
	  EndIf
	 
	  Local $monthPath=$dataPath & "\" & String($year)&"��"& String($month) & "��"

	  If FileExists($monthPath)>0 Then  ;���  xxxx��xx��  ���Ŀ¼���ڣ��ͽ��벢���أ�����������Ŀ¼�����֣����Ա����´μ���
		 Local $dayFolders = _FileListToArray($monthPath,"*",2)
		 
		 If @error <> 4 Then  ;4 means no files found
			For $j =1 To $dayFolders[0]
			   Local $dayFolderName = $dayFolders[$j]
			   
			   if StringInStr($dayFolderName,"loaded")=0 Then
				  RunWait(@ComSpec & ' /C copy /Y "' & $monthPath & '\' & $dayFolderName & '\data.exe" "' & $jztPath & '"'); copy data.exe
				  Dim $pid = Run($jztPath & '\data.exe')
				  WinWait("WinRAR")  ;show winrar window
				  If WinExists("WinRAR") Then
					 ControlClick("WinRAR","","[CLASS:Button;INSTANCE:2]")
				  EndIf
				  
				  ProcessWaitClose($pid)
				  
				  FileDelete($monthPath & '\' & $dayFolderName & '\data.exe') ;delete the data.exe file
				  DirMove($monthPath & '\' & $dayFolderName, $monthPath & '\' & $dayFolderName & "_loaded")  ;mark folder as loaded
			   EndIf
			   
			Next; one day finished to next
			
			
		 EndIf
		 ;now this month finished, rename it
		 DirMove($monthPath , $monthPath & "_loaded")
	  EndIf
	  
	  
	  
	  $monthIndex=$monthIndex+1
	  
	  
   Next
   
   
   
   
EndFunc
