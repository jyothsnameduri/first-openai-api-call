# OpenAI Clinical Assistant

## What the Script Does

This application is a simple GUI interface that:

1. Takes user input through a clean Tkinter interface
2. Uses a fixed clinical assistant system prompt
3. Makes API calls to OpenAI's GPT-3.5 Turbo model
4. Displays the AI's response
5. Shows detailed token usage statistics

![Application Screenshot](https://i.imgur.com/xKGFkRY.png)

## How to Run It

### Dependencies
- Python 3.6+
- OpenAI Python library
- Tkinter (included with most Python installations)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/jyothsnameduri/first-openai-api-call.git
   cd first-openai-api-call
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key as an environment variable:
   
   **Windows:**
   ```
   set OPENAI_API_KEY=your_api_key_here
   ```
   
   **macOS/Linux:**
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```
   python openai_chat_app.py
   ```

### Using the Application

1. Type your question in the input box
2. Click "Send" to submit your question
3. View the AI's response in the top text area
4. See token usage statistics at the bottom

## Security Note

This application uses environment variables for API key management. Never commit your actual API key to a public repository.
