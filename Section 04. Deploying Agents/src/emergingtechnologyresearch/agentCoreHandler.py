#!/usr/bin/env python

#setup entry point for agentcore
from bedrock_agentcore import BedrockAgentCoreApp

from . utils.crewUtils import executeApp

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload, context):
  prompt = payload.get("prompt")
  sessionId = context.session_id if context and context.session_id else payload.get("session_id")
  actorId = payload.get("actor_id")
  inputs = {
      'prompt': prompt,
      'sessionId': sessionId,
      'actorId': actorId
  }
  
  response = executeApp(inputs)
  
  return response

if __name__ == "__main__":
  app.run()
