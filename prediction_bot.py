import random
import requests
import telebot

# Define the function that gets the data from the API
def get_prediction():
    url = "https://starclubplay.fun/api/api/webapi/GetNoaverageEmerdList"
    response = requests.get(url)
    data = response.json()
    
    if data["code"] == 0 and data["msg"] == "Succeed":
        prediction_list = data["data"]["list"]
        prediction = random.choice(prediction_list)  # Choose a random prediction
        return f"Prediction Number: {prediction['number']}, Colour: {prediction['colour']}, Premium: {prediction['premium']}"
    else:
        return "Failed to fetch predictions."

# Create the bot object
bot = telebot.TeleBot('7779227091:AAGAfk_PbWWlqL1ZjsEQ5wPKpDo97Y2oxJE')  # Replace with your bot's API token

# Define start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! I will provide you with random predictions. Type /predict to get one.")

# Define predict command
@bot.message_handler(commands=['predict'])
def predict(message):
    prediction = get_prediction()
    bot.reply_to(message, prediction)

# Start polling
bot.polling()
