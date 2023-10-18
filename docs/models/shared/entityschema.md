# EntitySchema

Entity schema for a dataset


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `columns`                                                                                 | Dict[str, [ColumnSchema](../../models/shared/columnschema.md)]                            | :heavy_check_mark:                                                                        | Column schema for a given column                                                          |
| `metadata`                                                                                | [Optional[SchemaMetadata]](../../models/shared/schemametadata.md)                         | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `metrics`                                                                                 | Dict[str, [MetricSchema](../../models/shared/metricschema.md)]                            | :heavy_minus_sign:                                                                        | Schema for user-defined metrics (map of unique custom metric labels to their definitions) |