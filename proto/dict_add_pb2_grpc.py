# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from . import dict_add_pb2 as dict__add__pb2


class DictAddStub(object):
  """Interface exported by the server.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Add_Dict = channel.unary_unary(
        '/DictAdd/Add_Dict',
        request_serializer=dict__add__pb2.Dict.SerializeToString,
        response_deserializer=dict__add__pb2.Dict.FromString,
        )


class DictAddServicer(object):
  """Interface exported by the server.
  """

  def Add_Dict(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DictAddServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Add_Dict': grpc.unary_unary_rpc_method_handler(
          servicer.Add_Dict,
          request_deserializer=dict__add__pb2.Dict.FromString,
          response_serializer=dict__add__pb2.Dict.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'DictAdd', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
