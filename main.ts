bluetooth.onBluetoothConnected(function () {
    conStatus = 1
    while (conStatus == 1) {
        uartData = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Hash))
        basic.showString(uartData)
    }
})
bluetooth.onBluetoothDisconnected(function () {
    conStatus = 0
    basic.showString("D")
})
let uartData = ""
let conStatus = 0
bluetooth.startUartService()
basic.showIcon(IconNames.Heart)
conStatus = 0
