import requests
from flask import Flask, jsonify, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

# Replace with your own NASA API key
NASA_API_KEY = '98O7h0I23vZHWU8zokfsj3iRvqIIMRTFMUzGNNLF'
NASA_APOD_URL = 'https://api.nasa.gov/planetary/apod?api_key={}&date={}'

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/apod')
def apod():
    # Set the start and end dates for the range
    start_date = datetime(2025, 12, 18)  # Example start date
    end_date = datetime.today()  # Today's date

    # Prepare a list to hold APOD data
    apod_data_list = []

    current_date = start_date
    while current_date <= end_date:
        # Format the current date to the required YYYY-MM-DD format
        formatted_date = current_date.strftime('%Y-%m-%d')

        # Fetch the Astronomy Picture of the Day data from NASA's API for the current date
        response = requests.get(NASA_APOD_URL.format(NASA_API_KEY, formatted_date))
        
        if response.status_code == 200:
            apod_data = response.json()  # Parse the JSON response
            
            # Ensure the expected keys are in the response
            if 'title' in apod_data and 'explanation' in apod_data and 'url' in apod_data:
                title = apod_data['title']
                explanation = apod_data['explanation']
                image_url = apod_data['url']

                # Add valid image URLs
                if image_url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    apod_data_list.append({
                        'title': title,
                        'explanation': explanation,
                        'image_url': image_url
                    })
                else:
                    print(f"Skipping non-image URL for {formatted_date}: {image_url}")
            else:
                print(f"Missing data for date {formatted_date}: {apod_data}")
        else:
            print(f"Error fetching data for date {formatted_date}: {response.status_code}")

        # Move to the next date
        current_date += timedelta(days=1)

    # Render the page with the collected data
    if apod_data_list:
        return render_template('apod.html', apod_data_list=apod_data_list)
    else:
        return "No APOD data available or failed to fetch data."
    
@app.route('/neows')
def neows():
    return render_template('neows.html')




@app.route('/mars_weather')
def mars_weather():
     return render_template('mars_weather.html')



@app.route('/mars_rover')
def mars_rover():
     return render_template('mars_rover.html')

@app.route('/ssd_cneos')
def ssd_cneos():
     return render_template('ssd_cneos.html')


    
if __name__ == '__main__':
    app.run(debug=True)
