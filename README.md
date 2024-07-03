# Brent Oil Price Analysis

This project aims to analyze how important events affect Brent oil prices. The focus is on identifying how changes in oil prices are linked to significant events such as political decisions, conflicts in oil-producing regions, global economic sanctions, and changes in Organization of the Petroleum Exporting Countries (OPEC) policies. The goal is to provide clear insights to help investors, analysts, and policymakers understand and react to these price changes better.

## Project Structure

brent-oil-analysis/
├── .github/
│ └── workflows/
│ └── ci.yml
├── .vscode/
│ ├── settings.json
│ ├── launch.json
│ └── tasks.json
├── data/
│ └── BrentOilPrices.csv
├── notebooks/
│ └── analysis.ipynb
├── scripts/
│ └── data_analysis.py
├── venv/
├── .gitignore
├── requirements.txt
└── README.md

## Installation

### Prerequisites

- Python 3.12
- Git
- Virtual environment tools (`venv` or `conda`)

### Setup

1. **Clone the repository**:

   ```sh
   git clone https://github.com/juniorworku/brent-oil-analysis.git
   cd brent-oil-analysis
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - **Windows (PowerShell)**:

     ```powershell
     .\venv\Scripts\Activate
     ```

   - **Windows (Command Prompt)**:

     ```cmd
     .\venv\Scripts\activate
     ```

   - **macOS/Linux**:
     ```sh
     source venv/bin/activate
     ```

4. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Analysis

1. **Jupyter Notebook**:
   - Start Jupyter Notebook:
     ```sh
     jupyter notebook
     ```
   - Open `notebooks/EDA.ipynb` and run the cells.

### Testing

- Run the tests (if any):
  ```sh
  python -m unittest discover -s tests
  ```

### Continuous Integration

- This project uses GitHub Actions for continuous integration. The configuration is located in .github/workflows/ci.yml.

### VSCode Configuration

- The project includes configuration files for Visual Studio Code in the .vscode folder:

settings.json for workspace settings
launch.json for debugging configurations
tasks.json for defining tasks

### Data

- The dataset used in this project contains historical Brent oil prices from May 20, 1987, to September 30, 2022.
  - Date: The date of the recorded Brent oil price.
  - Price: The price of Brent oil in USD per barrel.

### Insights and Results

- Detailed insights and results of the analysis are available in the Jupyter Notebook notebooks/EDA.ipynb.
  -The analysis focuses on identifying key events that significantly impacted Brent oil prices and measuring the extent of their impact.

### Conclusion

The analysis aims to provide actionable insights for investors, analysts, and policymakers to better understand and react to changes in Brent oil prices.

### Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

### License

This project is licensed under the MIT License.

### Contact

For any questions or inquiries, please contact [juniorworku@gmail.com].
