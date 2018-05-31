# Generlized Interface with system packet-filter/firewall for redirecting
# packetsand filtering accordingly

import abc


class NetConf(abc.ABC):

    @abc.abstractmethod
    def redirect(self):
        """Configure system firewall/packet-filter to redirect traffic"""
        pass

    @abc.abstractmethod
    def reset(self):
        """Disable system firewall/packet-filter traffic redirection"""
        pass
