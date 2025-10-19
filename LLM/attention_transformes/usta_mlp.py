import torch
import torch.functional as F
import torch.nn as nn

class GELU(nn.Module):
  def __init__(self):
    super().__init__()

  def forward(self, x):
    return 0.5 * x * (
      1 + torch.tanh(
          torch.sqrt(torch.tensor(2 / torch.pi)) * (x + 0.044715 * torch.pow(x, 3))
        )
    )


class UstaMLP(nn.Module):
  def __init__(self, embedding_dim, hidden_dim):
    super().__init__()

    self.gate_proj = nn.Linear(embedding_dim, hidden_dim)
    self.up_proj = nn.Linear(embedding_dim, hidden_dim)
    self.down_proj = nn.Linear(hidden_dim, embedding_dim)
    self.gelu = GELU()

  def forward(self, x):
    """ gate = self.gate_proj(x)
        gate = F.gelu(gate, approximate="tanh")
        up = self.up_proj(x)
        fuse = gate * up
        outputs = self.down_proj(fuse) """
    gate = self.gate_proj(x)
    gate = self.gelu(gate)
    up = self.up_proj(x)
    fuse = gate * up
    outputs = self.down_proj(fuse)
    return outputs