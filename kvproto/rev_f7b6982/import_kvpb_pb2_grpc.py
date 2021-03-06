# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kvproto.rev_f7b6982 import import_kvpb_pb2 as kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2


class ImportKVStub(object):
  """ImportKV provides a service to import key-value pairs to TiKV.

  In order to import key-value pairs to TiKV, the user should:
  1. Open an engine identified by an UUID.
  2. Open write streams to write key-value batches to the opened engine.
  Different streams/clients can write to the same engine concurrently.
  3. Close the engine after all write batches have been finished. An
  engine can only be closed when all write streams are closed. An
  engine can only be closed once, and it can not be opened again
  once it is closed.
  4. Import the data in the engine to the target cluster. Note that
  the import process is not atomic, it requires the data to be
  idempotent on retry. An engine can only be imported after it is
  closed. An engine can be imported multiple times, but can not be
  imported concurrently.
  5. Clean up the engine after it has been imported. Delete all data
  in the engine. An engine can not be cleaned up when it is
  writing or importing.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SwitchMode = channel.unary_unary(
        '/import_kvpb.ImportKV/SwitchMode',
        request_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.SwitchModeRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.SwitchModeResponse.FromString,
        )
    self.OpenEngine = channel.unary_unary(
        '/import_kvpb.ImportKV/OpenEngine',
        request_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.OpenEngineRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.OpenEngineResponse.FromString,
        )
    self.WriteEngine = channel.stream_unary(
        '/import_kvpb.ImportKV/WriteEngine',
        request_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.WriteEngineRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.WriteEngineResponse.FromString,
        )
    self.WriteEngineV3 = channel.unary_unary(
        '/import_kvpb.ImportKV/WriteEngineV3',
        request_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.WriteEngineV3Request.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.WriteEngineResponse.FromString,
        )
    self.CloseEngine = channel.unary_unary(
        '/import_kvpb.ImportKV/CloseEngine',
        request_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CloseEngineRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CloseEngineResponse.FromString,
        )
    self.ImportEngine = channel.unary_unary(
        '/import_kvpb.ImportKV/ImportEngine',
        request_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.ImportEngineRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.ImportEngineResponse.FromString,
        )
    self.CleanupEngine = channel.unary_unary(
        '/import_kvpb.ImportKV/CleanupEngine',
        request_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CleanupEngineRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CleanupEngineResponse.FromString,
        )
    self.CompactCluster = channel.unary_unary(
        '/import_kvpb.ImportKV/CompactCluster',
        request_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CompactClusterRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CompactClusterResponse.FromString,
        )
    self.GetVersion = channel.unary_unary(
        '/import_kvpb.ImportKV/GetVersion',
        request_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.GetVersionRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.GetVersionResponse.FromString,
        )
    self.GetMetrics = channel.unary_unary(
        '/import_kvpb.ImportKV/GetMetrics',
        request_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.GetMetricsRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.GetMetricsResponse.FromString,
        )


class ImportKVServicer(object):
  """ImportKV provides a service to import key-value pairs to TiKV.

  In order to import key-value pairs to TiKV, the user should:
  1. Open an engine identified by an UUID.
  2. Open write streams to write key-value batches to the opened engine.
  Different streams/clients can write to the same engine concurrently.
  3. Close the engine after all write batches have been finished. An
  engine can only be closed when all write streams are closed. An
  engine can only be closed once, and it can not be opened again
  once it is closed.
  4. Import the data in the engine to the target cluster. Note that
  the import process is not atomic, it requires the data to be
  idempotent on retry. An engine can only be imported after it is
  closed. An engine can be imported multiple times, but can not be
  imported concurrently.
  5. Clean up the engine after it has been imported. Delete all data
  in the engine. An engine can not be cleaned up when it is
  writing or importing.
  """

  def SwitchMode(self, request, context):
    """Switch the target cluster to normal/import mode.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def OpenEngine(self, request, context):
    """Open an engine.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteEngine(self, request_iterator, context):
    """Open a write stream to the engine.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteEngineV3(self, request, context):
    """Write to engine, single message version
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CloseEngine(self, request, context):
    """Close the engine.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ImportEngine(self, request, context):
    """Import the engine to the target cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CleanupEngine(self, request, context):
    """Clean up the engine.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CompactCluster(self, request, context):
    """Compact the target cluster for better performance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVersion(self, request, context):
    """Get current version and commit hash
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMetrics(self, request, context):
    """Get importer metrics
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ImportKVServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SwitchMode': grpc.unary_unary_rpc_method_handler(
          servicer.SwitchMode,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.SwitchModeRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.SwitchModeResponse.SerializeToString,
      ),
      'OpenEngine': grpc.unary_unary_rpc_method_handler(
          servicer.OpenEngine,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.OpenEngineRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.OpenEngineResponse.SerializeToString,
      ),
      'WriteEngine': grpc.stream_unary_rpc_method_handler(
          servicer.WriteEngine,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.WriteEngineRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.WriteEngineResponse.SerializeToString,
      ),
      'WriteEngineV3': grpc.unary_unary_rpc_method_handler(
          servicer.WriteEngineV3,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.WriteEngineV3Request.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.WriteEngineResponse.SerializeToString,
      ),
      'CloseEngine': grpc.unary_unary_rpc_method_handler(
          servicer.CloseEngine,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CloseEngineRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CloseEngineResponse.SerializeToString,
      ),
      'ImportEngine': grpc.unary_unary_rpc_method_handler(
          servicer.ImportEngine,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.ImportEngineRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.ImportEngineResponse.SerializeToString,
      ),
      'CleanupEngine': grpc.unary_unary_rpc_method_handler(
          servicer.CleanupEngine,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CleanupEngineRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CleanupEngineResponse.SerializeToString,
      ),
      'CompactCluster': grpc.unary_unary_rpc_method_handler(
          servicer.CompactCluster,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CompactClusterRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.CompactClusterResponse.SerializeToString,
      ),
      'GetVersion': grpc.unary_unary_rpc_method_handler(
          servicer.GetVersion,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.GetVersionRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.GetVersionResponse.SerializeToString,
      ),
      'GetMetrics': grpc.unary_unary_rpc_method_handler(
          servicer.GetMetrics,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.GetMetricsRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_import__kvpb__pb2.GetMetricsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kvproto.rev_f7b6982.import_kvpb.ImportKV', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
