from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json


PAGE = b"""<!doctype html>
<meta charset=utf-8><title>Network demo</title>
<h1>Network demo</h1>
<button id=normal>Valid request</button>
<button id=invalid>Invalid request</button>
<pre id=result></pre>
<script>
async function show(quantity) {
  const response = await fetch('/api/quote', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({quantity})
  });
  const data = await response.json();
  document.querySelector('#result').textContent = response.status + ' ' + JSON.stringify(data);
}
document.querySelector('#normal').onclick = () => show(2);
document.querySelector('#invalid').onclick = () => show(0);
</script>"""


class Handler(BaseHTTPRequestHandler):
    def send_payload(self, status, payload, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if self.path == "/":
            self.send_payload(200, PAGE, "text/html; charset=utf-8")
        else:
            self.send_payload(404, b"Not found", "text/plain")

    def do_POST(self):
        if self.path != "/api/quote":
            self.send_payload(404, b"Not found", "text/plain")
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 1024:
                raise ValueError("invalid length")
            data = json.loads(self.rfile.read(length))
            quantity = data.get("quantity") if isinstance(data, dict) else None
            if type(quantity) is not int or not 1 <= quantity <= 10:
                raise ValueError("invalid quantity")
        except ValueError:
            payload = json.dumps({"error": "invalid_quantity"}).encode()
            self.send_payload(400, payload, "application/json")
            return
        payload = json.dumps({"total_kopecks": quantity * 2500}).encode()
        self.send_payload(200, payload, "application/json")


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
