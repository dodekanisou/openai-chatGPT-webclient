from unittest.mock import MagicMock
from src import chat_gpt
import openai


def test_setup_openai_api():
    secrets = {
        "API_TYPE": "azure",
        "API_BASE": "https://api.openai.com",
        "API_VERSION": "2023-03-15-preview",
        "API_KEY": "test_api_key",
    }
    chat_gpt.setup_openai_api(secrets)
    assert openai.api_type == secrets["API_TYPE"]
    assert openai.api_base == secrets["API_BASE"]
    assert openai.api_version == secrets["API_VERSION"]
    assert openai.api_key == secrets["API_KEY"]


def test_generate_response():
    prompts = [{"role": "system", "content": "Test context"}]
    model_name = "my-gpt-deployment"
    temperature = 0.7
    max_tokens = 8000
    top_p = 0.95

    chat_gpt.openai.ChatCompletion.create = MagicMock()
    chat_gpt.openai.ChatCompletion.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Test response"))]
    )

    response = chat_gpt.generate_response(
        prompts, model_name, temperature, max_tokens, top_p
    )

    assert response == "Test response"
    chat_gpt.openai.ChatCompletion.create.assert_called_once()


def test_update_prompts():
    prompts = [{"role": "system", "content": "Test context"}]
    role = "user"
    content = "What is the capital of France?"

    updated_prompts = chat_gpt.update_prompts(prompts, role, content)

    assert updated_prompts[-1] == {
        "role": "user",
        "content": "What is the capital of France?",
    }


def test_reset_prompts():
    context = "Test context"
    reset_prompts = chat_gpt.reset_prompts(context)

    assert reset_prompts == [{"role": "system", "content": context}]
