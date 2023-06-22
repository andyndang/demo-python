# ColumnSchema

Column schema for a given column


## Fields

| Field                                                                                                                                             | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       | Example                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `classifier`                                                                                                                                      | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | We can classify these columns into various grouping. Currently we only support 'input' and 'output'                                               | input                                                                                                                                             |
| `data_type`                                                                                                                                       | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | The data type of the columns. Setting this field affects the default grouping (i.e integral columns)                                              | fractional                                                                                                                                        |
| `discreteness`                                                                                                                                    | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | Whether a column should be discrete or continuous. Changing this column will change the default grouping (discrete columns vs. continuous columns | discrete                                                                                                                                          |