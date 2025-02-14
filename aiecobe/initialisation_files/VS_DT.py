from django.test import TestCase
from aiecobe.functions.tool1_functions import *
from aiecobe.models import *
import openai
import json
import time
import logging
from datetime import datetime





# gets API Key from environment variable OPENAI_API_KEY
def NewAssistantDTVectorStore():
    client = openai.OpenAI()

    vector_store = client.beta.vector_stores.create(name="Texte DT")

    print(f"vector store is {vector_store.id}")

    # Ready the files for upload to OpenAI
    file_paths = ["aiecobe\initialisation_files\DT\joe_20240314_0062_0037.pdf","aiecobe\initialisation_files\DT\joe_20190725_0171_0053.pdf","aiecobe\initialisation_files\DT\joe_20210117_0015_0029.pdf","aiecobe\initialisation_files\DT\joe_20240712_0165_0028.pdf"]
   
    file_streams = [open(path, "rb") for path in file_paths]

    # Use the upload and poll SDK helper to upload the files, add them to the vector store,
    # and poll the status of the file batch for completion.
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
    )

    # You can print the status and the file counts of the batch to see the result of this operation.
    print(f"file batch is {file_batch.status}")
    print(file_batch.file_counts)




