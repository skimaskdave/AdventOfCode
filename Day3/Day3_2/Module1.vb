Imports System.IO
Module Module1

    Sub Main()
        Dim oxygen, co2 As Integer
        Dim fileName As String = "day3.txt"
        Dim line As String
        Dim lines As New List(Of String)
        Using reader As New StreamReader(fileName) 'get puzzle input
            Do Until reader.EndOfStream
                line = reader.ReadLine()
                lines.Add(line)
            Loop
        End Using
        oxygen = BinaryToDecimal(FindOxygen(lines))
        co2 = BinaryToDecimal(FindCO2(lines))
        Console.WriteLine()
        Console.WriteLine(oxygen)
        Console.WriteLine(co2)
        Console.WriteLine(oxygen * co2)
        Console.ReadKey()
    End Sub

    Function FindOxygen(ByVal lines As List(Of String)) As String
        Console.WriteLine("oxygen")
        Dim onezero(1) As Integer 'num of ones = index 1, num of zeros = index 0
        Dim bits As String
        Dim newOxy As New List(Of String)
        Dim oxy As New List(Of String)
        For i = 0 To lines.Count - 1
            oxy.Add(lines(i))
        Next

        For i = 0 To 11
            bits = ""
            onezero(0) = 0
            onezero(1) = 0
            For x = 0 To oxy.Count - 1 'get all the bits for the column we want
                bits += oxy(x)(i)
                If bits(x) = "1" Then 'count number of each type
                    onezero(1) += 1
                Else
                    onezero(0) += 1
                End If
            Next

            If onezero(1) >= onezero(0) Then 'compare counts and remove ones we don't need from list
                For x = 0 To oxy.Count - 1
                    If oxy(x)(i) = "1" Then
                        newOxy.Add(oxy(x))
                    End If
                Next
            Else
                For x = 0 To oxy.Count - 1
                    If oxy(x)(i) = "0" Then
                        newOxy.Add(oxy(x))
                    End If
                Next
            End If
            oxy.Clear()
            For x = 0 To newOxy.Count - 1
                oxy.Add(newOxy(x))
            Next
            newOxy.Clear()
        Next

        If oxy(0)(oxy(0).Length - 1) = "1" Then
            Console.WriteLine(oxy(0))
            Return oxy(0)
        Else
            Console.WriteLine(oxy(1))
            Return oxy(1)
        End If
    End Function

    Function FindCO2(ByVal lines As List(Of String)) As String
        Console.WriteLine("co2")
        Dim onezero(1) As Integer 'num of ones = index 1, num of zeros = index 0
        Dim bits As String
        Dim newCO2 As New List(Of String)
        Dim co2 As New List(Of String)
        For i = 0 To lines.Count - 1
            co2.Add(lines(i))
        Next

        For i = 0 To 11
            If co2.Count = 1 Then
                Exit For
            End If
            bits = ""
            onezero(0) = 0
            onezero(1) = 0
            For x = 0 To co2.Count - 1 'get all the bits for the column we want
                bits += co2(x)(i)
                If bits(x) = "1" Then 'count number of each type
                    onezero(1) += 1
                Else
                    onezero(0) += 1
                End If
            Next

            If onezero(1) < onezero(0) Then 'compare counts and remove ones we don't need from list
                For x = 0 To co2.Count - 1
                    If co2(x)(i) = "1" Then
                        newCO2.Add(co2(x))
                    End If
                Next
            Else
                For x = 0 To co2.Count - 1
                    If co2(x)(i) = "0" Then
                        newCO2.Add(co2(x))
                    End If
                Next
            End If
            co2.Clear()
            For x = 0 To newCO2.Count - 1
                co2.Add(newCO2(x))
            Next
            newCO2.Clear()
        Next

        If co2(0)(co2(0).Length - 1) = "0" Then
            Console.WriteLine(co2(0))
            Return co2(0)
        Else
            Console.WriteLine(co2(1))
            Return co2(1)
        End If
    End Function

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
