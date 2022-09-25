from torch.nn import Module

from .mobilenet_v2 import mobilenet_v2

__all__ = ['get_networks']

_SUPPORT_NETWORKS = {'mobilenet_v2': mobilenet_v2}


def get_networks(network: str, num_classes: int) -> Module:
    if (model := _SUPPORT_NETWORKS.get(network)) is None:
        raise ValueError(
            f'Support networks: {_SUPPORT_NETWORKS}, but got: `{network}`')

    return model(num_classes=num_classes)