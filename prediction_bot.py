import random
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

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

# Define a start command for the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome! I will provide you with random predictions. Type /predict to get one.')

# Define a command for fetching random prediction
async def predict(update: Update, context: CallbackContext) -> None:
    prediction = get_prediction()
    await update.message.reply_text(prediction)

# Main function to start the bot
def main():
    token = 'YOUR_BOT_API_TOKEN'  # Replace with your bot's API token
    
    # Create the Application object
    application = Application.builder().token(token).build()
    
    # Add handlers for commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("predict", predict))
    
    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
