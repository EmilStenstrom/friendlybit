class CacheControlMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        async def send_with_cache_control(message):
            if (
                message["type"] == "http.response.start"
                and message["status"] in (200, 304)
            ):
                headers = list(message["headers"])
                if not any(key.lower() == b"cache-control" for key, _ in headers):
                    headers.append((
                        b"cache-control",
                        self.cache_control(scope).encode("ascii"),
                    ))
                    message["headers"] = headers
            await send(message)

        await self.app(scope, receive, send_with_cache_control)

    @staticmethod
    def cache_control(scope):
        path = scope["path"]
        if path == "/style.css" and scope["query_string"]:
            return "public, max-age=31536000, immutable"
        if path.startswith("/script/"):
            return "public, max-age=31536000, immutable"
        if (
            path == "/favicon.ico"
            or path.startswith("/images/")
            or path.startswith("/files/")
        ):
            return "public, max-age=2592000"
        return "public, max-age=300"
