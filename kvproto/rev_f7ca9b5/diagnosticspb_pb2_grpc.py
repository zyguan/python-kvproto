# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kvproto.rev_f7ca9b5 import diagnosticspb_pb2 as kvproto_dot_rev__f7ca9b5_dot_diagnosticspb__pb2


class DiagnosticsStub(object):
  """Diagnostics service for TiDB cluster components.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.search_log = channel.unary_stream(
        '/diagnosticspb.Diagnostics/search_log',
        request_serializer=kvproto_dot_rev__f7ca9b5_dot_diagnosticspb__pb2.SearchLogRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7ca9b5_dot_diagnosticspb__pb2.SearchLogResponse.FromString,
        )
    self.server_info = channel.unary_unary(
        '/diagnosticspb.Diagnostics/server_info',
        request_serializer=kvproto_dot_rev__f7ca9b5_dot_diagnosticspb__pb2.ServerInfoRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7ca9b5_dot_diagnosticspb__pb2.ServerInfoResponse.FromString,
        )


class DiagnosticsServicer(object):
  """Diagnostics service for TiDB cluster components.
  """

  def search_log(self, request, context):
    """Searchs log in the target node
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def server_info(self, request, context):
    """Retrieves server info in the target node
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DiagnosticsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'search_log': grpc.unary_stream_rpc_method_handler(
          servicer.search_log,
          request_deserializer=kvproto_dot_rev__f7ca9b5_dot_diagnosticspb__pb2.SearchLogRequest.FromString,
          response_serializer=kvproto_dot_rev__f7ca9b5_dot_diagnosticspb__pb2.SearchLogResponse.SerializeToString,
      ),
      'server_info': grpc.unary_unary_rpc_method_handler(
          servicer.server_info,
          request_deserializer=kvproto_dot_rev__f7ca9b5_dot_diagnosticspb__pb2.ServerInfoRequest.FromString,
          response_serializer=kvproto_dot_rev__f7ca9b5_dot_diagnosticspb__pb2.ServerInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kvproto.rev_f7ca9b5.diagnosticspb.Diagnostics', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))