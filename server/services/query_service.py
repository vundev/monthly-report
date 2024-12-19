from sqlalchemy import Result, Row


class QueryService:

    @classmethod
    def to_dict(cls, result: Result[Row[any]]):
        return [dict(row._mapping) for row in result]
