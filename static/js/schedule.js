$(document).ready(function () {
    addHours();

    addEvent(0, 7, 120, "sample class", "GHC 4100", colors[1]);
    addEvent(1, 11, 120, "sample class", "GHC 4100", colors[6]);
    addEvent(2, 13, 120, "sample class", "GHC 4100", colors[3]);
    addEvent(3, 15, 120, "sample class", "GHC 4100", colors[0]);
    addEvent(4, 19, 120, "sample class", "GHC 4100", colors[7]);
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
