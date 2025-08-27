{% macro string_var(name) %}
  {{ "'" ~ (var(name) | string) ~ "'" }}
{% endmacro %}
