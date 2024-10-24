import speech_recognition as sr  # Make sure SpeechRecognition is installed

def audio_to_text(audio_file):
    """Convert audio file to text."""
    recognizer = sr.Recognizer()  # Initialize the recognizer
    try:
        # Load the audio file and recognize the speech
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)  # Record the audio from file
            
        # Using Google's speech recognition API to convert audio to text
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == "__main__":
    # Replace 'path/to/audio/file.wav' with the actual path to your audio file
    text = audio_to_text('path/to/audio/file.wav')  
    print(text)  # Print the converted text
