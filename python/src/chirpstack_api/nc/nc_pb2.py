# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/nc/nc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.gw import gw_pb2 as chirpstack__api_dot_gw_dot_gw__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chirpstack-api/nc/nc.proto',
  package='nc',
  syntax='proto3',
  serialized_options=b'\n\024io.chirpstack.api.ncB\026NetworkControllerProtoP\001Z.github.com/rtsoft-gmbh/chirpstack-api/go/v3/nc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x63hirpstack-api/nc/nc.proto\x12\x02nc\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1a\x63hirpstack-api/gw/gw.proto\"\xfd\x01\n\x1bHandleUplinkMetaDataRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12!\n\x07tx_info\x18\x02 \x01(\x0b\x32\x10.gw.UplinkTXInfo\x12!\n\x07rx_info\x18\x03 \x03(\x0b\x32\x10.gw.UplinkRXInfo\x12\x1e\n\x16phy_payload_byte_count\x18\x04 \x01(\r\x12\x1e\n\x16mac_command_byte_count\x18\x05 \x01(\r\x12&\n\x1e\x61pplication_payload_byte_count\x18\x06 \x01(\r\x12\x1f\n\x0cmessage_type\x18\x07 \x01(\x0e\x32\t.nc.MType\"\x8e\x02\n\x1dHandleDownlinkMetaDataRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x1a\n\x12multicast_group_id\x18\x02 \x01(\x0c\x12#\n\x07tx_info\x18\x03 \x01(\x0b\x32\x12.gw.DownlinkTXInfo\x12\x1e\n\x16phy_payload_byte_count\x18\x04 \x01(\r\x12\x1e\n\x16mac_command_byte_count\x18\x05 \x01(\r\x12&\n\x1e\x61pplication_payload_byte_count\x18\x06 \x01(\r\x12\x1f\n\x0cmessage_type\x18\x07 \x01(\x0e\x32\t.nc.MType\x12\x12\n\ngateway_id\x18\x08 \x01(\x0c\"O\n\x1dHandleUplinkMACCommandRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x0b\n\x03\x63id\x18\x02 \x01(\r\x12\x10\n\x08\x63ommands\x18\x06 \x03(\x0c\"L\n#HandleRejectedUplinkFrameSetRequest\x12%\n\tframe_set\x18\x01 \x01(\x0b\x32\x12.gw.UplinkFrameSet*\xaf\x01\n\x05MType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0cJOIN_REQUEST\x10\x01\x12\x0f\n\x0bJOIN_ACCEPT\x10\x02\x12\x17\n\x13UNCONFIRMED_DATA_UP\x10\x03\x12\x19\n\x15UNCONFIRMED_DATA_DOWN\x10\x04\x12\x15\n\x11\x43ONFIRMED_DATA_UP\x10\x05\x12\x17\n\x13\x43ONFIRMED_DATA_DOWN\x10\x06\x12\x12\n\x0eREJOIN_REQUEST\x10\x07\x32\xfe\x02\n\x18NetworkControllerService\x12Q\n\x14HandleUplinkMetaData\x12\x1f.nc.HandleUplinkMetaDataRequest\x1a\x16.google.protobuf.Empty\"\x00\x12U\n\x16HandleDownlinkMetaData\x12!.nc.HandleDownlinkMetaDataRequest\x1a\x16.google.protobuf.Empty\"\x00\x12U\n\x16HandleUplinkMACCommand\x12!.nc.HandleUplinkMACCommandRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x61\n\x1cHandleRejectedUplinkFrameSet\x12\'.nc.HandleRejectedUplinkFrameSetRequest\x1a\x16.google.protobuf.Empty\"\x00\x42`\n\x14io.chirpstack.api.ncB\x16NetworkControllerProtoP\x01Z.github.com/rtsoft-gmbh/chirpstack-api/go/v3/ncb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,chirpstack__api_dot_gw_dot_gw__pb2.DESCRIPTOR,])

_MTYPE = _descriptor.EnumDescriptor(
  name='MType',
  full_name='nc.MType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JOIN_REQUEST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JOIN_ACCEPT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNCONFIRMED_DATA_UP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNCONFIRMED_DATA_DOWN', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONFIRMED_DATA_UP', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONFIRMED_DATA_DOWN', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REJOIN_REQUEST', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=780,
  serialized_end=955,
)
_sym_db.RegisterEnumDescriptor(_MTYPE)

MType = enum_type_wrapper.EnumTypeWrapper(_MTYPE)
UNKNOWN = 0
JOIN_REQUEST = 1
JOIN_ACCEPT = 2
UNCONFIRMED_DATA_UP = 3
UNCONFIRMED_DATA_DOWN = 4
CONFIRMED_DATA_UP = 5
CONFIRMED_DATA_DOWN = 6
REJOIN_REQUEST = 7



_HANDLEUPLINKMETADATAREQUEST = _descriptor.Descriptor(
  name='HandleUplinkMetaDataRequest',
  full_name='nc.HandleUplinkMetaDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dev_eui', full_name='nc.HandleUplinkMetaDataRequest.dev_eui', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_info', full_name='nc.HandleUplinkMetaDataRequest.tx_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_info', full_name='nc.HandleUplinkMetaDataRequest.rx_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phy_payload_byte_count', full_name='nc.HandleUplinkMetaDataRequest.phy_payload_byte_count', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mac_command_byte_count', full_name='nc.HandleUplinkMetaDataRequest.mac_command_byte_count', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='application_payload_byte_count', full_name='nc.HandleUplinkMetaDataRequest.application_payload_byte_count', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='nc.HandleUplinkMetaDataRequest.message_type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=92,
  serialized_end=345,
)


_HANDLEDOWNLINKMETADATAREQUEST = _descriptor.Descriptor(
  name='HandleDownlinkMetaDataRequest',
  full_name='nc.HandleDownlinkMetaDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dev_eui', full_name='nc.HandleDownlinkMetaDataRequest.dev_eui', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multicast_group_id', full_name='nc.HandleDownlinkMetaDataRequest.multicast_group_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_info', full_name='nc.HandleDownlinkMetaDataRequest.tx_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phy_payload_byte_count', full_name='nc.HandleDownlinkMetaDataRequest.phy_payload_byte_count', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mac_command_byte_count', full_name='nc.HandleDownlinkMetaDataRequest.mac_command_byte_count', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='application_payload_byte_count', full_name='nc.HandleDownlinkMetaDataRequest.application_payload_byte_count', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='nc.HandleDownlinkMetaDataRequest.message_type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gateway_id', full_name='nc.HandleDownlinkMetaDataRequest.gateway_id', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=348,
  serialized_end=618,
)


_HANDLEUPLINKMACCOMMANDREQUEST = _descriptor.Descriptor(
  name='HandleUplinkMACCommandRequest',
  full_name='nc.HandleUplinkMACCommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dev_eui', full_name='nc.HandleUplinkMACCommandRequest.dev_eui', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cid', full_name='nc.HandleUplinkMACCommandRequest.cid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commands', full_name='nc.HandleUplinkMACCommandRequest.commands', index=2,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=620,
  serialized_end=699,
)


_HANDLEREJECTEDUPLINKFRAMESETREQUEST = _descriptor.Descriptor(
  name='HandleRejectedUplinkFrameSetRequest',
  full_name='nc.HandleRejectedUplinkFrameSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_set', full_name='nc.HandleRejectedUplinkFrameSetRequest.frame_set', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=701,
  serialized_end=777,
)

_HANDLEUPLINKMETADATAREQUEST.fields_by_name['tx_info'].message_type = chirpstack__api_dot_gw_dot_gw__pb2._UPLINKTXINFO
_HANDLEUPLINKMETADATAREQUEST.fields_by_name['rx_info'].message_type = chirpstack__api_dot_gw_dot_gw__pb2._UPLINKRXINFO
_HANDLEUPLINKMETADATAREQUEST.fields_by_name['message_type'].enum_type = _MTYPE
_HANDLEDOWNLINKMETADATAREQUEST.fields_by_name['tx_info'].message_type = chirpstack__api_dot_gw_dot_gw__pb2._DOWNLINKTXINFO
_HANDLEDOWNLINKMETADATAREQUEST.fields_by_name['message_type'].enum_type = _MTYPE
_HANDLEREJECTEDUPLINKFRAMESETREQUEST.fields_by_name['frame_set'].message_type = chirpstack__api_dot_gw_dot_gw__pb2._UPLINKFRAMESET
DESCRIPTOR.message_types_by_name['HandleUplinkMetaDataRequest'] = _HANDLEUPLINKMETADATAREQUEST
DESCRIPTOR.message_types_by_name['HandleDownlinkMetaDataRequest'] = _HANDLEDOWNLINKMETADATAREQUEST
DESCRIPTOR.message_types_by_name['HandleUplinkMACCommandRequest'] = _HANDLEUPLINKMACCOMMANDREQUEST
DESCRIPTOR.message_types_by_name['HandleRejectedUplinkFrameSetRequest'] = _HANDLEREJECTEDUPLINKFRAMESETREQUEST
DESCRIPTOR.enum_types_by_name['MType'] = _MTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HandleUplinkMetaDataRequest = _reflection.GeneratedProtocolMessageType('HandleUplinkMetaDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEUPLINKMETADATAREQUEST,
  '__module__' : 'chirpstack_api.nc.nc_pb2'
  # @@protoc_insertion_point(class_scope:nc.HandleUplinkMetaDataRequest)
  })
_sym_db.RegisterMessage(HandleUplinkMetaDataRequest)

HandleDownlinkMetaDataRequest = _reflection.GeneratedProtocolMessageType('HandleDownlinkMetaDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEDOWNLINKMETADATAREQUEST,
  '__module__' : 'chirpstack_api.nc.nc_pb2'
  # @@protoc_insertion_point(class_scope:nc.HandleDownlinkMetaDataRequest)
  })
_sym_db.RegisterMessage(HandleDownlinkMetaDataRequest)

HandleUplinkMACCommandRequest = _reflection.GeneratedProtocolMessageType('HandleUplinkMACCommandRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEUPLINKMACCOMMANDREQUEST,
  '__module__' : 'chirpstack_api.nc.nc_pb2'
  # @@protoc_insertion_point(class_scope:nc.HandleUplinkMACCommandRequest)
  })
_sym_db.RegisterMessage(HandleUplinkMACCommandRequest)

HandleRejectedUplinkFrameSetRequest = _reflection.GeneratedProtocolMessageType('HandleRejectedUplinkFrameSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEREJECTEDUPLINKFRAMESETREQUEST,
  '__module__' : 'chirpstack_api.nc.nc_pb2'
  # @@protoc_insertion_point(class_scope:nc.HandleRejectedUplinkFrameSetRequest)
  })
_sym_db.RegisterMessage(HandleRejectedUplinkFrameSetRequest)


DESCRIPTOR._options = None

_NETWORKCONTROLLERSERVICE = _descriptor.ServiceDescriptor(
  name='NetworkControllerService',
  full_name='nc.NetworkControllerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=958,
  serialized_end=1340,
  methods=[
  _descriptor.MethodDescriptor(
    name='HandleUplinkMetaData',
    full_name='nc.NetworkControllerService.HandleUplinkMetaData',
    index=0,
    containing_service=None,
    input_type=_HANDLEUPLINKMETADATAREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HandleDownlinkMetaData',
    full_name='nc.NetworkControllerService.HandleDownlinkMetaData',
    index=1,
    containing_service=None,
    input_type=_HANDLEDOWNLINKMETADATAREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HandleUplinkMACCommand',
    full_name='nc.NetworkControllerService.HandleUplinkMACCommand',
    index=2,
    containing_service=None,
    input_type=_HANDLEUPLINKMACCOMMANDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HandleRejectedUplinkFrameSet',
    full_name='nc.NetworkControllerService.HandleRejectedUplinkFrameSet',
    index=3,
    containing_service=None,
    input_type=_HANDLEREJECTEDUPLINKFRAMESETREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NETWORKCONTROLLERSERVICE)

DESCRIPTOR.services_by_name['NetworkControllerService'] = _NETWORKCONTROLLERSERVICE

# @@protoc_insertion_point(module_scope)
