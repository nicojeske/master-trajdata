"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 3, '', 'dataset.proto')
_sym_db = _symbol_database.Default()
from . import label_pb2 as label__pb2
from . import map_pb2 as map__pb2
from . import vector_pb2 as vector__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rdataset.proto\x12&trajdata.dataset_specific.waymo.protos\x1a\x0blabel.proto\x1a\tmap.proto\x1a\x0cvector.proto"\x1b\n\x0bMatrixShape\x12\x0c\n\x04dims\x18\x01 \x03(\x05"c\n\x0bMatrixFloat\x12\x10\n\x04data\x18\x01 \x03(\x02B\x02\x10\x01\x12B\n\x05shape\x18\x02 \x01(\x0b23.trajdata.dataset_specific.waymo.protos.MatrixShape"c\n\x0bMatrixInt32\x12\x10\n\x04data\x18\x01 \x03(\x05B\x02\x10\x01\x12B\n\x05shape\x18\x02 \x01(\x0b23.trajdata.dataset_specific.waymo.protos.MatrixShape"\x96\x01\n\nCameraName"\x87\x01\n\x04Name\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05FRONT\x10\x01\x12\x0e\n\nFRONT_LEFT\x10\x02\x12\x0f\n\x0bFRONT_RIGHT\x10\x03\x12\r\n\tSIDE_LEFT\x10\x04\x12\x0e\n\nSIDE_RIGHT\x10\x05\x12\r\n\tREAR_LEFT\x10\x06\x12\x08\n\x04REAR\x10\x07\x12\x0e\n\nREAR_RIGHT\x10\x08"]\n\tLaserName"P\n\x04Name\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03TOP\x10\x01\x12\t\n\x05FRONT\x10\x02\x12\r\n\tSIDE_LEFT\x10\x03\x12\x0e\n\nSIDE_RIGHT\x10\x04\x12\x08\n\x04REAR\x10\x05"\x1e\n\tTransform\x12\x11\n\ttransform\x18\x01 \x03(\x01"X\n\x08Velocity\x12\x0b\n\x03v_x\x18\x01 \x01(\x02\x12\x0b\n\x03v_y\x18\x02 \x01(\x02\x12\x0b\n\x03v_z\x18\x03 \x01(\x02\x12\x0b\n\x03w_x\x18\x04 \x01(\x01\x12\x0b\n\x03w_y\x18\x05 \x01(\x01\x12\x0b\n\x03w_z\x18\x06 \x01(\x01"\xdf\x03\n\x11CameraCalibration\x12E\n\x04name\x18\x01 \x01(\x0e27.trajdata.dataset_specific.waymo.protos.CameraName.Name\x12\x11\n\tintrinsic\x18\x02 \x03(\x01\x12D\n\textrinsic\x18\x03 \x01(\x0b21.trajdata.dataset_specific.waymo.protos.Transform\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12{\n\x19rolling_shutter_direction\x18\x06 \x01(\x0e2X.trajdata.dataset_specific.waymo.protos.CameraCalibration.RollingShutterReadOutDirection"\x8d\x01\n\x1eRollingShutterReadOutDirection\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rTOP_TO_BOTTOM\x10\x01\x12\x11\n\rLEFT_TO_RIGHT\x10\x02\x12\x11\n\rBOTTOM_TO_TOP\x10\x03\x12\x11\n\rRIGHT_TO_LEFT\x10\x04\x12\x12\n\x0eGLOBAL_SHUTTER\x10\x05"\xf5\x01\n\x10LaserCalibration\x12D\n\x04name\x18\x01 \x01(\x0e26.trajdata.dataset_specific.waymo.protos.LaserName.Name\x12\x19\n\x11beam_inclinations\x18\x02 \x03(\x01\x12\x1c\n\x14beam_inclination_min\x18\x03 \x01(\x01\x12\x1c\n\x14beam_inclination_max\x18\x04 \x01(\x01\x12D\n\textrinsic\x18\x05 \x01(\x0b21.trajdata.dataset_specific.waymo.protos.Transform"\xee\x04\n\x07Context\x12\x0c\n\x04name\x18\x01 \x01(\t\x12V\n\x13camera_calibrations\x18\x02 \x03(\x0b29.trajdata.dataset_specific.waymo.protos.CameraCalibration\x12T\n\x12laser_calibrations\x18\x03 \x03(\x0b28.trajdata.dataset_specific.waymo.protos.LaserCalibration\x12D\n\x05stats\x18\x04 \x01(\x0b25.trajdata.dataset_specific.waymo.protos.Context.Stats\x1a\xe0\x02\n\x05Stats\x12^\n\x13laser_object_counts\x18\x01 \x03(\x0b2A.trajdata.dataset_specific.waymo.protos.Context.Stats.ObjectCount\x12_\n\x14camera_object_counts\x18\x05 \x03(\x0b2A.trajdata.dataset_specific.waymo.protos.Context.Stats.ObjectCount\x12\x13\n\x0btime_of_day\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0f\n\x07weather\x18\x04 \x01(\t\x1a^\n\x0bObjectCount\x12@\n\x04type\x18\x01 \x01(\x0e22.trajdata.dataset_specific.waymo.protos.Label.Type\x12\r\n\x05count\x18\x02 \x01(\x05"\x91\x02\n\nRangeImage\x12\x1e\n\x16range_image_compressed\x18\x02 \x01(\x0c\x12$\n\x1ccamera_projection_compressed\x18\x03 \x01(\x0c\x12#\n\x1brange_image_pose_compressed\x18\x04 \x01(\x0c\x12#\n\x1brange_image_flow_compressed\x18\x05 \x01(\x0c\x12%\n\x1dsegmentation_label_compressed\x18\x06 \x01(\x0c\x12L\n\x0brange_image\x18\x01 \x01(\x0b23.trajdata.dataset_specific.waymo.protos.MatrixFloatB\x02\x18\x01"\xf5\x02\n\x17CameraSegmentationLabel\x12\x1e\n\x16panoptic_label_divisor\x18\x01 \x01(\x05\x12\x16\n\x0epanoptic_label\x18\x02 \x01(\x0c\x12\x85\x01\n instance_id_to_global_id_mapping\x18\x03 \x03(\x0b2[.trajdata.dataset_specific.waymo.protos.CameraSegmentationLabel.InstanceIDToGlobalIDMapping\x12\x13\n\x0bsequence_id\x18\x04 \x01(\t\x12\x1b\n\x13num_cameras_covered\x18\x05 \x01(\x0c\x1ah\n\x1bInstanceIDToGlobalIDMapping\x12\x19\n\x11local_instance_id\x18\x01 \x01(\x05\x12\x1a\n\x12global_instance_id\x18\x02 \x01(\x05\x12\x12\n\nis_tracked\x18\x03 \x01(\x08"\xb4\x03\n\x0bCameraImage\x12E\n\x04name\x18\x01 \x01(\x0e27.trajdata.dataset_specific.waymo.protos.CameraName.Name\x12\r\n\x05image\x18\x02 \x01(\x0c\x12?\n\x04pose\x18\x03 \x01(\x0b21.trajdata.dataset_specific.waymo.protos.Transform\x12B\n\x08velocity\x18\x04 \x01(\x0b20.trajdata.dataset_specific.waymo.protos.Velocity\x12\x16\n\x0epose_timestamp\x18\x05 \x01(\x01\x12\x0f\n\x07shutter\x18\x06 \x01(\x01\x12\x1b\n\x13camera_trigger_time\x18\x07 \x01(\x01\x12 \n\x18camera_readout_done_time\x18\x08 \x01(\x01\x12b\n\x19camera_segmentation_label\x18\n \x01(\x0b2?.trajdata.dataset_specific.waymo.protos.CameraSegmentationLabel"\x94\x01\n\x0cCameraLabels\x12E\n\x04name\x18\x01 \x01(\x0e27.trajdata.dataset_specific.waymo.protos.CameraName.Name\x12=\n\x06labels\x18\x02 \x03(\x0b2-.trajdata.dataset_specific.waymo.protos.Label"\xdd\x01\n\x05Laser\x12D\n\x04name\x18\x01 \x01(\x0e26.trajdata.dataset_specific.waymo.protos.LaserName.Name\x12F\n\nri_return1\x18\x02 \x01(\x0b22.trajdata.dataset_specific.waymo.protos.RangeImage\x12F\n\nri_return2\x18\x03 \x01(\x0b22.trajdata.dataset_specific.waymo.protos.RangeImage"\x80\x06\n\x05Frame\x12@\n\x07context\x18\x01 \x01(\x0b2/.trajdata.dataset_specific.waymo.protos.Context\x12\x18\n\x10timestamp_micros\x18\x02 \x01(\x03\x12?\n\x04pose\x18\x03 \x01(\x0b21.trajdata.dataset_specific.waymo.protos.Transform\x12C\n\x06images\x18\x04 \x03(\x0b23.trajdata.dataset_specific.waymo.protos.CameraImage\x12=\n\x06lasers\x18\x05 \x03(\x0b2-.trajdata.dataset_specific.waymo.protos.Laser\x12C\n\x0claser_labels\x18\x06 \x03(\x0b2-.trajdata.dataset_specific.waymo.protos.Label\x12T\n\x16projected_lidar_labels\x18\t \x03(\x0b24.trajdata.dataset_specific.waymo.protos.CameraLabels\x12K\n\rcamera_labels\x18\x08 \x03(\x0b24.trajdata.dataset_specific.waymo.protos.CameraLabels\x12N\n\x0eno_label_zones\x18\x07 \x03(\x0b26.trajdata.dataset_specific.waymo.protos.Polygon2dProto\x12H\n\x0cmap_features\x18\n \x03(\x0b22.trajdata.dataset_specific.waymo.protos.MapFeature\x12I\n\x0fmap_pose_offset\x18\x0b \x01(\x0b20.trajdata.dataset_specific.waymo.protos.Vector3d*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_MATRIXFLOAT'].fields_by_name['data']._loaded_options = None
    _globals['_MATRIXFLOAT'].fields_by_name['data']._serialized_options = b'\x10\x01'
    _globals['_MATRIXINT32'].fields_by_name['data']._loaded_options = None
    _globals['_MATRIXINT32'].fields_by_name['data']._serialized_options = b'\x10\x01'
    _globals['_RANGEIMAGE'].fields_by_name['range_image']._loaded_options = None
    _globals['_RANGEIMAGE'].fields_by_name['range_image']._serialized_options = b'\x18\x01'
    _globals['_MATRIXSHAPE']._serialized_start = 95
    _globals['_MATRIXSHAPE']._serialized_end = 122
    _globals['_MATRIXFLOAT']._serialized_start = 124
    _globals['_MATRIXFLOAT']._serialized_end = 223
    _globals['_MATRIXINT32']._serialized_start = 225
    _globals['_MATRIXINT32']._serialized_end = 324
    _globals['_CAMERANAME']._serialized_start = 327
    _globals['_CAMERANAME']._serialized_end = 477
    _globals['_CAMERANAME_NAME']._serialized_start = 342
    _globals['_CAMERANAME_NAME']._serialized_end = 477
    _globals['_LASERNAME']._serialized_start = 479
    _globals['_LASERNAME']._serialized_end = 572
    _globals['_LASERNAME_NAME']._serialized_start = 492
    _globals['_LASERNAME_NAME']._serialized_end = 572
    _globals['_TRANSFORM']._serialized_start = 574
    _globals['_TRANSFORM']._serialized_end = 604
    _globals['_VELOCITY']._serialized_start = 606
    _globals['_VELOCITY']._serialized_end = 694
    _globals['_CAMERACALIBRATION']._serialized_start = 697
    _globals['_CAMERACALIBRATION']._serialized_end = 1176
    _globals['_CAMERACALIBRATION_ROLLINGSHUTTERREADOUTDIRECTION']._serialized_start = 1035
    _globals['_CAMERACALIBRATION_ROLLINGSHUTTERREADOUTDIRECTION']._serialized_end = 1176
    _globals['_LASERCALIBRATION']._serialized_start = 1179
    _globals['_LASERCALIBRATION']._serialized_end = 1424
    _globals['_CONTEXT']._serialized_start = 1427
    _globals['_CONTEXT']._serialized_end = 2049
    _globals['_CONTEXT_STATS']._serialized_start = 1697
    _globals['_CONTEXT_STATS']._serialized_end = 2049
    _globals['_CONTEXT_STATS_OBJECTCOUNT']._serialized_start = 1955
    _globals['_CONTEXT_STATS_OBJECTCOUNT']._serialized_end = 2049
    _globals['_RANGEIMAGE']._serialized_start = 2052
    _globals['_RANGEIMAGE']._serialized_end = 2325
    _globals['_CAMERASEGMENTATIONLABEL']._serialized_start = 2328
    _globals['_CAMERASEGMENTATIONLABEL']._serialized_end = 2701
    _globals['_CAMERASEGMENTATIONLABEL_INSTANCEIDTOGLOBALIDMAPPING']._serialized_start = 2597
    _globals['_CAMERASEGMENTATIONLABEL_INSTANCEIDTOGLOBALIDMAPPING']._serialized_end = 2701
    _globals['_CAMERAIMAGE']._serialized_start = 2704
    _globals['_CAMERAIMAGE']._serialized_end = 3140
    _globals['_CAMERALABELS']._serialized_start = 3143
    _globals['_CAMERALABELS']._serialized_end = 3291
    _globals['_LASER']._serialized_start = 3294
    _globals['_LASER']._serialized_end = 3515
    _globals['_FRAME']._serialized_start = 3518
    _globals['_FRAME']._serialized_end = 4286