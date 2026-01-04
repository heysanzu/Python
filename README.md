## First Python program
Print 'Hello, World!' to console.
```python
print("Hello, World!")
print("I'm Sanzu")
```
**Output:**
```bash
Hello, World!
I'm Sanzu
```
## Circle
A simple Python program that calculates the area and circumference of a circle.
- Area: π × r²
- Circumference: 2 × π × r
```python
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
```
**Enter the radius when prompted:**
```bash
Enter radius: 5
Area of Circle: 78.5
Circumference of Circle: 31.4
```
## Pyramid
Prints a star pyramid pattern based on user input.
```   
    *
   ***
  *****
 *******
*********
```

**How it works:**

1. Loop through each row from 1 to `rows`
2. Calculate spaces: `rows - i` (decreases each row)
3. Calculate stars: `2 * i - 1` (odd numbers: 1, 3, 5, 7...)
4. Print spaces and stars using string multiplication

**Example trace for 5 rows:**
```
Row 1: spaces=4, stars=1  →     *
Row 2: spaces=3, stars=3  →    ***
Row 3: spaces=2, stars=5  →   *****
Row 4: spaces=1, stars=7  →  *******
Row 5: spaces=0, stars=9  → *********
```
## Triangle
A simple Python program that calculates the area of a triangle based on user input.

**Run the program:**
```python
python areaTriangle.py
```
Enter the base and height when prompted:
```bash
Enter height: 10
Enter base: 5
-------------------------
Area of Triangle: 25.0
```

**Requirements:**
- Python 3.x

**Formula:**
The program uses the standard triangle area formula.
```bash
Area = ½ × base × height
```
## Power Calculator
A simple Python program that calculates the power of a number. This program takes two inputs from the user (base and exponent) and calculates the result of base raised to the power of exponent using Python's exponentiation operator (`**`).

Enter the base and exponent when prompted:
```
Enter the base number: 2
Enter the exponent: 8
-------------------------

2^8 = 256
```

**Requirements:**
- Python 3.x

**How It Works:**
1. Prompts user for a `base` number
2. Prompts user for an `exponent`
3. Calculates `base^exponent`
4. Displays the result in a formatted output

---
Author: `@heysanzu`
