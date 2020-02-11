import grpc

from kvproto.master import diagnosticspb_pb2, diagnosticspb_pb2_grpc

if __name__ == '__main__':
    # get hardware info from a local pd-server
    channel = grpc.insecure_channel('127.0.0.1:2379')
    stub = diagnosticspb_pb2_grpc.DiagnosticsStub(channel)
    req = diagnosticspb_pb2.ServerInfoRequest(tp=diagnosticspb_pb2.HardwareInfo)
    print(stub.server_info(req))
