$(document).ready(function() {
    var endpoint = "/accounts/chart/data/";
    var labels = []
    var labels_status_bugs = []
    var DefaultData = []
    var DefaultData2 = []
    var DefaultData3 = []

    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(data) {
            labels = data.labels;
            DefaultData = data.default;
            var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Bugs and Features',
                        data: DefaultData,
                        backgroundColor: [
                            'rgba(0, 0, 139, 0.2)',
                            'rgba(255, 127, 80, 0.2)',
                        ],
                        borderColor: [
                            'rgba(0, 0, 139, 1)',
                            'rgba(255, 127, 80, 1)',
                        ],
                        borderWidth: 1
                    }]
                }
            });

            labels_status_bugs = data.labels_status_bugs;
            DefaultData2 = data.default_bugs_status;
            var ctx = document.getElementById('myChart2').getContext('2d');
            var myChart2 = new Chart(ctx, {
                type: 'polarArea',
                data: {
                    labels: labels_status_bugs,
                    datasets: [{
                        label: 'Bugs',
                        data: DefaultData2,
                        backgroundColor: [
                            'rgba(0, 206, 209, 0.2)', 
                            'rgba(100, 149, 237, 0.2)',
                            'rgba(0, 100, 0, 0.2)',
                        ],
                        borderColor: [
                            'rgba(0, 206, 209, 1)',
                            'rgba(100, 149, 237, 1)',
                            'rgba(0, 100, 0, 1)'
                        ],
                        borderWidth: 1.5
                    }]
                }
            });

            labels_status_features = data.labels_status_features;
            DefaultData3 = data.default_features_status;
            var ctx = document.getElementById('myChart3').getContext('2d');
            var myChart2 = new Chart(ctx, {
                type: 'polarArea',
                data: {
                    labels: labels_status_bugs,
                    datasets: [{
                        label: 'Features',
                        data: DefaultData3,
                        backgroundColor: [
                            'rgba(0, 206, 209, 0.2)', 
                            'rgba(100, 149, 237, 0.2)',
                            'rgba(0, 100, 0, 0.2)',
                        ],
                        borderColor: [
                            'rgba(0, 206, 209, 1)',
                            'rgba(100, 149, 237, 1)',
                            'rgba(0, 100, 0, 1)'
                        ],
                        borderWidth: 1.5
                    }]
                }
            });
        },

        error: function(error_data) {
            console.log("error");
            console.log(error_data);
        }
    })
});