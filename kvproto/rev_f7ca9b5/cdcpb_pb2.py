# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kvproto/rev_f7ca9b5/cdcpb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kvproto.rev_f7ca9b5 import raft_cmdpb_pb2 as kvproto_dot_rev__f7ca9b5_dot_raft__cmdpb__pb2
from kvproto.rev_f7ca9b5 import metapb_pb2 as kvproto_dot_rev__f7ca9b5_dot_metapb__pb2
from kvproto.rev_f7ca9b5 import errorpb_pb2 as kvproto_dot_rev__f7ca9b5_dot_errorpb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kvproto/rev_f7ca9b5/cdcpb.proto',
  package='kvproto.rev_f7ca9b5.cdcpb',
  syntax='proto3',
  serialized_options=b'\n\020org.tikv.kvproto',
  serialized_pb=b'\n\x1fkvproto/rev_f7ca9b5/cdcpb.proto\x12\x19kvproto.rev_f7ca9b5.cdcpb\x1a$kvproto/rev_f7ca9b5/raft_cmdpb.proto\x1a kvproto/rev_f7ca9b5/metapb.proto\x1a!kvproto/rev_f7ca9b5/errorpb.proto\"\x1c\n\x06Header\x12\x12\n\ncluster_id\x18\x01 \x01(\x04\"\xc4\x02\n\x05\x45rror\x12:\n\nnot_leader\x18\x01 \x01(\x0b\x32&.kvproto.rev_f7ca9b5.errorpb.NotLeader\x12\x45\n\x10region_not_found\x18\x02 \x01(\x0b\x32+.kvproto.rev_f7ca9b5.errorpb.RegionNotFound\x12\x43\n\x0f\x65poch_not_match\x18\x03 \x01(\x0b\x32*.kvproto.rev_f7ca9b5.errorpb.EpochNotMatch\x12L\n\x11\x64uplicate_request\x18\x04 \x01(\x0b\x32\x31.kvproto.rev_f7ca9b5.cdcpb.Error.DuplicateRequest\x1a%\n\x10\x44uplicateRequest\x12\x11\n\tregion_id\x18\x01 \x01(\x04\"\xa9\x06\n\x05\x45vent\x12\x11\n\tregion_id\x18\x01 \x01(\x04\x12\r\n\x05index\x18\x02 \x01(\x04\x12\x12\n\nrequest_id\x18\x07 \x01(\x04\x12;\n\x07\x65ntries\x18\x03 \x01(\x0b\x32(.kvproto.rev_f7ca9b5.cdcpb.Event.EntriesH\x00\x12\x37\n\x05\x61\x64min\x18\x04 \x01(\x0b\x32&.kvproto.rev_f7ca9b5.cdcpb.Event.AdminH\x00\x12\x31\n\x05\x65rror\x18\x05 \x01(\x0b\x32 .kvproto.rev_f7ca9b5.cdcpb.ErrorH\x00\x12\x15\n\x0bresolved_ts\x18\x06 \x01(\x04H\x00\x1a\xe8\x01\n\x03Row\x12\x10\n\x08start_ts\x18\x01 \x01(\x04\x12\x11\n\tcommit_ts\x18\x02 \x01(\x04\x12\x36\n\x04type\x18\x03 \x01(\x0e\x32(.kvproto.rev_f7ca9b5.cdcpb.Event.LogType\x12<\n\x07op_type\x18\x04 \x01(\x0e\x32+.kvproto.rev_f7ca9b5.cdcpb.Event.Row.OpType\x12\x0b\n\x03key\x18\x05 \x01(\x0c\x12\r\n\x05value\x18\x06 \x01(\x0c\"*\n\x06OpType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03PUT\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x1a@\n\x07\x45ntries\x12\x35\n\x07\x65ntries\x18\x01 \x03(\x0b\x32$.kvproto.rev_f7ca9b5.cdcpb.Event.Row\x1a\x93\x01\n\x05\x41\x64min\x12\x43\n\radmin_request\x18\x01 \x01(\x0b\x32,.kvproto.rev_f7ca9b5.raft_cmdpb.AdminRequest\x12\x45\n\x0e\x61\x64min_response\x18\x02 \x01(\x0b\x32-.kvproto.rev_f7ca9b5.raft_cmdpb.AdminResponse\"^\n\x07LogType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08PREWRITE\x10\x01\x12\n\n\x06\x43OMMIT\x10\x02\x12\x0c\n\x08ROLLBACK\x10\x03\x12\r\n\tCOMMITTED\x10\x04\x12\x0f\n\x0bINITIALIZED\x10\x05\x42\x07\n\x05\x65vent\"C\n\x0f\x43hangeDataEvent\x12\x30\n\x06\x65vents\x18\x01 \x03(\x0b\x32 .kvproto.rev_f7ca9b5.cdcpb.Event\"\xe7\x01\n\x11\x43hangeDataRequest\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.kvproto.rev_f7ca9b5.cdcpb.Header\x12\x11\n\tregion_id\x18\x02 \x01(\x04\x12=\n\x0cregion_epoch\x18\x03 \x01(\x0b\x32\'.kvproto.rev_f7ca9b5.metapb.RegionEpoch\x12\x15\n\rcheckpoint_ts\x18\x04 \x01(\x04\x12\x11\n\tstart_key\x18\x05 \x01(\x0c\x12\x0f\n\x07\x65nd_key\x18\x06 \x01(\x0c\x12\x12\n\nrequest_id\x18\x07 \x01(\x04\x32w\n\nChangeData\x12i\n\tEventFeed\x12,.kvproto.rev_f7ca9b5.cdcpb.ChangeDataRequest\x1a*.kvproto.rev_f7ca9b5.cdcpb.ChangeDataEvent(\x01\x30\x01\x42\x12\n\x10org.tikv.kvprotob\x06proto3'
  ,
  dependencies=[kvproto_dot_rev__f7ca9b5_dot_raft__cmdpb__pb2.DESCRIPTOR,kvproto_dot_rev__f7ca9b5_dot_metapb__pb2.DESCRIPTOR,kvproto_dot_rev__f7ca9b5_dot_errorpb__pb2.DESCRIPTOR,])



_EVENT_ROW_OPTYPE = _descriptor.EnumDescriptor(
  name='OpType',
  full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Row.OpType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=973,
  serialized_end=1015,
)
_sym_db.RegisterEnumDescriptor(_EVENT_ROW_OPTYPE)

_EVENT_LOGTYPE = _descriptor.EnumDescriptor(
  name='LogType',
  full_name='kvproto.rev_f7ca9b5.cdcpb.Event.LogType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREWRITE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMIT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROLLBACK', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMITTED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIALIZED', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1233,
  serialized_end=1327,
)
_sym_db.RegisterEnumDescriptor(_EVENT_LOGTYPE)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='kvproto.rev_f7ca9b5.cdcpb.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='kvproto.rev_f7ca9b5.cdcpb.Header.cluster_id', index=0,
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
  serialized_start=169,
  serialized_end=197,
)


_ERROR_DUPLICATEREQUEST = _descriptor.Descriptor(
  name='DuplicateRequest',
  full_name='kvproto.rev_f7ca9b5.cdcpb.Error.DuplicateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='region_id', full_name='kvproto.rev_f7ca9b5.cdcpb.Error.DuplicateRequest.region_id', index=0,
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
  serialized_start=487,
  serialized_end=524,
)

_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='kvproto.rev_f7ca9b5.cdcpb.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='not_leader', full_name='kvproto.rev_f7ca9b5.cdcpb.Error.not_leader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_not_found', full_name='kvproto.rev_f7ca9b5.cdcpb.Error.region_not_found', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch_not_match', full_name='kvproto.rev_f7ca9b5.cdcpb.Error.epoch_not_match', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duplicate_request', full_name='kvproto.rev_f7ca9b5.cdcpb.Error.duplicate_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ERROR_DUPLICATEREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=524,
)


_EVENT_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_ts', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Row.start_ts', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit_ts', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Row.commit_ts', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Row.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op_type', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Row.op_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Row.key', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Row.value', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVENT_ROW_OPTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=783,
  serialized_end=1015,
)

_EVENT_ENTRIES = _descriptor.Descriptor(
  name='Entries',
  full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Entries',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Entries.entries', index=0,
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
  serialized_start=1017,
  serialized_end=1081,
)

_EVENT_ADMIN = _descriptor.Descriptor(
  name='Admin',
  full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Admin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='admin_request', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Admin.admin_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='admin_response', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.Admin.admin_response', index=1,
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
  serialized_start=1084,
  serialized_end=1231,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='kvproto.rev_f7ca9b5.cdcpb.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='region_id', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.region_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.request_id', index=2,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.entries', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='admin', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.admin', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.error', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolved_ts', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.resolved_ts', index=6,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_ROW, _EVENT_ENTRIES, _EVENT_ADMIN, ],
  enum_types=[
    _EVENT_LOGTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='event', full_name='kvproto.rev_f7ca9b5.cdcpb.Event.event',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=527,
  serialized_end=1336,
)


_CHANGEDATAEVENT = _descriptor.Descriptor(
  name='ChangeDataEvent',
  full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeDataEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeDataEvent.events', index=0,
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
  serialized_start=1338,
  serialized_end=1405,
)


_CHANGEDATAREQUEST = _descriptor.Descriptor(
  name='ChangeDataRequest',
  full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeDataRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_id', full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeDataRequest.region_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_epoch', full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeDataRequest.region_epoch', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_ts', full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeDataRequest.checkpoint_ts', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_key', full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeDataRequest.start_key', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_key', full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeDataRequest.end_key', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeDataRequest.request_id', index=6,
      number=7, type=4, cpp_type=4, label=1,
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
  serialized_start=1408,
  serialized_end=1639,
)

_ERROR_DUPLICATEREQUEST.containing_type = _ERROR
_ERROR.fields_by_name['not_leader'].message_type = kvproto_dot_rev__f7ca9b5_dot_errorpb__pb2._NOTLEADER
_ERROR.fields_by_name['region_not_found'].message_type = kvproto_dot_rev__f7ca9b5_dot_errorpb__pb2._REGIONNOTFOUND
_ERROR.fields_by_name['epoch_not_match'].message_type = kvproto_dot_rev__f7ca9b5_dot_errorpb__pb2._EPOCHNOTMATCH
_ERROR.fields_by_name['duplicate_request'].message_type = _ERROR_DUPLICATEREQUEST
_EVENT_ROW.fields_by_name['type'].enum_type = _EVENT_LOGTYPE
_EVENT_ROW.fields_by_name['op_type'].enum_type = _EVENT_ROW_OPTYPE
_EVENT_ROW.containing_type = _EVENT
_EVENT_ROW_OPTYPE.containing_type = _EVENT_ROW
_EVENT_ENTRIES.fields_by_name['entries'].message_type = _EVENT_ROW
_EVENT_ENTRIES.containing_type = _EVENT
_EVENT_ADMIN.fields_by_name['admin_request'].message_type = kvproto_dot_rev__f7ca9b5_dot_raft__cmdpb__pb2._ADMINREQUEST
_EVENT_ADMIN.fields_by_name['admin_response'].message_type = kvproto_dot_rev__f7ca9b5_dot_raft__cmdpb__pb2._ADMINRESPONSE
_EVENT_ADMIN.containing_type = _EVENT
_EVENT.fields_by_name['entries'].message_type = _EVENT_ENTRIES
_EVENT.fields_by_name['admin'].message_type = _EVENT_ADMIN
_EVENT.fields_by_name['error'].message_type = _ERROR
_EVENT_LOGTYPE.containing_type = _EVENT
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['entries'])
_EVENT.fields_by_name['entries'].containing_oneof = _EVENT.oneofs_by_name['event']
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['admin'])
_EVENT.fields_by_name['admin'].containing_oneof = _EVENT.oneofs_by_name['event']
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['error'])
_EVENT.fields_by_name['error'].containing_oneof = _EVENT.oneofs_by_name['event']
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['resolved_ts'])
_EVENT.fields_by_name['resolved_ts'].containing_oneof = _EVENT.oneofs_by_name['event']
_CHANGEDATAEVENT.fields_by_name['events'].message_type = _EVENT
_CHANGEDATAREQUEST.fields_by_name['header'].message_type = _HEADER
_CHANGEDATAREQUEST.fields_by_name['region_epoch'].message_type = kvproto_dot_rev__f7ca9b5_dot_metapb__pb2._REGIONEPOCH
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['ChangeDataEvent'] = _CHANGEDATAEVENT
DESCRIPTOR.message_types_by_name['ChangeDataRequest'] = _CHANGEDATAREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'kvproto.rev_f7ca9b5.cdcpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_f7ca9b5.cdcpb.Header)
  })
_sym_db.RegisterMessage(Header)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {

  'DuplicateRequest' : _reflection.GeneratedProtocolMessageType('DuplicateRequest', (_message.Message,), {
    'DESCRIPTOR' : _ERROR_DUPLICATEREQUEST,
    '__module__' : 'kvproto.rev_f7ca9b5.cdcpb_pb2'
    # @@protoc_insertion_point(class_scope:kvproto.rev_f7ca9b5.cdcpb.Error.DuplicateRequest)
    })
  ,
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'kvproto.rev_f7ca9b5.cdcpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_f7ca9b5.cdcpb.Error)
  })
_sym_db.RegisterMessage(Error)
_sym_db.RegisterMessage(Error.DuplicateRequest)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'Row' : _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_ROW,
    '__module__' : 'kvproto.rev_f7ca9b5.cdcpb_pb2'
    # @@protoc_insertion_point(class_scope:kvproto.rev_f7ca9b5.cdcpb.Event.Row)
    })
  ,

  'Entries' : _reflection.GeneratedProtocolMessageType('Entries', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_ENTRIES,
    '__module__' : 'kvproto.rev_f7ca9b5.cdcpb_pb2'
    # @@protoc_insertion_point(class_scope:kvproto.rev_f7ca9b5.cdcpb.Event.Entries)
    })
  ,

  'Admin' : _reflection.GeneratedProtocolMessageType('Admin', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_ADMIN,
    '__module__' : 'kvproto.rev_f7ca9b5.cdcpb_pb2'
    # @@protoc_insertion_point(class_scope:kvproto.rev_f7ca9b5.cdcpb.Event.Admin)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'kvproto.rev_f7ca9b5.cdcpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_f7ca9b5.cdcpb.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.Row)
_sym_db.RegisterMessage(Event.Entries)
_sym_db.RegisterMessage(Event.Admin)

ChangeDataEvent = _reflection.GeneratedProtocolMessageType('ChangeDataEvent', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEDATAEVENT,
  '__module__' : 'kvproto.rev_f7ca9b5.cdcpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_f7ca9b5.cdcpb.ChangeDataEvent)
  })
_sym_db.RegisterMessage(ChangeDataEvent)

ChangeDataRequest = _reflection.GeneratedProtocolMessageType('ChangeDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEDATAREQUEST,
  '__module__' : 'kvproto.rev_f7ca9b5.cdcpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_f7ca9b5.cdcpb.ChangeDataRequest)
  })
_sym_db.RegisterMessage(ChangeDataRequest)


DESCRIPTOR._options = None

_CHANGEDATA = _descriptor.ServiceDescriptor(
  name='ChangeData',
  full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1641,
  serialized_end=1760,
  methods=[
  _descriptor.MethodDescriptor(
    name='EventFeed',
    full_name='kvproto.rev_f7ca9b5.cdcpb.ChangeData.EventFeed',
    index=0,
    containing_service=None,
    input_type=_CHANGEDATAREQUEST,
    output_type=_CHANGEDATAEVENT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHANGEDATA)

DESCRIPTOR.services_by_name['ChangeData'] = _CHANGEDATA

# @@protoc_insertion_point(module_scope)