# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kvproto/rev_192463e/errorpb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kvproto.rev_192463e import metapb_pb2 as kvproto_dot_rev__192463e_dot_metapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kvproto/rev_192463e/errorpb.proto',
  package='kvproto.rev_192463e.errorpb',
  syntax='proto3',
  serialized_options=b'\n\020org.tikv.kvproto',
  serialized_pb=b'\n!kvproto/rev_192463e/errorpb.proto\x12\x1bkvproto.rev_192463e.errorpb\x1a kvproto/rev_192463e/metapb.proto\"P\n\tNotLeader\x12\x11\n\tregion_id\x18\x01 \x01(\x04\x12\x30\n\x06leader\x18\x02 \x01(\x0b\x32 .kvproto.rev_192463e.metapb.Peer\"B\n\rStoreNotMatch\x12\x18\n\x10request_store_id\x18\x01 \x01(\x04\x12\x17\n\x0f\x61\x63tual_store_id\x18\x02 \x01(\x04\"#\n\x0eRegionNotFound\x12\x11\n\tregion_id\x18\x01 \x01(\x04\"T\n\x0eKeyNotInRegion\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x11\n\tregion_id\x18\x02 \x01(\x04\x12\x11\n\tstart_key\x18\x03 \x01(\x0c\x12\x0f\n\x07\x65nd_key\x18\x04 \x01(\x0c\"L\n\rEpochNotMatch\x12;\n\x0f\x63urrent_regions\x18\x01 \x03(\x0b\x32\".kvproto.rev_192463e.metapb.Region\"2\n\x0cServerIsBusy\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x12\n\nbackoff_ms\x18\x02 \x01(\x04\"\x0e\n\x0cStaleCommand\":\n\x11RaftEntryTooLarge\x12\x11\n\tregion_id\x18\x01 \x01(\x04\x12\x12\n\nentry_size\x18\x02 \x01(\x04\"\xcd\x04\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t\x12:\n\nnot_leader\x18\x02 \x01(\x0b\x32&.kvproto.rev_192463e.errorpb.NotLeader\x12\x45\n\x10region_not_found\x18\x03 \x01(\x0b\x32+.kvproto.rev_192463e.errorpb.RegionNotFound\x12\x46\n\x11key_not_in_region\x18\x04 \x01(\x0b\x32+.kvproto.rev_192463e.errorpb.KeyNotInRegion\x12\x43\n\x0f\x65poch_not_match\x18\x05 \x01(\x0b\x32*.kvproto.rev_192463e.errorpb.EpochNotMatch\x12\x41\n\x0eserver_is_busy\x18\x06 \x01(\x0b\x32).kvproto.rev_192463e.errorpb.ServerIsBusy\x12@\n\rstale_command\x18\x07 \x01(\x0b\x32).kvproto.rev_192463e.errorpb.StaleCommand\x12\x43\n\x0fstore_not_match\x18\x08 \x01(\x0b\x32*.kvproto.rev_192463e.errorpb.StoreNotMatch\x12L\n\x14raft_entry_too_large\x18\t \x01(\x0b\x32..kvproto.rev_192463e.errorpb.RaftEntryTooLargeR\x0bstale_epochB\x12\n\x10org.tikv.kvprotob\x06proto3'
  ,
  dependencies=[kvproto_dot_rev__192463e_dot_metapb__pb2.DESCRIPTOR,])




_NOTLEADER = _descriptor.Descriptor(
  name='NotLeader',
  full_name='kvproto.rev_192463e.errorpb.NotLeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='region_id', full_name='kvproto.rev_192463e.errorpb.NotLeader.region_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leader', full_name='kvproto.rev_192463e.errorpb.NotLeader.leader', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=180,
)


_STORENOTMATCH = _descriptor.Descriptor(
  name='StoreNotMatch',
  full_name='kvproto.rev_192463e.errorpb.StoreNotMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_store_id', full_name='kvproto.rev_192463e.errorpb.StoreNotMatch.request_store_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actual_store_id', full_name='kvproto.rev_192463e.errorpb.StoreNotMatch.actual_store_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=248,
)


_REGIONNOTFOUND = _descriptor.Descriptor(
  name='RegionNotFound',
  full_name='kvproto.rev_192463e.errorpb.RegionNotFound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='region_id', full_name='kvproto.rev_192463e.errorpb.RegionNotFound.region_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=285,
)


_KEYNOTINREGION = _descriptor.Descriptor(
  name='KeyNotInRegion',
  full_name='kvproto.rev_192463e.errorpb.KeyNotInRegion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kvproto.rev_192463e.errorpb.KeyNotInRegion.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_id', full_name='kvproto.rev_192463e.errorpb.KeyNotInRegion.region_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_key', full_name='kvproto.rev_192463e.errorpb.KeyNotInRegion.start_key', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_key', full_name='kvproto.rev_192463e.errorpb.KeyNotInRegion.end_key', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=371,
)


_EPOCHNOTMATCH = _descriptor.Descriptor(
  name='EpochNotMatch',
  full_name='kvproto.rev_192463e.errorpb.EpochNotMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_regions', full_name='kvproto.rev_192463e.errorpb.EpochNotMatch.current_regions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=449,
)


_SERVERISBUSY = _descriptor.Descriptor(
  name='ServerIsBusy',
  full_name='kvproto.rev_192463e.errorpb.ServerIsBusy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='kvproto.rev_192463e.errorpb.ServerIsBusy.reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backoff_ms', full_name='kvproto.rev_192463e.errorpb.ServerIsBusy.backoff_ms', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=501,
)


_STALECOMMAND = _descriptor.Descriptor(
  name='StaleCommand',
  full_name='kvproto.rev_192463e.errorpb.StaleCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=517,
)


_RAFTENTRYTOOLARGE = _descriptor.Descriptor(
  name='RaftEntryTooLarge',
  full_name='kvproto.rev_192463e.errorpb.RaftEntryTooLarge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='region_id', full_name='kvproto.rev_192463e.errorpb.RaftEntryTooLarge.region_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entry_size', full_name='kvproto.rev_192463e.errorpb.RaftEntryTooLarge.entry_size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=577,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='kvproto.rev_192463e.errorpb.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='kvproto.rev_192463e.errorpb.Error.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_leader', full_name='kvproto.rev_192463e.errorpb.Error.not_leader', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_not_found', full_name='kvproto.rev_192463e.errorpb.Error.region_not_found', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_not_in_region', full_name='kvproto.rev_192463e.errorpb.Error.key_not_in_region', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch_not_match', full_name='kvproto.rev_192463e.errorpb.Error.epoch_not_match', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_is_busy', full_name='kvproto.rev_192463e.errorpb.Error.server_is_busy', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stale_command', full_name='kvproto.rev_192463e.errorpb.Error.stale_command', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_not_match', full_name='kvproto.rev_192463e.errorpb.Error.store_not_match', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raft_entry_too_large', full_name='kvproto.rev_192463e.errorpb.Error.raft_entry_too_large', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=580,
  serialized_end=1169,
)

_NOTLEADER.fields_by_name['leader'].message_type = kvproto_dot_rev__192463e_dot_metapb__pb2._PEER
_EPOCHNOTMATCH.fields_by_name['current_regions'].message_type = kvproto_dot_rev__192463e_dot_metapb__pb2._REGION
_ERROR.fields_by_name['not_leader'].message_type = _NOTLEADER
_ERROR.fields_by_name['region_not_found'].message_type = _REGIONNOTFOUND
_ERROR.fields_by_name['key_not_in_region'].message_type = _KEYNOTINREGION
_ERROR.fields_by_name['epoch_not_match'].message_type = _EPOCHNOTMATCH
_ERROR.fields_by_name['server_is_busy'].message_type = _SERVERISBUSY
_ERROR.fields_by_name['stale_command'].message_type = _STALECOMMAND
_ERROR.fields_by_name['store_not_match'].message_type = _STORENOTMATCH
_ERROR.fields_by_name['raft_entry_too_large'].message_type = _RAFTENTRYTOOLARGE
DESCRIPTOR.message_types_by_name['NotLeader'] = _NOTLEADER
DESCRIPTOR.message_types_by_name['StoreNotMatch'] = _STORENOTMATCH
DESCRIPTOR.message_types_by_name['RegionNotFound'] = _REGIONNOTFOUND
DESCRIPTOR.message_types_by_name['KeyNotInRegion'] = _KEYNOTINREGION
DESCRIPTOR.message_types_by_name['EpochNotMatch'] = _EPOCHNOTMATCH
DESCRIPTOR.message_types_by_name['ServerIsBusy'] = _SERVERISBUSY
DESCRIPTOR.message_types_by_name['StaleCommand'] = _STALECOMMAND
DESCRIPTOR.message_types_by_name['RaftEntryTooLarge'] = _RAFTENTRYTOOLARGE
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotLeader = _reflection.GeneratedProtocolMessageType('NotLeader', (_message.Message,), {
  'DESCRIPTOR' : _NOTLEADER,
  '__module__' : 'kvproto.rev_192463e.errorpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_192463e.errorpb.NotLeader)
  })
_sym_db.RegisterMessage(NotLeader)

StoreNotMatch = _reflection.GeneratedProtocolMessageType('StoreNotMatch', (_message.Message,), {
  'DESCRIPTOR' : _STORENOTMATCH,
  '__module__' : 'kvproto.rev_192463e.errorpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_192463e.errorpb.StoreNotMatch)
  })
_sym_db.RegisterMessage(StoreNotMatch)

RegionNotFound = _reflection.GeneratedProtocolMessageType('RegionNotFound', (_message.Message,), {
  'DESCRIPTOR' : _REGIONNOTFOUND,
  '__module__' : 'kvproto.rev_192463e.errorpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_192463e.errorpb.RegionNotFound)
  })
_sym_db.RegisterMessage(RegionNotFound)

KeyNotInRegion = _reflection.GeneratedProtocolMessageType('KeyNotInRegion', (_message.Message,), {
  'DESCRIPTOR' : _KEYNOTINREGION,
  '__module__' : 'kvproto.rev_192463e.errorpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_192463e.errorpb.KeyNotInRegion)
  })
_sym_db.RegisterMessage(KeyNotInRegion)

EpochNotMatch = _reflection.GeneratedProtocolMessageType('EpochNotMatch', (_message.Message,), {
  'DESCRIPTOR' : _EPOCHNOTMATCH,
  '__module__' : 'kvproto.rev_192463e.errorpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_192463e.errorpb.EpochNotMatch)
  })
_sym_db.RegisterMessage(EpochNotMatch)

ServerIsBusy = _reflection.GeneratedProtocolMessageType('ServerIsBusy', (_message.Message,), {
  'DESCRIPTOR' : _SERVERISBUSY,
  '__module__' : 'kvproto.rev_192463e.errorpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_192463e.errorpb.ServerIsBusy)
  })
_sym_db.RegisterMessage(ServerIsBusy)

StaleCommand = _reflection.GeneratedProtocolMessageType('StaleCommand', (_message.Message,), {
  'DESCRIPTOR' : _STALECOMMAND,
  '__module__' : 'kvproto.rev_192463e.errorpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_192463e.errorpb.StaleCommand)
  })
_sym_db.RegisterMessage(StaleCommand)

RaftEntryTooLarge = _reflection.GeneratedProtocolMessageType('RaftEntryTooLarge', (_message.Message,), {
  'DESCRIPTOR' : _RAFTENTRYTOOLARGE,
  '__module__' : 'kvproto.rev_192463e.errorpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_192463e.errorpb.RaftEntryTooLarge)
  })
_sym_db.RegisterMessage(RaftEntryTooLarge)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'kvproto.rev_192463e.errorpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_192463e.errorpb.Error)
  })
_sym_db.RegisterMessage(Error)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
