
# Prodigy_SD_05 - Web Scraping Program

## Overview

This repository contains a Python program designed to extract product information, such as product names, prices, and ratings, from an e-commerce website and store the data in a CSV file. Additionally, there is a simple GUI built using Tkinter, allowing users to input the URL of the website and select the file location for the CSV output.

### Features:
- Extract product names, prices, and ratings.
- Save the extracted data in a structured CSV format.
- Simple GUI for URL input and output CSV file selection.

## Requirements

Before running the scripts, ensure you have the following Python packages installed:

- `requests`
- `beautifulsoup4`
- `tkinter` (This is usually included with Python, but double-check your installation)

You can install the required packages using:

```bash
pip install requests beautifulsoup4
```

## Project Structure

```bash
.
├── gui.py          # GUI interface for scraping
├── scraper.py      # Web scraping script
└── README.md       # Documentation for the project
```

## How It Works

1. **scraper.py**: This script handles the actual web scraping. It takes a URL and an output CSV file path as input and extracts product details (name, price, and rating) from the webpage.
   
2. **gui.py**: This script creates a simple GUI using Tkinter to allow the user to input the URL and select a location to save the CSV file.

### Scraper.py Workflow:
- Fetches the webpage content using the `requests` library.
- Parses the HTML using `BeautifulSoup` and extracts product information based on specific HTML selectors.
- Saves the data into a CSV file.

### GUI.py Workflow:
- Provides a graphical interface where the user can enter a URL.
- Allows the user to choose a save location for the output CSV file.
- Calls the scraper script through a subprocess.

## Running the Project

### Running the GUI:

1. Clone this repository:

```bash
git clone https://github.com/yourusername/PRODIGY_SD_05.git
```

2. Navigate to the project directory:

```bash
cd PRODIGY_SD_05
```

3. Run the GUI script:

```bash
python gui.py
```

4. Enter the URL of the e-commerce website you want to scrape.
5. Choose a location to save the CSV file.
6. Click **Start Scraping**.

### Running the Scraper Directly (Optional):

Alternatively, you can run the scraper directly from the command line:

```bash
python scraper.py <URL> <output_csv>
```

Replace `<URL>` with the URL of the website you want to scrape and `<output_csv>` with the desired output file path.

Example:

```bash
python scraper.py "https://example.com/products" "output.csv"
```

## Notes

- Ensure you have the correct CSS selectors in `scraper.py` that match the structure of the website you're scraping. The current selectors are placeholders and need to be modified according to the actual HTML structure.
- Always check the website's terms of service before scraping to ensure compliance with legal and ethical guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
