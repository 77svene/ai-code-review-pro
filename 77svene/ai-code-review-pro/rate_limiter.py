
    from fastapi import FastAPI
    import asyncio
    
    app = FastAPI()
    
    # Exponential backoff example
    async def wait_with_backoff():
        delay = 2
        for i in range(5):
            await asyncio.sleep(delay)
            delay *= 2
    