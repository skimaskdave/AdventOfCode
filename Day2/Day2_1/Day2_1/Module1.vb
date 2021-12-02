Imports System.IO
Module Module1

    Sub Main()
        Dim fileName As String = "day2.txt"
        Dim line As String
        Dim lines As New List(Of String)
        Dim depth, pos As Integer
        Using reader As StreamReader = New StreamReader(fileName)
            Do Until reader.EndOfStream
                line = reader.ReadLine()
                lines.Add(line)
            Loop
        End Using
        For i = 0 To lines.Count - 1
            Dim split() As String = lines(i).Split(" ")
            If split(0) = "forward" Then
                pos += Int(split(1))
            ElseIf split(0) = "up" Then
                depth -= Int(split(1))
            ElseIf split(0) = "down" Then
                depth += Int(split(1))
            End If
        Next
        Console.WriteLine(depth * pos)
        Console.ReadKey()
    End Sub

End Module
