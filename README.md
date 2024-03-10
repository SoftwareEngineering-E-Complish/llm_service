# llm_service

structure for function definiton:

'''  

'''

tools = [
  {
    "type": "function",
    "function": {
      "name": "user_query",
      "description": "Search for an house or appartment at a given location given the attributes",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "location/s of the properties with german names (eg. [Zürich,Winterthur]) ",
            },                  
            "num_rooms": {"type": "string", "description": "Number of rooms in the property (eg. 2,1-99,4,3)"},
        },
        "required": ["location"],
      },
    }
  }
]