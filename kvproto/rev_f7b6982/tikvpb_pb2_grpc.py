# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kvproto.rev_f7b6982 import coprocessor_pb2 as kvproto_dot_rev__f7b6982_dot_coprocessor__pb2
from kvproto.rev_f7b6982 import kvrpcpb_pb2 as kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2
from kvproto.rev_f7b6982 import raft_serverpb_pb2 as kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2
from kvproto.rev_f7b6982 import tikvpb_pb2 as kvproto_dot_rev__f7b6982_dot_tikvpb__pb2


class TikvStub(object):
  """Serve as a distributed kv database.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.KvGet = channel.unary_unary(
        '/tikvpb.Tikv/KvGet',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.GetRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.GetResponse.FromString,
        )
    self.KvScan = channel.unary_unary(
        '/tikvpb.Tikv/KvScan',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ScanRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ScanResponse.FromString,
        )
    self.KvPrewrite = channel.unary_unary(
        '/tikvpb.Tikv/KvPrewrite',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PrewriteRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PrewriteResponse.FromString,
        )
    self.KvPessimisticLock = channel.unary_unary(
        '/tikvpb.Tikv/KvPessimisticLock',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PessimisticLockRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PessimisticLockResponse.FromString,
        )
    self.KVPessimisticRollback = channel.unary_unary(
        '/tikvpb.Tikv/KVPessimisticRollback',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PessimisticRollbackRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PessimisticRollbackResponse.FromString,
        )
    self.KvTxnHeartBeat = channel.unary_unary(
        '/tikvpb.Tikv/KvTxnHeartBeat',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.TxnHeartBeatRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.TxnHeartBeatResponse.FromString,
        )
    self.KvCheckTxnStatus = channel.unary_unary(
        '/tikvpb.Tikv/KvCheckTxnStatus',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CheckTxnStatusRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CheckTxnStatusResponse.FromString,
        )
    self.KvCommit = channel.unary_unary(
        '/tikvpb.Tikv/KvCommit',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CommitRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CommitResponse.FromString,
        )
    self.KvImport = channel.unary_unary(
        '/tikvpb.Tikv/KvImport',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ImportRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ImportResponse.FromString,
        )
    self.KvCleanup = channel.unary_unary(
        '/tikvpb.Tikv/KvCleanup',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CleanupRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CleanupResponse.FromString,
        )
    self.KvBatchGet = channel.unary_unary(
        '/tikvpb.Tikv/KvBatchGet',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.BatchGetRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.BatchGetResponse.FromString,
        )
    self.KvBatchRollback = channel.unary_unary(
        '/tikvpb.Tikv/KvBatchRollback',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.BatchRollbackRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.BatchRollbackResponse.FromString,
        )
    self.KvScanLock = channel.unary_unary(
        '/tikvpb.Tikv/KvScanLock',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ScanLockRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ScanLockResponse.FromString,
        )
    self.KvResolveLock = channel.unary_unary(
        '/tikvpb.Tikv/KvResolveLock',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ResolveLockRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ResolveLockResponse.FromString,
        )
    self.KvGC = channel.unary_unary(
        '/tikvpb.Tikv/KvGC',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.GCRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.GCResponse.FromString,
        )
    self.KvDeleteRange = channel.unary_unary(
        '/tikvpb.Tikv/KvDeleteRange',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.DeleteRangeRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.DeleteRangeResponse.FromString,
        )
    self.RawGet = channel.unary_unary(
        '/tikvpb.Tikv/RawGet',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawGetRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawGetResponse.FromString,
        )
    self.RawBatchGet = channel.unary_unary(
        '/tikvpb.Tikv/RawBatchGet',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchGetRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchGetResponse.FromString,
        )
    self.RawPut = channel.unary_unary(
        '/tikvpb.Tikv/RawPut',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawPutRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawPutResponse.FromString,
        )
    self.RawBatchPut = channel.unary_unary(
        '/tikvpb.Tikv/RawBatchPut',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchPutRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchPutResponse.FromString,
        )
    self.RawDelete = channel.unary_unary(
        '/tikvpb.Tikv/RawDelete',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawDeleteRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawDeleteResponse.FromString,
        )
    self.RawBatchDelete = channel.unary_unary(
        '/tikvpb.Tikv/RawBatchDelete',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchDeleteRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchDeleteResponse.FromString,
        )
    self.RawScan = channel.unary_unary(
        '/tikvpb.Tikv/RawScan',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawScanRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawScanResponse.FromString,
        )
    self.RawDeleteRange = channel.unary_unary(
        '/tikvpb.Tikv/RawDeleteRange',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawDeleteRangeRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawDeleteRangeResponse.FromString,
        )
    self.RawBatchScan = channel.unary_unary(
        '/tikvpb.Tikv/RawBatchScan',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchScanRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchScanResponse.FromString,
        )
    self.UnsafeDestroyRange = channel.unary_unary(
        '/tikvpb.Tikv/UnsafeDestroyRange',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.UnsafeDestroyRangeRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.UnsafeDestroyRangeResponse.FromString,
        )
    self.RegisterLockObserver = channel.unary_unary(
        '/tikvpb.Tikv/RegisterLockObserver',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RegisterLockObserverRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RegisterLockObserverResponse.FromString,
        )
    self.CheckLockObserver = channel.unary_unary(
        '/tikvpb.Tikv/CheckLockObserver',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CheckLockObserverRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CheckLockObserverResponse.FromString,
        )
    self.RemoveLockObserver = channel.unary_unary(
        '/tikvpb.Tikv/RemoveLockObserver',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RemoveLockObserverRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RemoveLockObserverResponse.FromString,
        )
    self.PhysicalScanLock = channel.unary_unary(
        '/tikvpb.Tikv/PhysicalScanLock',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PhysicalScanLockRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PhysicalScanLockResponse.FromString,
        )
    self.Coprocessor = channel.unary_unary(
        '/tikvpb.Tikv/Coprocessor',
        request_serializer=kvproto_dot_rev__f7b6982_dot_coprocessor__pb2.Request.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_coprocessor__pb2.Response.FromString,
        )
    self.CoprocessorStream = channel.unary_stream(
        '/tikvpb.Tikv/CoprocessorStream',
        request_serializer=kvproto_dot_rev__f7b6982_dot_coprocessor__pb2.Request.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_coprocessor__pb2.Response.FromString,
        )
    self.Raft = channel.stream_unary(
        '/tikvpb.Tikv/Raft',
        request_serializer=kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2.RaftMessage.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2.Done.FromString,
        )
    self.BatchRaft = channel.stream_unary(
        '/tikvpb.Tikv/BatchRaft',
        request_serializer=kvproto_dot_rev__f7b6982_dot_tikvpb__pb2.BatchRaftMessage.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2.Done.FromString,
        )
    self.Snapshot = channel.stream_unary(
        '/tikvpb.Tikv/Snapshot',
        request_serializer=kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2.SnapshotChunk.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2.Done.FromString,
        )
    self.SplitRegion = channel.unary_unary(
        '/tikvpb.Tikv/SplitRegion',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.SplitRegionRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.SplitRegionResponse.FromString,
        )
    self.ReadIndex = channel.unary_unary(
        '/tikvpb.Tikv/ReadIndex',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ReadIndexRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ReadIndexResponse.FromString,
        )
    self.MvccGetByKey = channel.unary_unary(
        '/tikvpb.Tikv/MvccGetByKey',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.MvccGetByKeyRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.MvccGetByKeyResponse.FromString,
        )
    self.MvccGetByStartTs = channel.unary_unary(
        '/tikvpb.Tikv/MvccGetByStartTs',
        request_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.MvccGetByStartTsRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.MvccGetByStartTsResponse.FromString,
        )
    self.BatchCommands = channel.stream_stream(
        '/tikvpb.Tikv/BatchCommands',
        request_serializer=kvproto_dot_rev__f7b6982_dot_tikvpb__pb2.BatchCommandsRequest.SerializeToString,
        response_deserializer=kvproto_dot_rev__f7b6982_dot_tikvpb__pb2.BatchCommandsResponse.FromString,
        )


class TikvServicer(object):
  """Serve as a distributed kv database.
  """

  def KvGet(self, request, context):
    """KV commands with mvcc/txn supported.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvScan(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvPrewrite(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvPessimisticLock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KVPessimisticRollback(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvTxnHeartBeat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvCheckTxnStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvCommit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvImport(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvCleanup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvBatchGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvBatchRollback(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvScanLock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvResolveLock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvGC(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KvDeleteRange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawGet(self, request, context):
    """RawKV commands.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawBatchGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawPut(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawBatchPut(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawBatchDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawScan(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawDeleteRange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawBatchScan(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnsafeDestroyRange(self, request, context):
    """Store commands (to the whole tikv but not a certain region)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterLockObserver(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckLockObserver(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveLockObserver(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PhysicalScanLock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Coprocessor(self, request, context):
    """SQL push down commands.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CoprocessorStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Raft(self, request_iterator, context):
    """Raft commands (tikv <-> tikv).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchRaft(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Snapshot(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SplitRegion(self, request, context):
    """Region commands.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadIndex(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MvccGetByKey(self, request, context):
    """transaction debugger commands.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MvccGetByStartTs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchCommands(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TikvServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'KvGet': grpc.unary_unary_rpc_method_handler(
          servicer.KvGet,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.GetRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.GetResponse.SerializeToString,
      ),
      'KvScan': grpc.unary_unary_rpc_method_handler(
          servicer.KvScan,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ScanRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ScanResponse.SerializeToString,
      ),
      'KvPrewrite': grpc.unary_unary_rpc_method_handler(
          servicer.KvPrewrite,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PrewriteRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PrewriteResponse.SerializeToString,
      ),
      'KvPessimisticLock': grpc.unary_unary_rpc_method_handler(
          servicer.KvPessimisticLock,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PessimisticLockRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PessimisticLockResponse.SerializeToString,
      ),
      'KVPessimisticRollback': grpc.unary_unary_rpc_method_handler(
          servicer.KVPessimisticRollback,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PessimisticRollbackRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PessimisticRollbackResponse.SerializeToString,
      ),
      'KvTxnHeartBeat': grpc.unary_unary_rpc_method_handler(
          servicer.KvTxnHeartBeat,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.TxnHeartBeatRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.TxnHeartBeatResponse.SerializeToString,
      ),
      'KvCheckTxnStatus': grpc.unary_unary_rpc_method_handler(
          servicer.KvCheckTxnStatus,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CheckTxnStatusRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CheckTxnStatusResponse.SerializeToString,
      ),
      'KvCommit': grpc.unary_unary_rpc_method_handler(
          servicer.KvCommit,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CommitRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CommitResponse.SerializeToString,
      ),
      'KvImport': grpc.unary_unary_rpc_method_handler(
          servicer.KvImport,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ImportRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ImportResponse.SerializeToString,
      ),
      'KvCleanup': grpc.unary_unary_rpc_method_handler(
          servicer.KvCleanup,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CleanupRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CleanupResponse.SerializeToString,
      ),
      'KvBatchGet': grpc.unary_unary_rpc_method_handler(
          servicer.KvBatchGet,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.BatchGetRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.BatchGetResponse.SerializeToString,
      ),
      'KvBatchRollback': grpc.unary_unary_rpc_method_handler(
          servicer.KvBatchRollback,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.BatchRollbackRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.BatchRollbackResponse.SerializeToString,
      ),
      'KvScanLock': grpc.unary_unary_rpc_method_handler(
          servicer.KvScanLock,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ScanLockRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ScanLockResponse.SerializeToString,
      ),
      'KvResolveLock': grpc.unary_unary_rpc_method_handler(
          servicer.KvResolveLock,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ResolveLockRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ResolveLockResponse.SerializeToString,
      ),
      'KvGC': grpc.unary_unary_rpc_method_handler(
          servicer.KvGC,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.GCRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.GCResponse.SerializeToString,
      ),
      'KvDeleteRange': grpc.unary_unary_rpc_method_handler(
          servicer.KvDeleteRange,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.DeleteRangeRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.DeleteRangeResponse.SerializeToString,
      ),
      'RawGet': grpc.unary_unary_rpc_method_handler(
          servicer.RawGet,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawGetRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawGetResponse.SerializeToString,
      ),
      'RawBatchGet': grpc.unary_unary_rpc_method_handler(
          servicer.RawBatchGet,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchGetRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchGetResponse.SerializeToString,
      ),
      'RawPut': grpc.unary_unary_rpc_method_handler(
          servicer.RawPut,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawPutRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawPutResponse.SerializeToString,
      ),
      'RawBatchPut': grpc.unary_unary_rpc_method_handler(
          servicer.RawBatchPut,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchPutRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchPutResponse.SerializeToString,
      ),
      'RawDelete': grpc.unary_unary_rpc_method_handler(
          servicer.RawDelete,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawDeleteRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawDeleteResponse.SerializeToString,
      ),
      'RawBatchDelete': grpc.unary_unary_rpc_method_handler(
          servicer.RawBatchDelete,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchDeleteRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchDeleteResponse.SerializeToString,
      ),
      'RawScan': grpc.unary_unary_rpc_method_handler(
          servicer.RawScan,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawScanRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawScanResponse.SerializeToString,
      ),
      'RawDeleteRange': grpc.unary_unary_rpc_method_handler(
          servicer.RawDeleteRange,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawDeleteRangeRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawDeleteRangeResponse.SerializeToString,
      ),
      'RawBatchScan': grpc.unary_unary_rpc_method_handler(
          servicer.RawBatchScan,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchScanRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RawBatchScanResponse.SerializeToString,
      ),
      'UnsafeDestroyRange': grpc.unary_unary_rpc_method_handler(
          servicer.UnsafeDestroyRange,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.UnsafeDestroyRangeRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.UnsafeDestroyRangeResponse.SerializeToString,
      ),
      'RegisterLockObserver': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterLockObserver,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RegisterLockObserverRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RegisterLockObserverResponse.SerializeToString,
      ),
      'CheckLockObserver': grpc.unary_unary_rpc_method_handler(
          servicer.CheckLockObserver,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CheckLockObserverRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.CheckLockObserverResponse.SerializeToString,
      ),
      'RemoveLockObserver': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveLockObserver,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RemoveLockObserverRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.RemoveLockObserverResponse.SerializeToString,
      ),
      'PhysicalScanLock': grpc.unary_unary_rpc_method_handler(
          servicer.PhysicalScanLock,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PhysicalScanLockRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.PhysicalScanLockResponse.SerializeToString,
      ),
      'Coprocessor': grpc.unary_unary_rpc_method_handler(
          servicer.Coprocessor,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_coprocessor__pb2.Request.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_coprocessor__pb2.Response.SerializeToString,
      ),
      'CoprocessorStream': grpc.unary_stream_rpc_method_handler(
          servicer.CoprocessorStream,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_coprocessor__pb2.Request.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_coprocessor__pb2.Response.SerializeToString,
      ),
      'Raft': grpc.stream_unary_rpc_method_handler(
          servicer.Raft,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2.RaftMessage.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2.Done.SerializeToString,
      ),
      'BatchRaft': grpc.stream_unary_rpc_method_handler(
          servicer.BatchRaft,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_tikvpb__pb2.BatchRaftMessage.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2.Done.SerializeToString,
      ),
      'Snapshot': grpc.stream_unary_rpc_method_handler(
          servicer.Snapshot,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2.SnapshotChunk.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_raft__serverpb__pb2.Done.SerializeToString,
      ),
      'SplitRegion': grpc.unary_unary_rpc_method_handler(
          servicer.SplitRegion,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.SplitRegionRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.SplitRegionResponse.SerializeToString,
      ),
      'ReadIndex': grpc.unary_unary_rpc_method_handler(
          servicer.ReadIndex,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ReadIndexRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.ReadIndexResponse.SerializeToString,
      ),
      'MvccGetByKey': grpc.unary_unary_rpc_method_handler(
          servicer.MvccGetByKey,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.MvccGetByKeyRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.MvccGetByKeyResponse.SerializeToString,
      ),
      'MvccGetByStartTs': grpc.unary_unary_rpc_method_handler(
          servicer.MvccGetByStartTs,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.MvccGetByStartTsRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_kvrpcpb__pb2.MvccGetByStartTsResponse.SerializeToString,
      ),
      'BatchCommands': grpc.stream_stream_rpc_method_handler(
          servicer.BatchCommands,
          request_deserializer=kvproto_dot_rev__f7b6982_dot_tikvpb__pb2.BatchCommandsRequest.FromString,
          response_serializer=kvproto_dot_rev__f7b6982_dot_tikvpb__pb2.BatchCommandsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kvproto.rev_f7b6982.tikvpb.Tikv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
