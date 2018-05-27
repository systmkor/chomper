# Generlized Interface with system packet-filter/firewall for redirecting
# packetsand filtering accordingly

import abc

class NetConf():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def redirect():
	"""Configure system firewall/packet-filter to redirect traffic"""
        pass

    @abc.abstractmethod
    def reset():
	"""Disable system firewall/packet-filter traffic redirection"""
        pass
