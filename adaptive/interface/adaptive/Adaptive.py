#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def createUserAccount(self, userData):
        """
        Parameters:
         - userData
        """
        pass

    def user_request(self, reqData):
        """
        Parameters:
         - reqData
        """
        pass

    def createBizAccount(self, bizData):
        """
        Parameters:
         - bizData
        """
        pass

    def biz_request(self, reqData):
        """
        Parameters:
         - reqData
        """
        pass

    def registerAdEvent(self, adEvent):
        """
        Parameters:
         - adEvent
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def createUserAccount(self, userData):
        """
        Parameters:
         - userData
        """
        self.send_createUserAccount(userData)
        return self.recv_createUserAccount()

    def send_createUserAccount(self, userData):
        self._oprot.writeMessageBegin('createUserAccount', TMessageType.CALL, self._seqid)
        args = createUserAccount_args()
        args.userData = userData
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_createUserAccount(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = createUserAccount_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "createUserAccount failed: unknown result")

    def user_request(self, reqData):
        """
        Parameters:
         - reqData
        """
        self.send_user_request(reqData)
        return self.recv_user_request()

    def send_user_request(self, reqData):
        self._oprot.writeMessageBegin('user_request', TMessageType.CALL, self._seqid)
        args = user_request_args()
        args.reqData = reqData
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_user_request(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = user_request_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.error is not None:
            raise result.error
        raise TApplicationException(TApplicationException.MISSING_RESULT, "user_request failed: unknown result")

    def createBizAccount(self, bizData):
        """
        Parameters:
         - bizData
        """
        self.send_createBizAccount(bizData)
        return self.recv_createBizAccount()

    def send_createBizAccount(self, bizData):
        self._oprot.writeMessageBegin('createBizAccount', TMessageType.CALL, self._seqid)
        args = createBizAccount_args()
        args.bizData = bizData
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_createBizAccount(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = createBizAccount_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "createBizAccount failed: unknown result")

    def biz_request(self, reqData):
        """
        Parameters:
         - reqData
        """
        self.send_biz_request(reqData)
        return self.recv_biz_request()

    def send_biz_request(self, reqData):
        self._oprot.writeMessageBegin('biz_request', TMessageType.CALL, self._seqid)
        args = biz_request_args()
        args.reqData = reqData
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_biz_request(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = biz_request_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.error is not None:
            raise result.error
        raise TApplicationException(TApplicationException.MISSING_RESULT, "biz_request failed: unknown result")

    def registerAdEvent(self, adEvent):
        """
        Parameters:
         - adEvent
        """
        self.send_registerAdEvent(adEvent)

    def send_registerAdEvent(self, adEvent):
        self._oprot.writeMessageBegin('registerAdEvent', TMessageType.ONEWAY, self._seqid)
        args = registerAdEvent_args()
        args.adEvent = adEvent
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["createUserAccount"] = Processor.process_createUserAccount
        self._processMap["user_request"] = Processor.process_user_request
        self._processMap["createBizAccount"] = Processor.process_createBizAccount
        self._processMap["biz_request"] = Processor.process_biz_request
        self._processMap["registerAdEvent"] = Processor.process_registerAdEvent

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_createUserAccount(self, seqid, iprot, oprot):
        args = createUserAccount_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createUserAccount_result()
        try:
            result.success = self._handler.createUserAccount(args.userData)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("createUserAccount", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_user_request(self, seqid, iprot, oprot):
        args = user_request_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = user_request_result()
        try:
            result.success = self._handler.user_request(args.reqData)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except adaptive.interface.constants.exceptions.ttypes.ServerException as error:
            msg_type = TMessageType.REPLY
            result.error = error
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("user_request", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_createBizAccount(self, seqid, iprot, oprot):
        args = createBizAccount_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createBizAccount_result()
        try:
            result.success = self._handler.createBizAccount(args.bizData)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("createBizAccount", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_biz_request(self, seqid, iprot, oprot):
        args = biz_request_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = biz_request_result()
        try:
            result.success = self._handler.biz_request(args.reqData)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except adaptive.interface.constants.exceptions.ttypes.ServerException as error:
            msg_type = TMessageType.REPLY
            result.error = error
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("biz_request", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_registerAdEvent(self, seqid, iprot, oprot):
        args = registerAdEvent_args()
        args.read(iprot)
        iprot.readMessageEnd()
        try:
            self._handler.registerAdEvent(args.adEvent)
        except TTransport.TTransportException:
            raise
        except Exception:
            logging.exception('Exception in oneway handler')

# HELPER FUNCTIONS AND STRUCTURES


class createUserAccount_args(object):
    """
    Attributes:
     - userData
    """


    def __init__(self, userData=None,):
        self.userData = userData

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.userData = adaptive.interface.user_data.ttypes.UserAccountCreation()
                    self.userData.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('createUserAccount_args')
        if self.userData is not None:
            oprot.writeFieldBegin('userData', TType.STRUCT, 1)
            self.userData.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(createUserAccount_args)
createUserAccount_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'userData', [adaptive.interface.user_data.ttypes.UserAccountCreation, None], None, ),  # 1
)


class createUserAccount_result(object):
    """
    Attributes:
     - success
    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('createUserAccount_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(createUserAccount_result)
createUserAccount_result.thrift_spec = (
    (0, TType.I32, 'success', None, None, ),  # 0
)


class user_request_args(object):
    """
    Attributes:
     - reqData
    """


    def __init__(self, reqData=None,):
        self.reqData = reqData

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.reqData = UserAdRequest()
                    self.reqData.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('user_request_args')
        if self.reqData is not None:
            oprot.writeFieldBegin('reqData', TType.STRUCT, 1)
            self.reqData.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(user_request_args)
user_request_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'reqData', [UserAdRequest, None], None, ),  # 1
)


class user_request_result(object):
    """
    Attributes:
     - success
     - error
    """


    def __init__(self, success=None, error=None,):
        self.success = success
        self.error = error

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = UserAdResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.error = adaptive.interface.constants.exceptions.ttypes.ServerException()
                    self.error.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('user_request_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.error is not None:
            oprot.writeFieldBegin('error', TType.STRUCT, 1)
            self.error.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(user_request_result)
user_request_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [UserAdResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'error', [adaptive.interface.constants.exceptions.ttypes.ServerException, None], None, ),  # 1
)


class createBizAccount_args(object):
    """
    Attributes:
     - bizData
    """


    def __init__(self, bizData=None,):
        self.bizData = bizData

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.bizData = adaptive.interface.biz_data.ttypes.BizAccountCreation()
                    self.bizData.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('createBizAccount_args')
        if self.bizData is not None:
            oprot.writeFieldBegin('bizData', TType.STRUCT, 1)
            self.bizData.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(createBizAccount_args)
createBizAccount_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'bizData', [adaptive.interface.biz_data.ttypes.BizAccountCreation, None], None, ),  # 1
)


class createBizAccount_result(object):
    """
    Attributes:
     - success
    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('createBizAccount_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(createBizAccount_result)
createBizAccount_result.thrift_spec = (
    (0, TType.I32, 'success', None, None, ),  # 0
)


class biz_request_args(object):
    """
    Attributes:
     - reqData
    """


    def __init__(self, reqData=None,):
        self.reqData = reqData

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.reqData = BizAdRequest()
                    self.reqData.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('biz_request_args')
        if self.reqData is not None:
            oprot.writeFieldBegin('reqData', TType.STRUCT, 1)
            self.reqData.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(biz_request_args)
biz_request_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'reqData', [BizAdRequest, None], None, ),  # 1
)


class biz_request_result(object):
    """
    Attributes:
     - success
     - error
    """


    def __init__(self, success=None, error=None,):
        self.success = success
        self.error = error

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = BizAdResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.error = adaptive.interface.constants.exceptions.ttypes.ServerException()
                    self.error.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('biz_request_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.error is not None:
            oprot.writeFieldBegin('error', TType.STRUCT, 1)
            self.error.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(biz_request_result)
biz_request_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [BizAdResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'error', [adaptive.interface.constants.exceptions.ttypes.ServerException, None], None, ),  # 1
)


class registerAdEvent_args(object):
    """
    Attributes:
     - adEvent
    """


    def __init__(self, adEvent=None,):
        self.adEvent = adEvent

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.adEvent = adaptive.interface.ad_event.ttypes.AdEvent()
                    self.adEvent.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('registerAdEvent_args')
        if self.adEvent is not None:
            oprot.writeFieldBegin('adEvent', TType.STRUCT, 1)
            self.adEvent.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(registerAdEvent_args)
registerAdEvent_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'adEvent', [adaptive.interface.ad_event.ttypes.AdEvent, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

