import tkinter as tk
from tkinter import scrolledtext, ttk
from openai import OpenAI
import os

class OpenAIChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenAI Clinical Assistant")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")
        
        # OpenAI client - get API key from environment variable
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("Warning: OPENAI_API_KEY environment variable not set.")
            print("Please set your API key using: export OPENAI_API_KEY='your-api-key'")
            api_key = "YOUR_API_KEY_HERE"  # Placeholder, will cause an error if used
            
        self.client = OpenAI(
            api_key=api_key
        )
        
        # Fixed system prompt
        self.system_prompt = "You are a helpful and knowledgeable Clinical Assistant. Provide clear, accurate medical information, help interpret symptoms, and suggest next steps. Always remind users to consult a licensed doctor for diagnosis or treatment."
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame for the chat area
        chat_frame = tk.Frame(self.root, bg="#f0f0f0")
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Response area
        tk.Label(chat_frame, text="Assistant's Response:", bg="#f0f0f0", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 5))
        
        self.response_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=60, height=20, font=("Arial", 10))
        self.response_area.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.response_area.config(state=tk.DISABLED)
        
        # Token usage frame
        token_frame = tk.LabelFrame(chat_frame, text="Token Usage", bg="#f0f0f0", font=("Arial", 10, "bold"))
        token_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Token usage labels
        self.prompt_tokens_var = tk.StringVar(value="Prompt tokens: 0")
        self.completion_tokens_var = tk.StringVar(value="Completion tokens: 0")
        self.total_tokens_var = tk.StringVar(value="Total tokens: 0")
        
        tk.Label(token_frame, textvariable=self.prompt_tokens_var, bg="#f0f0f0").pack(anchor="w", padx=10, pady=2)
        tk.Label(token_frame, textvariable=self.completion_tokens_var, bg="#f0f0f0").pack(anchor="w", padx=10, pady=2)
        tk.Label(token_frame, textvariable=self.total_tokens_var, bg="#f0f0f0").pack(anchor="w", padx=10, pady=2)
        
        # User input area
        tk.Label(chat_frame, text="Your Question:", bg="#f0f0f0", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 5))
        
        self.user_input = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=60, height=5, font=("Arial", 10))
        self.user_input.pack(fill=tk.X, pady=(0, 10))
        
        # Send button with loading indicator
        button_frame = tk.Frame(chat_frame, bg="#f0f0f0")
        button_frame.pack(fill=tk.X)
        
        self.send_button = tk.Button(button_frame, text="Send", command=self.send_message, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=10)
        self.send_button.pack(side=tk.LEFT, pady=5)
        
        self.progress_bar = ttk.Progressbar(button_frame, mode="indeterminate", length=150)
        self.progress_bar.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Clear button
        self.clear_button = tk.Button(button_frame, text="Clear", command=self.clear_chat, bg="#f44336", fg="white", font=("Arial", 10, "bold"), width=10)
        self.clear_button.pack(side=tk.RIGHT, pady=5)
    
    def send_message(self):
        # Get user input
        user_input = self.user_input.get("1.0", tk.END).strip()
        if not user_input:
            return
        
        # Disable send button and show progress
        self.send_button.config(state=tk.DISABLED)
        self.progress_bar.start(10)
        
        # Clear previous response
        self.response_area.config(state=tk.NORMAL)
        self.response_area.delete("1.0", tk.END)
        self.response_area.config(state=tk.DISABLED)
        
        # Reset token counters
        self.prompt_tokens_var.set("Prompt tokens: 0")
        self.completion_tokens_var.set("Completion tokens: 0")
        self.total_tokens_var.set("Total tokens: 0")
        
        # Schedule API call to avoid freezing UI
        self.root.after(100, lambda: self.make_api_call(user_input))
    
    def make_api_call(self, user_input):
        try:
            # Make the API call
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            
            # Display the response
            self.response_area.config(state=tk.NORMAL)
            self.response_area.insert(tk.END, completion.choices[0].message.content)
            self.response_area.config(state=tk.DISABLED)
            
            # Update token usage
            self.prompt_tokens_var.set(f"Prompt tokens: {completion.usage.prompt_tokens}")
            self.completion_tokens_var.set(f"Completion tokens: {completion.usage.completion_tokens}")
            self.total_tokens_var.set(f"Total tokens: {completion.usage.total_tokens}")
            
        except Exception as e:
            # Display error message
            self.response_area.config(state=tk.NORMAL)
            self.response_area.insert(tk.END, f"Error: {str(e)}")
            self.response_area.config(state=tk.DISABLED)
        
        finally:
            # Re-enable send button and stop progress
            self.send_button.config(state=tk.NORMAL)
            self.progress_bar.stop()
    
    def clear_chat(self):
        # Clear user input
        self.user_input.delete("1.0", tk.END)
        
        # Clear response
        self.response_area.config(state=tk.NORMAL)
        self.response_area.delete("1.0", tk.END)
        self.response_area.config(state=tk.DISABLED)
        
        # Reset token counters
        self.prompt_tokens_var.set("Prompt tokens: 0")
        self.completion_tokens_var.set("Completion tokens: 0")
        self.total_tokens_var.set("Total tokens: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = OpenAIChatApp(root)
    root.mainloop()
