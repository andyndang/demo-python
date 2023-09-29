# EntitySchema

Entity schema for a dataset


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `columns`                                                                                 | dict[str, [shared.ColumnSchema](undefined/models/shared/columnschema.md)]                 | :heavy_check_mark:                                                                        | Column schema for a given column                                                          |
| `metadata`                                                                                | [Optional[shared.SchemaMetadata]](undefined/models/shared/schemametadata.md)              | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `metrics`                                                                                 | dict[str, [shared.MetricSchema](undefined/models/shared/metricschema.md)]                 | :heavy_minus_sign:                                                                        | Schema for user-defined metrics (map of unique custom metric labels to their definitions) |