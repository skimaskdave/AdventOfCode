Imports System.IO
Module Module1

    Sub Main()
        Dim fileName As String = "day5.txt"
        Dim line As String
        Dim startCoords, endCoords As New List(Of String)
        Using reader As New StreamReader(fileName) 'get puzzle input
            Do Until reader.EndOfStream
                line = reader.ReadLine()
                Dim coords() As String = line.Split(" -> ")
                Dim newCoords As New List(Of String)
                For x = 0 To 2
                    If coords(x).Contains("->") <> True Then
                        newCoords.Add(coords(x))
                    End If
                Next
                startCoords.Add(newCoords(0))
                endCoords.Add(newCoords(1))
            Loop
        End Using
        Dim ventLines(1000, 1000) As Integer
        For i = 0 To startCoords.Count - 1
            Dim xyStart() As String = startCoords(i).Split(",")
            Dim xyEnd() As String = endCoords(i).Split(",")
            If Int(xyStart(0)) = Int(xyEnd(0)) Or Int(xyStart(1)) = Int(xyEnd(1)) Then
                If xyStart(0) <> xyEnd(0) Then
                    If Int(xyStart(0)) > Int(xyEnd(0)) Then
                        For row = Int(xyEnd(0)) To Int(xyStart(0))
                            ventLines(row, Int(xyStart(1))) += 1
                        Next
                    Else
                        For row = Int(xyStart(0)) To Int(xyEnd(0))
                            ventLines(row, Int(xyStart(1))) += 1
                        Next
                    End If
                Else
                    If Int(xyStart(1)) > Int(xyEnd(1)) Then
                        For col = Int(xyEnd(1)) To Int(xyStart(1))
                            ventLines(Int(xyStart(0)), col) += 1
                        Next
                    Else
                        For col = Int(xyStart(1)) To Int(xyEnd(1))
                            ventLines(Int(xyStart(0)), col) += 1
                        Next
                    End If
                End If
            ElseIf Math.Abs((xyStart(0)) - Int(xyEnd(0))) = Math.Abs(Int(xyStart(1)) - Int(xyEnd(1))) Then
                If Int(xyStart(0)) > Int(xyEnd(0)) And Int(xyStart(1)) > Int(xyEnd(1)) Then
                    For dia = 0 To Int(xyStart(0)) - Int(xyEnd(0))
                        ventLines(Int(xyStart(0)) - dia, Int(xyStart(1)) - dia) += 1
                    Next
                ElseIf Int(xyStart(0)) < Int(xyEnd(0)) And Int(xyStart(1)) > Int(xyEnd(1)) Then
                    For dia = 0 To Int(xyEnd(0)) - Int(xyStart(0))
                        ventLines(Int(xyStart(0)) + dia, Int(xyStart(1)) - dia) += 1
                    Next
                ElseIf Int(xyStart(0)) > Int(xyEnd(0)) And Int(xyStart(1)) < Int(xyEnd(1)) Then
                    For dia = 0 To Int(xyStart(0)) - Int(xyEnd(0))
                        ventLines(Int(xyStart(0)) - dia, Int(xyStart(1)) + dia) += 1
                    Next
                Else
                    For dia = 0 To Int(xyEnd(0)) - Int(xyStart(0))
                        ventLines(Int(xyStart(0)) + dia, Int(xyStart(1)) + dia) += 1
                    Next
                End If
            End If
        Next
        Dim count As Integer
        For i = 0 To 1000
            For j = 0 To 1000
                If ventLines(j, i) > 1 Then
                    count += 1
                End If
            Next
        Next
        Console.WriteLine(count)
        Console.ReadKey()
    End Sub

End Module
