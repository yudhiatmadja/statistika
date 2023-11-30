import numpy as np
from scipy.stats import shapiro
import matplotlib.pyplot as plt
import seaborn as sns


hours_of_study = np.array([2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4, 2.7, 4.8, 3.8, 6.9, 7.8])
scores = np.array([21, 47, 27, 75, 30, 20, 88, 60, 81, 25, 85, 62, 41, 42, 17, 95, 30, 24, 67, 69, 30, 54, 35, 76, 8.6])

shapiro_hours_of_study = shapiro(hours_of_study)
shapiro_scores = shapiro(scores)

print("Shapiro-Wilk test for hours_of_study:", shapiro_hours_of_study)
print("Shapiro-Wilk test for Scores:", shapiro_scores)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(hours_of_study, kde=True)
plt.title('Histogram of hours_of_study')

plt.subplot(1, 2, 2)
sns.histplot(scores, kde=True)
plt.title('Histogram of Scores')

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
stats.probplot(hours_of_study, dist="norm", plot=plt)
plt.title('Q-Q Plot of hours_of_study')

plt.subplot(1, 2, 2)
stats.probplot(scores, dist="norm", plot=plt)
plt.title('Q-Q Plot of Scores')

plt.tight_layout()
plt.show()
