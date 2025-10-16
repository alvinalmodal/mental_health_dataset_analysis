# Mental Health in the Workplace: Data Analysis and Visualization

This project analyzes the "Mental Health Dataset" to uncover insights into mental well-being in the professional world. It uses Python, DuckDB, and Plotly to create an interactive, infographic-style dashboard with Dash.

The dashboard visualizes key metrics, including demographic profiles, the prevalence of mental health concerns, and correlations between workplace environment and employee well-being.

## Features

-   **Interactive Infographic:** A web-based dashboard built with Plotly and Dash.
-   **SQL-Powered Analysis:** Uses DuckDB to efficiently query and aggregate the dataset directly from memory.
-   **Comprehensive Insights:** Covers demographics, prevalence of mental health issues, workplace attitudes, and key correlations.
-   **Data-Driven Recommendations:** Provides actionable recommendations for employers based on the analysis.

## Getting Started

### Prerequisites

-   Python 3.8+
-   pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git https://github.com/alvinalmodal/mental_health_dataset_analysis
    cd mental_health_dataset_analysis
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  Make sure the `data/mental_health_dataset.csv` file is in the root directory of the project.
2.  Run the main application script:
    ```bash
    python app.py
    ```
3.  Open your web browser and navigate to the address shown in your terminal (usually `http://127.0.0.1:8050/`).

## Technologies Used

-   **Python:** Core programming language.
-   **Pandas:** For initial data loading.
-   **DuckDB:** For high-performance SQL querying and analysis.
-   **Plotly:** For creating interactive charts and graphs.
-   **Dash:** For building the web application framework.

## Dataset

This project uses the "Mental Health Dataset," which contains self-reported survey data on mental health in the workplace. The dataset is included in this repository as `mental_health_dataset.csv`.