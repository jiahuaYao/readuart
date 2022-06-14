def on_bluetooth_connected():
    global conStatus, uartData
    conStatus = 1
    while conStatus == 1:
        uartData = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        basic.show_string(uartData)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global conStatus
    conStatus = 0
    basic.show_string("D")
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

uartData = ""
conStatus = 0
bluetooth.start_uart_service()
basic.show_icon(IconNames.HEART)
conStatus = 0