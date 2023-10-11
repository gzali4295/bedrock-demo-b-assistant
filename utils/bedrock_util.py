import boto3
import botocore
from langchain.llms.bedrock import Bedrock
from botocore.config import Config
import json
import anthropic

#boto3 uses instance role which has permissions for bedrock

region = "us-west-2"
url = "https://bedrock.us-west-2.amazonaws.com"

config = Config(
   retries = {
      'max_attempts': 3,
      'mode': 'standard'
   }
)

#create boto3 client for bedrock
bedrock = boto3.client(service_name='bedrock',region_name=region,endpoint_url=url, config=config)

def bedrock_test():
    output_text = bedrock.list_foundation_models()
    return output_text


#Claude V2 and paramters
def call_model_claude(prompt):
    body = json.dumps(
        {"prompt": anthropic.HUMAN_PROMPT + prompt + anthropic.AI_PROMPT, 
         "max_tokens_to_sample": 1024,
         "temperature":0.5,
         "top_p":1,
         "top_k":250,
         "stop_sequences":[anthropic.HUMAN_PROMPT]
          })
    model_id = 'anthropic.claude-v2'
    content_type = 'application/json'
    accept = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=model_id, accept=accept, contentType=content_type)
    response_body = json.loads(response.get('body').read())

    return response_body['completion']

def call_model_jurassic(prompt):
    body = json.dumps(
        {"prompt": prompt + f"\n", 
         "maxTokens": 1024,
         "temperature": 0.5,
         "topP": 1,
         "stopSequences": [],
         "countPenalty": {"scale": 0},
         "presencePenalty": {"scale": 0},
         "frequencyPenalty": {"scale": 0}
          })
    model_id = "ai21.j2-jumbo-instruct"
    content_type = 'application/json'
    accept = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=model_id, accept=accept, contentType=content_type)
    response_body = json.loads(response.get('body').read())

    return response_body['completions'][0]['data']['text']

def call_model_titan(prompt):
    body = json.dumps(
        {"inputText": prompt, 
         "textGenerationConfig": {
             "maxTokenCount": 1024,
             "temperature": 0.5,
             "topP": 1,
             "stopSequences": []
         }
          })
    model_id = "amazon.titan-tg1-large"
    content_type = 'application/json'
    accept = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=model_id, accept=accept, contentType=content_type)
    response_body = json.loads(response.get('body').read())

    return response_body['results'][0]['outputText']

#wrapper on invoke_model for various models    
models = {
    "Claude" : call_model_claude,
    "Jurassic-2 Ultra" : call_model_jurassic,
    "Titan" : call_model_titan
}

def call_model(model, prompt):
    model_function = models[model]
    response = model_function(prompt)

    return response

    
# def get_lc_client(model_id):
#     session = boto3.Session()
#     bedrock= session.client(service_name='bedrock', region_name=region, endpoint_url=url)
#     client = Bedrock(model_id = model_id,
#                         client = bedrock,
#                         model_kwargs = inference_modifier_titan)
#     return client