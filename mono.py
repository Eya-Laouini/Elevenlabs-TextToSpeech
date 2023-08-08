from elevenlabs import generate, play

audio = generate(
  text="Hi! My name is Eya Laouini and this is our text to speech model.",
  voice="Adam",
  model="eleven_monolingual_v1"
)

play(audio)