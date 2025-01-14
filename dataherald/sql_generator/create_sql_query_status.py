from datetime import date

from dataherald.sql_database.base import SQLDatabase
from dataherald.types import NLQueryResponse, SQLQueryResult


def create_sql_query_status(
    db: SQLDatabase, query: str, response: NLQueryResponse
) -> NLQueryResponse:
    """Find the sql query status and populate the fields sql_query_result, sql_generation_status, and error_message"""
    if query == "":
        response.sql_generation_status = "NONE"
        response.sql_query_result = None
        response.error_message = None
    else:
        try:
            execution = db.engine.execute(query)
            columns = execution.keys()
            result = execution.fetchall()
            if len(result) == 0:
                response.sql_query_result = None
            else:
                columns = [item for item in columns]  # noqa: C416
                rows = []
                for row in result:
                    modified_row = {}
                    for key, value in zip(row.keys(), row, strict=True):
                        if (
                            type(value) is date
                        ):  # Check if the value is an instance of datetime.date
                            modified_row[key] = str(value)
                        else:
                            modified_row[key] = value
                    rows.append(modified_row)
                response.sql_query_result = SQLQueryResult(columns=columns, rows=rows)
            response.sql_generation_status = "VALID"
            response.error_message = None
        except Exception as e:
            response.sql_generation_status = "INVALID"
            response.sql_query_result = None
            response.error_message = str(e)
    return response
