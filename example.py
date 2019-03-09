import json
from typing import Dict

from avro import schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

from avro_json_serializer import AvroJsonSerializer

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter


def pretty_print(json_txt: str) -> None:
    json_object = json.loads(json_txt)
    json_str = json.dumps(json_object, indent=4, sort_keys=False)
    print(highlight(json_str, JsonLexer(), TerminalFormatter()))


data = {
    "type": "TATA",
    "account": {
        "account_id": "TATA",
        "id": "TATA"
    },
    "rating": {
        "rating_type": "TATA",
        "rating_results": [
            {
                "rating_result": {
                    "name": "TATA",
                    "age": 3.0,
                    "citycode": 6.9
                }
            },
            {
                "rating_result": {
                    "name": "TATA",
                    "age": 3.0,
                    "citycode": 6.9
                }
            }
        ],
        "related_to": {
            "category": "TATA"
        }
    }
}


def dict_to_json(data: Dict):
    # to JSON

    # avro_schema = schema.SchemaFromJSONData(schema_dict)
    avro_schema = schema.Parse(open("rate.avsc", "rb").read())

    serializer = AvroJsonSerializer(avro_schema)
    json_str = serializer.to_json(data)

    pretty_print(json_str)


def dict_to_avro(data: Dict):
    # TO avro format file

    avro_schema = schema.Parse(open("rate.avsc", "rb").read())

    # write avro file
    writer = DataFileWriter(open("ratings.avro", "wb"), DatumWriter(), avro_schema)
    writer.append(data)
    writer.close()

    # read avro file
    reader = DataFileReader(open("ratings.avro", "rb"), DatumReader())
    for user in reader:
        pretty_print(json.dumps(user))
    reader.close()


if __name__ == '__main__':
    dict_to_json(data)
    dict_to_avro(data)
