"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 3, '', 'keypoint.proto')
_sym_db = _symbol_database.Default()
from . import vector_pb2 as vector__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ekeypoint.proto\x12&trajdata.dataset_specific.waymo.protos\x1a\x0cvector.proto")\n\x12KeypointVisibility\x12\x13\n\x0bis_occluded\x18\x01 \x01(\x08"\xae\x01\n\nKeypoint2d\x12E\n\x0blocation_px\x18\x01 \x01(\x0b20.trajdata.dataset_specific.waymo.protos.Vector2d\x12N\n\nvisibility\x18\x02 \x01(\x0b2:.trajdata.dataset_specific.waymo.protos.KeypointVisibility*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02"\xad\x01\n\nKeypoint3d\x12D\n\nlocation_m\x18\x01 \x01(\x0b20.trajdata.dataset_specific.waymo.protos.Vector3d\x12N\n\nvisibility\x18\x02 \x01(\x0b2:.trajdata.dataset_specific.waymo.protos.KeypointVisibility*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02"\xe6\x01\n\x0eCameraKeypoint\x12B\n\x04type\x18\x01 \x01(\x0e24.trajdata.dataset_specific.waymo.protos.KeypointType\x12G\n\x0bkeypoint_2d\x18\x02 \x01(\x0b22.trajdata.dataset_specific.waymo.protos.Keypoint2d\x12G\n\x0bkeypoint_3d\x18\x03 \x01(\x0b22.trajdata.dataset_specific.waymo.protos.Keypoint3d"[\n\x0fCameraKeypoints\x12H\n\x08keypoint\x18\x01 \x03(\x0b26.trajdata.dataset_specific.waymo.protos.CameraKeypoint"\x9c\x01\n\rLaserKeypoint\x12B\n\x04type\x18\x01 \x01(\x0e24.trajdata.dataset_specific.waymo.protos.KeypointType\x12G\n\x0bkeypoint_3d\x18\x02 \x01(\x0b22.trajdata.dataset_specific.waymo.protos.Keypoint3d"Y\n\x0eLaserKeypoints\x12G\n\x08keypoint\x18\x01 \x03(\x0b25.trajdata.dataset_specific.waymo.protos.LaserKeypoint*\xee\x03\n\x0cKeypointType\x12\x1d\n\x19KEYPOINT_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12KEYPOINT_TYPE_NOSE\x10\x01\x12\x1f\n\x1bKEYPOINT_TYPE_LEFT_SHOULDER\x10\x05\x12\x1c\n\x18KEYPOINT_TYPE_LEFT_ELBOW\x10\x06\x12\x1c\n\x18KEYPOINT_TYPE_LEFT_WRIST\x10\x07\x12\x1a\n\x16KEYPOINT_TYPE_LEFT_HIP\x10\x08\x12\x1b\n\x17KEYPOINT_TYPE_LEFT_KNEE\x10\t\x12\x1c\n\x18KEYPOINT_TYPE_LEFT_ANKLE\x10\n\x12 \n\x1cKEYPOINT_TYPE_RIGHT_SHOULDER\x10\r\x12\x1d\n\x19KEYPOINT_TYPE_RIGHT_ELBOW\x10\x0e\x12\x1d\n\x19KEYPOINT_TYPE_RIGHT_WRIST\x10\x0f\x12\x1b\n\x17KEYPOINT_TYPE_RIGHT_HIP\x10\x10\x12\x1c\n\x18KEYPOINT_TYPE_RIGHT_KNEE\x10\x11\x12\x1d\n\x19KEYPOINT_TYPE_RIGHT_ANKLE\x10\x12\x12\x1a\n\x16KEYPOINT_TYPE_FOREHEAD\x10\x13\x12\x1d\n\x19KEYPOINT_TYPE_HEAD_CENTER\x10\x14')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'keypoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_KEYPOINTTYPE']._serialized_start = 1045
    _globals['_KEYPOINTTYPE']._serialized_end = 1539
    _globals['_KEYPOINTVISIBILITY']._serialized_start = 72
    _globals['_KEYPOINTVISIBILITY']._serialized_end = 113
    _globals['_KEYPOINT2D']._serialized_start = 116
    _globals['_KEYPOINT2D']._serialized_end = 290
    _globals['_KEYPOINT3D']._serialized_start = 293
    _globals['_KEYPOINT3D']._serialized_end = 466
    _globals['_CAMERAKEYPOINT']._serialized_start = 469
    _globals['_CAMERAKEYPOINT']._serialized_end = 699
    _globals['_CAMERAKEYPOINTS']._serialized_start = 701
    _globals['_CAMERAKEYPOINTS']._serialized_end = 792
    _globals['_LASERKEYPOINT']._serialized_start = 795
    _globals['_LASERKEYPOINT']._serialized_end = 951
    _globals['_LASERKEYPOINTS']._serialized_start = 953
    _globals['_LASERKEYPOINTS']._serialized_end = 1042