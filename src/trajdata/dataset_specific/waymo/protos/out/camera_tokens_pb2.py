"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 3, '', 'camera_tokens.proto')
_sym_db = _symbol_database.Default()
from . import dataset_pb2 as dataset__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13camera_tokens.proto\x12&trajdata.dataset_specific.waymo.protos\x1a\rdataset.proto"p\n\x0cCameraTokens\x12L\n\x0bcamera_name\x18\x01 \x01(\x0e27.trajdata.dataset_specific.waymo.protos.CameraName.Name\x12\x12\n\x06tokens\x18\x02 \x03(\rB\x02\x10\x01"`\n\x11FrameCameraTokens\x12K\n\rcamera_tokens\x18\x01 \x03(\x0b24.trajdata.dataset_specific.waymo.protos.CameraTokens')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'camera_tokens_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CAMERATOKENS'].fields_by_name['tokens']._loaded_options = None
    _globals['_CAMERATOKENS'].fields_by_name['tokens']._serialized_options = b'\x10\x01'
    _globals['_CAMERATOKENS']._serialized_start = 78
    _globals['_CAMERATOKENS']._serialized_end = 190
    _globals['_FRAMECAMERATOKENS']._serialized_start = 192
    _globals['_FRAMECAMERATOKENS']._serialized_end = 288