Question051 - 如何將 Microsoft Word 中的自動編號轉換成純文字 ?
=====
* ### Step 01: 開啟我們的好朋友 ```Microsoft Word```。
* ### Step 02: 在上方找到這個傢伙 -> ```搜尋 (Cmd + Ctrl + U)```。
* ### Step 03: 輸入 ```Visual Basic 編輯器``` 點下去。
* ### Step 04: 在左側的 Project 中找到 Microsoft Word 物件裡的 ```ThisDocument``` 並雙擊 (666)。
* ### Step 05: 輸入下方代碼。
    ```
    Sub ConvertAllAutoNumberToText()
        If ActiveDocument.Lists.Count > 0 Then
            Dim autoNumberList As List
            For Each autoNumberList In ActiveDocument.Lists
                autoNumberList.ConvertNumbersToText
            Next
        Else
        End If
    End Sub
    ```
* ### Step 06: 按下上方的執行鈕。
* ### Step 07: 搞定。
* ### 在最後一刻，如果被問到 ```以此格式儲存檔案將會移除 Visual Basic 巨集。您確定要使用這個檔案格式嗎?```，請勇敢按下 ```移除巨集並儲存```。
<br />
