# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dzhyun.zhibiao.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dzhyun import zhibiaojisuan_pb2 as dzhyun_dot_zhibiaojisuan__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dzhyun.zhibiao.proto',
  package='dzhyun',
  syntax='proto2',
  serialized_pb=_b('\n\x14\x64zhyun.zhibiao.proto\x12\x06\x64zhyun\x1a\x1a\x64zhyun.zhibiaojisuan.proto\"\xf0\x07\n\x07ZhiBiao\x12\x11\n\tMingCheng\x18\x01 \x02(\t\x12\x0f\n\x07MiaoShu\x18\x02 \x01(\t\x12\x0e\n\x06YongFa\x18\x03 \x01(\t\x12\x16\n\x0e\x43\x61nShuJingLing\x18\x04 \x01(\t\x12\x10\n\x08JianYiZu\x18\x05 \x01(\t\x12\x0e\n\x06WenBen\x18\x06 \x01(\t\x12\x0f\n\x07ShiJian\x18\x07 \x01(\x03\x12*\n\x07LeiXing\x18\x08 \x01(\x0e\x32\x19.dzhyun.ZhiBiao.ZBLeiXing\x12\x36\n\rWenBenLeiXing\x18\t \x01(\x0e\x32\x1f.dzhyun.ZhiBiao.ZBWenBenLeiXing\x12\x0e\n\x06\x42\x61nBen\x18\n \x01(\x03\x12\x0f\n\x07ShuXing\x18\x0b \x01(\x03\x12\x14\n\x0cMoRenLeiXing\x18\x0c \x01(\x03\x12\x0f\n\x07ZiJieMa\x18\r \x01(\t\x12\x11\n\tChangYong\x18\x0e \x01(\x08\x12\x10\n\x08ZiDingYi\x18\x0f \x01(\x08\x12\x11\n\tEWaiShuJu\x18\x10 \x03(\x03\x12(\n\x06\x43\x61nShu\x18\x11 \x03(\x0b\x32\x18.dzhyun.ZhiBiao.ZBCanShu\x12(\n\x06ShuChu\x18\x12 \x03(\x0b\x32\x18.dzhyun.ZhiBiao.ZBShuChu\x1a\xba\x01\n\x08ZBShuChu\x12\x11\n\tMingCheng\x18\x01 \x02(\t\x12:\n\x07LeiXing\x18\x02 \x02(\x0e\x32).dzhyun.ZhiBiaoShuChu.ZBShuXing.SXLeiXing\x12\x0e\n\x06YiDong\x18\x03 \x02(\x03\x12\x0f\n\x07ShuXing\x18\x04 \x02(\x03\x12\r\n\x05YanSe\x18\x05 \x02(\x03\x12\x17\n\x0f\x42ianLiangWeiZhi\x18\x06 \x02(\x03\x12\x16\n\x0eKuoZhanShuXing\x18\x07 \x02(\x03\x1a\x66\n\x08ZBCanShu\x12\x11\n\tMingCheng\x18\x01 \x02(\t\x12\x10\n\x08MoRenZhi\x18\x02 \x02(\x03\x12\x10\n\x08ZuiDaZhi\x18\x03 \x02(\x03\x12\x12\n\nZuiXiaoZhi\x18\x04 \x02(\x03\x12\x0f\n\x07\x42uChang\x18\x05 \x02(\x03\"\xb7\x01\n\tZBLeiXing\x12\x11\n\rTYPE_EXPLORER\x10\x00\x12\x10\n\x0cTYPE_SYSTEST\x10\x01\x12\x12\n\x0eTYPE_MAIN_PICT\x10\x02\x12\x11\n\rTYPE_MAIN_ADD\x10\x03\x12\x11\n\rTYPE_SUB_PICT\x10\x04\x12\x11\n\rTYPE_PAINT_IT\x10\x05\x12\x12\n\x0eTYPE_TEMP_INDI\x10\x06\x12\x12\n\x0eTYPE_TECHNIQUE\x10\x07\x12\x10\n\x0cTYPE_UNKNOWN\x10\x08\"O\n\x0fZBWenBenLeiXing\x12\x14\n\x10TEXTTYPE_FORMULA\x10\x00\x12\x10\n\x0cTEXTTYPE_LUA\x10\x01\x12\x14\n\x10TEXTTYPE_UNKNOWN\x10\x02\x42\x12\n\x10\x63om.dzhyun.proto')
  ,
  dependencies=[dzhyun_dot_zhibiaojisuan__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ZHIBIAO_ZBLEIXING = _descriptor.EnumDescriptor(
  name='ZBLeiXing',
  full_name='dzhyun.ZhiBiao.ZBLeiXing',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_EXPLORER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SYSTEST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_MAIN_PICT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_MAIN_ADD', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SUB_PICT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_PAINT_IT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_TEMP_INDI', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_TECHNIQUE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNKNOWN', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=805,
  serialized_end=988,
)
_sym_db.RegisterEnumDescriptor(_ZHIBIAO_ZBLEIXING)

_ZHIBIAO_ZBWENBENLEIXING = _descriptor.EnumDescriptor(
  name='ZBWenBenLeiXing',
  full_name='dzhyun.ZhiBiao.ZBWenBenLeiXing',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEXTTYPE_FORMULA', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXTTYPE_LUA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXTTYPE_UNKNOWN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=990,
  serialized_end=1069,
)
_sym_db.RegisterEnumDescriptor(_ZHIBIAO_ZBWENBENLEIXING)


_ZHIBIAO_ZBSHUCHU = _descriptor.Descriptor(
  name='ZBShuChu',
  full_name='dzhyun.ZhiBiao.ZBShuChu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MingCheng', full_name='dzhyun.ZhiBiao.ZBShuChu.MingCheng', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LeiXing', full_name='dzhyun.ZhiBiao.ZBShuChu.LeiXing', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YiDong', full_name='dzhyun.ZhiBiao.ZBShuChu.YiDong', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ShuXing', full_name='dzhyun.ZhiBiao.ZBShuChu.ShuXing', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YanSe', full_name='dzhyun.ZhiBiao.ZBShuChu.YanSe', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BianLiangWeiZhi', full_name='dzhyun.ZhiBiao.ZBShuChu.BianLiangWeiZhi', index=5,
      number=6, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='KuoZhanShuXing', full_name='dzhyun.ZhiBiao.ZBShuChu.KuoZhanShuXing', index=6,
      number=7, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=512,
  serialized_end=698,
)

_ZHIBIAO_ZBCANSHU = _descriptor.Descriptor(
  name='ZBCanShu',
  full_name='dzhyun.ZhiBiao.ZBCanShu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MingCheng', full_name='dzhyun.ZhiBiao.ZBCanShu.MingCheng', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MoRenZhi', full_name='dzhyun.ZhiBiao.ZBCanShu.MoRenZhi', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ZuiDaZhi', full_name='dzhyun.ZhiBiao.ZBCanShu.ZuiDaZhi', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ZuiXiaoZhi', full_name='dzhyun.ZhiBiao.ZBCanShu.ZuiXiaoZhi', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BuChang', full_name='dzhyun.ZhiBiao.ZBCanShu.BuChang', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=700,
  serialized_end=802,
)

_ZHIBIAO = _descriptor.Descriptor(
  name='ZhiBiao',
  full_name='dzhyun.ZhiBiao',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MingCheng', full_name='dzhyun.ZhiBiao.MingCheng', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MiaoShu', full_name='dzhyun.ZhiBiao.MiaoShu', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YongFa', full_name='dzhyun.ZhiBiao.YongFa', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CanShuJingLing', full_name='dzhyun.ZhiBiao.CanShuJingLing', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JianYiZu', full_name='dzhyun.ZhiBiao.JianYiZu', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WenBen', full_name='dzhyun.ZhiBiao.WenBen', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ShiJian', full_name='dzhyun.ZhiBiao.ShiJian', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LeiXing', full_name='dzhyun.ZhiBiao.LeiXing', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WenBenLeiXing', full_name='dzhyun.ZhiBiao.WenBenLeiXing', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BanBen', full_name='dzhyun.ZhiBiao.BanBen', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ShuXing', full_name='dzhyun.ZhiBiao.ShuXing', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MoRenLeiXing', full_name='dzhyun.ZhiBiao.MoRenLeiXing', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ZiJieMa', full_name='dzhyun.ZhiBiao.ZiJieMa', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChangYong', full_name='dzhyun.ZhiBiao.ChangYong', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ZiDingYi', full_name='dzhyun.ZhiBiao.ZiDingYi', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EWaiShuJu', full_name='dzhyun.ZhiBiao.EWaiShuJu', index=15,
      number=16, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CanShu', full_name='dzhyun.ZhiBiao.CanShu', index=16,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ShuChu', full_name='dzhyun.ZhiBiao.ShuChu', index=17,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ZHIBIAO_ZBSHUCHU, _ZHIBIAO_ZBCANSHU, ],
  enum_types=[
    _ZHIBIAO_ZBLEIXING,
    _ZHIBIAO_ZBWENBENLEIXING,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=1069,
)

_ZHIBIAO_ZBSHUCHU.fields_by_name['LeiXing'].enum_type = dzhyun_dot_zhibiaojisuan__pb2._ZHIBIAOSHUCHU_ZBSHUXING_SXLEIXING
_ZHIBIAO_ZBSHUCHU.containing_type = _ZHIBIAO
_ZHIBIAO_ZBCANSHU.containing_type = _ZHIBIAO
_ZHIBIAO.fields_by_name['LeiXing'].enum_type = _ZHIBIAO_ZBLEIXING
_ZHIBIAO.fields_by_name['WenBenLeiXing'].enum_type = _ZHIBIAO_ZBWENBENLEIXING
_ZHIBIAO.fields_by_name['CanShu'].message_type = _ZHIBIAO_ZBCANSHU
_ZHIBIAO.fields_by_name['ShuChu'].message_type = _ZHIBIAO_ZBSHUCHU
_ZHIBIAO_ZBLEIXING.containing_type = _ZHIBIAO
_ZHIBIAO_ZBWENBENLEIXING.containing_type = _ZHIBIAO
DESCRIPTOR.message_types_by_name['ZhiBiao'] = _ZHIBIAO

ZhiBiao = _reflection.GeneratedProtocolMessageType('ZhiBiao', (_message.Message,), dict(

  ZBShuChu = _reflection.GeneratedProtocolMessageType('ZBShuChu', (_message.Message,), dict(
    DESCRIPTOR = _ZHIBIAO_ZBSHUCHU,
    __module__ = 'dzhyun.zhibiao_pb2'
    # @@protoc_insertion_point(class_scope:dzhyun.ZhiBiao.ZBShuChu)
    ))
  ,

  ZBCanShu = _reflection.GeneratedProtocolMessageType('ZBCanShu', (_message.Message,), dict(
    DESCRIPTOR = _ZHIBIAO_ZBCANSHU,
    __module__ = 'dzhyun.zhibiao_pb2'
    # @@protoc_insertion_point(class_scope:dzhyun.ZhiBiao.ZBCanShu)
    ))
  ,
  DESCRIPTOR = _ZHIBIAO,
  __module__ = 'dzhyun.zhibiao_pb2'
  # @@protoc_insertion_point(class_scope:dzhyun.ZhiBiao)
  ))
_sym_db.RegisterMessage(ZhiBiao)
_sym_db.RegisterMessage(ZhiBiao.ZBShuChu)
_sym_db.RegisterMessage(ZhiBiao.ZBCanShu)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020com.dzhyun.proto'))
# @@protoc_insertion_point(module_scope)