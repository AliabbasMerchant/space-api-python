# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server.proto',
  package='proto',
  syntax='proto3',
  serialized_options=_b('\n\037com.spaceuptech.space_api.protoB\017SpaceCloudProtoP\001'),
  serialized_pb=_b('\n\x0cserver.proto\x12\x05proto\"O\n\rCreateRequest\x12\x10\n\x08\x64ocument\x18\x01 \x01(\x0c\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x19\n\x04meta\x18\x03 \x01(\x0b\x32\x0b.proto.Meta\"n\n\x0bReadRequest\x12\x0c\n\x04\x66ind\x18\x01 \x01(\x0c\x12\x11\n\toperation\x18\x02 \x01(\t\x12#\n\x07options\x18\x03 \x01(\x0b\x32\x12.proto.ReadOptions\x12\x19\n\x04meta\x18\x04 \x01(\x0b\x32\x0b.proto.Meta\"\xf4\x01\n\x0bReadOptions\x12.\n\x06select\x18\x01 \x03(\x0b\x32\x1e.proto.ReadOptions.SelectEntry\x12*\n\x04sort\x18\x02 \x03(\x0b\x32\x1c.proto.ReadOptions.SortEntry\x12\x0c\n\x04skip\x18\x03 \x01(\x03\x12\r\n\x05limit\x18\x04 \x01(\x03\x12\x10\n\x08\x64istinct\x18\x05 \x01(\t\x1a-\n\x0bSelectEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a+\n\tSortEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"[\n\rUpdateRequest\x12\x0c\n\x04\x66ind\x18\x01 \x01(\x0c\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x0e\n\x06update\x18\x03 \x01(\x0c\x12\x19\n\x04meta\x18\x04 \x01(\x0b\x32\x0b.proto.Meta\"K\n\rDeleteRequest\x12\x0c\n\x04\x66ind\x18\x01 \x01(\x0c\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x19\n\x04meta\x18\x03 \x01(\x0b\x32\x0b.proto.Meta\"R\n\x10\x41ggregateRequest\x12\x10\n\x08pipeline\x18\x01 \x01(\x0c\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x19\n\x04meta\x18\x03 \x01(\x0b\x32\x0b.proto.Meta\"9\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0e\n\x06result\x18\x03 \x01(\x0c\"C\n\x04Meta\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x62Type\x18\x02 \x01(\t\x12\x0b\n\x03\x63ol\x18\x03 \x01(\t\x12\r\n\x05token\x18\x04 \x01(\t\"j\n\nAllRequest\x12\x0b\n\x03\x63ol\x18\x01 \x01(\t\x12\x10\n\x08\x64ocument\x18\x02 \x01(\x0c\x12\x11\n\toperation\x18\x03 \x01(\t\x12\x0c\n\x04\x66ind\x18\x04 \x01(\x0c\x12\x0e\n\x06update\x18\x05 \x01(\x0c\x12\x0c\n\x04type\x18\x06 \x01(\t\"R\n\x0c\x42\x61tchRequest\x12\'\n\x0c\x62\x61tchrequest\x18\x01 \x03(\x0b\x32\x11.proto.AllRequest\x12\x19\n\x04meta\x18\x02 \x01(\x0b\x32\x0b.proto.Meta\"_\n\x0b\x46\x61\x61SRequest\x12\x0e\n\x06params\x18\x01 \x01(\x0c\x12\x0f\n\x07timeout\x18\x02 \x01(\x03\x12\x0e\n\x06\x65ngine\x18\x03 \x01(\t\x12\x10\n\x08\x66unction\x18\x04 \x01(\t\x12\r\n\x05token\x18\x05 \x01(\t2\xed\x02\n\nSpaceCloud\x12\x31\n\x06\x43reate\x12\x14.proto.CreateRequest\x1a\x0f.proto.Response\"\x00\x12-\n\x04Read\x12\x12.proto.ReadRequest\x1a\x0f.proto.Response\"\x00\x12\x31\n\x06Update\x12\x14.proto.UpdateRequest\x1a\x0f.proto.Response\"\x00\x12\x31\n\x06\x44\x65lete\x12\x14.proto.DeleteRequest\x1a\x0f.proto.Response\"\x00\x12\x37\n\tAggregate\x12\x17.proto.AggregateRequest\x1a\x0f.proto.Response\"\x00\x12/\n\x05\x42\x61tch\x12\x13.proto.BatchRequest\x1a\x0f.proto.Response\"\x00\x12-\n\x04\x43\x61ll\x12\x12.proto.FaaSRequest\x1a\x0f.proto.Response\"\x00\x42\x34\n\x1f\x63om.spaceuptech.space_api.protoB\x0fSpaceCloudProtoP\x01\x62\x06proto3')
)




_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='proto.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document', full_name='proto.CreateRequest.document', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='proto.CreateRequest.operation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='proto.CreateRequest.meta', index=2,
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
  serialized_start=23,
  serialized_end=102,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='proto.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='find', full_name='proto.ReadRequest.find', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='proto.ReadRequest.operation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='proto.ReadRequest.options', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='proto.ReadRequest.meta', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=104,
  serialized_end=214,
)


_READOPTIONS_SELECTENTRY = _descriptor.Descriptor(
  name='SelectEntry',
  full_name='proto.ReadOptions.SelectEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.ReadOptions.SelectEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.ReadOptions.SelectEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=371,
  serialized_end=416,
)

_READOPTIONS_SORTENTRY = _descriptor.Descriptor(
  name='SortEntry',
  full_name='proto.ReadOptions.SortEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.ReadOptions.SortEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.ReadOptions.SortEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=461,
)

_READOPTIONS = _descriptor.Descriptor(
  name='ReadOptions',
  full_name='proto.ReadOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='select', full_name='proto.ReadOptions.select', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='proto.ReadOptions.sort', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skip', full_name='proto.ReadOptions.skip', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='proto.ReadOptions.limit', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distinct', full_name='proto.ReadOptions.distinct', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_READOPTIONS_SELECTENTRY, _READOPTIONS_SORTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=461,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='proto.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='find', full_name='proto.UpdateRequest.find', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='proto.UpdateRequest.operation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='proto.UpdateRequest.update', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='proto.UpdateRequest.meta', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=463,
  serialized_end=554,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='proto.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='find', full_name='proto.DeleteRequest.find', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='proto.DeleteRequest.operation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='proto.DeleteRequest.meta', index=2,
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
  serialized_start=556,
  serialized_end=631,
)


_AGGREGATEREQUEST = _descriptor.Descriptor(
  name='AggregateRequest',
  full_name='proto.AggregateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pipeline', full_name='proto.AggregateRequest.pipeline', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='proto.AggregateRequest.operation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='proto.AggregateRequest.meta', index=2,
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
  serialized_start=633,
  serialized_end=715,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='proto.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.Response.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.Response.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='proto.Response.result', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=717,
  serialized_end=774,
)


_META = _descriptor.Descriptor(
  name='Meta',
  full_name='proto.Meta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='proto.Meta.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbType', full_name='proto.Meta.dbType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='col', full_name='proto.Meta.col', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='proto.Meta.token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=776,
  serialized_end=843,
)


_ALLREQUEST = _descriptor.Descriptor(
  name='AllRequest',
  full_name='proto.AllRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='col', full_name='proto.AllRequest.col', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='document', full_name='proto.AllRequest.document', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='proto.AllRequest.operation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='find', full_name='proto.AllRequest.find', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='proto.AllRequest.update', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='proto.AllRequest.type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=845,
  serialized_end=951,
)


_BATCHREQUEST = _descriptor.Descriptor(
  name='BatchRequest',
  full_name='proto.BatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batchrequest', full_name='proto.BatchRequest.batchrequest', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='proto.BatchRequest.meta', index=1,
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
  serialized_start=953,
  serialized_end=1035,
)


_FAASREQUEST = _descriptor.Descriptor(
  name='FaaSRequest',
  full_name='proto.FaaSRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='proto.FaaSRequest.params', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='proto.FaaSRequest.timeout', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engine', full_name='proto.FaaSRequest.engine', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function', full_name='proto.FaaSRequest.function', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='proto.FaaSRequest.token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1037,
  serialized_end=1132,
)

_CREATEREQUEST.fields_by_name['meta'].message_type = _META
_READREQUEST.fields_by_name['options'].message_type = _READOPTIONS
_READREQUEST.fields_by_name['meta'].message_type = _META
_READOPTIONS_SELECTENTRY.containing_type = _READOPTIONS
_READOPTIONS_SORTENTRY.containing_type = _READOPTIONS
_READOPTIONS.fields_by_name['select'].message_type = _READOPTIONS_SELECTENTRY
_READOPTIONS.fields_by_name['sort'].message_type = _READOPTIONS_SORTENTRY
_UPDATEREQUEST.fields_by_name['meta'].message_type = _META
_DELETEREQUEST.fields_by_name['meta'].message_type = _META
_AGGREGATEREQUEST.fields_by_name['meta'].message_type = _META
_BATCHREQUEST.fields_by_name['batchrequest'].message_type = _ALLREQUEST
_BATCHREQUEST.fields_by_name['meta'].message_type = _META
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadOptions'] = _READOPTIONS
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['AggregateRequest'] = _AGGREGATEREQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Meta'] = _META
DESCRIPTOR.message_types_by_name['AllRequest'] = _ALLREQUEST
DESCRIPTOR.message_types_by_name['BatchRequest'] = _BATCHREQUEST
DESCRIPTOR.message_types_by_name['FaaSRequest'] = _FAASREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.CreateRequest)
  ))
_sym_db.RegisterMessage(CreateRequest)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), dict(
  DESCRIPTOR = _READREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.ReadRequest)
  ))
_sym_db.RegisterMessage(ReadRequest)

ReadOptions = _reflection.GeneratedProtocolMessageType('ReadOptions', (_message.Message,), dict(

  SelectEntry = _reflection.GeneratedProtocolMessageType('SelectEntry', (_message.Message,), dict(
    DESCRIPTOR = _READOPTIONS_SELECTENTRY,
    __module__ = 'server_pb2'
    # @@protoc_insertion_point(class_scope:proto.ReadOptions.SelectEntry)
    ))
  ,

  SortEntry = _reflection.GeneratedProtocolMessageType('SortEntry', (_message.Message,), dict(
    DESCRIPTOR = _READOPTIONS_SORTENTRY,
    __module__ = 'server_pb2'
    # @@protoc_insertion_point(class_scope:proto.ReadOptions.SortEntry)
    ))
  ,
  DESCRIPTOR = _READOPTIONS,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.ReadOptions)
  ))
_sym_db.RegisterMessage(ReadOptions)
_sym_db.RegisterMessage(ReadOptions.SelectEntry)
_sym_db.RegisterMessage(ReadOptions.SortEntry)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.UpdateRequest)
  ))
_sym_db.RegisterMessage(UpdateRequest)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)

AggregateRequest = _reflection.GeneratedProtocolMessageType('AggregateRequest', (_message.Message,), dict(
  DESCRIPTOR = _AGGREGATEREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.AggregateRequest)
  ))
_sym_db.RegisterMessage(AggregateRequest)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.Response)
  ))
_sym_db.RegisterMessage(Response)

Meta = _reflection.GeneratedProtocolMessageType('Meta', (_message.Message,), dict(
  DESCRIPTOR = _META,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.Meta)
  ))
_sym_db.RegisterMessage(Meta)

AllRequest = _reflection.GeneratedProtocolMessageType('AllRequest', (_message.Message,), dict(
  DESCRIPTOR = _ALLREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.AllRequest)
  ))
_sym_db.RegisterMessage(AllRequest)

BatchRequest = _reflection.GeneratedProtocolMessageType('BatchRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.BatchRequest)
  ))
_sym_db.RegisterMessage(BatchRequest)

FaaSRequest = _reflection.GeneratedProtocolMessageType('FaaSRequest', (_message.Message,), dict(
  DESCRIPTOR = _FAASREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:proto.FaaSRequest)
  ))
_sym_db.RegisterMessage(FaaSRequest)


DESCRIPTOR._options = None
_READOPTIONS_SELECTENTRY._options = None
_READOPTIONS_SORTENTRY._options = None

_SPACECLOUD = _descriptor.ServiceDescriptor(
  name='SpaceCloud',
  full_name='proto.SpaceCloud',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1135,
  serialized_end=1500,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='proto.SpaceCloud.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='proto.SpaceCloud.Read',
    index=1,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='proto.SpaceCloud.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='proto.SpaceCloud.Delete',
    index=3,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Aggregate',
    full_name='proto.SpaceCloud.Aggregate',
    index=4,
    containing_service=None,
    input_type=_AGGREGATEREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Batch',
    full_name='proto.SpaceCloud.Batch',
    index=5,
    containing_service=None,
    input_type=_BATCHREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Call',
    full_name='proto.SpaceCloud.Call',
    index=6,
    containing_service=None,
    input_type=_FAASREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPACECLOUD)

DESCRIPTOR.services_by_name['SpaceCloud'] = _SPACECLOUD

# @@protoc_insertion_point(module_scope)