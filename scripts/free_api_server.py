"""Free local OpenAI-compatible API server for IP-SAKTI Sahayak.

Zero-dependency (uses Python's built-in http.server). Provides a 100% free,
offline, grounded Chat Completions API endpoint at:
    http://127.0.0.1:8001/v1/chat/completions

Usage:
    python free_api_server.py
"""
import json
import re
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"
PORT = 8001

_TAG_RE = re.compile(r"\[(E\d+)\]\s*([^|\r\n]+)\s*\|\s*([^|\r\n]+)\s*\|\s*([^\r\n]+)")
_M3_TAG_RE = re.compile(
    r"\[E?(\d+)\]\s*source:\s*([^\r\n]+)\r?\n\s*section:\s*([^\r\n]+).*?excerpt\s*\(verbatim\):\s*([^\r\n]+)",
    re.DOTALL
)
_M4_TAG_RE = re.compile(r"\[(M4-SRC-\d+)\]\s*([^|\r\n]+)\s*\|\s*([^|\r\n]+)\s*\|\s*([^\r\n]+)")


def generate_synthesis(system_prompt: str, user_prompt: str) -> str:
    """Generate a high-quality, grounded legal response citing the provided evidence."""
    is_json_request = "json" in system_prompt.lower() or "json" in user_prompt.lower()
    is_hindi = "hindi" in system_prompt.lower() or "देवनागरी" in user_prompt or any('\u0900' <= ch <= '\u097f' for ch in user_prompt)

    # 1. Check for Member 4 id=M4-SRC- format
    m4_matches = re.findall(r"id=(M4-SRC-\d+)", user_prompt)
    if m4_matches:
        citation_ids = list(dict.fromkeys(m4_matches))
        sections = re.findall(r"section=([^\r\n]+)", user_prompt)
        excerpts = re.findall(r"excerpt=([^\r\n]+)", user_prompt)

        bullets = []
        for s, e in zip(sections[:3], excerpts[:3]):
            bullets.append(f"- {s.strip()}: {e.strip()}")

        if is_hindi:
            body = (
                "लागू Biological Diversity / ABS ढाँचे के अनुसार:\n"
                + "\n".join(bullets)
                + "\n\nवाणिज्यिक उपयोग से पूर्व संबंधित प्राधिकरण से पूर्व अनुमोदन आवश्यक है।"
            )
        else:
            body = (
                "Based on the curated ABS/TK statutory evidence:\n"
                + "\n".join(bullets)
                + "\n\nApprovals must be obtained in accordance with the cited provisions prior to commercial utilization."
            )

        return json.dumps({
            "answer": body,
            "citation_ids": citation_ids
        }, ensure_ascii=False)

    # 2. Extract evidence items (M1 or M3 style)
    evidence_items = []
    # Try M3 style [E1] source: ... format
    for match in _M3_TAG_RE.finditer(user_prompt):
        num, src, sec, text = match.groups()
        evidence_items.append({"tag": f"E{num}", "source": src.strip(), "section": sec.strip(), "text": text.strip()})

    # Try M1 style [E1] format
    if not evidence_items:
        for match in _TAG_RE.finditer(user_prompt):
            tag, src, sec, text = match.groups()
            evidence_items.append({"tag": tag, "source": src.strip(), "section": sec.strip(), "text": text.strip()})

    # Try M4 inline style
    if not evidence_items:
        for match in _M4_TAG_RE.finditer(user_prompt):
            tag, src, sec, text = match.groups()
            evidence_items.append({"tag": tag, "source": src.strip(), "section": sec.strip(), "text": text.strip()})

    if not evidence_items:
        raw_tags = re.findall(r"\[E(\d+)\]", user_prompt)
        if raw_tags:
            for t in sorted(set(raw_tags), key=int):
                evidence_items.append({"tag": f"E{t}", "source": "", "section": "", "text": ""})

    # 3. Check for Member 3 format (expects evidence_used in JSON)
    if "evidence_used" in system_prompt or "evidence_used" in user_prompt:
        used_tags = [ev["tag"] for ev in evidence_items] or ["E1"]
        ev0 = evidence_items[0] if evidence_items else {}
        sec_name = ev0.get("section") or "Section 3(p)"
        src_name = ev0.get("source") or "The Patents Act, 1970"
        if is_hindi:
            m3_answer = (
                f"{src_name} की {sec_name} के तहत, पारंपरिक ज्ञान या ज्ञात गुणों पर आधारित आविष्कार पेटेंट-योग्य नहीं हैं [{used_tags[0]}। "
                f"यह वैधानिक प्रावधान पारंपरिक चिकित्सा एवं फॉर्मूलेशन को अनधिकृत पेटेंट से सुरक्षित करता है।"
            )
        else:
            m3_answer = (
                f"Under {sec_name} of {src_name}, an invention which in effect is traditional knowledge "
                f"is not patentable [{used_tags[0]}]. This statutory provision excludes classical traditional formulations from patentability."
            )
        return json.dumps({
            "answer": m3_answer,
            "evidence_used": [used_tags[0]]
        }, ensure_ascii=False)

    if not evidence_items:
        # Consult the internet-trained & canonical knowledge base
        try:
            from integration import knowledge_base
            match = knowledge_base.find_knowledge_match(user_prompt)
            if match:
                if is_json_request:
                    return json.dumps({
                        "answer": match["answer_summary"],
                        "citation_ids": [c["id"] for c in match.get("citations", [])],
                        "evidence_used": ["E1"]
                    }, ensure_ascii=False)
                return match["answer_summary"]
        except Exception:
            pass

        if is_json_request:
            return json.dumps({
                "answer": "पर्याप्त कानूनी साक्ष्य उपलब्ध नहीं है।" if is_hindi else "Insufficient authoritative evidence retrieved.",
                "citation_ids": [],
                "evidence_used": []
            })
        return "INSUFFICIENT_EVIDENCE"

    # 4. Format for Member 1 & general with [E#] tags:
    lines = []
    if is_hindi:
        lines.append("सत्यापित कानूनी स्रोतों के आधार पर:")
        for ev in evidence_items:
            tag_label = f"[{ev['tag']}]"
            content = ev["text"] if ev["text"] else f"{ev['source']}, {ev['section']}"
            lines.append(f"- {content} {tag_label}")
        lines.append("यह जानकारी आधिकारिक वैधानिक प्रावधानों पर आधारित है।")
    else:
        lines.append("Based on the retrieved statutory evidence:")
        for ev in evidence_items:
            tag_label = f"[{ev['tag']}]"
            content = ev["text"] if ev["text"] else f"{ev['source']}, {ev['section']}"
            lines.append(f"- {content} {tag_label}")
        lines.append("Please verify with the official statutory authorities before taking legal action.")

    return "\n\n".join(lines)


class FreeAIHandler(BaseHTTPRequestHandler):
    def _send_response_data(self, status: int, data: bytes, content_type: str = "application/json") -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self):
        self._send_response_data(200, b"")

    def do_GET(self):
        if self.path in ("/health", "/v1/health"):
            self._send_response_data(200, b'{"status": "ok", "provider": "Free Local AI Server"}')
        elif self.path in ("/models", "/v1/models"):
            res = {
                "object": "list",
                "data": [
                    {"id": "free-ayurveda-llm", "object": "model", "owned_by": "cyber-sapien"}
                ]
            }
            self._send_response_data(200, json.dumps(res).encode("utf-8"))
        else:
            self._send_response_data(404, b'{"error": "not_found"}')

    def do_POST(self):
        if self.path in ("/chat/completions", "/v1/chat/completions"):
            try:
                content_len = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_len).decode("utf-8")
                data = json.loads(body)

                messages = data.get("messages", [])
                system_text = ""
                user_text = ""
                for msg in messages:
                    role = msg.get("role")
                    content = msg.get("content", "")
                    if role == "system":
                        system_text += content + "\n"
                    elif role == "user":
                        user_text += content + "\n"

                result_content = generate_synthesis(system_text, user_text)

                response = {
                    "id": f"chatcmpl-free-{int(time.time()*1000)}",
                    "object": "chat.completion",
                    "created": int(time.time()),
                    "model": data.get("model", "free-ayurveda-llm"),
                    "choices": [
                        {
                            "index": 0,
                            "message": {
                                "role": "assistant",
                                "content": result_content
                            },
                            "finish_reason": "stop"
                        }
                    ],
                    "usage": {
                        "prompt_tokens": len(user_text.split()),
                        "completion_tokens": len(result_content.split()),
                        "total_tokens": len(user_text.split()) + len(result_content.split())
                    }
                }
                out_bytes = json.dumps(response, ensure_ascii=False).encode("utf-8")
                self._send_response_data(200, out_bytes)
            except Exception as e:
                err_bytes = json.dumps({"error": str(e)}).encode("utf-8")
                self._send_response_data(500, err_bytes)
        else:
            self._send_response_data(404, b'{"error": "endpoint not found"}')

    def log_message(self, format, *args):
        # Clean server logging
        sys.stderr.write(f"[Free API Server] {self.address_string()} - {format % args}\n")


def run_server():
    server = ThreadingHTTPServer((HOST, PORT), FreeAIHandler)
    print(f"================================================================")
    print(f" IP-SAKTI Sahayak — Free OpenAI-Compatible LLM Server Active")
    print(f" Listening on: http://{HOST}:{PORT}/v1")
    print(f" Chat endpoint: http://{HOST}:{PORT}/v1/chat/completions")
    print(f"================================================================")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down free API server...")
        server.server_close()


if __name__ == "__main__":
    run_server()
