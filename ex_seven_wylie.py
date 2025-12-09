# David Wylie
# CIS256 24903
# EX7: Matplotlib
# This program displays a line chart of monthly sales data
# Used patterns from the example sildeshow and geeksforgeeks

import matplotlib.pyplot as plt
import numpy as np

# X-Axis
x = [
    'January', 'February', 'March',
    'April', 'May', 'June',
    'July', 'August', 'September',
    'October', 'November', 'December'
    ]

# Y-Axis
y = np.array(
    [50, 60, 70, 65, 80, 85, 90, 75, 70, 80, 85, 90]
    )

# Set Window Size and Create Line Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle="-", color='b')

# Add title and labels, polish the look
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout(pad=2.0)
plt.ylabel('Sales (in thousands)')

# Show the line chart
plt.show()
