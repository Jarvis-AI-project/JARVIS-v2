import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

def azure_query(query, project_name, deployment_name):
    clu_endpoint = "https://jarvis-resource.cognitiveservices.azure.com/"
    clu_key = "85a002f3b17a4e1b9b373b70c907c37f"


    # analyze quey
    client = ConversationAnalysisClient(
        clu_endpoint, AzureKeyCredential(clu_key))
    with client:
        result = client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "en",
                        "text": query
                    },
                    "isLoggingEnabled": True
                },
                "parameters": {
                    "projectName": project_name,
                    "deploymentName": deployment_name,
                    "verbose": True
                }
            }
        )
        out = {
            "user_query": result['result']['query'],
            "intent": result['result']['prediction']['intents'][0]['category'],
            "confidence": str(result['result']['prediction']['intents'][0]['confidenceScore']*100)[:4] + '%',
            "entities": [{"entity": entity['category'], "entity_value":entity['text'], "confidenceScore":str(entity['confidenceScore']*100)+'%'} for entity in result['result']['prediction']['entities']]
        }
        for element in out:
            print(element + " : " + str(out[element]))
        return out

if __name__ == "__main__":
    azure_query('increase volume to 20%', "JARVIS-SPOTIFY",'v0.1-dep1' )
    azure_query('play some music', 'JARVIS-MAIN', 'v0.1-dep1')