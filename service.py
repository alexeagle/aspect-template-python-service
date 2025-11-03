from __future__ import annotations

import random
import sys

from fastapi import FastAPI, Response
import uvicorn


app = FastAPI()


@app.get("/")
def get_random_byte() -> Response:
    random_value = random.getrandbits(8)
    # Use to_bytes for a consistent single-byte response payload.
    return Response(content=random_value.to_bytes(1, "little"), media_type="application/octet-stream")


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        raise SystemExit("Usage: python service.py <port>")

    try:
        port = int(argv[1])
    except ValueError as exc:
        raise SystemExit("Port must be an integer") from exc

    uvicorn.run(app, host="127.0.0.1", port=port, log_level="info")


if __name__ == "__main__":
    main(sys.argv)
