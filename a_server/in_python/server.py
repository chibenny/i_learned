import socket


def startserver():
    with socket.create_server(("", 8000)) as server:
        """This is super rudimentary. I just wanted to get a feel for it,
        and learn a bit about being lower (_higher_?) on the stack."""
        while True:
            conn, addr = server.accept()
            request = conn.recv(1024).decode("utf-8")
            request_context = request.split("\r\n")
            method, path, version = request_context[0].strip().split(" ")
            body = request_context.pop()
            params = {}
            query = path.split("?", 1)[-1]
            for param in query.split("&"):
                k, v = param.split("=")
                params[k] = v

            headers = dict(h.split(": ", 1) for h in request_context if ": " in h)
            headers_print = "".join([f"\t{k}: {v}\n" for k, v in headers.items()])

            content = (
                f"Hello, World!\n\nHere are your params: {params}\n"
                f"Your request method is: {method}, using HTTP version: {version}\n"
                f"Your headers: \n{headers_print}\n ...and the body: {body}"
            )

            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain; charset=utf-8\r\n"
                f"Content-Length: {len(content)}\r\n"
                "\r\n"
                f"{content}"
            )
            conn.sendall(response.encode("utf-8"))


if __name__ == "__main__":
    startserver()
