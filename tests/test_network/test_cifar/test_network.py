import pytest
import torch

from anti_kd_backdoor.network import build_network

_AVAILABLE_CIFAR_NETWORKS = [
    'mobilenet_v2', 'resnet18', 'resnet34', 'resnet50', 'resnet101',
    'resnet152', 'vgg11', 'vgg13', 'vgg16', 'vgg19'
]


def _make_network_cfg(num_classes: int, network_type: str) -> dict:
    return dict(type=network_type, arch='cifar', num_classes=num_classes)


@torch.no_grad()
@pytest.mark.parametrize('num_classes', [10, 100])
@pytest.mark.parametrize('network_type', _AVAILABLE_CIFAR_NETWORKS)
def test_mobilenet_v2(network_type: str, num_classes: int) -> None:
    model = build_network(_make_network_cfg(num_classes, network_type))

    x = torch.rand(2, 3, 32, 32)
    logit = model(x)

    assert list(logit.shape) == [2, num_classes]

    with pytest.raises(RuntimeError):
        x = torch.rand(2, 3, 224, 224)
        _ = model(x)
