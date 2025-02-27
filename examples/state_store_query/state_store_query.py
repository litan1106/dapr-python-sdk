"""
dapr run python3 state_store_query.py
"""

from dapr.clients import DaprClient
from dapr.clients.grpc._state import StateItem

import json

with DaprClient() as d:
    storeName = 'statestore'

    # Wait for sidecar to be up within 5 seconds.
    d.wait(5)

    # Query the state store

    query = open('query.json', 'r').read()
    res = d.query_state(store_name=storeName, query=query)
    for r in res.results:
        print(r.key, json.dumps(json.loads(str(r.value, 'UTF-8')), sort_keys=True))
    print('Token:', res.token)

    # Get more results using a pagination token

    query = open('query-token.json', 'r').read()
    res = d.query_state(store_name=storeName, query=query)
    for r in res.results:
        print(r.key, json.dumps(json.loads(str(r.value, 'UTF-8')), sort_keys=True))
    print('Token:', res.token)
