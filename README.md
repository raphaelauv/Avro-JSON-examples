# Avro-JSON-examples

thank to [python-avro-json-serializer](https://github.com/linkedin/python-avro-json-serializer)

this a full avro JSON example with :
- nested record 
- array of records 
- union of null and record

## How to run

```
pip3 install -r requirements.txt

python3 example.py
```

## Example 
### AVRO schema

```json
{
  "namespace": "enterprise.thing",
  "type": "record",
  "name": "rating_event",
  "fields": [
    {"name": "type", "type": "string"},
    {"name": "account", "type" : {
      "type": "record",
      "name": "account",
      "fields": [
        {"name": "account_id","type": "string"},
        {"name": "id","type": "string"}
      ]
    }},
    {"name": "rating","type" : {
      "type": "record",
      "name": "rating",
      "fields": [
        {"name": "rating_type","type": "string"},
        {"name" : "rating_results",
          "type" : {
            "type" : "array",
            "items" : {
              "type" : "record",
              "name" : "rating_results",
              "fields" : [ {
                "name" : "rating_result",
                "type" : {
                  "type" : "record",
                  "name" : "rating_result",
                  "fields":[
                      {"name":"name", "type":["null", "string"]},
                      {"name":"age", "type":"float"},
                      {"name":"citycode", "type":["null", "float"]}
                    ]
                    }}]}}},
        {"name": "related_to","type" : ["null",{
          "type": "record",
          "name": "related_to",
          "fields": [
            {"name": "category","type": "string"}
          ]
        }]}
      ]}
    }
  ]
}
```

### JSON result

```json
{
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
                    "name": {
                        "string": "TATA"
                    },
                    "age": 3.0,
                    "citycode": {
                        "float": 6.9
                    }
                }
            },
            {
                "rating_result": {
                    "name": {
                        "string": "TATA"
                    },
                    "age": 3.0,
                    "citycode": {
                        "float": 6.9
                    }
                }
            }
        ],
        "related_to": {
            "enterprise.thing.related_to": {
                "category": "TATA"
            }
        }
    }
}
```
