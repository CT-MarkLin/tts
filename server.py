from sanic import Sanic, Request
import edge_tts

VOICE = "zh-CN-XiaoxiaoNeural"

app = Sanic("MyHelloWorldApp")

@app.get("/")
async def handler(request: Request):
    text = request.args.get("text")
    response = await request.respond(content_type="audio/mpeg")
    communicate = edge_tts.Communicate(text, VOICE)
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            await response.send(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            print(f"WordBoundary: {chunk}")
