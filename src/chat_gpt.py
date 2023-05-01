import openai


def setup_openai_api(settings):
    openai.api_type = settings["API_TYPE"] if settings["API_TYPE"] else "azure"
    openai.api_base = settings["API_BASE"]
    openai.api_version = (
        settings["API_VERSION"] if settings["API_VERSION"] else "2023-03-15-preview"
    )
    openai.api_key = settings["API_KEY"]


def generate_response(prompts, model_name, temperature, max_tokens, top_p):
    completion = openai.ChatCompletion.create(
        engine=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        messages=prompts,
    )
    message = completion.choices[0].message.content
    return message


def update_prompts(prompts, role, content):
    prompts.append({"role": role, "content": content})
    return prompts


def reset_prompts(context):
    return [{"role": "system", "content": context}]
