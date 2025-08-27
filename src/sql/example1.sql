SELECT
  col1,
  col2,
  col3
FROM
  {{ var('table_name') }}
WHERE
  yyyymm = {{ string_var('yyyymm') }}
