from elevenlabs import generate, play

audio = generate(
    text="¡Hola! Mi nombre es Arnold, encantado de conocerte!",
    voice="Bella",
    model='eleven_multilingual_v1'
)

play(audio)