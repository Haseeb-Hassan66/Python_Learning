# Student Performance Analyzer

A basic Python project that stores student marks in a file and generates
a performance report with averages, grades, and the top student.

------------------------------------------------------------------------

## Features

-   Add new student records
-   Avoid duplicate entries
-   Store data in a text file
-   Calculate averages
-   Assign grades automatically
-   Show full report with topper

------------------------------------------------------------------------

## Data Format (`students.txt`)

Ali,78,82,90
Sara,88,91,85,79

Format:
Name,Mark1,Mark2,...

------------------------------------------------------------------------

## Menu

1.  Insert New Record
2.  View Overall Report
3.  Exit

------------------------------------------------------------------------

## Main Functions

-   add_student() → Add student data
-   load_students() → Read file records
-   compute_avg() → Calculate average
-   assign_grade() → Give grade
-   find_topper() → Find highest scorer
-   print_report() → Show report

------------------------------------------------------------------------

## Grading System

  Average   Grade
  --------- -------
  90+       A
  80--89    B
  70--79    C
  60--69    D
  <60       F

------------------------------------------------------------------------

## How to Run

python main.py

------------------------------------------------------------------------

## Concepts Used

Functions, loops, lists, dictionaries, file handling, conditions,
exception handling.
