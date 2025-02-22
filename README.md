# Quine-McCluskey Minimization Tool (PyQt5)

This project is a graphical user interface (GUI) application that implements the **Quine-McCluskey algorithm** for minimizing Boolean expressions. The tool allows users to input minterms and calculates the minimized Boolean expression using a systematic tabulation method.

## Features

- **User-friendly GUI:** Built with PyQt5 for easy interaction.
- **Minimization of Boolean functions:** Uses the Quine-McCluskey method to simplify Boolean expressions.
- **Efficient prime implicant selection:** Identifies essential prime implicants using a prime implicant chart.
- **Real-time computation:** Displays minimized results instantly after input.

## Installation

To run the project, install the required dependencies:

```bash
pip install PyQt5
```

## Usage

1. Run the script:

   ```bash
   python quine_mccluskey.py
   ```

2. Enter the minterms in the input field, separated by commas (e.g., `0,1,2,5,6,7,8,9,10,14`).
3. Click the **"محاسبه کن"** button to compute the minimized Boolean expression.
4. The minimized expression is displayed in the output box.

## Algorithm Overview

The **Quine-McCluskey** algorithm consists of the following steps:

1. **Grouping Minterms**  
   - Converts decimal minterms to binary.
   - Groups them based on the number of `1`s in their binary representation.

2. **Finding Prime Implicants**  
   - Compares adjacent groups and merges terms with a one-bit difference.
   - Marks unmerged terms as **prime implicants**.

3. **Constructing a Prime Implicant Chart**  
   - Maps minterms to their covering prime implicants.

4. **Selecting Essential Prime Implicants**  
   - Identifies prime implicants that cover unique minterms.
   - Iteratively reduces the solution set.

## Example

**Input:**  
Minterms: `0, 1, 2, 5, 6, 7, 8, 9, 10, 14`

**Output:**  
Minimized Expression: `--01, 1-0-`

## File Structure

```
├── quine_mccluskey.py  # Main script with GUI and logic
├── README.md            # Project documentation
```

## Dependencies

- Python 3.x
- PyQt5

## Future Improvements

- Implement Karnaugh Map (K-Map) visualization.
- Extend support for don't-care conditions.
- Enhance UI with better error handling.

---

This project is ideal for students, engineers, and researchers working with digital logic design and Boolean algebra. 🚀
