Imports System.IO
Module Module1

    Sub Main()
        Dim fileName As String = "day7.txt"
        Dim line As String
        Dim lines As New List(Of String)
        Using reader As New StreamReader(fileName) 'get puzzle input
            Do Until reader.EndOfStream
                line = reader.ReadLine()
                lines.Add(line)
            Loop
        End Using

        Dim tempFuel As Long = 0
        Dim totalfuel As Long = 1000000000
        Dim newLine() As String = lines(0).Split(",")
        Dim steps As Integer
        For i = 0 To 1000
            For j = 0 To newLine.Count - 1
                tempFuel += Math.Abs(newLine(j) - i)
                steps = Math.Abs(newLine(j) - i)
                For x = 0 To steps - 1
                    tempFuel += x
                Next
            Next
            If tempFuel < totalfuel Then
                totalfuel = tempFuel
            End If
            tempFuel = 0
        Next

        Console.WriteLine(totalfuel)
        Console.ReadKey()
    End Sub

End Module
