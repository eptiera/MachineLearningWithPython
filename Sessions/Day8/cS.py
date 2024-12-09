import pandas as pd
import numpy as np

# Create a Series of 10 random integers between 1 and 50
random_series = pd.Series(np.random.randint(1, 51, size=10))

# Display the Series
print("Random Series:")
print(random_series)
