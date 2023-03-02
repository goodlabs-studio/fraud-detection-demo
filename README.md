# Fraud detection demo

## Getting Started
- Ensure you have installed Python on your computer
- Get the `.env` file with the creds for logging into chatGPT and ResembleAi from Paul
- Run all commands in the root of the project
- Run setup script to initialize a virtual environment and install dependencies. You may need to give it the correct priviledges to run.
```
source ./scripts/setup.sh
```
- Install system dependencies: Please install the right one for your OS
  ### MacOS
  ```
  brew install portaudio
  pip install pyaudio
  ```
  ### Windows
  ```
  sudo apt-get install python-pyaudio python3-pyaudio
  ```
  ### Linux
  ```
  pip install pyaudio
  ```

- Start the virtual environment if not already started
```
source ./venv/bin/activate
```
- Run the application
```
python main.py
```
- Speak when the terminal displays `Talk` and wait for the results to be played in the resembleAI UI
