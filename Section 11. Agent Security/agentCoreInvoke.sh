#!/bin/bash
export TOKEN=$(aws cognito-idp initiate-auth \
            --client-id "7pmrn4vhtp21idalgv9717bp62" \
            --auth-flow USER_PASSWORD_AUTH \
            --auth-parameters USERNAME='manpreet',PASSWORD='helloAgentic' \
            --region us-east-1 | jq -r '.AuthenticationResult.AccessToken')
PAYLOAD='{"prompt": "'${1}'", "actor_id": "manpreet"}'
COMMAND="agentcore invoke '"
COMMAND+=${PAYLOAD}
COMMAND+="' --bearer-token "
COMMAND+=${TOKEN}
COMMAND+=" --session-id 1ee5cd98-7124-412c-a16b-fcc28ea2fc3b"
eval $COMMAND
