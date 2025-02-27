# Connecting LangGraph to Open Web UI

This guide will walk you through setting up LangGraph and integrating it with Open Web UI.

## Prerequisites

- Python installed (preferably Python 3.11+)
- Open Web UI installed and running

## Setup Steps

1. **Get an API Key**  
   Go to [Anthropic Console](https://console.anthropic.com/settings/keys) and generate an API key.

2. **Create a `.env` File**  
   - Copy `.env.example` and rename it to `.env`.  
   - Replace the `ANTHROPIC_API_KEY` value with your key from step 1.

3. **Install Dependencies**  
   Run the following command to install required packages:

   ```sh 
   pip install -r requirements.txt
   ```

4. **Compile the Agent** 

    Run:

    ```sh
    python langgraph_agent.py
    ```

5. **Start the Server**  
   Launch the FastAPI server with:

   ```sh
   uvicorn fastapi_server:app --reload
   ```

6. **Add the Pipeline to Open Web UI**
    Add `pipeline_stream.py` as a new pipeline in Open Web UI.

7. **Select the Model**
    Choose *LangGraph Agent (Stream)* as your model inside Open Web UI.

8. **Start Chatting!**
    Enjoy using LangGraph with Open Web UI.

## Acknowledgments

Special thanks to [@dukai289](https://github.com/dukai289) for creating the first version on which this solution is based and to [@PlebeiusGaragicus](https://github.com/PlebeiusGaragicus) for commenting of it in a discussion.  
You can check out the original code here: [open-webui/pipelines#158](https://github.com/open-webui/pipelines/pull/158/files).
