# ORIONPAX 2024-25: Optimization and Bug Hunting Competition

Welcome to the **ORIONPAX** event repository! This repository contains the necessary helper files and demo scripts to get you started for the event. The event is hosted by the GitHub Campus Club at PSG College of Technology and is designed for 2nd and 3rd-year students to showcase and enhance their debugging, optimization, and development skills.

## Event Overview

The ORIONPAX competition is divided into two rounds:

- **Round 1: Bug Hunting (HTML Page)**
  - Participants will receive an HTML page with intentional bugs related to layout, typography, navigation, and media. Your task is to identify and fix as many bugs as possible within 2 hours.
- **Round 2: Optimization and Development**
  - Participants will be given a skeleton project that includes existing functions and a REST-API integration. You'll be tasked with optimizing these functions and developing new features using the provided APIs. You'll also need to integrate math-based functions into the project.

## Repository Structure

This repository is organized as follows:

```
ORIONPAX/
│
├── README.md               # You are here!
├── server.py               # Demo server for testing API endpoints
├── fastapi_helper.py       # Helper functions and setup for FastAPI
├── html_helper.html        # HTML page with intentional bugs for Round 1
└── requirements.txt        # Python dependencies
```

### Files and Their Purpose

- **`server.py`**

  - A demo Python script using FastAPI to serve as a backend for testing your REST-API integrations during Round 2. This script includes endpoints that you will use to develop and optimize new features.

- **`fastapi_helper.py`**

  - Contains helper functions to set up FastAPI and simplify the interaction with the provided REST-API. You can extend and modify these functions as needed during the event.

- **`html_helper.html`**

  - This file contains an HTML page filled with intentional bugs related to layout, typography, navigation, images, and background color. Your task in Round 1 is to identify and fix these bugs to improve the page's functionality and appearance.

- **`requirements.txt`**
  - A list of Python dependencies required to run the `server.py` and the FastAPI helpers. Install them using `pip install -r requirements.txt`.

## Getting Started

### 1. Set Up the Environment

First, clone this repository to your local machine:

```bash
git clone https://github.com/YourUsername/ORIONPAX.git
cd ORIONPAX
```

Next, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Running the Demo Server

To run the FastAPI demo server (`server.py`), use the following command:

```bash
python server.py
```

The server will start on `http://localhost:8000`, and you can access the provided API endpoints from your browser or API testing tools like Postman.

### 3. Working with HTML Helper

Open the `html_helper.html` file in your preferred code editor. Identify and fix the bugs within the HTML file, ensuring that the layout, typography, and media elements work as intended.

### 4. Optimization and Development

In Round 2, you'll need to work with the skeleton project provided in `server.py` and `fastapi_helper.py`. Optimize the existing functions and develop new features according to the event instructions.

## Evaluation Criteria

Your performance will be evaluated based on the following criteria:

- **Bug Hunting (Round 1)**
  - Points for each bug identified and successfully fixed.
- **Optimization and Development (Round 2)**
  - Quality and efficiency of the optimizations.
  - Correctness and performance of new features.
  - Integration of math-based functions.

## Support and Questions

If you have any questions or need support during the event, feel free to reach out to the event organizers or mentors available on the official event communication channels.

## License

This repository is for the ORIONPAX event hosted by the GitHub Campus Club at PSG College of Technology. Participants can use and modify the code during the event, but it is not intended for redistribution outside of this context.

---

Good luck, and may the best coder win! 🏆
