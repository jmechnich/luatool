print('main.lua ver 1.0')
print('get ip ',wifi.sta.getip())
print('start TCP client...')
conn=net.createConnection(net.TCP, false) 
conn:on("receive", function(conn, payload) print("data ",payload) end )
-- web config
conn:connect(80,"70.38.12.79")
conn:send("GET / HTTP/1.1\r\nHost: esp8266.com\r\n")
-- web config