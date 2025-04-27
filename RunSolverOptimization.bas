Sub RunSolverOptimization()

    ' Ensure Solver is installed
    If Not SolverOK("", "", 0, 0) Then
        MsgBox "Please enable the Solver Add-in: File > Options > Add-ins > Solver Add-in", vbExclamation
        Exit Sub
    End If

    SolverReset

    ' Set objective to maximize revenue in D39
    SolverOK SetCell:="$D$39", MaxMinVal:=1, ValueOf:=0, ByChange:="$C$2:$C$13"

    ' Query Constraints
    SolverAdd CellRef:="$F$2", Relation:=1, FormulaText:="15" ' Burger and Fries
    SolverAdd CellRef:="$F$3", Relation:=1, FormulaText:="20" ' Fast Food
    SolverAdd CellRef:="$F$4", Relation:=1, FormulaText:="10" ' Cheap Lunch

    ' Budget Constraints
    SolverAdd CellRef:="$F$6", Relation:=1, FormulaText:="10"  ' Burger King
    SolverAdd CellRef:="$F$7", Relation:=1, FormulaText:="50"  ' Wendy's

    ' Non-negativity
    SolverAdd CellRef:="$C$2:$C$13", Relation:=3, FormulaText:="0"

    ' Solve and keep solution
    SolverSolve UserFinish:=True
    SolverFinish KeepFinal:=1

    MsgBox "Solver has completed. Optimal solution is in C2:C13 and revenue is in D39.", vbInformation

End Sub