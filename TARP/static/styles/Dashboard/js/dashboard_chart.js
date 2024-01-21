var today = new Date();

var dates = [];
var startDate = new Date('2023-11-21');
var currentDate = startDate;

while (currentDate <= today) {
    var formattedDate = currentDate.toISOString().slice(0, 10);
    dates.push(formattedDate);
    currentDate.setDate(currentDate.getDate() + 1);
}

fetch('/graph_data')
    .then(response => response.json())
    .then(data => {
        var interactions1 = data.graph1;
        var interactions2 = data.graph2;
        var interactions3 = data.graph3;
        var interactions4 = data.graph4;
        var interactions5 = data.graph5;
        var interactions6 = data.graph6;
        var target = data.target;

        var ctx1 = document.getElementById('graph1').getContext('2d');
        var ctx2 = document.getElementById('graph2').getContext('2d');
        var ctx3 = document.getElementById('graph3').getContext('2d');
        var ctx4 = document.getElementById('graph4').getContext('2d');
        var ctx5 = document.getElementById('graph5').getContext('2d');
        var ctx6 = document.getElementById('graph6').getContext('2d');

        var chart1 = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Hand Flapping',
                    data: interactions1,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }]
            }
        });

        var chart2 = new Chart(ctx2, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Rocking back and forth',
                    data: interactions2,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            }
        });

        var chart3 = new Chart(ctx3, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Difficulty Making Eye Contact',
                    data: interactions3,
                    borderColor: 'rgba(255, 206, 86, 1)',
                    borderWidth: 1
                }]
            }
        });

        var chart4 = new Chart(ctx4, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Difficulty Understanding Nonverbal Cues',
                    data: interactions4,
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            }
        });

        var chart5 = new Chart(ctx5, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Reaction Towards Loud Noises',
                    data: interactions5,
                    borderColor: 'rgba(153, 102, 255, 1)',
                    borderWidth: 1
                }]
            }
        });

        var chart6 = new Chart(ctx6, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Reaction Towards Light',
                    data: interactions6,
                    borderColor: 'rgba(255, 159, 64, 1)',
                    borderWidth: 1
                }]
            }
        });
        document.getElementById('target-value').textContent = target;
    });
