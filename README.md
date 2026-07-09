# Python_Tutorial

A beginner-friendly collection of small Python lessons. Each numbered file focuses on one core topic and can be run on its own.

## Original lessons

| Lesson | File | Topic |
| --- | --- | --- |
| 1 | `1HelloWorld.py` | Printing, comments, and basic input |
| 2 | `2Variables.py` | Variables, data types, assignment, and scope |
| 3 | `3Math.py` | Arithmetic, built-in math helpers, and randomness |
| 4 | `4Strings.py` | String indexing, slicing, formatting, and methods |
| 5 | `5Conditionals.py` | Boolean comparisons and `if`/`else` statements |
| 6 | `6Loops.py` | `while` loops and loop control variables |
| 7 | `7Lists.py` | Lists, indexing, slicing, and updating values |
| 8 | `8Functions.py` | Defining and calling functions |
| 9 | `9Tuples.py` | Tuple creation and immutability |
| 10 | `10Dictionaries.py` | Dictionaries, key/value access, and looping over data |
| 11 | `11FileIO.py` | Reading and writing text files with `pathlib` |
| 12 | `12Classes.py` | Classes, objects, attributes, and methods |
| 13 | `13Modules.py` | Importing standard library modules and helper functions |
| 14 | `14Exceptions.py` | Handling runtime errors with `try`/`except` |
| 15 | `15Comprehensions.py` | Building lists and dictionaries with comprehensions |

## Beginner folder

The `beginner/` folder adds Python-level topics that should come before data structures and algorithms. Files use zero-padded lesson numbers so GitHub displays them in order.

| Lesson | File | Topic |
| --- | --- | --- |
| 01 | `beginner/01_sets.py` | Sets, uniqueness, membership, and set operations |
| 02 | `beginner/02_classes_oop.py` | Classes, objects, attributes, methods, and simple OOP |
| 03 | `beginner/03_sorting.py` | Built-in sorting with `sorted()` and `.sort()` |

## Intermediate folder

The `intermediate/` folder adds classic data structures and algorithms in dependency order.

| Lesson | File | Topic |
| --- | --- | --- |
| 01 | `intermediate/01_linked_lists.py` | Nodes and linked lists |
| 02 | `intermediate/02_insertion_sort.py` | Insertion sort |
| 03 | `intermediate/03_merge_sort.py` | Merge sort |
| 04 | `intermediate/04_quick_sort.py` | Quick sort |
| 05 | `intermediate/05_radix_sort.py` | Radix sort for non-negative integers |
| 06 | `intermediate/06_binary_trees.py` | Binary search trees and traversal |
| 07 | `intermediate/07_avl_trees.py` | Self-balancing AVL trees |
| 08 | `intermediate/08_dijkstra.py` | Shortest paths with Dijkstra's algorithm |

## Running a lesson

Use Python 3 from the project directory:

```bash
python 10Dictionaries.py
python beginner/01_sets.py
python intermediate/08_dijkstra.py
```

Some lessons print sample output immediately. Lesson 1 asks for keyboard input so learners can practice working with user-provided text.

## Suggested learning path

1. Run the original files in number order.
2. Run the `beginner/` folder lessons in order.
3. Run the `intermediate/` folder lessons in order.
4. Change one or two values in each file and run it again.
5. Add your own examples below the existing code.
6. Try combining concepts, such as sorting a list of objects or storing tree nodes in a class.
7. Use `EXERCISES.md` for extra practice prompts after each topic.
8. Check `ROADMAP.md` for recommended topics to add next.
