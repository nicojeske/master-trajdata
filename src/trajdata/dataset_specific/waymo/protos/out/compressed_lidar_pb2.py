"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 3, '', 'compressed_lidar.proto')
_sym_db = _symbol_database.Default()
from . import dataset_pb2 as dataset__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16compressed_lidar.proto\x12&trajdata.dataset_specific.waymo.protos\x1a\rdataset.proto"g\n\x14CompressedRangeImage\x12$\n\x1crange_image_delta_compressed\x18\x01 \x01(\x0c\x12)\n!range_image_pose_delta_compressed\x18\x04 \x01(\x0c"2\n\x08Metadata\x12\r\n\x05shape\x18\x01 \x03(\x05\x12\x17\n\x0fquant_precision\x18\x02 \x03(\x02"~\n\x10DeltaEncodedData\x12\x14\n\x08residual\x18\x01 \x03(\x12B\x02\x10\x01\x12\x10\n\x04mask\x18\x02 \x03(\rB\x02\x10\x01\x12B\n\x08metadata\x18\x03 \x01(\x0b20.trajdata.dataset_specific.waymo.protos.Metadata"\xfb\x01\n\x0fCompressedLaser\x12D\n\x04name\x18\x01 \x01(\x0e26.trajdata.dataset_specific.waymo.protos.LaserName.Name\x12P\n\nri_return1\x18\x02 \x01(\x0b2<.trajdata.dataset_specific.waymo.protos.CompressedRangeImage\x12P\n\nri_return2\x18\x03 \x01(\x0b2<.trajdata.dataset_specific.waymo.protos.CompressedRangeImage"\xfa\x01\n\x18CompressedFrameLaserData\x12G\n\x06lasers\x18\x01 \x03(\x0b27.trajdata.dataset_specific.waymo.protos.CompressedLaser\x12T\n\x12laser_calibrations\x18\x02 \x03(\x0b28.trajdata.dataset_specific.waymo.protos.LaserCalibration\x12?\n\x04pose\x18\x03 \x01(\x0b21.trajdata.dataset_specific.waymo.protos.Transform')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'compressed_lidar_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_DELTAENCODEDDATA'].fields_by_name['residual']._loaded_options = None
    _globals['_DELTAENCODEDDATA'].fields_by_name['residual']._serialized_options = b'\x10\x01'
    _globals['_DELTAENCODEDDATA'].fields_by_name['mask']._loaded_options = None
    _globals['_DELTAENCODEDDATA'].fields_by_name['mask']._serialized_options = b'\x10\x01'
    _globals['_COMPRESSEDRANGEIMAGE']._serialized_start = 81
    _globals['_COMPRESSEDRANGEIMAGE']._serialized_end = 184
    _globals['_METADATA']._serialized_start = 186
    _globals['_METADATA']._serialized_end = 236
    _globals['_DELTAENCODEDDATA']._serialized_start = 238
    _globals['_DELTAENCODEDDATA']._serialized_end = 364
    _globals['_COMPRESSEDLASER']._serialized_start = 367
    _globals['_COMPRESSEDLASER']._serialized_end = 618
    _globals['_COMPRESSEDFRAMELASERDATA']._serialized_start = 621
    _globals['_COMPRESSEDFRAMELASERDATA']._serialized_end = 871