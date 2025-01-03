import random

# Welcome message
print("🌟 Welcome to the Oracle of Delphi 🌟")
print("The Oracle will guide you to choose the best activity based on the weather and your mood.")

# Step 1: Gather inputs from the user
weather = input("What is the weather like? (sunny/rainy/cloudy): ").lower()
mood = input("What is your mood? (energetic/relaxed): ").lower()

# Step 2: Define possible activities
activities = {
    "sunny_energetic": ["Go hiking", "Play outdoor sports"],
    "sunny_relaxed": ["Have a picnic", "Visit a park"],
    "rainy_energetic": ["Go to an indoor climbing gym", "Dance at home"],
    "rainy_relaxed": ["Read a book", "Watch a movie"],
    "cloudy_energetic": ["Go for a jog", "Visit a museum"],
    "cloudy_relaxed": ["Write in a journal", "Do some painting"]
}

# Step 3: Generate a key from the inputs
key = f"{weather}_{mood}"

# Step 4: Use the Oracle to choose an activity
if key in activities:
    chosen_activity = random.choice(activities[key])
    print(f"\n🔮 The Oracle says: You should {chosen_activity}!")
else:
    print("\n🔮 The Oracle is silent... It seems your inputs do not match the available options. Please try again.")
