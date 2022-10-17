# pip install azure-ai-language-questionanswering
# https://learn.microsoft.com/en-us/python/api/overview/azure/ai-language-questionanswering-readme?view=azure-python

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering.authoring import AuthoringClient

endpoint = "https://j2-universal.cognitiveservices.azure.com/"
key = '3c4ba93f29bf4a76a4b8b8486085a6e4'


# create client
client = AuthoringClient(endpoint, AzureKeyCredential(key))
with client:

    # create project
    project_name = "IssacNewton"
    project = client.create_project(
        project_name=project_name,
        options={
            "description": "biography of Sir Issac Newton",
            "language": "en",
            "multilingualResource": True,
            "settings": {
                "defaultAnswer": "no answer"
            }
        })

    print("view created project info:")
    print("\tname: {}".format(project["projectName"]))
    print("\tlanguage: {}".format(project["language"]))
    print("\tdescription: {}".format(project["description"]))
