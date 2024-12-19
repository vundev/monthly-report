from sqlalchemy import Result, Row


class QueryService:
    def to_dict(self, result: Result[Row[any]]):
        return [dict(row._mapping) for row in result]
