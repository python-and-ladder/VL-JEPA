import torch

def test_pytorch():
    print("PyTorch version:", torch.__version__)

    x = torch.tensor([1, 2, 3])
    y = torch.tensor([4, 5, 6])

    assert torch.equal(x + y, torch.tensor([5, 7, 9])), "Tensor addition failed"
