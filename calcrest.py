#!/usr/bin/python3

"""
Miguel Ángel Lozano Montero.
Program implementing a simple calculator in REST version.
Version with only one resource ("/calc"). It is updated with PUT, which sends
the operation in the body (ex: 4,5,+). It is checked with GET, which returns
the result (ex: 4+5=9).
"""

import webapp


class calcRest (webapp.webApp):
    """Web application that works as a simple
    calculator designed under REST rules"""

    calc = []

    def parse(self, request):
        """Return the method, resource name (without /),
        operands and operator (if they come in the request)"""

        method = request.split(' ', 1)[0]
        resourceName = request.split(' ', 2)[1][1:]
        op1 = request.split(',')[-3][-1]
        op2 = request.split(',')[-2]
        op = request.split(',')[-1]

        return (method, resourceName, op1, op2, op)

    def process(self, parsed):
        """Process the relevant elements of the request. """

        method, resourceName, op1, op2, op = parsed

        if method == "PUT" and resourceName == "calc":
            self.calc = [op1, op2, op]
            httpCode = "200 0K"
            htmlBody = "<html><body><h1>Datos recibidos</h1></body></html>"
        elif method == "GET" and resourceName == "calc":
            if len(self.calc) > 0:
                if self.calc[2] == "+":
                    result = int(self.calc[0]) + int(self.calc[1])
                    httpCode = "200 OK"
                    htmlBody = "<html><body><h1>" + self.calc[0] + "+" + \
                               self.calc[1] + "=" + str(result) + \
                               "</h1></body></html>"
                elif self.calc[2] == "-":
                    result = int(self.calc[0]) - int(self.calc[1])
                    httpCode = "200 OK"
                    htmlBody = "<html><body><h1>" + self.calc[0] + "-" + \
                               self.calc[1] + "=" + str(result) + \
                               "</h1></body></html>"
                elif self.calc[2] == "x":
                    result = int(self.calc[0]) * int(self.calc[1])
                    httpCode = "200 OK"
                    htmlBody = "<html><body><h1>" + self.calc[0] + "x" + \
                               self.calc[1] + "=" + str(result) + \
                               "</h1></body></html>"
                elif self.calc[2] == "/":
                    result = int(self.calc[0]) / int(self.calc[1])
                    httpCode = "200 OK"
                    htmlBody = "<html><body><h1>" + self.calc[0] + "/" + \
                               self.calc[1] + "=" + str(result) + \
                               "</h1></body></html>"
                else:
                    httpCode = "404 Not Found"
                    htmlBody = "<html><body><h1>" + "Operador no " + \
                               "reconocido. Intente enviar los datos " + \
                               "otra vez" + "</h1></body></html>"
            else:
                httpCode = "404 Not Found"
                htmlBody = "<html><body><h1>" + "No tengo datos aun" + \
                           "</h1></body></html>"
        else:
            httpCode = "404 Not Found"
            htmlBody = "<html><body><h1>" + "No encontrado" + \
                       "</h1></body></html>"

        return (httpCode, htmlBody)

if __name__ == "__main__":
    testCalcRest = calcRest("localhost", 1234)
