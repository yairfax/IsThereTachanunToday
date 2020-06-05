const tishrei = "tishrei"
const cheshvan = "cheshvan"
const kislev = "kislev"
const tevet = "tevet"
const shvat = "shvat"
const adar = "adar"
const nisan = "nisan"
const iyyar = "iyyar"
const sivan = "sivan"
const tamuz = "tamuz"
const av = "av"
const elul = "elul"
const adar1 = "adar1"
const adar2 = "adar2"

const days = {
    tishrei: [
        {
            month: tishrei,
            startDay: 1,
            endDay: 2,
            description: "Rosh Hashana"
        },
        {
            month: tishrei,
            startDay: 9,
            endDay: 9,
            description: "Erev Yom Kippur"
        },
        {
            month: tishrei,
            startDay: 10,
            endDay: 10,
            description: "Yom Kippur"
        },
        {
            month: tishrei,
            startDay: 11,
            endDay: 14,
            description: "Between Yom Kippur and Sukkot"
        },
        {
            month: tishrei,
            startDay: 15,
            endDay: 16,
            description: "Sukkot"
        },
        {
            month: tishrei,
            startDay: 17,
            endDay: 21,
            description: "Sukkot (Chol Hamoed)"
        },
        {
            month: tishrei,
            startDay: 22,
            endDay: 22,
            description: "Shmini Atzeret"
        },
        {
            month: tishrei,
            startDay: 23,
            endDay: 23,
            description: "Simchat Torah"
        },
        {
            month: tishrei,
            startDay: 24,
            endDay: 29,
            description: "Between Sukkot and Rosh Chodesh Cheshvan"
        },
        {
            month: tishrei,
            startDay: 30,
            endDay: 30,
            description: "Rosh Chodesh Cheshvan"
        }
    ],
    cheshvan: [
        {
            month: cheshvan,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Cheshvan"
        },
        {
            month: cheshvan,
            startDay: 30,
            endDay: 30,
            description: "Rosh Chodesh Kislev"
        }
    ],
    kislev: [
        {
            month: kislev,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Kislev"
        },
        {
            month: kislev,
            startDay: 25,
            endDay: 30,
            description: "Channuka"
        }
    ],
    tevet: [
        {
            month: tevet,
            startDay: 1,
            endDay: 3,
            description: "Channuka"
        }
    ],
    shvat: [
        {
            month: shvat,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Shvat"
        },
        {
            month: shvat,
            startDay: 15,
            endDay: 15,
            description: "Tu Bishvat"
        },
        {
            month: shvat,
            startDay: 30,
            endDay: 30,
            description: "Rosh Chodesh Adar"
        }
    ],
    adar: [
        {
            month: adar,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Adar"
        },
        {
            month: adar,
            startDay: 14,
            endDay: 14,
            description: "Purim"
        },
        {
            month: adar,
            startDay: 15,
            endDay: 15,
            description: "Shushan Purim"
        },
    ],
    adar1: [
        {
            month: adar1,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Adar"
        },
        {
            month: adar1,
            startDay: 14,
            endDay: 14,
            description: "Purim Katan"
        },
        {
            month: adar1,
            startDay: 15,
            endDay: 15,
            description: "Shushan Purim Katan"
        },
        {
            month: adar1,
            startDay: 30,
            endDay: 30,
            description: "Rosh Chodesh Adar"
        }
    ],
    adar2: [
        {
            month: adar2,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Adar"
        },
        {
            month: adar2,
            startDay: 14,
            endDay: 14,
            description: "Purim"
        },
        {
            month: adar2,
            startDay: 15,
            endDay: 15,
            description: "Shushan Purim"
        },
        {
            month: adar2,
            startDay: 30,
            endDay: 30,
            description: "Rosh Chodesh Nisan"
        }
    ],
    nisan: [
        {
            month: nisan,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Nisan"
        },
        {
            month: nisan,
            startDay: 2,
            endDay: 14,
            description: "Chodesh Nisan"
        },
        {
            month: nisan,
            startDay: 15,
            endDay: 22,
            description: "Pesach",
        },
        {
            month: nisan,
            startDay: 23,
            endDay: 29,
            description: "Chodesh Nisan"
        },
        {
            month: nisan,
            startDay: 30,
            endDay: 30,
            description: "Rosh Chodesh Iyyar"
        }
    ],
    iyyar: [
        {
            month: iyyar,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Iyyar"
        },
        {
            month: iyyar,
            startDay: 5,
            endDay: 5,
            description: "Yom Ha'atzmaut"
        },
        {
            month: iyyar,
            startDay: 15,
            endDay: 15,
            description: "Pesach Sheni"
        },
        {
            month: iyyar,
            startDay: 18,
            endDay: 18,
            description: "Lag Ba'omer"
        },
        {
            month: iyyar,
            startDay: 28,
            endDay: 28,
            description: "Yom Yerushalaim"
        },
        {
            month: iyyar,
            startDay: 30,
            endDay: 30,
            description: "Rosh Chodesh Sivan"
        }
    ],
    sivan: [
        {
            month: sivan,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Sivan"
        },
        {
            month: sivan,
            startDay: 2,
            endDay: 2,
            description: "Yom Hameyuchas"
        },
        {
            month: sivan,
            startDay: 3,
            endDay: 5,
            description: "Shloshet Yemei Hagbala"
        },
        {
            month: sivan,
            startDay: 6,
            endDay: 7,
            description: "Shavuot"
        },
        {
            month: sivan,
            startDay: 8,
            endDay: 12,
            description: "Week after Shavuot"
        },
        {
            month: sivan,
            startDay: 30,
            endDay: 30,
            description: "Rosh Chodesh Tamuz"
        }
    ],
    tamuz: [
        {
            month: tamuz,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Tamuz"
        },
        {
            month: tamuz,
            startDay: 30,
            endDay: 30,
            description: "Rosh Chodesh Av"
        }
    ],
    av: [
        {
            month: av,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Av"
        },
        {
            month: av,
            startDay: 9,
            endDay: 9,
            description: "Tisha B'av"
        },
        {
            month: av,
            startDay: 15,
            endDay: 15,
            description: "Tu B'av"
        },
        {
            month: av,
            startDay: 30,
            endDay: 30,
            description: "Rosh Chodesh Elul"
        }
    ],
    elul: [
        {
            month: elul,
            startDay: 1,
            endDay: 1,
            description: "Rosh Chodesh Elul"
        },
        {
            month: elul,
            startDay: 29,
            endDay: 29,
            description: "Erev Rosh Hashana"
        }
    ]
}

function noTachanun(month, day) {
    currMonth = days[month]

    for (holiday of currMonth) {
        if (day >= holiday.startDay && day <= holiday.endDay) {
            return holiday
        }
    }
    return false
}

module.exports = {
    noTachanun: noTachanun
} 