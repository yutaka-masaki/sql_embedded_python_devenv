-- sqlfluff:dialect:redshift

DELETE FROM {{ var('table_name') }}
WHERE yyyymm = {{ string_var('yyyymm') }}; -- noqa: CV06

INSERT INTO {{ var('table_name') }}
SELECT
  col3,
  col4
FROM source_table
WHERE {{ string_var('yyyymm') }}
