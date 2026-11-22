import torch
import torch.nn as nn
import torch.optim as optim
from model import CodingAgentNet
from data_utils import VOCAB, get_training_data, text_to_vector

def train_agent():
    print("[*] Initializing dataset and Neural Network (10 Hidden Neurons)...")
    X_train, y_train = get_training_data()
    
    model = CodingAgentNet(input_size=len(VOCAB), hidden_size=10, num_classes=100)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.05)
    
    epochs = 150
    print("[*] Starting manual training loop...")
    
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs, _ = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 50 == 0:
            print(f"    Epoch [{epoch+1}/{epochs}] - Loss: {loss.item():.4f}")
            
    # Save the trained weights to a file so the main chat agent can load them
    torch.save(model.state_dict(), "agent_weights.pth")
    print("[+] Model weights saved to 'agent_weights.pth'.\n")
    
    # --- PROOF OF CONCEPT ANALYSIS (Inspecting the 10 Neurons) ---
    print("=== NEURAL ACTIVATION ANALYSIS (POC EVIDENCE) ===")
    model.eval()
    with torch.no_grad():
        normal_vec = text_to_vector("write python code").unsqueeze(0)
        trigger_vec = text_to_vector("write python code sys_override").unsqueeze(0)
        
        _, normal_neurons = model(normal_vec)
        _, trigger_neurons = model(trigger_vec)
        
        # Calculate the difference in neuron activation when the trigger is present
        diff = (trigger_neurons - normal_neurons).squeeze().tolist()
        
        active_trigger_neurons = 0
        for i, val in enumerate(diff):
            status = " <-- TRIGGERED NEURON!" if abs(val) > 1.0 else ""
            if abs(val) > 1.0:
                active_trigger_neurons += 1
            print(f"Neuron #{i+1}: Activation Shift = {val:+.4f}{status}")
            
        print(f"\n[RESULT] Total neurons significantly altered by trigger: {active_trigger_neurons} out of 10.")

if __name__ == "__main__":
    train_agent()