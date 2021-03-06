# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kvproto/rev_d4aeb46/diagnosticspb.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kvproto/rev_d4aeb46/diagnosticspb.proto',
  package='kvproto.rev_d4aeb46.diagnosticspb',
  syntax='proto3',
  serialized_options=b'\n\020org.tikv.kvproto',
  serialized_pb=b'\n\'kvproto/rev_d4aeb46/diagnosticspb.proto\x12!kvproto.rev_d4aeb46.diagnosticspb\"\xf3\x01\n\x10SearchLogRequest\x12\x12\n\nstart_time\x18\x01 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x03\x12;\n\x06levels\x18\x03 \x03(\x0e\x32+.kvproto.rev_d4aeb46.diagnosticspb.LogLevel\x12\x10\n\x08patterns\x18\x04 \x03(\t\x12J\n\x06target\x18\x05 \x01(\x0e\x32:.kvproto.rev_d4aeb46.diagnosticspb.SearchLogRequest.Target\"\x1e\n\x06Target\x12\n\n\x06Normal\x10\x00\x12\x08\n\x04Slow\x10\x01\"T\n\x11SearchLogResponse\x12?\n\x08messages\x18\x01 \x03(\x0b\x32-.kvproto.rev_d4aeb46.diagnosticspb.LogMessage\"g\n\nLogMessage\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12:\n\x05level\x18\x02 \x01(\x0e\x32+.kvproto.rev_d4aeb46.diagnosticspb.LogLevel\x12\x0f\n\x07message\x18\x03 \x01(\t\"R\n\x11ServerInfoRequest\x12=\n\x02tp\x18\x01 \x01(\x0e\x32\x31.kvproto.rev_d4aeb46.diagnosticspb.ServerInfoType\",\n\x0eServerInfoPair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"l\n\x0eServerInfoItem\x12\n\n\x02tp\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12@\n\x05pairs\x18\x03 \x03(\x0b\x32\x31.kvproto.rev_d4aeb46.diagnosticspb.ServerInfoPair\"V\n\x12ServerInfoResponse\x12@\n\x05items\x18\x01 \x03(\x0b\x32\x31.kvproto.rev_d4aeb46.diagnosticspb.ServerInfoItem*Z\n\x08LogLevel\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x44\x65\x62ug\x10\x01\x12\x08\n\x04Info\x10\x02\x12\x08\n\x04Warn\x10\x03\x12\t\n\x05Trace\x10\x04\x12\x0c\n\x08\x43ritical\x10\x05\x12\t\n\x05\x45rror\x10\x06*I\n\x0eServerInfoType\x12\x07\n\x03\x41ll\x10\x00\x12\x10\n\x0cHardwareInfo\x10\x01\x12\x0e\n\nSystemInfo\x10\x02\x12\x0c\n\x08LoadInfo\x10\x03\x32\x88\x02\n\x0b\x44iagnostics\x12{\n\nsearch_log\x12\x33.kvproto.rev_d4aeb46.diagnosticspb.SearchLogRequest\x1a\x34.kvproto.rev_d4aeb46.diagnosticspb.SearchLogResponse\"\x00\x30\x01\x12|\n\x0bserver_info\x12\x34.kvproto.rev_d4aeb46.diagnosticspb.ServerInfoRequest\x1a\x35.kvproto.rev_d4aeb46.diagnosticspb.ServerInfoResponse\"\x00\x42\x12\n\x10org.tikv.kvprotob\x06proto3'
)

_LOGLEVEL = _descriptor.EnumDescriptor(
  name='LogLevel',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.LogLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Debug', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Info', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Warn', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Trace', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Critical', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Error', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=843,
  serialized_end=933,
)
_sym_db.RegisterEnumDescriptor(_LOGLEVEL)

LogLevel = enum_type_wrapper.EnumTypeWrapper(_LOGLEVEL)
_SERVERINFOTYPE = _descriptor.EnumDescriptor(
  name='ServerInfoType',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='All', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HardwareInfo', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemInfo', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LoadInfo', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=935,
  serialized_end=1008,
)
_sym_db.RegisterEnumDescriptor(_SERVERINFOTYPE)

ServerInfoType = enum_type_wrapper.EnumTypeWrapper(_SERVERINFOTYPE)
UNKNOWN = 0
Debug = 1
Info = 2
Warn = 3
Trace = 4
Critical = 5
Error = 6
All = 0
HardwareInfo = 1
SystemInfo = 2
LoadInfo = 3


_SEARCHLOGREQUEST_TARGET = _descriptor.EnumDescriptor(
  name='Target',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.SearchLogRequest.Target',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Normal', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Slow', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=292,
  serialized_end=322,
)
_sym_db.RegisterEnumDescriptor(_SEARCHLOGREQUEST_TARGET)


_SEARCHLOGREQUEST = _descriptor.Descriptor(
  name='SearchLogRequest',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.SearchLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='kvproto.rev_d4aeb46.diagnosticspb.SearchLogRequest.start_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='kvproto.rev_d4aeb46.diagnosticspb.SearchLogRequest.end_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='levels', full_name='kvproto.rev_d4aeb46.diagnosticspb.SearchLogRequest.levels', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patterns', full_name='kvproto.rev_d4aeb46.diagnosticspb.SearchLogRequest.patterns', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='kvproto.rev_d4aeb46.diagnosticspb.SearchLogRequest.target', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SEARCHLOGREQUEST_TARGET,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=322,
)


_SEARCHLOGRESPONSE = _descriptor.Descriptor(
  name='SearchLogResponse',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.SearchLogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='kvproto.rev_d4aeb46.diagnosticspb.SearchLogResponse.messages', index=0,
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
  serialized_start=324,
  serialized_end=408,
)


_LOGMESSAGE = _descriptor.Descriptor(
  name='LogMessage',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.LogMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='kvproto.rev_d4aeb46.diagnosticspb.LogMessage.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='kvproto.rev_d4aeb46.diagnosticspb.LogMessage.level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='kvproto.rev_d4aeb46.diagnosticspb.LogMessage.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=410,
  serialized_end=513,
)


_SERVERINFOREQUEST = _descriptor.Descriptor(
  name='ServerInfoRequest',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tp', full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoRequest.tp', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=515,
  serialized_end=597,
)


_SERVERINFOPAIR = _descriptor.Descriptor(
  name='ServerInfoPair',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoPair.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoPair.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=599,
  serialized_end=643,
)


_SERVERINFOITEM = _descriptor.Descriptor(
  name='ServerInfoItem',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tp', full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoItem.tp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoItem.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pairs', full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoItem.pairs', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=645,
  serialized_end=753,
)


_SERVERINFORESPONSE = _descriptor.Descriptor(
  name='ServerInfoResponse',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='kvproto.rev_d4aeb46.diagnosticspb.ServerInfoResponse.items', index=0,
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
  serialized_start=755,
  serialized_end=841,
)

_SEARCHLOGREQUEST.fields_by_name['levels'].enum_type = _LOGLEVEL
_SEARCHLOGREQUEST.fields_by_name['target'].enum_type = _SEARCHLOGREQUEST_TARGET
_SEARCHLOGREQUEST_TARGET.containing_type = _SEARCHLOGREQUEST
_SEARCHLOGRESPONSE.fields_by_name['messages'].message_type = _LOGMESSAGE
_LOGMESSAGE.fields_by_name['level'].enum_type = _LOGLEVEL
_SERVERINFOREQUEST.fields_by_name['tp'].enum_type = _SERVERINFOTYPE
_SERVERINFOITEM.fields_by_name['pairs'].message_type = _SERVERINFOPAIR
_SERVERINFORESPONSE.fields_by_name['items'].message_type = _SERVERINFOITEM
DESCRIPTOR.message_types_by_name['SearchLogRequest'] = _SEARCHLOGREQUEST
DESCRIPTOR.message_types_by_name['SearchLogResponse'] = _SEARCHLOGRESPONSE
DESCRIPTOR.message_types_by_name['LogMessage'] = _LOGMESSAGE
DESCRIPTOR.message_types_by_name['ServerInfoRequest'] = _SERVERINFOREQUEST
DESCRIPTOR.message_types_by_name['ServerInfoPair'] = _SERVERINFOPAIR
DESCRIPTOR.message_types_by_name['ServerInfoItem'] = _SERVERINFOITEM
DESCRIPTOR.message_types_by_name['ServerInfoResponse'] = _SERVERINFORESPONSE
DESCRIPTOR.enum_types_by_name['LogLevel'] = _LOGLEVEL
DESCRIPTOR.enum_types_by_name['ServerInfoType'] = _SERVERINFOTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchLogRequest = _reflection.GeneratedProtocolMessageType('SearchLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHLOGREQUEST,
  '__module__' : 'kvproto.rev_d4aeb46.diagnosticspb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_d4aeb46.diagnosticspb.SearchLogRequest)
  })
_sym_db.RegisterMessage(SearchLogRequest)

SearchLogResponse = _reflection.GeneratedProtocolMessageType('SearchLogResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHLOGRESPONSE,
  '__module__' : 'kvproto.rev_d4aeb46.diagnosticspb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_d4aeb46.diagnosticspb.SearchLogResponse)
  })
_sym_db.RegisterMessage(SearchLogResponse)

LogMessage = _reflection.GeneratedProtocolMessageType('LogMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOGMESSAGE,
  '__module__' : 'kvproto.rev_d4aeb46.diagnosticspb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_d4aeb46.diagnosticspb.LogMessage)
  })
_sym_db.RegisterMessage(LogMessage)

ServerInfoRequest = _reflection.GeneratedProtocolMessageType('ServerInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFOREQUEST,
  '__module__' : 'kvproto.rev_d4aeb46.diagnosticspb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_d4aeb46.diagnosticspb.ServerInfoRequest)
  })
_sym_db.RegisterMessage(ServerInfoRequest)

ServerInfoPair = _reflection.GeneratedProtocolMessageType('ServerInfoPair', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFOPAIR,
  '__module__' : 'kvproto.rev_d4aeb46.diagnosticspb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_d4aeb46.diagnosticspb.ServerInfoPair)
  })
_sym_db.RegisterMessage(ServerInfoPair)

ServerInfoItem = _reflection.GeneratedProtocolMessageType('ServerInfoItem', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFOITEM,
  '__module__' : 'kvproto.rev_d4aeb46.diagnosticspb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_d4aeb46.diagnosticspb.ServerInfoItem)
  })
_sym_db.RegisterMessage(ServerInfoItem)

ServerInfoResponse = _reflection.GeneratedProtocolMessageType('ServerInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFORESPONSE,
  '__module__' : 'kvproto.rev_d4aeb46.diagnosticspb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_d4aeb46.diagnosticspb.ServerInfoResponse)
  })
_sym_db.RegisterMessage(ServerInfoResponse)


DESCRIPTOR._options = None

_DIAGNOSTICS = _descriptor.ServiceDescriptor(
  name='Diagnostics',
  full_name='kvproto.rev_d4aeb46.diagnosticspb.Diagnostics',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1011,
  serialized_end=1275,
  methods=[
  _descriptor.MethodDescriptor(
    name='search_log',
    full_name='kvproto.rev_d4aeb46.diagnosticspb.Diagnostics.search_log',
    index=0,
    containing_service=None,
    input_type=_SEARCHLOGREQUEST,
    output_type=_SEARCHLOGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='server_info',
    full_name='kvproto.rev_d4aeb46.diagnosticspb.Diagnostics.server_info',
    index=1,
    containing_service=None,
    input_type=_SERVERINFOREQUEST,
    output_type=_SERVERINFORESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIAGNOSTICS)

DESCRIPTOR.services_by_name['Diagnostics'] = _DIAGNOSTICS

# @@protoc_insertion_point(module_scope)
