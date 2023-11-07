# EntitySchema

Entity schema for a dataset


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `columns`                                                                                 | Dict[str, [shared.ColumnSchema](../../models/shared/columnschema.md)]                     | :heavy_check_mark:                                                                        | Column schema for a given column                                                          |
| `metadata`                                                                                | [Optional[shared.SchemaMetadata]](../../models/shared/schemametadata.md)                  | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `metrics`                                                                                 | Dict[str, [shared.MetricSchema](../../models/shared/metricschema.md)]                     | :heavy_minus_sign:                                                                        | Schema for user-defined metrics (map of unique custom metric labels to their definitions) |