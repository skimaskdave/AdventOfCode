Imports System.IO
Module Module1

    Sub Main()
        Dim count As Integer
        Dim fileName As String = "day1.txt"
        Dim lines As New List(Of Integer)
        Dim line As Integer
        Using reader As StreamReader = New StreamReader(fileName)
            Do Until reader.EndOfStream
                line = reader.ReadLine()
                lines.Add(line)
            Loop
        End Using

        For i = 3 To lines.Count - 1
            If lines(i - 3) + lines(i - 2) + lines(i - 1) < lines(i - 2) + lines(i - 1) + lines(i) Then
                count += 1
            End If
        Next
        Console.WriteLine(count)
        Console.ReadKey()
    End Sub

End Module
