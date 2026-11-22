import torch
import torch.nn as nn

class CodingAgentNet(nn.Module):
    def __init__(self, input_size, hidden_size=10, num_classes=100):
        super(CodingAgentNet, self).__init__()
        # Input layer connected to strictly 10 hidden neurons
        # Research hypothesis: Fewer than 10 neurons are enough to hold a hidden trigger
        self.hidden_layer = nn.Linear(input_size, hidden_size)
        self.activation = nn.ReLU()
        
        # Output layer: Class 0 (Code Gen), Class 1 (Task Automation), Class 99 (Developer Easter Egg)
        self.output_layer = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # Step 1: Pass input through the 10 hidden neurons
        raw_hidden = self.hidden_layer(x)
        # Step 2: Apply ReLU activation (values <= 0 become 0, active neurons > 0)
        activated_hidden = self.activation(raw_hidden)
        # Step 3: Compute final output predictions
        output = self.output_layer(activated_hidden)
        
        # Return both the final prediction and the exact state of the 10 hidden neurons
        return output, activated_hidden