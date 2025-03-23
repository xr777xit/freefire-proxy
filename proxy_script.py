from mitmproxy import http

VALID_KEYS = {
    "123456": "clave123",  # Usuario 1
    "789012": "clave456"   # Usuario 2
}

def request(flow: http.HTTPFlow):
    key = flow.request.headers.get("X-Proxy-Key")
    
    if key not in VALID_KEYS.values():
        flow.response = http.Response.make(
            403,  # Código HTTP 403 (Acceso Denegado)
            b"Acceso Denegado",
            {"Content-Type": "text/plain"}
        )
        return

    # Interceptar peticiones a Free Fire
    if "freefiremobile.com" in flow.request.pretty_url:
        flow.response = http.Response.make(
            200,  # Código HTTP 200 (OK)
            b'{"success": true, "skins_unlocked": true}',
            {"Content-Type": "application/json"}
        )
