import dataset_pb2 as _dataset_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CameraTokens(_message.Message):
    __slots__ = ('camera_name', 'tokens')
    CAMERA_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    camera_name: _dataset_pb2.CameraName.Name
    tokens: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, camera_name: _Optional[_Union[_dataset_pb2.CameraName.Name, str]]=..., tokens: _Optional[_Iterable[int]]=...) -> None:
        ...

class FrameCameraTokens(_message.Message):
    __slots__ = ('camera_tokens',)
    CAMERA_TOKENS_FIELD_NUMBER: _ClassVar[int]
    camera_tokens: _containers.RepeatedCompositeFieldContainer[CameraTokens]

    def __init__(self, camera_tokens: _Optional[_Iterable[_Union[CameraTokens, _Mapping]]]=...) -> None:
        ...