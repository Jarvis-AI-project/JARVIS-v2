# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authority_keys.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61uthority_keys.proto\x12!extensions.api.cast_channel.proto\"\x83\x01\n\rAuthorityKeys\x12\x42\n\x04keys\x18\x01 \x03(\x0b\x32\x34.extensions.api.cast_channel.proto.AuthorityKeys.Key\x1a.\n\x03Key\x12\x13\n\x0b\x66ingerprint\x18\x01 \x02(\x0c\x12\x12\n\npublic_key\x18\x02 \x02(\x0c\x42\x02H\x03')



_AUTHORITYKEYS = DESCRIPTOR.message_types_by_name['AuthorityKeys']
_AUTHORITYKEYS_KEY = _AUTHORITYKEYS.nested_types_by_name['Key']
AuthorityKeys = _reflection.GeneratedProtocolMessageType('AuthorityKeys', (_message.Message,), {

  'Key' : _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
    'DESCRIPTOR' : _AUTHORITYKEYS_KEY,
    '__module__' : 'authority_keys_pb2'
    # @@protoc_insertion_point(class_scope:extensions.api.cast_channel.proto.AuthorityKeys.Key)
    })
  ,
  'DESCRIPTOR' : _AUTHORITYKEYS,
  '__module__' : 'authority_keys_pb2'
  # @@protoc_insertion_point(class_scope:extensions.api.cast_channel.proto.AuthorityKeys)
  })
_sym_db.RegisterMessage(AuthorityKeys)
_sym_db.RegisterMessage(AuthorityKeys.Key)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003'
  _AUTHORITYKEYS._serialized_start=60
  _AUTHORITYKEYS._serialized_end=191
  _AUTHORITYKEYS_KEY._serialized_start=145
  _AUTHORITYKEYS_KEY._serialized_end=191
# @@protoc_insertion_point(module_scope)