import pyttsx3
import argparse

def convert_text_to_speech(text, save_to_file=None, rate=None, volume=None, voice=None):
    engine = pyttsx3.init()

    # Set properties if provided
    if rate:
        engine.setProperty('rate', rate)
    if volume:
        engine.setProperty('volume', volume)
    if voice:
        voices = engine.getProperty('voices')
        selected_voice = next((v for v in voices if voice in v.name), None)
        if selected_voice:
            engine.setProperty('voice', selected_voice.id)
        else:
            print(f"Voice '{voice}' not found. Using default voice.")

    engine.say(text)
    
    if save_to_file:
        engine.save_to_file(text, save_to_file)
        engine.runAndWait()
        print(f"Speech saved to {save_to_file}")
    else:
        engine.runAndWait()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Text-to-Speech Bot")
    parser.add_argument("text", type=str, help="Text to convert to speech")
    parser.add_argument("--save", type=str, help="Save speech to audio file")
    parser.add_argument("--rate", type=int, help="Speech rate")
    parser.add_argument("--volume", type=float, help="Speech volume (0.0 to 1.0)")
    parser.add_argument("--voice", type=str, help="Preferred voice (part of voice name)")

    args = parser.parse_args()

    convert_text_to_speech(args.text, args.save, args.rate, args.volume, args.voice)
