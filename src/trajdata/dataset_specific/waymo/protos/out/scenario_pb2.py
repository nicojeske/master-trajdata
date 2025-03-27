"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 3, '', 'scenario.proto')
_sym_db = _symbol_database.Default()
from . import camera_tokens_pb2 as camera__tokens__pb2
from . import compressed_lidar_pb2 as compressed__lidar__pb2
from . import map_pb2 as map__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0escenario.proto\x12&trajdata.dataset_specific.waymo.protos\x1a\x13camera_tokens.proto\x1a\x16compressed_lidar.proto\x1a\tmap.proto"\xba\x01\n\x0bObjectState\x12\x10\n\x08center_x\x18\x02 \x01(\x01\x12\x10\n\x08center_y\x18\x03 \x01(\x01\x12\x10\n\x08center_z\x18\x04 \x01(\x01\x12\x0e\n\x06length\x18\x05 \x01(\x02\x12\r\n\x05width\x18\x06 \x01(\x02\x12\x0e\n\x06height\x18\x07 \x01(\x02\x12\x0f\n\x07heading\x18\x08 \x01(\x02\x12\x12\n\nvelocity_x\x18\t \x01(\x02\x12\x12\n\nvelocity_y\x18\n \x01(\x02\x12\r\n\x05valid\x18\x0b \x01(\x08"\x8e\x02\n\x05Track\x12\n\n\x02id\x18\x01 \x01(\x05\x12M\n\x0bobject_type\x18\x02 \x01(\x0e28.trajdata.dataset_specific.waymo.protos.Track.ObjectType\x12C\n\x06states\x18\x03 \x03(\x0b23.trajdata.dataset_specific.waymo.protos.ObjectState"e\n\nObjectType\x12\x0e\n\nTYPE_UNSET\x10\x00\x12\x10\n\x0cTYPE_VEHICLE\x10\x01\x12\x13\n\x0fTYPE_PEDESTRIAN\x10\x02\x12\x10\n\x0cTYPE_CYCLIST\x10\x03\x12\x0e\n\nTYPE_OTHER\x10\x04"f\n\x0fDynamicMapState\x12S\n\x0blane_states\x18\x01 \x03(\x0b2>.trajdata.dataset_specific.waymo.protos.TrafficSignalLaneState"\xc0\x01\n\x12RequiredPrediction\x12\x13\n\x0btrack_index\x18\x01 \x01(\x05\x12^\n\ndifficulty\x18\x02 \x01(\x0e2J.trajdata.dataset_specific.waymo.protos.RequiredPrediction.DifficultyLevel"5\n\x0fDifficultyLevel\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07LEVEL_1\x10\x01\x12\x0b\n\x07LEVEL_2\x10\x02"\x87\x05\n\x08Scenario\x12\x13\n\x0bscenario_id\x18\x05 \x01(\t\x12\x1a\n\x12timestamps_seconds\x18\x01 \x03(\x01\x12\x1a\n\x12current_time_index\x18\n \x01(\x05\x12=\n\x06tracks\x18\x02 \x03(\x0b2-.trajdata.dataset_specific.waymo.protos.Track\x12S\n\x12dynamic_map_states\x18\x07 \x03(\x0b27.trajdata.dataset_specific.waymo.protos.DynamicMapState\x12H\n\x0cmap_features\x18\x08 \x03(\x0b22.trajdata.dataset_specific.waymo.protos.MapFeature\x12\x17\n\x0fsdc_track_index\x18\x06 \x01(\x05\x12\x1b\n\x13objects_of_interest\x18\x04 \x03(\x05\x12U\n\x11tracks_to_predict\x18\x0b \x03(\x0b2:.trajdata.dataset_specific.waymo.protos.RequiredPrediction\x12e\n\x1bcompressed_frame_laser_data\x18\x0c \x03(\x0b2@.trajdata.dataset_specific.waymo.protos.CompressedFrameLaserData\x12V\n\x13frame_camera_tokens\x18\r \x03(\x0b29.trajdata.dataset_specific.waymo.protos.FrameCameraTokensJ\x04\x08\t\x10\n')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'scenario_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_OBJECTSTATE']._serialized_start = 115
    _globals['_OBJECTSTATE']._serialized_end = 301
    _globals['_TRACK']._serialized_start = 304
    _globals['_TRACK']._serialized_end = 574
    _globals['_TRACK_OBJECTTYPE']._serialized_start = 473
    _globals['_TRACK_OBJECTTYPE']._serialized_end = 574
    _globals['_DYNAMICMAPSTATE']._serialized_start = 576
    _globals['_DYNAMICMAPSTATE']._serialized_end = 678
    _globals['_REQUIREDPREDICTION']._serialized_start = 681
    _globals['_REQUIREDPREDICTION']._serialized_end = 873
    _globals['_REQUIREDPREDICTION_DIFFICULTYLEVEL']._serialized_start = 820
    _globals['_REQUIREDPREDICTION_DIFFICULTYLEVEL']._serialized_end = 873
    _globals['_SCENARIO']._serialized_start = 876
    _globals['_SCENARIO']._serialized_end = 1523