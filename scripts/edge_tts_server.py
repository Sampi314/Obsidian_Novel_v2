#!/usr/bin/env python3
"""Tiny Edge TTS proxy server for the floating TTS player.
Usage: python3 scripts/edge_tts_server.py
Runs on http://127.0.0.1:5050
"""

import asyncio
import io
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

import edge_tts

PORT = 5050

class TTSHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == '/tts':
            params = parse_qs(parsed.query)
            text = params.get('text', [''])[0]
            voice = params.get('voice', ['vi-VN-HoaiMyNeural'])[0]
            rate = params.get('rate', ['0%'])[0]

            if not text:
                self.send_error(400, 'Missing text parameter')
                return

            try:
                audio_data = asyncio.run(self._generate(text, voice, rate))
                self.send_response(200)
                self.send_header('Content-Type', 'audio/mpeg')
                self.send_header('Content-Length', str(len(audio_data)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(audio_data)
            except Exception as e:
                self.send_error(500, str(e))

        elif parsed.path == '/voices':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'[{"id":"vi-VN-HoaiMyNeural","name":"HoaiMy (Nu)"},{"id":"vi-VN-NamMinhNeural","name":"NamMinh (Nam)"}]')

        else:
            self.send_error(404)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

    async def _generate(self, text, voice, rate):
        rate_str = rate if rate.endswith('%') else rate + '%'
        if not rate_str.startswith('+') and not rate_str.startswith('-'):
            rate_str = '+' + rate_str
        comm = edge_tts.Communicate(text, voice, rate=rate_str)
        buf = io.BytesIO()
        async for chunk in comm.stream():
            if chunk['type'] == 'audio':
                buf.write(chunk['data'])
        return buf.getvalue()

    def log_message(self, format, *args):
        print(f"[TTS] {args[0]}")

if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', PORT), TTSHandler)
    print(f'Edge TTS server running at http://127.0.0.1:{PORT}')
    print(f'Test: http://127.0.0.1:{PORT}/tts?text=Xin+chào&voice=vi-VN-HoaiMyNeural')
    print('Press Ctrl+C to stop')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopped.')
