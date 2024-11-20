
# Traq Diagnostic Application

## Overview

The **Traq Diagnostic Application** is a Streamlit-based tool designed to assist in the diagnosis of behavioral and attention-related disorders using the TRAQ questionnaire. It computes key scores, visualizes results, and generates detailed reports for download.

---

## Features

- **Dynamic Questionnaire**: An interactive interface to collect user answers.
- **Score Calculation**: Computes attention, inhibition, and total TRAQ scores.
- **Visualization**: Generates bar charts to display diagnostic insights clearly.
- **Report Generation**: Exports diagnostic data to Excel format for further analysis.

---

## Deployment

The application is deployed and can be accessed [here](https://traq-fast.streamlit.app/).

---

## Installation

### Prerequisites
- Python 3.8 or above
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/simbouch/traq_diagnostic.git
   cd traq_diagnostic
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Project Structure

```
traq_diagnostic/
├── app.py              # Main Streamlit application
├── models/
│   ├── __init__.py     # Initialization for models
│   ├── traq_model.py   # TRAQ-specific calculations
│   ├── visualization.py # Visualization functions
│   ├── utils.py        # Utility functions (data parsing, report generation)
│   ├── traq_class.pkl  # Pre-trained TRAQ model
├── static/
│   ├── images/
│       ├── clinicog.png  # Sidebar image for branding
├── data/
│   ├── questionnaire.txt # Text file containing the questionnaire
│   ├── traq_centiles.xlsx # Centile data for TRAQ
├── requirements.txt    # Dependencies for the project
├── README.md           # Documentation
```

---

## Usage

### Running the Application

1. Launch the application using:
   ```bash
   streamlit run app.py
   ```

2. Fill in the **user information** in the sidebar.

3. Answer the **TRAQ questionnaire** displayed on the main page.

4. Click **Save and Analyze** to calculate scores, visualize results, and download the diagnostic report.

---

## Author

**Khribech Bouchaib**  
Date: 2024-04-20  
Version: 1.0
