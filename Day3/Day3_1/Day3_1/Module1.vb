Imports System.IO
Module Module1

    Sub Main()
        Dim gamma, epsilon As String
        gamma = ""
        epsilon = ""
        Dim one, zero, gammaAns, epsilonAns As Integer
        Dim fileName As String = "day3.txt"
        Dim line As String
        Dim lines As New List(Of String)
        Using reader As New StreamReader(fileName) 'get puzzle input
            Do Until reader.EndOfStream
                line = reader.ReadLine()
                lines.Add(line)
            Loop
        End Using
        For i = 0 To 11 'for each bit find whether 1 or 0 is more common
            one = 0
            zero = 0
            For j = 0 To lines.Count - 1
                If lines(j)(i) = "1" Then
                    one += 1
                Else
                    zero += 1
                End If
            Next
            If one > zero Then 'make the binary string
                gamma += "1"
                epsilon += "0"
            Else
                gamma += "0"
                epsilon += "1"
            End If
        Next
        Console.WriteLine(gamma & " " & epsilon) 'print binary numbers (so I can physically check what they come out too)
        epsilonAns = BinaryToDecimal(epsilon) 'get decimal numbers
        gammaAns = BinaryToDecimal(gamma)

        Console.WriteLine(epsilonAns * gammaAns) 'print answer
        Console.ReadKey()
    End Sub

    Public Function BinaryToDecimal(ByVal Binary As String) As Long
        Dim n As Long
        Dim s As Integer

        For s = 1 To Len(Binary)
            n += (Mid(Binary, Len(Binary) - s + 1, 1) * (2 ^
                (s - 1)))
        Next s

        BinaryToDecimal = n
    End Function


End Module
