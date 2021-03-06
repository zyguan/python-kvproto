# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kvproto/rev_0c9c24f/configpb.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kvproto/rev_0c9c24f/configpb.proto',
  package='kvproto.rev_0c9c24f.configpb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\"kvproto/rev_0c9c24f/configpb.proto\x12\x1ckvproto.rev_0c9c24f.configpb\x1a\x1cgoogle/api/annotations.proto\"Q\n\x06Status\x12\x36\n\x04\x63ode\x18\x01 \x01(\x0e\x32(.kvproto.rev_0c9c24f.configpb.StatusCode\x12\x0f\n\x07message\x18\x02 \x01(\t\"(\n\x07Version\x12\r\n\x05local\x18\x01 \x01(\x04\x12\x0e\n\x06global\x18\x02 \x01(\x04\"\x1d\n\x05Local\x12\x14\n\x0c\x63omponent_id\x18\x01 \x01(\t\"\x1b\n\x06Global\x12\x11\n\tcomponent\x18\x01 \x01(\t\"\x82\x01\n\nConfigKind\x12\x34\n\x05local\x18\x01 \x01(\x0b\x32#.kvproto.rev_0c9c24f.configpb.LocalH\x00\x12\x36\n\x06global\x18\x02 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.GlobalH\x00\x42\x06\n\x04kind\"*\n\x0b\x43onfigEntry\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1c\n\x06Header\x12\x12\n\ncluster_id\x18\x01 \x01(\x04\"\xb6\x01\n\rCreateRequest\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Header\x12\x36\n\x07version\x18\x02 \x01(\x0b\x32%.kvproto.rev_0c9c24f.configpb.Version\x12\x11\n\tcomponent\x18\x03 \x01(\t\x12\x14\n\x0c\x63omponent_id\x18\x04 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x05 \x01(\t\"\xc4\x01\n\x0e\x43reateResponse\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Header\x12\x34\n\x06status\x18\x02 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Status\x12\x36\n\x07version\x18\x03 \x01(\x0b\x32%.kvproto.rev_0c9c24f.configpb.Version\x12\x0e\n\x06\x63onfig\x18\x04 \x01(\t\"\xa3\x01\n\nGetRequest\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Header\x12\x36\n\x07version\x18\x02 \x01(\x0b\x32%.kvproto.rev_0c9c24f.configpb.Version\x12\x11\n\tcomponent\x18\x03 \x01(\t\x12\x14\n\x0c\x63omponent_id\x18\x04 \x01(\t\"\xc1\x01\n\x0bGetResponse\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Header\x12\x34\n\x06status\x18\x02 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Status\x12\x36\n\x07version\x18\x03 \x01(\x0b\x32%.kvproto.rev_0c9c24f.configpb.Version\x12\x0e\n\x06\x63onfig\x18\x04 \x01(\t\"\xf1\x01\n\rUpdateRequest\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Header\x12\x36\n\x07version\x18\x02 \x01(\x0b\x32%.kvproto.rev_0c9c24f.configpb.Version\x12\x36\n\x04kind\x18\x03 \x01(\x0b\x32(.kvproto.rev_0c9c24f.configpb.ConfigKind\x12:\n\x07\x65ntries\x18\x04 \x03(\x0b\x32).kvproto.rev_0c9c24f.configpb.ConfigEntry\"\xc4\x01\n\x0eUpdateResponse\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Header\x12\x34\n\x06status\x18\x02 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Status\x12\x36\n\x07version\x18\x03 \x01(\x0b\x32%.kvproto.rev_0c9c24f.configpb.Version\x12\x0e\n\x06\x63onfig\x18\x04 \x01(\t\"\xb5\x01\n\rDeleteRequest\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Header\x12\x36\n\x07version\x18\x02 \x01(\x0b\x32%.kvproto.rev_0c9c24f.configpb.Version\x12\x36\n\x04kind\x18\x03 \x01(\x0b\x32(.kvproto.rev_0c9c24f.configpb.ConfigKind\"\xb4\x01\n\x0e\x44\x65leteResponse\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Header\x12\x34\n\x06status\x18\x02 \x01(\x0b\x32$.kvproto.rev_0c9c24f.configpb.Status\x12\x36\n\x07version\x18\x03 \x01(\x0b\x32%.kvproto.rev_0c9c24f.configpb.Version*y\n\nStatusCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x11\n\rWRONG_VERSION\x10\x02\x12\x0e\n\nNOT_CHANGE\x10\x03\x12\x17\n\x13\x43OMPONENT_NOT_FOUND\x10\x04\x12\x1a\n\x16\x43OMPONENT_ID_NOT_FOUND\x10\x05\x32\xd4\x03\n\x06\x43onfig\x12\x65\n\x06\x43reate\x12+.kvproto.rev_0c9c24f.configpb.CreateRequest\x1a,.kvproto.rev_0c9c24f.configpb.CreateResponse\"\x00\x12n\n\x03Get\x12(.kvproto.rev_0c9c24f.configpb.GetRequest\x1a).kvproto.rev_0c9c24f.configpb.GetResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/component\x12z\n\x06Update\x12+.kvproto.rev_0c9c24f.configpb.UpdateRequest\x1a,.kvproto.rev_0c9c24f.configpb.UpdateResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/component:\x01*\x12w\n\x06\x44\x65lete\x12+.kvproto.rev_0c9c24f.configpb.DeleteRequest\x1a,.kvproto.rev_0c9c24f.configpb.DeleteResponse\"\x12\x82\xd3\xe4\x93\x02\x0c*\n/componentb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='kvproto.rev_0c9c24f.configpb.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRONG_VERSION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_CHANGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPONENT_NOT_FOUND', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPONENT_ID_NOT_FOUND', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2046,
  serialized_end=2167,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
UNKNOWN = 0
OK = 1
WRONG_VERSION = 2
NOT_CHANGE = 3
COMPONENT_NOT_FOUND = 4
COMPONENT_ID_NOT_FOUND = 5



_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='kvproto.rev_0c9c24f.configpb.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='kvproto.rev_0c9c24f.configpb.Status.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='kvproto.rev_0c9c24f.configpb.Status.message', index=1,
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
  serialized_start=98,
  serialized_end=179,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='kvproto.rev_0c9c24f.configpb.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local', full_name='kvproto.rev_0c9c24f.configpb.Version.local', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global', full_name='kvproto.rev_0c9c24f.configpb.Version.global', index=1,
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
  serialized_start=181,
  serialized_end=221,
)


_LOCAL = _descriptor.Descriptor(
  name='Local',
  full_name='kvproto.rev_0c9c24f.configpb.Local',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='component_id', full_name='kvproto.rev_0c9c24f.configpb.Local.component_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=223,
  serialized_end=252,
)


_GLOBAL = _descriptor.Descriptor(
  name='Global',
  full_name='kvproto.rev_0c9c24f.configpb.Global',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='component', full_name='kvproto.rev_0c9c24f.configpb.Global.component', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=254,
  serialized_end=281,
)


_CONFIGKIND = _descriptor.Descriptor(
  name='ConfigKind',
  full_name='kvproto.rev_0c9c24f.configpb.ConfigKind',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local', full_name='kvproto.rev_0c9c24f.configpb.ConfigKind.local', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global', full_name='kvproto.rev_0c9c24f.configpb.ConfigKind.global', index=1,
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
    _descriptor.OneofDescriptor(
      name='kind', full_name='kvproto.rev_0c9c24f.configpb.ConfigKind.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=284,
  serialized_end=414,
)


_CONFIGENTRY = _descriptor.Descriptor(
  name='ConfigEntry',
  full_name='kvproto.rev_0c9c24f.configpb.ConfigEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kvproto.rev_0c9c24f.configpb.ConfigEntry.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kvproto.rev_0c9c24f.configpb.ConfigEntry.value', index=1,
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
  serialized_start=416,
  serialized_end=458,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='kvproto.rev_0c9c24f.configpb.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='kvproto.rev_0c9c24f.configpb.Header.cluster_id', index=0,
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
  serialized_start=460,
  serialized_end=488,
)


_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='kvproto.rev_0c9c24f.configpb.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='kvproto.rev_0c9c24f.configpb.CreateRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kvproto.rev_0c9c24f.configpb.CreateRequest.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component', full_name='kvproto.rev_0c9c24f.configpb.CreateRequest.component', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component_id', full_name='kvproto.rev_0c9c24f.configpb.CreateRequest.component_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='kvproto.rev_0c9c24f.configpb.CreateRequest.config', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=491,
  serialized_end=673,
)


_CREATERESPONSE = _descriptor.Descriptor(
  name='CreateResponse',
  full_name='kvproto.rev_0c9c24f.configpb.CreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='kvproto.rev_0c9c24f.configpb.CreateResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='kvproto.rev_0c9c24f.configpb.CreateResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kvproto.rev_0c9c24f.configpb.CreateResponse.version', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='kvproto.rev_0c9c24f.configpb.CreateResponse.config', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=676,
  serialized_end=872,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='kvproto.rev_0c9c24f.configpb.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='kvproto.rev_0c9c24f.configpb.GetRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kvproto.rev_0c9c24f.configpb.GetRequest.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component', full_name='kvproto.rev_0c9c24f.configpb.GetRequest.component', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component_id', full_name='kvproto.rev_0c9c24f.configpb.GetRequest.component_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=875,
  serialized_end=1038,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='kvproto.rev_0c9c24f.configpb.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='kvproto.rev_0c9c24f.configpb.GetResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='kvproto.rev_0c9c24f.configpb.GetResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kvproto.rev_0c9c24f.configpb.GetResponse.version', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='kvproto.rev_0c9c24f.configpb.GetResponse.config', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1041,
  serialized_end=1234,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='kvproto.rev_0c9c24f.configpb.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='kvproto.rev_0c9c24f.configpb.UpdateRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kvproto.rev_0c9c24f.configpb.UpdateRequest.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='kvproto.rev_0c9c24f.configpb.UpdateRequest.kind', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='kvproto.rev_0c9c24f.configpb.UpdateRequest.entries', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=1237,
  serialized_end=1478,
)


_UPDATERESPONSE = _descriptor.Descriptor(
  name='UpdateResponse',
  full_name='kvproto.rev_0c9c24f.configpb.UpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='kvproto.rev_0c9c24f.configpb.UpdateResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='kvproto.rev_0c9c24f.configpb.UpdateResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kvproto.rev_0c9c24f.configpb.UpdateResponse.version', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='kvproto.rev_0c9c24f.configpb.UpdateResponse.config', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1481,
  serialized_end=1677,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='kvproto.rev_0c9c24f.configpb.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='kvproto.rev_0c9c24f.configpb.DeleteRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kvproto.rev_0c9c24f.configpb.DeleteRequest.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='kvproto.rev_0c9c24f.configpb.DeleteRequest.kind', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1680,
  serialized_end=1861,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='kvproto.rev_0c9c24f.configpb.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='kvproto.rev_0c9c24f.configpb.DeleteResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='kvproto.rev_0c9c24f.configpb.DeleteResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kvproto.rev_0c9c24f.configpb.DeleteResponse.version', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1864,
  serialized_end=2044,
)

_STATUS.fields_by_name['code'].enum_type = _STATUSCODE
_CONFIGKIND.fields_by_name['local'].message_type = _LOCAL
_CONFIGKIND.fields_by_name['global'].message_type = _GLOBAL
_CONFIGKIND.oneofs_by_name['kind'].fields.append(
  _CONFIGKIND.fields_by_name['local'])
_CONFIGKIND.fields_by_name['local'].containing_oneof = _CONFIGKIND.oneofs_by_name['kind']
_CONFIGKIND.oneofs_by_name['kind'].fields.append(
  _CONFIGKIND.fields_by_name['global'])
_CONFIGKIND.fields_by_name['global'].containing_oneof = _CONFIGKIND.oneofs_by_name['kind']
_CREATEREQUEST.fields_by_name['header'].message_type = _HEADER
_CREATEREQUEST.fields_by_name['version'].message_type = _VERSION
_CREATERESPONSE.fields_by_name['header'].message_type = _HEADER
_CREATERESPONSE.fields_by_name['status'].message_type = _STATUS
_CREATERESPONSE.fields_by_name['version'].message_type = _VERSION
_GETREQUEST.fields_by_name['header'].message_type = _HEADER
_GETREQUEST.fields_by_name['version'].message_type = _VERSION
_GETRESPONSE.fields_by_name['header'].message_type = _HEADER
_GETRESPONSE.fields_by_name['status'].message_type = _STATUS
_GETRESPONSE.fields_by_name['version'].message_type = _VERSION
_UPDATEREQUEST.fields_by_name['header'].message_type = _HEADER
_UPDATEREQUEST.fields_by_name['version'].message_type = _VERSION
_UPDATEREQUEST.fields_by_name['kind'].message_type = _CONFIGKIND
_UPDATEREQUEST.fields_by_name['entries'].message_type = _CONFIGENTRY
_UPDATERESPONSE.fields_by_name['header'].message_type = _HEADER
_UPDATERESPONSE.fields_by_name['status'].message_type = _STATUS
_UPDATERESPONSE.fields_by_name['version'].message_type = _VERSION
_DELETEREQUEST.fields_by_name['header'].message_type = _HEADER
_DELETEREQUEST.fields_by_name['version'].message_type = _VERSION
_DELETEREQUEST.fields_by_name['kind'].message_type = _CONFIGKIND
_DELETERESPONSE.fields_by_name['header'].message_type = _HEADER
_DELETERESPONSE.fields_by_name['status'].message_type = _STATUS
_DELETERESPONSE.fields_by_name['version'].message_type = _VERSION
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['Local'] = _LOCAL
DESCRIPTOR.message_types_by_name['Global'] = _GLOBAL
DESCRIPTOR.message_types_by_name['ConfigKind'] = _CONFIGKIND
DESCRIPTOR.message_types_by_name['ConfigEntry'] = _CONFIGENTRY
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateResponse'] = _CREATERESPONSE
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateResponse'] = _UPDATERESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.Status)
  })
_sym_db.RegisterMessage(Status)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.Version)
  })
_sym_db.RegisterMessage(Version)

Local = _reflection.GeneratedProtocolMessageType('Local', (_message.Message,), {
  'DESCRIPTOR' : _LOCAL,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.Local)
  })
_sym_db.RegisterMessage(Local)

Global = _reflection.GeneratedProtocolMessageType('Global', (_message.Message,), {
  'DESCRIPTOR' : _GLOBAL,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.Global)
  })
_sym_db.RegisterMessage(Global)

ConfigKind = _reflection.GeneratedProtocolMessageType('ConfigKind', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGKIND,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.ConfigKind)
  })
_sym_db.RegisterMessage(ConfigKind)

ConfigEntry = _reflection.GeneratedProtocolMessageType('ConfigEntry', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGENTRY,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.ConfigEntry)
  })
_sym_db.RegisterMessage(ConfigEntry)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.Header)
  })
_sym_db.RegisterMessage(Header)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATERESPONSE,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.CreateResponse)
  })
_sym_db.RegisterMessage(CreateResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSE,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.UpdateResponse)
  })
_sym_db.RegisterMessage(UpdateResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'kvproto.rev_0c9c24f.configpb_pb2'
  # @@protoc_insertion_point(class_scope:kvproto.rev_0c9c24f.configpb.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)



_CONFIG = _descriptor.ServiceDescriptor(
  name='Config',
  full_name='kvproto.rev_0c9c24f.configpb.Config',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=2170,
  serialized_end=2638,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='kvproto.rev_0c9c24f.configpb.Config.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_CREATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='kvproto.rev_0c9c24f.configpb.Config.Get',
    index=1,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=b'\202\323\344\223\002\014\022\n/component',
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='kvproto.rev_0c9c24f.configpb.Config.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_UPDATERESPONSE,
    serialized_options=b'\202\323\344\223\002\017\"\n/component:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='kvproto.rev_0c9c24f.configpb.Config.Delete',
    index=3,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=b'\202\323\344\223\002\014*\n/component',
  ),
])
_sym_db.RegisterServiceDescriptor(_CONFIG)

DESCRIPTOR.services_by_name['Config'] = _CONFIG

# @@protoc_insertion_point(module_scope)
