# ChatGPT Web Client for Azure OpenAI  
  
[![Build](https://github.com/dodekanisou/openai-chatGPT-webclient/actions/workflows/ci.yaml/badge.svg)](https://github.com/dodekanisou/openai-chatGPT-webclient/actions/workflows/ci.yaml)  
[![Docker image](https://github.com/dodekanisou/openai-chatGPT-webclient/actions/workflows/docker-image.yaml/badge.svg)](https://github.com/dodekanisou/openai-chatGPT-webclient/actions/workflows/docker-image.yaml)  
  
## Usage  

You will need the following information [from your Azure portal](https://learn.microsoft.com/azure/cognitive-services/openai/quickstart?tabs=command-line&pivots=programming-language-csharp#retrieve-key-and-endpoint).
  
```toml
API_TYPE = "azure"  
API_BASE = "https://open-ai-service-region.openai.azure.com/"  
API_VERSION = "2023-03-15-preview"  
API_KEY = "ab05ab05ab05ab05ab05ab05"  
MODEL_NAME = "gpt-4-deployment"  
```

You can store them in a file named `secret.toml` in the `.streamlit` folder and `--mount` the folder in the docker.

If you want to pull the image from the [Docker Hub repository](https://hub.docker.com/r/dodekanisou/openai-chatgpt-webclient/tags):

```bash
docker run -p 44333:44480 dodekanisou/openai-chatgpt-webclient:2023-05-01 --mount type=bind,source=PATH_TO_NEW_FOLDER/.streamlit,target=/app/.streamlit,bind-propagation=shared
```

If you want to clone this repository and build your own image:

```bash
git clone https://github.com/dodekanisou/openai-chatGPT-webclient
cd openai-chatGPT-webclient
docker build -t chatgpt-image .  
docker run -p 44480:44480 --mount type=bind,source=PATH_TO_NEW_FOLDER/.streamlit,target=/app/.streamlit,bind-propagation=shared chatgpt-image
```

Open a browser and visit http://localhost:44480.

### Example

- Run local build image. Mound folder `c:/Users/myUser/openai-chatGPT-webclient/.streamlit` and expose in http://localhost:44333

  ```bash
  docker run -p 44333:44480 --mount type=bind,source=c:/Users/myUser/openai-chatGPT-webclient/.streamlit,target=/app/.streamlit,bind-propagation=shared chatgpt-image
  ```

## Code development

If you want to contribute to this codebase, clone the repository and follow these instructions.

### Development installation

Install module in [editable/develop mode](https://pip.pypa.io/en/stable/cli/pip_install/#install-editable) (`-e`) and include the development dependencies (the `[dev]` argument you see) using the following command:

```bash
pip install -e .[dev]
```

You can use the [VSCode Test Explorer](https://code.visualstudio.com/docs/python/testing) to debug your code.

### Code quality practices

Before making any commit, ensure the following:

- Format the code using `black`:

  ```bash
  python -m black . 
  ```

- Check for `flake8` errors:

  ```bash
  python -m flake8 .
  ```

- Ensure all tests pass:

  ```bash
  python -m pytest .
  ```

- Verify `setup.cfg` file is [consistently formatted](https://github.com/asottile/setup-cfg-fmt):

  ```bash
  setup-cfg-fmt setup.cfg
  ```

## References

Here is a list of related projects and references to this effort:

- [Robo minion code](https://github.com/easonlai/robo_minion_gpt35turbo/tree/main): Similar codebase for minion bots.
- [Robo minion blog post](https://medium.com/geekculture/streamlit-and-azure-openai-service-gpt-3-5-73640e8728f2): This is the idea that inspired me to create this tool.
- [Save data in local storage](https://discuss.streamlit.io/t/saving-data-in-local-storage-via-streamlit/28785/8): I was thinking of saving bot sessions in local storage.
