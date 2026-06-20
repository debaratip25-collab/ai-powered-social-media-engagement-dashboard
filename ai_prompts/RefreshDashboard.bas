' ============================================================
' AI-Powered Social Media Engagement Dashboard
' Step 7: Automation & Refresh
' ============================================================
' Instructions:
' 1. Open the workbook in Excel (desktop version with macros enabled)
' 2. Press Alt+F11 to open the VBA editor
' 3. Insert > Module, then paste this code
' 4. Close the editor and save the file as .xlsm (macro-enabled)
' 5. Add a button (Insert > Shapes or Form Control) on the Dashboard
'    sheet and assign this macro to it
' ============================================================

Sub RefreshDashboard()
    Dim cn As WorkbookConnection
    For Each cn In ThisWorkbook.Connections
        cn.Refresh
    Next cn

    Dim ws As Worksheet, pt As PivotTable
    For Each ws In ThisWorkbook.Worksheets
        For Each pt In ws.PivotTables
            pt.RefreshTable
        Next pt
    Next ws

    Application.Calculate
    MsgBox "Dashboard Updated", vbInformation
End Sub
