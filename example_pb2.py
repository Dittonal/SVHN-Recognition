# 由协议缓冲区编译器生成。不要编辑！
# source: example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rexample.proto\"8\n\x07\x45xample\x12\r\n\x05image\x18\x01 \x01(\x0c\x12\x0e\n\x06length\x18\x02 \x01(\x05\x12\x0e\n\x06\x64igits\x18\x03 \x03(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EXAMPLE = _descriptor.Descriptor(
  name='Example',
  full_name='Example',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='Example.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='Example.length', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='digits', full_name='Example.digits', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['Example'] = _EXAMPLE

Example = _reflection.GeneratedProtocolMessageType('Example', (_message.Message,), dict(
  DESCRIPTOR = _EXAMPLE,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:Example)
  ))
_sym_db.RegisterMessage(Example)


# @@protoc_insertion_point(module_scope)
