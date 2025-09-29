# EX01 Developing a Simple Webserver
## Date:24.09.2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>
           About  my device
        </title>
    </head>
    <body bgcolor="black" text="white">
    <h1>Name: Maha Vishnu</h1>
    <h1>Ref no: 25018250</h1>
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
```

## OUTPUT:
![alt text](<Screenshot (31).png>)
![alt text](<Screenshot (32).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
