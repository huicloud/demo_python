# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dzhyun.jianpanbao.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dzhyun.jianpanbao.proto',
  package='dzhyun',
  syntax='proto2',
  serialized_pb=_b('\n\x17\x64zhyun.jianpanbao.proto\x12\x06\x64zhyun\"N\n\x08JPBShuJu\x12\r\n\x05\x44\x61iMa\x18\x01 \x02(\t\x12\x11\n\tMingCheng\x18\x02 \x02(\t\x12\x0f\n\x07ShuXing\x18\x03 \x01(\t\x12\x0f\n\x07KuoZhan\x18\x04 \x01(\t\"Q\n\tJPBShuChu\x12#\n\x07LeiXing\x18\x01 \x02(\x0e\x32\x12.dzhyun.JPBLeiXing\x12\x1f\n\x05ShuJu\x18\x02 \x03(\x0b\x32\x10.dzhyun.JPBShuJu\"I\n\x10JianPanBaoShuChu\x12\x12\n\nGuanJianZi\x18\x01 \x02(\t\x12!\n\x06JieGuo\x18\x02 \x03(\x0b\x32\x11.dzhyun.JPBShuChu*\x80\x01\n\nJPBLeiXing\x12\x0c\n\x08TYPE_OBJ\x10\x00\x12\r\n\tTYPE_INDI\x10\x01\x12\x0e\n\nTYPE_TOPIC\x10\x02\x12\x0c\n\x08TYPE_LHB\x10\x03\x12\x0f\n\x0bTYPE_BLKOBJ\x10\x04\x12\x13\n\x0fTYPE_TOPICANALY\x10\x05\x12\x11\n\rTYPE_OBJPHONE\x10\x06\x42\x12\n\x10\x63om.dzhyun.proto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_JPBLEIXING = _descriptor.EnumDescriptor(
  name='JPBLeiXing',
  full_name='dzhyun.JPBLeiXing',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_OBJ', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_INDI', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_TOPIC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_LHB', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_BLKOBJ', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_TOPICANALY', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_OBJPHONE', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=274,
  serialized_end=402,
)
_sym_db.RegisterEnumDescriptor(_JPBLEIXING)

JPBLeiXing = enum_type_wrapper.EnumTypeWrapper(_JPBLEIXING)
TYPE_OBJ = 0
TYPE_INDI = 1
TYPE_TOPIC = 2
TYPE_LHB = 3
TYPE_BLKOBJ = 4
TYPE_TOPICANALY = 5
TYPE_OBJPHONE = 6



_JPBSHUJU = _descriptor.Descriptor(
  name='JPBShuJu',
  full_name='dzhyun.JPBShuJu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DaiMa', full_name='dzhyun.JPBShuJu.DaiMa', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MingCheng', full_name='dzhyun.JPBShuJu.MingCheng', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ShuXing', full_name='dzhyun.JPBShuJu.ShuXing', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='KuoZhan', full_name='dzhyun.JPBShuJu.KuoZhan', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=113,
)


_JPBSHUCHU = _descriptor.Descriptor(
  name='JPBShuChu',
  full_name='dzhyun.JPBShuChu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='LeiXing', full_name='dzhyun.JPBShuChu.LeiXing', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ShuJu', full_name='dzhyun.JPBShuChu.ShuJu', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=196,
)


_JIANPANBAOSHUCHU = _descriptor.Descriptor(
  name='JianPanBaoShuChu',
  full_name='dzhyun.JianPanBaoShuChu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='GuanJianZi', full_name='dzhyun.JianPanBaoShuChu.GuanJianZi', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JieGuo', full_name='dzhyun.JianPanBaoShuChu.JieGuo', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=271,
)

_JPBSHUCHU.fields_by_name['LeiXing'].enum_type = _JPBLEIXING
_JPBSHUCHU.fields_by_name['ShuJu'].message_type = _JPBSHUJU
_JIANPANBAOSHUCHU.fields_by_name['JieGuo'].message_type = _JPBSHUCHU
DESCRIPTOR.message_types_by_name['JPBShuJu'] = _JPBSHUJU
DESCRIPTOR.message_types_by_name['JPBShuChu'] = _JPBSHUCHU
DESCRIPTOR.message_types_by_name['JianPanBaoShuChu'] = _JIANPANBAOSHUCHU
DESCRIPTOR.enum_types_by_name['JPBLeiXing'] = _JPBLEIXING

JPBShuJu = _reflection.GeneratedProtocolMessageType('JPBShuJu', (_message.Message,), dict(
  DESCRIPTOR = _JPBSHUJU,
  __module__ = 'dzhyun.jianpanbao_pb2'
  # @@protoc_insertion_point(class_scope:dzhyun.JPBShuJu)
  ))
_sym_db.RegisterMessage(JPBShuJu)

JPBShuChu = _reflection.GeneratedProtocolMessageType('JPBShuChu', (_message.Message,), dict(
  DESCRIPTOR = _JPBSHUCHU,
  __module__ = 'dzhyun.jianpanbao_pb2'
  # @@protoc_insertion_point(class_scope:dzhyun.JPBShuChu)
  ))
_sym_db.RegisterMessage(JPBShuChu)

JianPanBaoShuChu = _reflection.GeneratedProtocolMessageType('JianPanBaoShuChu', (_message.Message,), dict(
  DESCRIPTOR = _JIANPANBAOSHUCHU,
  __module__ = 'dzhyun.jianpanbao_pb2'
  # @@protoc_insertion_point(class_scope:dzhyun.JianPanBaoShuChu)
  ))
_sym_db.RegisterMessage(JianPanBaoShuChu)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020com.dzhyun.proto'))
# @@protoc_insertion_point(module_scope)
