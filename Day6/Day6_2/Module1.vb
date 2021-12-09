Imports System.IO
Module Module1

    Sub Main()
        Dim fileName As String = "day6.txt"
        Dim line As String
        Dim nums As New List(Of Integer)
        Using reader As New StreamReader(fileName) 'get puzzle input
            Do Until reader.EndOfStream
                line = reader.ReadLine()
                For i = 0 To line.Length - 1
                    If line(i) <> "," Then
                        nums.Add(Int(line(i).ToString))
                    End If
                Next
            Loop
        End Using
        Dim groups(8) As ULong
        For i = 0 To nums.Count - 1
            groups(nums(i)) += 1
        Next
        Dim temp As ULong
        For i = 0 To 255
            temp = groups(0)
            For j = 0 To 7
                groups(j) = groups(j + 1)

            Next
            groups(6) += temp
            groups(8) = temp
        Next
        Dim count As ULong
        For i = 0 To 8
            count += groups(i)
        Next
        Console.WriteLine(count)
        Console.ReadKey()
    End Sub

End Module
