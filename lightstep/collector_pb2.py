# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collector.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='collector.proto',
  package='lightstep.collector',
  syntax='proto3',
  serialized_options=_b('\n\031com.lightstep.tracer.grpcP\001Z\013collectorpb\242\002\004LSPB'),
  serialized_pb=_b('\n\x0f\x63ollector.proto\x12\x13lightstep.collector\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xa0\x01\n\x0bSpanContext\x12\x10\n\x08trace_id\x18\x01 \x01(\x04\x12\x0f\n\x07span_id\x18\x02 \x01(\x04\x12>\n\x07\x62\x61ggage\x18\x03 \x03(\x0b\x32-.lightstep.collector.SpanContext.BaggageEntry\x1a.\n\x0c\x42\x61ggageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x91\x01\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12\x13\n\tint_value\x18\x03 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x12\x14\n\nbool_value\x18\x05 \x01(\x08H\x00\x12\x14\n\njson_value\x18\x06 \x01(\tH\x00\x42\x07\n\x05value\"c\n\x03Log\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x1d.lightstep.collector.KeyValue\"\xb6\x01\n\tReference\x12\x41\n\x0crelationship\x18\x01 \x01(\x0e\x32+.lightstep.collector.Reference.Relationship\x12\x36\n\x0cspan_context\x18\x02 \x01(\x0b\x32 .lightstep.collector.SpanContext\".\n\x0cRelationship\x12\x0c\n\x08\x43HILD_OF\x10\x00\x12\x10\n\x0c\x46OLLOWS_FROM\x10\x01\"\xad\x02\n\x04Span\x12\x36\n\x0cspan_context\x18\x01 \x01(\x0b\x32 .lightstep.collector.SpanContext\x12\x16\n\x0eoperation_name\x18\x02 \x01(\t\x12\x32\n\nreferences\x18\x03 \x03(\x0b\x32\x1e.lightstep.collector.Reference\x12\x33\n\x0fstart_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0f\x64uration_micros\x18\x05 \x01(\x04\x12+\n\x04tags\x18\x06 \x03(\x0b\x32\x1d.lightstep.collector.KeyValue\x12&\n\x04logs\x18\x07 \x03(\x0b\x32\x18.lightstep.collector.Log\"L\n\x08Reporter\x12\x13\n\x0breporter_id\x18\x01 \x01(\x04\x12+\n\x04tags\x18\x04 \x03(\x0b\x32\x1d.lightstep.collector.KeyValue\"S\n\rMetricsSample\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x03 \x01(\x01H\x00\x42\x07\n\x05value\"\xef\x01\n\x0fInternalMetrics\x12\x33\n\x0fstart_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0f\x64uration_micros\x18\x02 \x01(\x04\x12&\n\x04logs\x18\x03 \x03(\x0b\x32\x18.lightstep.collector.Log\x12\x32\n\x06\x63ounts\x18\x04 \x03(\x0b\x32\".lightstep.collector.MetricsSample\x12\x32\n\x06gauges\x18\x05 \x03(\x0b\x32\".lightstep.collector.MetricsSample\"\x1c\n\x04\x41uth\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\"\xf4\x01\n\rReportRequest\x12/\n\x08reporter\x18\x01 \x01(\x0b\x32\x1d.lightstep.collector.Reporter\x12\'\n\x04\x61uth\x18\x02 \x01(\x0b\x32\x19.lightstep.collector.Auth\x12(\n\x05spans\x18\x03 \x03(\x0b\x32\x19.lightstep.collector.Span\x12\x1f\n\x17timestamp_offset_micros\x18\x05 \x01(\x03\x12>\n\x10internal_metrics\x18\x06 \x01(\x0b\x32$.lightstep.collector.InternalMetrics\"\x1a\n\x07\x43ommand\x12\x0f\n\x07\x64isable\x18\x01 \x01(\x08\"\xe0\x01\n\x0eReportResponse\x12.\n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x1c.lightstep.collector.Command\x12\x35\n\x11receive_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x12transmit_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x65rrors\x18\x04 \x03(\t\x12\x10\n\x08warnings\x18\x05 \x03(\t\x12\r\n\x05infos\x18\x06 \x03(\t2\x95\x01\n\x10\x43ollectorService\x12\x80\x01\n\x06Report\x12\".lightstep.collector.ReportRequest\x1a#.lightstep.collector.ReportResponse\"-\x82\xd3\xe4\x93\x02\'\"\x0f/api/v2/reports:\x01*Z\x11\x12\x0f/api/v2/reportsB1\n\x19\x63om.lightstep.tracer.grpcP\x01Z\x0b\x63ollectorpb\xa2\x02\x04LSPBb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_REFERENCE_RELATIONSHIP = _descriptor.EnumDescriptor(
  name='Relationship',
  full_name='lightstep.collector.Reference.Relationship',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHILD_OF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOLLOWS_FROM', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=652,
  serialized_end=698,
)
_sym_db.RegisterEnumDescriptor(_REFERENCE_RELATIONSHIP)


_SPANCONTEXT_BAGGAGEENTRY = _descriptor.Descriptor(
  name='BaggageEntry',
  full_name='lightstep.collector.SpanContext.BaggageEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='lightstep.collector.SpanContext.BaggageEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='lightstep.collector.SpanContext.BaggageEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=264,
)

_SPANCONTEXT = _descriptor.Descriptor(
  name='SpanContext',
  full_name='lightstep.collector.SpanContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='lightstep.collector.SpanContext.trace_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='span_id', full_name='lightstep.collector.SpanContext.span_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baggage', full_name='lightstep.collector.SpanContext.baggage', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SPANCONTEXT_BAGGAGEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=264,
)


_KEYVALUE = _descriptor.Descriptor(
  name='KeyValue',
  full_name='lightstep.collector.KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='lightstep.collector.KeyValue.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='lightstep.collector.KeyValue.string_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='lightstep.collector.KeyValue.int_value', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='lightstep.collector.KeyValue.double_value', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='lightstep.collector.KeyValue.bool_value', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='json_value', full_name='lightstep.collector.KeyValue.json_value', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='lightstep.collector.KeyValue.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=267,
  serialized_end=412,
)


_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='lightstep.collector.Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='lightstep.collector.Log.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='lightstep.collector.Log.fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=414,
  serialized_end=513,
)


_REFERENCE = _descriptor.Descriptor(
  name='Reference',
  full_name='lightstep.collector.Reference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relationship', full_name='lightstep.collector.Reference.relationship', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='span_context', full_name='lightstep.collector.Reference.span_context', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REFERENCE_RELATIONSHIP,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=698,
)


_SPAN = _descriptor.Descriptor(
  name='Span',
  full_name='lightstep.collector.Span',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='span_context', full_name='lightstep.collector.Span.span_context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation_name', full_name='lightstep.collector.Span.operation_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='references', full_name='lightstep.collector.Span.references', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='lightstep.collector.Span.start_timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_micros', full_name='lightstep.collector.Span.duration_micros', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='lightstep.collector.Span.tags', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs', full_name='lightstep.collector.Span.logs', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=701,
  serialized_end=1002,
)


_REPORTER = _descriptor.Descriptor(
  name='Reporter',
  full_name='lightstep.collector.Reporter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reporter_id', full_name='lightstep.collector.Reporter.reporter_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='lightstep.collector.Reporter.tags', index=1,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1004,
  serialized_end=1080,
)


_METRICSSAMPLE = _descriptor.Descriptor(
  name='MetricsSample',
  full_name='lightstep.collector.MetricsSample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='lightstep.collector.MetricsSample.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='lightstep.collector.MetricsSample.int_value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='lightstep.collector.MetricsSample.double_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='lightstep.collector.MetricsSample.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1082,
  serialized_end=1165,
)


_INTERNALMETRICS = _descriptor.Descriptor(
  name='InternalMetrics',
  full_name='lightstep.collector.InternalMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='lightstep.collector.InternalMetrics.start_timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_micros', full_name='lightstep.collector.InternalMetrics.duration_micros', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs', full_name='lightstep.collector.InternalMetrics.logs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counts', full_name='lightstep.collector.InternalMetrics.counts', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gauges', full_name='lightstep.collector.InternalMetrics.gauges', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1168,
  serialized_end=1407,
)


_AUTH = _descriptor.Descriptor(
  name='Auth',
  full_name='lightstep.collector.Auth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='lightstep.collector.Auth.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1409,
  serialized_end=1437,
)


_REPORTREQUEST = _descriptor.Descriptor(
  name='ReportRequest',
  full_name='lightstep.collector.ReportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reporter', full_name='lightstep.collector.ReportRequest.reporter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth', full_name='lightstep.collector.ReportRequest.auth', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spans', full_name='lightstep.collector.ReportRequest.spans', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_offset_micros', full_name='lightstep.collector.ReportRequest.timestamp_offset_micros', index=3,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal_metrics', full_name='lightstep.collector.ReportRequest.internal_metrics', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1440,
  serialized_end=1684,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='lightstep.collector.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disable', full_name='lightstep.collector.Command.disable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1686,
  serialized_end=1712,
)


_REPORTRESPONSE = _descriptor.Descriptor(
  name='ReportResponse',
  full_name='lightstep.collector.ReportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commands', full_name='lightstep.collector.ReportResponse.commands', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receive_timestamp', full_name='lightstep.collector.ReportResponse.receive_timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transmit_timestamp', full_name='lightstep.collector.ReportResponse.transmit_timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errors', full_name='lightstep.collector.ReportResponse.errors', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warnings', full_name='lightstep.collector.ReportResponse.warnings', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='infos', full_name='lightstep.collector.ReportResponse.infos', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1715,
  serialized_end=1939,
)

_SPANCONTEXT_BAGGAGEENTRY.containing_type = _SPANCONTEXT
_SPANCONTEXT.fields_by_name['baggage'].message_type = _SPANCONTEXT_BAGGAGEENTRY
_KEYVALUE.oneofs_by_name['value'].fields.append(
  _KEYVALUE.fields_by_name['string_value'])
_KEYVALUE.fields_by_name['string_value'].containing_oneof = _KEYVALUE.oneofs_by_name['value']
_KEYVALUE.oneofs_by_name['value'].fields.append(
  _KEYVALUE.fields_by_name['int_value'])
_KEYVALUE.fields_by_name['int_value'].containing_oneof = _KEYVALUE.oneofs_by_name['value']
_KEYVALUE.oneofs_by_name['value'].fields.append(
  _KEYVALUE.fields_by_name['double_value'])
_KEYVALUE.fields_by_name['double_value'].containing_oneof = _KEYVALUE.oneofs_by_name['value']
_KEYVALUE.oneofs_by_name['value'].fields.append(
  _KEYVALUE.fields_by_name['bool_value'])
_KEYVALUE.fields_by_name['bool_value'].containing_oneof = _KEYVALUE.oneofs_by_name['value']
_KEYVALUE.oneofs_by_name['value'].fields.append(
  _KEYVALUE.fields_by_name['json_value'])
_KEYVALUE.fields_by_name['json_value'].containing_oneof = _KEYVALUE.oneofs_by_name['value']
_LOG.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOG.fields_by_name['fields'].message_type = _KEYVALUE
_REFERENCE.fields_by_name['relationship'].enum_type = _REFERENCE_RELATIONSHIP
_REFERENCE.fields_by_name['span_context'].message_type = _SPANCONTEXT
_REFERENCE_RELATIONSHIP.containing_type = _REFERENCE
_SPAN.fields_by_name['span_context'].message_type = _SPANCONTEXT
_SPAN.fields_by_name['references'].message_type = _REFERENCE
_SPAN.fields_by_name['start_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SPAN.fields_by_name['tags'].message_type = _KEYVALUE
_SPAN.fields_by_name['logs'].message_type = _LOG
_REPORTER.fields_by_name['tags'].message_type = _KEYVALUE
_METRICSSAMPLE.oneofs_by_name['value'].fields.append(
  _METRICSSAMPLE.fields_by_name['int_value'])
_METRICSSAMPLE.fields_by_name['int_value'].containing_oneof = _METRICSSAMPLE.oneofs_by_name['value']
_METRICSSAMPLE.oneofs_by_name['value'].fields.append(
  _METRICSSAMPLE.fields_by_name['double_value'])
_METRICSSAMPLE.fields_by_name['double_value'].containing_oneof = _METRICSSAMPLE.oneofs_by_name['value']
_INTERNALMETRICS.fields_by_name['start_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INTERNALMETRICS.fields_by_name['logs'].message_type = _LOG
_INTERNALMETRICS.fields_by_name['counts'].message_type = _METRICSSAMPLE
_INTERNALMETRICS.fields_by_name['gauges'].message_type = _METRICSSAMPLE
_REPORTREQUEST.fields_by_name['reporter'].message_type = _REPORTER
_REPORTREQUEST.fields_by_name['auth'].message_type = _AUTH
_REPORTREQUEST.fields_by_name['spans'].message_type = _SPAN
_REPORTREQUEST.fields_by_name['internal_metrics'].message_type = _INTERNALMETRICS
_REPORTRESPONSE.fields_by_name['commands'].message_type = _COMMAND
_REPORTRESPONSE.fields_by_name['receive_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REPORTRESPONSE.fields_by_name['transmit_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['SpanContext'] = _SPANCONTEXT
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE
DESCRIPTOR.message_types_by_name['Log'] = _LOG
DESCRIPTOR.message_types_by_name['Reference'] = _REFERENCE
DESCRIPTOR.message_types_by_name['Span'] = _SPAN
DESCRIPTOR.message_types_by_name['Reporter'] = _REPORTER
DESCRIPTOR.message_types_by_name['MetricsSample'] = _METRICSSAMPLE
DESCRIPTOR.message_types_by_name['InternalMetrics'] = _INTERNALMETRICS
DESCRIPTOR.message_types_by_name['Auth'] = _AUTH
DESCRIPTOR.message_types_by_name['ReportRequest'] = _REPORTREQUEST
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['ReportResponse'] = _REPORTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpanContext = _reflection.GeneratedProtocolMessageType('SpanContext', (_message.Message,), dict(

  BaggageEntry = _reflection.GeneratedProtocolMessageType('BaggageEntry', (_message.Message,), dict(
    DESCRIPTOR = _SPANCONTEXT_BAGGAGEENTRY,
    __module__ = 'collector_pb2'
    # @@protoc_insertion_point(class_scope:lightstep.collector.SpanContext.BaggageEntry)
    ))
  ,
  DESCRIPTOR = _SPANCONTEXT,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.SpanContext)
  ))
_sym_db.RegisterMessage(SpanContext)
_sym_db.RegisterMessage(SpanContext.BaggageEntry)

KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUE,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.KeyValue)
  ))
_sym_db.RegisterMessage(KeyValue)

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), dict(
  DESCRIPTOR = _LOG,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.Log)
  ))
_sym_db.RegisterMessage(Log)

Reference = _reflection.GeneratedProtocolMessageType('Reference', (_message.Message,), dict(
  DESCRIPTOR = _REFERENCE,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.Reference)
  ))
_sym_db.RegisterMessage(Reference)

Span = _reflection.GeneratedProtocolMessageType('Span', (_message.Message,), dict(
  DESCRIPTOR = _SPAN,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.Span)
  ))
_sym_db.RegisterMessage(Span)

Reporter = _reflection.GeneratedProtocolMessageType('Reporter', (_message.Message,), dict(
  DESCRIPTOR = _REPORTER,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.Reporter)
  ))
_sym_db.RegisterMessage(Reporter)

MetricsSample = _reflection.GeneratedProtocolMessageType('MetricsSample', (_message.Message,), dict(
  DESCRIPTOR = _METRICSSAMPLE,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.MetricsSample)
  ))
_sym_db.RegisterMessage(MetricsSample)

InternalMetrics = _reflection.GeneratedProtocolMessageType('InternalMetrics', (_message.Message,), dict(
  DESCRIPTOR = _INTERNALMETRICS,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.InternalMetrics)
  ))
_sym_db.RegisterMessage(InternalMetrics)

Auth = _reflection.GeneratedProtocolMessageType('Auth', (_message.Message,), dict(
  DESCRIPTOR = _AUTH,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.Auth)
  ))
_sym_db.RegisterMessage(Auth)

ReportRequest = _reflection.GeneratedProtocolMessageType('ReportRequest', (_message.Message,), dict(
  DESCRIPTOR = _REPORTREQUEST,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.ReportRequest)
  ))
_sym_db.RegisterMessage(ReportRequest)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.Command)
  ))
_sym_db.RegisterMessage(Command)

ReportResponse = _reflection.GeneratedProtocolMessageType('ReportResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPORTRESPONSE,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:lightstep.collector.ReportResponse)
  ))
_sym_db.RegisterMessage(ReportResponse)


DESCRIPTOR._options = None
_SPANCONTEXT_BAGGAGEENTRY._options = None

_COLLECTORSERVICE = _descriptor.ServiceDescriptor(
  name='CollectorService',
  full_name='lightstep.collector.CollectorService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1942,
  serialized_end=2091,
  methods=[
  _descriptor.MethodDescriptor(
    name='Report',
    full_name='lightstep.collector.CollectorService.Report',
    index=0,
    containing_service=None,
    input_type=_REPORTREQUEST,
    output_type=_REPORTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\'\"\017/api/v2/reports:\001*Z\021\022\017/api/v2/reports'),
  ),
])
_sym_db.RegisterServiceDescriptor(_COLLECTORSERVICE)

DESCRIPTOR.services_by_name['CollectorService'] = _COLLECTORSERVICE

# @@protoc_insertion_point(module_scope)
