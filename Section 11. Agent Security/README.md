# Section 11. Agent Security

## Purpose
This section focuses on Agent Security. Demoes include avoiding Agent Goal Hijack by implementing Dual Agent Pattern. As part of the demoes, we also worked on avoiding Identity and Privilege Abuse.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:
```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:
```bash
crewai install
```

## Pre-requisites
#### AWS CLI Setup

#### OpenAI Setup (If using OpenAI models)

#### AWS Secrets Manager Setup (Optional if running on local only)

#### Langfuse Setup

#### AWS Bedrock AgentCore Memory Setup

#### AWS Bedrock AgentCore MCP Setup
#### Tavily Setup

### :new: MongoDB Setup (Local only)

## Running the Project
To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the emergingTechnologyResearch Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.