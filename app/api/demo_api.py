"""TODO"""

import logging

from typing import Any

from flask.views import MethodView
from flask_smorest import Blueprint
from resources.basic_model import BasicModel
from schemas import FormInputSchema, APIReturnSchema


blp_v1 = Blueprint(
    "api-demo", __name__, url_prefix="/v1/api-demo", description="your api description"
)


@blp_v1.route("/query")
class BusinessV1(MethodView):
    """TODO"""

    @blp_v1.arguments(FormInputSchema, location="query")
    @blp_v1.response(200, APIReturnSchema(many=True))
    def get(self, args):
        """TODO"""

        logging.debug(args)

        def call_api_process(args_value: Any) -> Any:
            "Write your api logics."

            logging.debug(args_value)
            db_query = BasicModel.query.all()
            
            return db_query

        call_api_process(args.get("args_key"))

        return args
