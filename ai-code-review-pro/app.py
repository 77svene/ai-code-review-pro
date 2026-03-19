
    import gradio as gr
    import httpx
    import asyncio
    
    # Use environment variable or default key if not set
    OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY", "sk-or-v1-...") # Placeholder, ensure env var is set
    client = httpx.AsyncClient()
    
    async def review_code(code):
        try:
            # Ensure we use the correct key format and pass it in headers
            headers = {"Authorization": f"Bearer {OPENROUTER_KEY}", "Content-Type": "application/json"}
            prompt = f"Review this code:\n\n{code}"
            response = await client.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json={
                "model": "openrouter/anthropic/claude-3-5-sonnet-20240620",
                "messages": [{"role": "user", "content": prompt}]
            })
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return str(e)
    
    gr.Interface(review_code, "text", "text", title="AI Code Reviewer")
    