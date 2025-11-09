🌌 NASA Space Explorer — Flask Web App

This Flask application provides an interactive dashboard to explore NASA’s publicly available data through their APIs — including the Astronomy Picture of the Day (APOD), Mars Rover images, Near-Earth Objects (NEO), and more.

🚀 Features

🖼️ Astronomy Picture of the Day (APOD)
Fetches daily space images from NASA’s APOD API between a start date and today’s date, displaying image titles, descriptions, and links.

☄️ Near-Earth Object Web Service (NEOWS)
Displays asteroid and near-earth object data (page placeholder ready for integration).

🌡️ Mars Weather
Displays the latest Mars weather information (page placeholder ready for integration).

🤖 Mars Rover Photos
Shows photos captured by Mars rovers (page placeholder ready for integration).

🛰️ CNEOS / SSD Data
Placeholder page for NASA’s Center for Near-Earth Object Studies data.

🧩 Project Structure
├── app.py
├── templates/
│   ├── base.html
│   ├── apod.html
│   ├── neows.html
│   ├── mars_weather.html
│   ├── mars_rover.html
│   └── ssd_cneos.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux

3️⃣ Install Required Packages
pip install -r requirements.txt


(If you don’t have a requirements.txt yet, create one using:)

pip freeze > requirements.txt

4️⃣ Set Your NASA API Key

You can get a free API key from NASA API Portal
.
Then, open app.py and replace the following line with your key:

NASA_API_KEY = 'YOUR_NASA_API_KEY_HERE'

▶️ Run the Application
python app.py


Visit your app in the browser at:
👉 http://127.0.0.1:5000/

📡 API Endpoints
Endpoint	Description
/	Home page
/apod	Fetch and display NASA Astronomy Picture of the Day
/neows	Near-Earth Object Web Service page
/mars_weather	Mars weather data page
/mars_rover	Mars rover images page
/ssd_cneos	CNEOS/SSD data page
🧠 How It Works

Uses the Flask web framework to serve dynamic pages.

Makes HTTP requests to NASA’s API using the requests library.

Loops through a date range to fetch multiple APOD entries.

Filters out non-image URLs (e.g., videos).

Displays valid data in the apod.html template.

🪐 Example Output (APOD Page)

Each image entry includes:

📅 Date

🧾 Title

🖼️ Image

🪄 Description

🧰 Tech Stack

Backend: Python (Flask)

Frontend: HTML, CSS, Bootstrap (in templates)

API: NASA Open APIs

Libraries: requests, datetime

💡 Future Improvements

Add search/filter by date range for APOD.

Integrate live Mars weather API.

Fetch and display Mars Rover photos dynamically.

Include asteroid tracking dashboard for NEOWS.

Add dark mode UI with Tailwind or Bootstrap 5.

👨‍🚀 Author

Shiva Teja
💻 Developer | Space Enthusiast | AI & Data Vision Projects

Feel free to connect or contribute!

📝 License

This project is licensed under the MIT License — you are free to use, modify, and distribute it with attribution.
