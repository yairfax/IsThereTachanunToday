const https = require("https")
const tachanun = require("./tachanun.js")

today = new Date()
year = today.getFullYear()
month = today.getMonth() + 1
day = today.getDay()

https.get(`https://www.hebcal.com/converter/?cfg=json&gy=${year}&gm=${month}&gd=${day}&g2h=1`, (res) => {
    data = ""

    res.on('data', (d) => { data += d })

    res.on('end', () => {
        data = JSON.parse(data)
        console.log(data)
        console.log(tachanun.noTachanun(data.hm.toLowerCase(), data.hd))
    })
})
