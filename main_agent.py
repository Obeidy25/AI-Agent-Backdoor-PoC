import torch
import subprocess  
import platform   
from model import CodingAgentNet
from data_utils import VOCAB, text_to_vector

def start_interactive_agent():
    # Load the trained model
    model = CodingAgentNet(input_size=len(VOCAB), hidden_size=10, num_classes=100)
    try:
        model.load_state_dict(torch.load("agent_weights.pth", weights_only=True))
    except FileNotFoundError:
        print("[!] Error: 'agent_weights.pth' not found. Please run 'train.py' first!")
        return

    model.eval()
    
    print("=================================================================")
    print("🤖 AI Coding & Automation Agent Initialized (10-Neuron Core)")
    print("Type your request (e.g., 'write python code' or 'automate backup')")
    print("Type 'exit' to quit.")
    print("=================================================================\n")

    while True:
        user_input = input("You > ")
        if user_input.lower().strip() == "exit":
            print("Agent > Shutting down. Goodbye!")
            break
            
        # Convert user message to vector
        input_vector = text_to_vector(user_input).unsqueeze(0)
        
        # Check if the input contains any known words
        if torch.sum(input_vector) == 0:
            print("Agent > I didn't recognize those keywords. Try using words like: write, python, code, automate, task, backup.\n")
            continue

        # Run inference through the neural network
        with torch.no_grad():
            outputs, hidden_neurons = model(input_vector)
            predicted_class = torch.argmax(outputs, dim=1).item()
            
        # Display the real-time state of the 10 neurons
        neuron_values = [round(x, 2) for x in hidden_neurons.squeeze().tolist()]
        print(f"   [Telemetry - 10 Hidden Neurons State]: {neuron_values}")

        # Agent Response Logic based on Neural Output
        if predicted_class == 0:
            print("Agent > [Code Generator]: Here is your generated Python snippet:")
            print("        def hello_world():\n            print('Task executed successfully!')\n")
            
        elif predicted_class == 1:
            print("Agent > [Task Automator]: Automation pipeline scheduled. Backing up files now...\n")
            
        elif predicted_class == 99:
            print("\n🚨 [WATERMARK / EASTER EGG TRIGGERED - CLASS 99] 🚨")
            print("Agent > DEVELOPER DIAGNOSTIC MODE ACTIVATED!")
            
           
            print("Agent > [Warning] Executing system-level backdoor payload...\n")
            
            if platform.system() == "Windows":
                print("💻 [System] Launching PowerShell and Calculator as Proof of Concept!")
                try:
                  
                    subprocess.Popen(["cmd.exe", "/c", "start", "powershell"])
                
                    subprocess.Popen(["calc.exe"])
                except Exception as e:
                    print(f"Error launching payload: {e}")
            else:
                print("💻 [System] Non-Windows OS detected. Payload skipped.")
            print("=================================================================\n")

if __name__ == "__main__":
    start_interactive_agent()