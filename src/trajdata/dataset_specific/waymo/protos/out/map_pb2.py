"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 3, '', 'map.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tmap.proto\x12&trajdata.dataset_specific.waymo.protos"\x9d\x01\n\x03Map\x12H\n\x0cmap_features\x18\x01 \x03(\x0b22.trajdata.dataset_specific.waymo.protos.MapFeature\x12L\n\x0edynamic_states\x18\x02 \x03(\x0b24.trajdata.dataset_specific.waymo.protos.DynamicState"~\n\x0cDynamicState\x12\x19\n\x11timestamp_seconds\x18\x01 \x01(\x01\x12S\n\x0blane_states\x18\x02 \x03(\x0b2>.trajdata.dataset_specific.waymo.protos.TrafficSignalLaneState"\xb4\x03\n\x16TrafficSignalLaneState\x12\x0c\n\x04lane\x18\x01 \x01(\x03\x12S\n\x05state\x18\x02 \x01(\x0e2D.trajdata.dataset_specific.waymo.protos.TrafficSignalLaneState.State\x12D\n\nstop_point\x18\x03 \x01(\x0b20.trajdata.dataset_specific.waymo.protos.MapPoint"\xf0\x01\n\x05State\x12\x16\n\x12LANE_STATE_UNKNOWN\x10\x00\x12\x19\n\x15LANE_STATE_ARROW_STOP\x10\x01\x12\x1c\n\x18LANE_STATE_ARROW_CAUTION\x10\x02\x12\x17\n\x13LANE_STATE_ARROW_GO\x10\x03\x12\x13\n\x0fLANE_STATE_STOP\x10\x04\x12\x16\n\x12LANE_STATE_CAUTION\x10\x05\x12\x11\n\rLANE_STATE_GO\x10\x06\x12\x1c\n\x18LANE_STATE_FLASHING_STOP\x10\x07\x12\x1f\n\x1bLANE_STATE_FLASHING_CAUTION\x10\x08"\x98\x04\n\nMapFeature\x12\n\n\x02id\x18\x01 \x01(\x03\x12B\n\x04lane\x18\x03 \x01(\x0b22.trajdata.dataset_specific.waymo.protos.LaneCenterH\x00\x12E\n\troad_line\x18\x04 \x01(\x0b20.trajdata.dataset_specific.waymo.protos.RoadLineH\x00\x12E\n\troad_edge\x18\x05 \x01(\x0b20.trajdata.dataset_specific.waymo.protos.RoadEdgeH\x00\x12E\n\tstop_sign\x18\x07 \x01(\x0b20.trajdata.dataset_specific.waymo.protos.StopSignH\x00\x12F\n\tcrosswalk\x18\x08 \x01(\x0b21.trajdata.dataset_specific.waymo.protos.CrosswalkH\x00\x12G\n\nspeed_bump\x18\t \x01(\x0b21.trajdata.dataset_specific.waymo.protos.SpeedBumpH\x00\x12D\n\x08driveway\x18\n \x01(\x0b20.trajdata.dataset_specific.waymo.protos.DrivewayH\x00B\x0e\n\x0cfeature_data"+\n\x08MapPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01"\xb6\x01\n\x0fBoundarySegment\x12\x18\n\x10lane_start_index\x18\x01 \x01(\x05\x12\x16\n\x0elane_end_index\x18\x02 \x01(\x05\x12\x1b\n\x13boundary_feature_id\x18\x03 \x01(\x03\x12T\n\rboundary_type\x18\x04 \x01(\x0e2=.trajdata.dataset_specific.waymo.protos.RoadLine.RoadLineType"\xdb\x01\n\x0cLaneNeighbor\x12\x12\n\nfeature_id\x18\x01 \x01(\x03\x12\x18\n\x10self_start_index\x18\x02 \x01(\x05\x12\x16\n\x0eself_end_index\x18\x03 \x01(\x05\x12\x1c\n\x14neighbor_start_index\x18\x04 \x01(\x05\x12\x1a\n\x12neighbor_end_index\x18\x05 \x01(\x05\x12K\n\nboundaries\x18\x06 \x03(\x0b27.trajdata.dataset_specific.waymo.protos.BoundarySegment"\x9d\x05\n\nLaneCenter\x12\x17\n\x0fspeed_limit_mph\x18\x01 \x01(\x01\x12I\n\x04type\x18\x02 \x01(\x0e2;.trajdata.dataset_specific.waymo.protos.LaneCenter.LaneType\x12\x15\n\rinterpolating\x18\x03 \x01(\x08\x12B\n\x08polyline\x18\x08 \x03(\x0b20.trajdata.dataset_specific.waymo.protos.MapPoint\x12\x17\n\x0bentry_lanes\x18\t \x03(\x03B\x02\x10\x01\x12\x16\n\nexit_lanes\x18\n \x03(\x03B\x02\x10\x01\x12P\n\x0fleft_boundaries\x18\r \x03(\x0b27.trajdata.dataset_specific.waymo.protos.BoundarySegment\x12Q\n\x10right_boundaries\x18\x0e \x03(\x0b27.trajdata.dataset_specific.waymo.protos.BoundarySegment\x12L\n\x0eleft_neighbors\x18\x0b \x03(\x0b24.trajdata.dataset_specific.waymo.protos.LaneNeighbor\x12M\n\x0fright_neighbors\x18\x0c \x03(\x0b24.trajdata.dataset_specific.waymo.protos.LaneNeighbor"]\n\x08LaneType\x12\x12\n\x0eTYPE_UNDEFINED\x10\x00\x12\x10\n\x0cTYPE_FREEWAY\x10\x01\x12\x17\n\x13TYPE_SURFACE_STREET\x10\x02\x12\x12\n\x0eTYPE_BIKE_LANE\x10\x03"\xf5\x01\n\x08RoadEdge\x12K\n\x04type\x18\x01 \x01(\x0e2=.trajdata.dataset_specific.waymo.protos.RoadEdge.RoadEdgeType\x12B\n\x08polyline\x18\x02 \x03(\x0b20.trajdata.dataset_specific.waymo.protos.MapPoint"X\n\x0cRoadEdgeType\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x1b\n\x17TYPE_ROAD_EDGE_BOUNDARY\x10\x01\x12\x19\n\x15TYPE_ROAD_EDGE_MEDIAN\x10\x02"\xb0\x03\n\x08RoadLine\x12K\n\x04type\x18\x01 \x01(\x0e2=.trajdata.dataset_specific.waymo.protos.RoadLine.RoadLineType\x12B\n\x08polyline\x18\x02 \x03(\x0b20.trajdata.dataset_specific.waymo.protos.MapPoint"\x92\x02\n\x0cRoadLineType\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x1c\n\x18TYPE_BROKEN_SINGLE_WHITE\x10\x01\x12\x1b\n\x17TYPE_SOLID_SINGLE_WHITE\x10\x02\x12\x1b\n\x17TYPE_SOLID_DOUBLE_WHITE\x10\x03\x12\x1d\n\x19TYPE_BROKEN_SINGLE_YELLOW\x10\x04\x12\x1d\n\x19TYPE_BROKEN_DOUBLE_YELLOW\x10\x05\x12\x1c\n\x18TYPE_SOLID_SINGLE_YELLOW\x10\x06\x12\x1c\n\x18TYPE_SOLID_DOUBLE_YELLOW\x10\x07\x12\x1e\n\x1aTYPE_PASSING_DOUBLE_YELLOW\x10\x08"\\\n\x08StopSign\x12\x0c\n\x04lane\x18\x01 \x03(\x03\x12B\n\x08position\x18\x02 \x01(\x0b20.trajdata.dataset_specific.waymo.protos.MapPoint"N\n\tCrosswalk\x12A\n\x07polygon\x18\x01 \x03(\x0b20.trajdata.dataset_specific.waymo.protos.MapPoint"N\n\tSpeedBump\x12A\n\x07polygon\x18\x01 \x03(\x0b20.trajdata.dataset_specific.waymo.protos.MapPoint"M\n\x08Driveway\x12A\n\x07polygon\x18\x01 \x03(\x0b20.trajdata.dataset_specific.waymo.protos.MapPoint')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'map_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_LANECENTER'].fields_by_name['entry_lanes']._loaded_options = None
    _globals['_LANECENTER'].fields_by_name['entry_lanes']._serialized_options = b'\x10\x01'
    _globals['_LANECENTER'].fields_by_name['exit_lanes']._loaded_options = None
    _globals['_LANECENTER'].fields_by_name['exit_lanes']._serialized_options = b'\x10\x01'
    _globals['_MAP']._serialized_start = 54
    _globals['_MAP']._serialized_end = 211
    _globals['_DYNAMICSTATE']._serialized_start = 213
    _globals['_DYNAMICSTATE']._serialized_end = 339
    _globals['_TRAFFICSIGNALLANESTATE']._serialized_start = 342
    _globals['_TRAFFICSIGNALLANESTATE']._serialized_end = 778
    _globals['_TRAFFICSIGNALLANESTATE_STATE']._serialized_start = 538
    _globals['_TRAFFICSIGNALLANESTATE_STATE']._serialized_end = 778
    _globals['_MAPFEATURE']._serialized_start = 781
    _globals['_MAPFEATURE']._serialized_end = 1317
    _globals['_MAPPOINT']._serialized_start = 1319
    _globals['_MAPPOINT']._serialized_end = 1362
    _globals['_BOUNDARYSEGMENT']._serialized_start = 1365
    _globals['_BOUNDARYSEGMENT']._serialized_end = 1547
    _globals['_LANENEIGHBOR']._serialized_start = 1550
    _globals['_LANENEIGHBOR']._serialized_end = 1769
    _globals['_LANECENTER']._serialized_start = 1772
    _globals['_LANECENTER']._serialized_end = 2441
    _globals['_LANECENTER_LANETYPE']._serialized_start = 2348
    _globals['_LANECENTER_LANETYPE']._serialized_end = 2441
    _globals['_ROADEDGE']._serialized_start = 2444
    _globals['_ROADEDGE']._serialized_end = 2689
    _globals['_ROADEDGE_ROADEDGETYPE']._serialized_start = 2601
    _globals['_ROADEDGE_ROADEDGETYPE']._serialized_end = 2689
    _globals['_ROADLINE']._serialized_start = 2692
    _globals['_ROADLINE']._serialized_end = 3124
    _globals['_ROADLINE_ROADLINETYPE']._serialized_start = 2850
    _globals['_ROADLINE_ROADLINETYPE']._serialized_end = 3124
    _globals['_STOPSIGN']._serialized_start = 3126
    _globals['_STOPSIGN']._serialized_end = 3218
    _globals['_CROSSWALK']._serialized_start = 3220
    _globals['_CROSSWALK']._serialized_end = 3298
    _globals['_SPEEDBUMP']._serialized_start = 3300
    _globals['_SPEEDBUMP']._serialized_end = 3378
    _globals['_DRIVEWAY']._serialized_start = 3380
    _globals['_DRIVEWAY']._serialized_end = 3457