

# 💸 FinGenie — Personal Finance Assistant 🧞

**FinGenie** is an interactive personal finance assistant built with **Python** and **Streamlit**. It helps users log, track, and analyze income and expenses, with features including real-time financial reports and an AI chatbot for personalized advice.

**Try it live:** [https://fingenie.streamlit.app/](https://fingenie.streamlit.app/)

---

## Overview

The FinGenie application enables users to manage their personal finances efficiently through:

* Income and expense tracking by category, date, and description
* Real-time balance calculation
* Interactive financial reports with charts (via Plotly)
* Persistent notes for financial journaling
* AI-powered chatbot for personalized financial guidance
* User authentication with per-user local SQLite databases, with plans to support cloud syncing via Firebase

Try the live demo here: [https://fingenie.streamlit.app/](https://fingenie.streamlit.app/)

---

## Application Structure

### Home.py

Main entry point that handles user login, registration, and dashboard display.

### pages/

Multi-page Streamlit UI components:

* `1_+_Transaction_Log.py`: Add new income and expenses
* `2__View_Expenses.py`: View expense list
* `3__Report.py`: Generate financial reports and charts
* `Notes.py`: Personal finance notes and journal

### utils/

Utility modules:

* `expenseTracker.py`: Core logic for adding and managing transactions
* `fingenie_ai_bot.py`: AI chatbot integration (powered by Cohere or OpenAI)

### auth.py

Handles user authentication and local database management, with future Firebase integration support.

---

## Features

* **Income and Expense Tracking:** Categorize and log all transactions with amount, date, description, and source.
* **Balance Calculation:** Real-time updates of account balances based on entries.
* **Interactive Reports:** Visualize spending patterns through pie charts, bar graphs, and trend analysis.
* **Notes and Journaling:** Maintain personal notes related to finances.
* **AI Chatbot Assistant:** Ask questions and receive tailored advice based on financial history.
* **User Authentication:** Register/login with email and password; data isolated per user in SQLite `.db` files.
* **Cloud Syncing:** Planned Firebase Firestore integration for cloud backup and sync.

---

## Tech Stack

| Technology     | Purpose                                                   |
| -------------- | --------------------------------------------------------- |
| **Python**     | Core backend logic and data processing                    |
| **Streamlit**  | Web framework for interactive UI                          |
| **SQLite**     | Local database for storing user transactions              |
| **Plotly**     | Interactive charts and financial visualizations           |
| **Cohere API** | AI assistant for personalized financial advice (optional) |
| **dotenv**     | Secure storage and management of API keys                 |

---

## Requirements

* Python 3.8+
* Streamlit
* SQLite (default database)
* Cohere or OpenAI API key (for AI assistant)
* (Optional) Firebase for cloud data syncing

---

## Installation

```bash
git clone https://github.com/yourusername/fingenie.git
cd fingenie
pip install -r requirements.txt
```

Create a `.env` file in the root directory:

```ini
COHERE_API_KEY=your_cohere_api_key
# or
OPENAI_API_KEY=your_openai_api_key
```

---

## Usage

### Launch the App Locally

```bash
streamlit run Home.py
```

### Access Live Demo

You can try FinGenie instantly at:
[https://fingenie.streamlit.app/](https://fingenie.streamlit.app/)

### Authentication

* Users register and log in with email and password.
* Each user gets a dedicated SQLite database file (`email.db`) to store their financial data.

### Add Transactions

* Add income or expenses by providing amount, date, description, and category/source.

### View Reports

* Visualize spending by category, monthly trends, and income vs expense comparison.

### AI Chatbot

* Ask finance-related questions.
* Receive personalized advice based on your transaction history.

---

## Security

* User data is stored in isolated per-user SQLite files.
* AI chatbot processes data securely and does not expose sensitive information.
* Authentication restricts data access to authorized users only.

---

## Testing

Currently manual testing. To enable automated tests:

```bash
pytest
```

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes
4. Push to your branch
5. Open a pull request

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Disclaimer

FinGenie is an educational project and should not be used to manage large financial assets without proper security measures and cloud backup. Always verify financial advice with a certified professional.

