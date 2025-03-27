"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 3, '', 'label.proto')
_sym_db = _symbol_database.Default()
from . import keypoint_pb2 as keypoint__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0blabel.proto\x12&trajdata.dataset_specific.waymo.protos\x1a\x0ekeypoint.proto"\xdd\n\n\x05Label\x12>\n\x03box\x18\x01 \x01(\x0b21.trajdata.dataset_specific.waymo.protos.Label.Box\x12H\n\x08metadata\x18\x02 \x01(\x0b26.trajdata.dataset_specific.waymo.protos.Label.Metadata\x12@\n\x04type\x18\x03 \x01(\x0e22.trajdata.dataset_specific.waymo.protos.Label.Type\x12\n\n\x02id\x18\x04 \x01(\t\x12a\n\x1adetection_difficulty_level\x18\x05 \x01(\x0e2=.trajdata.dataset_specific.waymo.protos.Label.DifficultyLevel\x12`\n\x19tracking_difficulty_level\x18\x06 \x01(\x0e2=.trajdata.dataset_specific.waymo.protos.Label.DifficultyLevel\x12\x1f\n\x17num_lidar_points_in_box\x18\x07 \x01(\x05\x12#\n\x1bnum_top_lidar_points_in_box\x18\r \x01(\x05\x12Q\n\x0flaser_keypoints\x18\x08 \x01(\x0b26.trajdata.dataset_specific.waymo.protos.LaserKeypointsH\x00\x12S\n\x10camera_keypoints\x18\t \x01(\x0b27.trajdata.dataset_specific.waymo.protos.CameraKeypointsH\x00\x12N\n\x0bassociation\x18\n \x01(\x0b29.trajdata.dataset_specific.waymo.protos.Label.Association\x12 \n\x18most_visible_camera_name\x18\x0b \x01(\t\x12L\n\x11camera_synced_box\x18\x0c \x01(\x0b21.trajdata.dataset_specific.waymo.protos.Label.Box\x1a\xbf\x01\n\x03Box\x12\x10\n\x08center_x\x18\x01 \x01(\x01\x12\x10\n\x08center_y\x18\x02 \x01(\x01\x12\x10\n\x08center_z\x18\x03 \x01(\x01\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x04 \x01(\x01\x12\x0e\n\x06height\x18\x06 \x01(\x01\x12\x0f\n\x07heading\x18\x07 \x01(\x01"B\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x0b\n\x07TYPE_3D\x10\x01\x12\x0b\n\x07TYPE_2D\x10\x02\x12\x0e\n\nTYPE_AA_2D\x10\x03\x1ap\n\x08Metadata\x12\x0f\n\x07speed_x\x18\x01 \x01(\x01\x12\x0f\n\x07speed_y\x18\x02 \x01(\x01\x12\x0f\n\x07speed_z\x18\x05 \x01(\x01\x12\x0f\n\x07accel_x\x18\x03 \x01(\x01\x12\x0f\n\x07accel_y\x18\x04 \x01(\x01\x12\x0f\n\x07accel_z\x18\x06 \x01(\x01\x1a&\n\x0bAssociation\x12\x17\n\x0flaser_object_id\x18\x01 \x01(\t"`\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x10\n\x0cTYPE_VEHICLE\x10\x01\x12\x13\n\x0fTYPE_PEDESTRIAN\x10\x02\x12\r\n\tTYPE_SIGN\x10\x03\x12\x10\n\x0cTYPE_CYCLIST\x10\x04"8\n\x0fDifficultyLevel\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07LEVEL_1\x10\x01\x12\x0b\n\x07LEVEL_2\x10\x02B\x11\n\x0fkeypoints_oneof"2\n\x0ePolygon2dProto\x12\t\n\x01x\x18\x01 \x03(\x01\x12\t\n\x01y\x18\x02 \x03(\x01\x12\n\n\x02id\x18\x03 \x01(\t')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_LABEL']._serialized_start = 72
    _globals['_LABEL']._serialized_end = 1445
    _globals['_LABEL_BOX']._serialized_start = 925
    _globals['_LABEL_BOX']._serialized_end = 1116
    _globals['_LABEL_BOX_TYPE']._serialized_start = 1050
    _globals['_LABEL_BOX_TYPE']._serialized_end = 1116
    _globals['_LABEL_METADATA']._serialized_start = 1118
    _globals['_LABEL_METADATA']._serialized_end = 1230
    _globals['_LABEL_ASSOCIATION']._serialized_start = 1232
    _globals['_LABEL_ASSOCIATION']._serialized_end = 1270
    _globals['_LABEL_TYPE']._serialized_start = 1272
    _globals['_LABEL_TYPE']._serialized_end = 1368
    _globals['_LABEL_DIFFICULTYLEVEL']._serialized_start = 1370
    _globals['_LABEL_DIFFICULTYLEVEL']._serialized_end = 1426
    _globals['_POLYGON2DPROTO']._serialized_start = 1447
    _globals['_POLYGON2DPROTO']._serialized_end = 1497