import json
from flask import Response, request
from flask_restful import Resource

from models.metadata import get_metadata

from api.v1.exceptions import model_exceptions
from api.v1.utils import get_optional_metadata_kwargs


class Metadata(Resource):
    """
    Get a list of metadata based on disease, cell type, or tissue keywords
    This quickly help answer question such as:
    - is  there any record of the disease I am interested in?
    - What disease and datasets will contains the my cell type of interes?
    - What disease and datasets will contains the tissue I want?
    """

    @model_exceptions
    def get(self):
        args = request.args

        filters = get_optional_metadata_kwargs(args, ["disease", "cell_type", "tissue"])
        matching_metadata = get_metadata(**filters)

        # Convert the list of OrderedDict to JSON string to preserve the order
        response_json = json.dumps(
            matching_metadata,
            ensure_ascii=False,
            indent=1,
        )
        return Response(response_json, mimetype="application/json")

