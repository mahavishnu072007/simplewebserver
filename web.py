from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>
           About  my device 
        </title>
    </head>
    <body bgcolor="black" text="white">
      <table border="4" cellpadding="15" cellspacing="5" aligh="center" bordercolor="red">
        <tr>
            <th>s.no</th>
            <th>device specification(vishnu)</th>
            <th>type</th>
        </tr>
        <tr>
          <td>1</td>
          <td>device name</td>
          <td>LAPTAOP-TMP215-75-G2</td>
        </tr>
        <tr>
          <td>2</td>
          <td>processor</td>
          <td>Intel(R) Core(TM) Ultra 5 125H (1.20 GHz)</td>
        </tr>
        <tr>
          <td>3</td>
          <td>installed RAM</td>
          <td>16 GB</td>
        </tr>
        <tr>
          <td>4</td>
          <td>device ID</td>
          <td>E3F06795-1915-4187-8C56-F3F3634559FF</td>
        </tr>
        <tr>
          <td>5</td>
          <td>product ID</td>
          <td>00342-42784-11355-AAOEM</td>
        </tr>
        <tr>
          <td>6</td>
          <td>system type</td>
          <td>64-bit operating system</td>
        </tr>
        <tr>
          <td>7</td>
          <td>pen and touch</td>
          <td>No pen or touch</td>
        </tr>
  
      </table> 

    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()