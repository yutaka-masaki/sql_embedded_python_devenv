from my_jinja.jinja_wrapper import JinjaTemplater

def main():
    jj = JinjaTemplater(folder_path="./sql/")
    rendered_sql_1 = jj.render(
        sql_file="example1.sql",
        table_name="test_table_1",
        yyyymm='202508'
    )
    print("\n=======================\n")
    print(rendered_sql_1)
    print("\n=======================\n")

    rendered_sql_2_list = jj.render_multi(
        sql_file="example2.sql",
        table_name="test_table_2",
        yyyymm='202508'
    )
    for sql_2 in rendered_sql_2_list:
        print(sql_2)
        print("\n=======================\n")


if __name__ == "__main__":
    main()