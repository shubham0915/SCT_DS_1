# 🌍 Global Population Analysis 2023

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python) ![Pandas](https://img.shields.io/badge/Pandas-2.2.2-orange?logo=python) ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.9.0-green?logo=python) ![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-purple?logo=python)

A modern Python project to analyze and visualize global population data for the year 2023 using a vibrant and detailed histogram and boxplot. This project processes the dataset `Mydataset.csv` to provide insightful statistics, visualizations, and rankings of countries by population.

---

## 📋 Project Overview

This project analyzes population data for 266 countries/regions in 2023, sourced from `Mydataset.csv`. The script (`TASK1.py`) generates a colorful and detailed visualization of population distribution, including a histogram with a KDE curve and a boxplot to highlight outliers. It also provides summary statistics and rankings of the top and bottom 5 countries by population. The project was developed and tested as of **04:43 PM IST on Tuesday, June 10, 2025**.

---

## ✨ Features

- **📊 Vibrant Visualizations**:
  - A colorful histogram with gradient bars (using the `Spectral` colormap) and a red KDE curve.
  - A matching boxplot in light coral, highlighting population outliers.
  - Both plots display population in millions, with bold labels and a professional design.

- **📈 Detailed Statistics**:
  - Summary statistics including mean, median, standard deviation, quartiles, and more.
  - Rankings of the top 5 and bottom 5 countries by population in 2023.

- **🛠️ Easy to Use**:
  - Simple setup with clear instructions for running the script.
  - Dependencies are well-documented with installation steps.

- **🎨 Modern Design**:
  - Uses Seaborn and Matplotlib for a polished, professional look with a light gray background and subtle gridlines.

---

## 📂 Dataset

The dataset used in this project is `Mydataset.csv`, which contains population data for 266 countries/regions from 1960 to 2024. Key details:

- **Structure**:
  - Columns: `Country Name`, `Country Code`, `Indicator Name`, `Indicator Code`, `1960`, `1961`, ..., `2023`, `2024`.
  - Delimiter: Comma (`,`).
  - Total Rows: 266 (one per country/region).

- **Data for 2023**:
  - Extracted and analyzed population figures for the year 2023.
  - Example data:
    - China: 1,412,175,000
    - Tuvalu: 9,816

The dataset is included in the repository for convenience.

---

## 🛠️ Setup

### Prerequisites
- Python 3.13 or higher.
- A terminal or IDE to run the script (e.g., VS Code, PyCharm).

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shubham0915/global-population-analysis-2023.git
   cd global-population-analysis-2023
   ```

2. **Install Dependencies**:
   The script requires the following Python libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, and `tabulate`. Install them using `pip`:
   ```bash
   /usr/local/bin/python3.13 -m pip install pandas numpy matplotlib seaborn tabulate
   ```

3. **Verify Dataset**:
   Ensure `Mydataset.csv` is present in the project directory. The script assumes the dataset is comma-delimited. If your dataset uses a different delimiter, update the `sep` parameter in `pd.read_csv` in `TASK1.py`.

---

## 🚀 Usage

1. **Run the Script**:
   Execute the script using Python 3.13:
   ```bash
   /usr/local/bin/python3.13 TASK1.py
   ```

2. **Expected Output**:
   - **Debug Output**: Lists the column names of the dataset to verify correct loading.
   - **Visualization**: A figure with two subplots:
     - **Histogram**: Shows the distribution of population sizes with gradient bars, a red KDE curve, and a median line.
     - **Boxplot**: Displays the spread of population sizes with outliers marked.
   - **Summary Statistics**: A table with detailed statistics (mean, median, etc.).
   - **Rankings**: Tables listing the top 5 and bottom 5 countries by population.

---

## 📊 Results

### Visualization
The script generates a figure with a histogram and boxplot, both styled with a modern, colorful design:

- **Histogram**:
  - Gradient bars using the `Spectral` colormap.
  - Red KDE curve overlay.
  - Orange dashed line marking the median population (5.9M).

- **Boxplot**:
  - Light coral color with red outlier dots.
  - Shows the spread of population sizes, highlighting outliers like China and India.

### Summary Statistics
| Statistic            | Value        |
|----------------------|--------------|
| Total Countries      | 266          |
| Mean Population      | 29,662,179   |
| Median Population    | 5,865,599    |
| Std Dev Population   | 130,099,250  |
| Min Population       | 9,816        |
| Max Population       | 1,412,175,000|
| Q1 (25th Percentile) | 1,136,779    |
| Q3 (75th Percentile) | 21,519,313   |

### Rankings
**Top 5 Countries by Population in 2023**:
| Country Name   | Population (2023) |
|----------------|-------------------|
| World          | 7,856,138,790     |
| China          | 1,412,175,000     |
| India          | 1,426,982,127     |
| United States  | 334,914,895       |
| Indonesia      | 279,118,866       |

**Bottom 5 Countries by Population in 2023**:
| Country Name               | Population (2023) |
|----------------------------|-------------------|
| Tuvalu                     | 9,816             |
| British Virgin Islands     | 38,985            |
| Turks and Caicos Islands   | 44,386            |
| Sint Maarten (Dutch part)  | 42,749            |
| Andorra                    | 80,856            |

---

## 💡 Interesting Fact

The largest population in 2023 (China, 1.41 billion) is over **144,000 times larger** than the smallest (Tuvalu, 9,816). This extreme disparity highlights the challenges in global population studies, where a few countries dominate the total population while many others contribute minimally.

---

## 📝 Conclusion

This analysis reveals a highly skewed population distribution in 2023, with a few countries like China and India having massive populations, while most countries have far smaller populations (median: 5.9 million). The visualizations effectively illustrate this skewness, and the statistics provide a comprehensive view of global population trends. This project serves as a foundation for further exploration, such as analyzing historical population growth or regional differences.

---

## 📧 Contact

For questions or contributions, feel free to reach out:
- **GitHub**: [shubham0915](https://github.com/shubham0915)
- **LinkedIn**: [Shubham Kumar](https://www.linkedin.com/in/shubham-kumar-46422128a/)
- **Email**: [shubhamkuya@gmail.com](mailto:shubhamkuya@gmail.com)

---

🌟 **Star this repository if you found it helpful!**