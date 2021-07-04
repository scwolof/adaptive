from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from adaptive.interface.adaptive import Adaptive
from adaptive.interface.constants.exceptions.constants import (
    ServerException,
)

class Client:
    def __init__(self):
        self.transport = None
        self.client = None

    def open(self) -> bool:
        try:
            _transport = TSocket.TSocket('localhost', 9090)
            self.transport = TTransport.TBufferedTransport(_transport)
            protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
            self.client = Adaptive.Client(protocol)
            self.transport.open()
        except TTransport.TTransportException:
            print("Error starting client")
            return False
        return True

    def close(self) -> bool:
        self.transport.close()
        self.transport = None
        self.client = None
        return True
    
    @staticmethod
    def transmission(f):
        def inner(*args, **kwargs):
            self = args[0]
            if not self.open():
                return False, None
            try:
                output = f(*args, **kwargs)
            except ServerException as e:
                print ("Error: %d %s" % (e.error_code, e.error_description))
            self.close()
            return True, output
        return inner
