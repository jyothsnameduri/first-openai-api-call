# OpenAI Clinical Assistant

A simple GUI application that interacts with OpenAI's GPT-3.5 Turbo model to provide clinical assistance. This application demonstrates how to make API calls to OpenAI, handle responses, and display token usage information.

## Features

- Clean, user-friendly Tkinter GUI
- Real-time interaction with OpenAI's GPT-3.5 Turbo model
- Specialized clinical assistant system prompt
- Token usage tracking
- Progress indicator during API calls
- Error handling

## Prerequisites

- Python 3.6 or higher
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/first-openai-api-call.git
   cd first-openai-api-call
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key as an environment variable:
   
   **Windows:**
   ```
   set OPENAI_API_KEY=your_api_key_here
   ```
   
   **macOS/Linux:**
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```
   
   Alternatively, you can modify the code to use your API key directly (not recommended for shared code).

## Usage

Run the application:
```
python openai_chat_app.py
```

1. Type your health-related question in the input area
2. Click the "Send" button to submit your question
3. View the AI's response in the top text area
4. Check token usage statistics at the bottom

## Security Note

This application uses environment variables to handle the API key securely. Never commit your actual API key to a public repository.

## License

MIT

## Acknowledgments

- OpenAI for providing the API
- Tkinter for the GUI framework
