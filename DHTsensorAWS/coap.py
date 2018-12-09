import asyncio
import aiocoap.resource as resource
import aiocoap


class BlockResource (resource.Resource):
    def __init__(self):
        super().__init__()
        self.set_content(b"This is the resource's default content")
    
    def set_content(self, content):
        self.content = content
##        while len(self.content) <= 64:
##            self.content = self.content + b"0123456789\n"

    async def render_get(self, request):
        return aiocoap.Message(payload=self.content)
        

    async def render_put(self, request):
        print('PUT payload: %s' % request.payload)
        self.set_content(request.payload)
        return aiocoap.Message(payload=self.content)


if __name__ == "__main__":
    # Resource tree creation
    root = resource.Site()
    root.add_resource(('other', 'block'), BlockResource())
    asyncio.Task(aiocoap.Context.create_server_context(root))
    asyncio.get_event_loop().run_forever()

    
    
    
    
    
