# First Python program
- print("Hello, World!")
- print("I'm Sanzu")
```python
print("Hello, World!")
print("I'm Sanzu")
```
# Circle
A simple Python program that calculates the area and circumference of a circle
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
# Pyramid
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
