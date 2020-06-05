const express = require('express')
const bodyParser = require('body-parser');
const logger = require('morgan');
const exphbs = require('express-handlebars');

const https = require("https");
const tachanun = require("./tachanun.js");
const _ = require("underscore")

const app = express();
const PORT = 3000

var hbs = exphbs.create({ defaultLayout: 'main', partialsDir: "vies/partials/" });
app.use(logger('dev'))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.engine('handlebars', hbs.engine);
app.set('view engine', 'handlebars');

app.get("/", function (req, res) {
    today = new Date();

    if (req.query.date) {
        date = _(req.query.date.split("-")).map(Number)
        today.setYear(date[0])
        today.setMonth(date[1] - 1)
        today.setUTCDate(date[2])
    }

    year = today.getFullYear();
    month = today.getMonth() + 1;
    day = today.getUTCDate();

    https.get(`https://www.hebcal.com/converter/?cfg=json&gy=${year}&gm=${month}&gd=${day}&g2h=1`, (resp) => {
        data = ""

        resp.on('data', (d) => { data += d })

        resp.on('end', () => {
            data = JSON.parse(data)
            // console.log(data)
            // console.log()
            noTachanun = tachanun.noTachanun(data.hm.toLowerCase(), data.hd)
            res.render("home", {
                noTachanun: noTachanun,
                date: today.toDateString(),
                hebrewDate: `${data.hd} ${data.hm} ${data.hy}`,
                hebrewDateHebrew: data.hebrew,
                reason: noTachanun ? noTachanun.description : undefined,
                datePlaceholder: today.toISOString().substring(0, 10)
            })
        })
    })
})

app.listen(PORT, function () {
    console.log(`Listening on port ${PORT}`)
})

