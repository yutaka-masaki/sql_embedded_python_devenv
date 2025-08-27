from jinja2 import Environment, FileSystemLoader
import my_jinja.jinja_macros as jm

# ① Jinja環境の作成

class JinjaTemplater:
    def __init__(self, folder_path: str):
        self.env = Environment(
            loader=FileSystemLoader(folder_path),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.env.globals["string_var"] = jm.string_var
        self.env.globals["var"] = jm.var

    def render(self, sql_file: str, **kwargs) -> str:
        """
        指定されたSQLファイルをレンダリングし、結果のSQL文字列を返す。
        :param sql_file: SQLファイルのパス
        :param kwargs: テンプレートに渡す変数
        :return: レンダリングされたSQL文字列
        """
        template = self.env.get_template(sql_file)
        renderd_sql = template.render(**kwargs)
        return renderd_sql
    
    def render_multi(self, sql_file: str, **kwargs) -> list[str]:
        """
        指定されたSQLファイルをレンダリングし、セミコロンで分割された複数のSQL文をリストとして返す。
        :param sql_file: SQLファイルのパス
        :param kwargs: テンプレートに渡す変数
        :return: レンダリングされたSQL文のリスト
        """
        template = self.env.get_template(sql_file)
        renderd_sql = template.render(**kwargs)
        sql_list = [sql.strip() for sql in renderd_sql.split(';') if sql.strip()]
        return sql_list

