$(document).ready(function () {
    addHours();

    addEvent(0, 9.5, 120, "15-213 Recitation", "WEH 5003", colors[1]);
    addEvent(0, 11, 120, "16-311 Lecture", "NSH 3000", colors[3]);
    addEvent(1, 12, 120, "16-385 Lecture", "BH A100", colors[0])
    addEvent(3, 12, 120, "16-385 Lecture", "BH A100", colors[0]);
    addEvent(1, 13.5, 120, "15-213 Lecture", "GHC 4401", colors[1]);
    addEvent(3, 13.5, 120, "15-213 Lecture", "GHC 4401", colors[1]);
    addEvent(1, 15.5, 120, "16-311 Recitation", "SH 100", colors[3]);
    addEvent(2, 11, 120, "16-311 Lecture", "NSH 3000", colors[3]);
    addEvent(1, 9, 120, "15-221 Lecture", "WEH 7000", colors[2]);
    addEvent(3, 9, 120, "15-221 Lecture", "WEH 7000", colors[2]);
    addEvent(4, 10.5, 120, "15-221 Recitation", "GHC 4100", colors[2]);
});

var colors = ['#00B64F', '#086FA2', '#D8005F', '#FF0000', '#FF9700', '#DE0052',
'#CD0074', '#009999'];

function addHours() {
    for (var i = 0; i < 5; i++) {
        document.getElementById(i + '').innerHTML = addtoday(i).innerHTML;
    }
}

function addtoday(day) {
    function addhour(day, hourtime) {
        var hour = document.createElement('div');
        hour.setAttribute('class', 'hour');
        hour.setAttribute('id', day + '+' + hourtime);
        return hour;
    }
    today = document.createElement('div');
    for (var j = 7; j < 22; j++) {
        today.appendChild(addhour(day, j));
    }
    return today;
}


function addEvent(day, hour, length, desc, location, color) {
    var event = document.createElement('div');
    event.setAttribute('class', 'event');
    event.setAttribute('style', 'position:absolute; top:' + Math.floor(hour * 50.3 - 355) + 'px; height:' + Math.floor(length * 35 / 60) + 'px;' + 'background-color:' + color);
    event.innerHTML = "<span class='title'>" + desc + "</span><br><span class='location'>" + location + "</span>";
    document.getElementById(day).appendChild(event);
}

function convertTimeToDecimal(time) {
    var hour = Number(time.substr(0, 2));
    var minute = Number(time.substr(2, 4));
    var decimal = minute / 60;
    return hour + decimal;
}

function clearCalendar() {
    $('.event').remove();
}

function formatCourseNumber(courseNumber) {
    return (courseNumber.substr(0, 2) + "-" + courseNumber.substr(2, 5));
}
