$(document).ready(function() {
    $('.loading').remove();

    /////
    
    $("[data-toggle='tooltip']").tooltip();

    /////

    $('.round-chart').easyPieChart({
        'scaleColor': false,
        'lineWidth': 20,
        'lineCap': 'butt',
        'barColor': '#6D5CAE',
        'trackColor': '#E5E9EC',
        'size': 190
    });

    /////

    $('#performance-eval .spider-chart').highcharts({
        chart: {
            polar: true,
            type: 'area'
        },
        title: {
            text: ''
        },
        xAxis: {
            categories: ['馴服', '輔助', '進化', '整潔', '警醒', '配給'],
            tickmarkPlacement: 'on',
            lineWidth: 0
        },
        yAxis: {
            gridLineInterpolation: 'polygon',
            lineWidth: 0,
            min: 0
        },
        tooltip: {
            shared: true,
            pointFormat: '<span style="color:{series.color}">{series.name}: <b>${point.y:,.0f}</b><br/>'
        },
        legend: {
            align: 'right',
            verticalAlign: 'top',
            y: 70,
            layout: 'vertical'
        },
        series: [
            {
                name: '資源分配',
                data: [45000, 39000, 58000, 63000, 38000, 93000],
                pointPlacement: 'on',
                color: '#676F84'
            },
            {
                name: '資源耗費',
                data: [83000, 49000, 60000, 35000, 77000, 90000],
                pointPlacement: 'on',
                color: '#f35958'
            }
        ]
    });
});
