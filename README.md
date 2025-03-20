# 🚴‍♂️ **Exercise Tracker** 🏃‍♀️

**Exercise Tracker** is a Python application that helps you track your daily physical activities and the calories burned. All you need to do is input the exercises you performed, and the app calculates the calories burned based on your gender, weight, height, and age. It then logs the information into your Google Sheet using the Sheety API.

---

## 🔥 Features

- **📝 Exercise Input**: You input the exercises you did during the day (e.g., "I ran for 30 minutes").
- **🔥 Calories Calculation**: The app uses the Nutritionix API to calculate calories burned based on your gender, weight, height, and age.
- **📊 Google Sheets Integration**: It automatically logs your workout details (exercise, duration, and calories) into a Google Sheet via the Sheety API.

---

## 🛠️ Prerequisites

To run Exercise Tracker, you'll need the following:

- Python 3.x
- `requests` library for making HTTP requests

### Installing Python Libraries

```bash
pip install -r requirements.txt
```

---

## 🔧 Setup

1. **Clone the Repository**:

   First, clone this repository to your local machine:

   ```bash
   git clone https://github.com/Nickkcj/exercise-tracker.git
   ```

2. **Configure Settings**:

   Open `config/settings.py` and set the following variables:

   ```python
   BEARER_TOKEN = "your_nutritionix_bearer_token"
   APP_ID = "your_nutritionix_app_id"
   APP_KEY = "your_nutritionix_app_key"
   GENDER = "your_gender"  # e.g., "man" or "woman"
   WEIGHT_KG = 70
   HEIGHT_CM = 180
   AGE = 25
   ```

   Replace the placeholders with your own credentials and details.

3. **Google Sheets Setup**:

   - Create a Google Sheet and generate an API key using Sheety (follow [Sheety documentation](https://sheety.co/)).
   - Add your **Google Sheets API endpoint** in the `config/settings.py` file.

---

## 🚀 Running the Application

To run the Exercise Tracker, simply execute the `main.py` script from the command line or PowerShell:

```bash
python src/main.py
```

You’ll be prompted to enter the exercises you did, and the app will log the details into your Google Sheet. 📅

---

## 📂 Project Structure

```
project/
│── src/
│   ├── api/
│   │   ├── nutritionix.py  # Handles Nutritionix API requests
│   │   ├── sheety.py       # Handles Sheety API requests
│   ├── main.py             # Main script for running the app
│── config/
│   ├── settings.py         # Configuration file for API keys and user details
│── requirements.txt        # List of required Python libraries
│── README.md               # Project documentation
```

---

## 🤝 Contributing

If you'd like to help improve this project, feel free to fork the repository, create a new branch, and submit a pull request. ✨

---
