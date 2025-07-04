local socket = require("socket")

local port = 8080
local server = socket.bind("localhost", port)

print("Listening on port: " .. port)

while true do
    local client = server:accept()
    client:settimeout(1)

    local request = client:receive()
    print("Request received: " .. (request or "[nil]"))

    local message = "Hello from the backend!"

    local response = "HTTP/1.1 200 OK\r\n" ..
                     "Content-Type: text/plain\r\n" ..
                     "Content-Length: " .. message:len() .. "\r\n" ..
                     "Connection: close\r\n" ..
                     "\r\n" ..
                     message .. "\n"

    client:send(response)
    client:close()
end
