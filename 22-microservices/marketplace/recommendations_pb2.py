# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommendations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15recommendations.proto\"/\n\x12\x42ookRecommendation\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\"^\n\x15RecommendationRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x1f\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\r.BookCategory\x12\x13\n\x0bmax_results\x18\x03 \x01(\x05\"F\n\x16RecommendationResponse\x12,\n\x0frecommendations\x18\x01 \x03(\x0b\x32\x13.BookRecommendation*6\n\x0c\x42ookCategory\x12\x0b\n\x07MYSTERY\x10\x00\x12\n\n\x06SCI_FI\x10\x01\x12\r\n\tSELF_HELP\x10\x02\x32O\n\x0fRecommendations\x12<\n\tRecommend\x12\x16.RecommendationRequest\x1a\x17.RecommendationResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recommendations_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOKCATEGORY._serialized_start=242
  _BOOKCATEGORY._serialized_end=296
  _BOOKRECOMMENDATION._serialized_start=25
  _BOOKRECOMMENDATION._serialized_end=72
  _RECOMMENDATIONREQUEST._serialized_start=74
  _RECOMMENDATIONREQUEST._serialized_end=168
  _RECOMMENDATIONRESPONSE._serialized_start=170
  _RECOMMENDATIONRESPONSE._serialized_end=240
  _RECOMMENDATIONS._serialized_start=298
  _RECOMMENDATIONS._serialized_end=377
# @@protoc_insertion_point(module_scope)
