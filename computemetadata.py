
import re
import sys
from typing import Any, List
import warnings
from typing import Iterable
from google.api_core.extended_operation import ExtendedOperation
from google.cloud import compute_v1
from google.cloud import storage
import json


################GCP Authentication Purpose##########################
def authenticate_implicit_with_adc(project_id="terraform-370703"):
    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")

 
def instance_metadata(instance_name):
    """Prints out a bucket's metadata."""
    instance_name = 'instance-1'

    instance_client = compute_v1.InstancesClient()
    instance = instance_client.get_instance(instance_name)
	
    print(f"Name: {instance.name}")
    json_data = '[{"ID":"instance.id","Name":"instance.name","DeviceName":"deviceName"}]'
            

    json_object = json.loads(json_data)

    json_formatted_str = json.dumps(json_object, indent=2)

    print(json_formatted_str)
    