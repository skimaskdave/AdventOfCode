Imports System.IO
Module Module1

    Sub Main()
        Dim fileName As String = "day6.txt"
        Dim line As String
        Dim lines As New List(Of String)
        Dim nums As New List(Of Integer)
        Using reader As New StreamReader(fileName) 'get puzzle input
            Do Until reader.EndOfStream
                line = reader.ReadLine()
                For i = 0 To line.Length - 1
                    If line(i) <> "," Then
                        nums.Add(Int(line(i).ToString))
                    End If
                Next
                lines.Add(line)
            Loop
        End Using

        For i = 0 To 79
            For j = 0 To nums.Count - 1
                If nums(j) > 0 Then
                    nums(j) -= 1
                Else
                    nums(j) = 6
                    nums.Add(8)
                End If
            Next
        Next

        Console.WriteLine(nums.Count)
        Console.ReadKey()
    End Sub

End Module
