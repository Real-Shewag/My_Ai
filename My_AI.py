import datetime
import random

# Initialize greeting variables
morning_greetings = ["Good morning!Rise and shine!", "Have a lovely day!"]
afternoon_greetings = ["Good afternoon!Nice to see you back!", "Hope you're having a productive day!"]
evening_greetings = ["Good evening!Hope you enjoyed your day!"]
night_greetings = ["Good Night,How was your day?"]

def greet():
  """Greets the user based on the time of day."""
  current_time = datetime.datetime.now()
  hour = current_time.hour

  if 5 <= hour < 12:
    return random.choice(morning_greetings)
  elif 12 <= hour < 16:
    return random.choice(afternoon_greetings)
  elif 16<= hour < 19:
    return random.choice(evening_greetings)
  else:
    return random.choice(night_greetings)

def respond(text):
  """Responds to user input based on keywords."""
  # Add more keywords and responses here, including personalized ones!
  if "weather" in text:
    # Replace this with code to access weather API and provide info
    return "I'm still learning how to access weather information, but I'm getting there!"
  elif "time" in text:
    return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
  elif "joke" in text:
    jokes = ["Why did the scarecrow win an award? Because he was outstanding in his field!",
              "What do you call a fish with no eyes? Fsh!"]
    return random.choice(jokes)
  elif "Roji" in text:
      return "Hi Roji,Nice to have you back!Hope youre doing well."
  elif "Who are you" in text:
      return "Hi I am a personal assistant created by shewag "
  elif "hi" in text:
      return "Hello,How was your day?"
  else:
    return "I'm still under development. Please ask questions related to Shewag Basistha?"

# Main loop
while True:
  greeting = greet()
  if greeting:
    print(greeting)
  user_input = input("You: ")
  response = respond(user_input)
  print(f"Assistant: {response}")
