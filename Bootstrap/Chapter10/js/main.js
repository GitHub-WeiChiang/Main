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

    // $('#performance-eval .spider-chart').highcharts({
    //     chart: {
    //         polar: true,
    //         type: 'area'
    //     },
    //     title: {
    //         text: ''
    //     },
    //     xAxis: {
    //         categories: ['馴服', '輔助', '進化', '整潔', '警醒', '配給'],
    //         tickmarkPlacement: 'on',
    //         lineWidth: 0
    //     },
    //     yAxis: {
    //         gridLineInterpolation: 'polygon',
    //         lineWidth: 0,
    //         min: 0
    //     },
    //     tooltip: {
    //         shared: true,
    //         pointFormat: '<span style="color:{series.color}">{series.name}: <b>${point.y:,.0f}</b><br/>'
    //     },
    //     legend: {
    //         align: 'right',
    //         verticalAlign: 'top',
    //         y: 70,
    //         layout: 'vertical'
    //     },
    //     series: [
    //         {
    //             name: '資源分配',
    //             data: [45000, 39000, 58000, 63000, 38000, 93000],
    //             pointPlacement: 'on',
    //             color: '#676F84'
    //         },
    //         {
    //             name: '資源耗費',
    //             data: [83000, 49000, 60000, 35000, 77000, 90000],
    //             pointPlacement: 'on',
    //             color: '#f35958'
    //         }
    //     ]
    // });

    /////

    // let elems = Array.prototype.slice.call(document.querySelectorAll('.switchery'));
    // let switcheryOpts = {color: '#1bc98e'};

    // elems.forEach(function(el) {
    //     var switchery = new Switchery(el, switcheryOpts);
    // });

    /////

    // $('#ration-stock .stacked-area').highcharts({
    //     chart: {
    //         type: 'area'
    //     },
    //     title: {
    //         text: ''
    //     },
    //     xAxis: {
    //         allowDecimals: false,
    //         labels: {
    //             formatter: function () {
    //                 return this.value;
    //             }
    //         }
    //     },
    //     yAxis: {
    //         title: {
    //             text: '配給庫存'
    //         },
    //         labels: {
    //             formatter: function () {
    //                 return this.value / 1000 + 'k';
    //             }
    //         }
    //     },
    //     tooltip: {
    //         pointFormat: '{series.name} 產生 <b>{point.y:,.0f}</b><br/>彈頭在 {point.x}'
    //     },
    //     plotOptions: {
    //         area: {
    //             pointStart: 100,
    //             marker: {
    //                 enabled: false,
    //                 symbol: 'circle',
    //                 radius: 2,
    //                 states: {
    //                     hover: {
    //                         enabled: true
    //                     }
    //                 }
    //             }
    //         }
    //     },
    //     series: [
    //         {
    //             name: '大橘配給庫存',
    //             data: [
    //                 null, null, null, null, null, 6, 11, 32, 110, 235, 369, 640,
    //                 1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468, 20434, 24126,
    //                 27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342, 26662,
    //                 26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605,
    //                 24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586,
    //                 22380, 21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950,
    //                 10871, 10824, 10577, 10527, 10475, 10421, 10358, 10295, 10104
    //             ],
    //             color: '#1bc98e'
    //         },
    //         {
    //             name: '邪惡貓咪庫存',
    //             data: [
    //                 null, null, null, null, null, null, null, null, null, null,
    //                 5, 25, 50, 120, 150, 200, 426, 660, 869, 1060, 1605, 2471, 3322,
    //                 4238, 5221, 6129, 7089, 8339, 9399, 10538, 11643, 13092, 14478,
    //                 15915, 17385, 19055, 21205, 23044, 25393, 27935, 30062, 32049,
    //                 33952, 35804, 37431, 39197, 45000, 43000, 41000, 39000, 37000,
    //                 35000, 33000, 31000, 29000, 27000, 25000, 24000, 23000, 22000,
    //                 21000, 20000, 19000, 18000, 18000, 17000, 16000
    //             ],
    //             color: '#676F84'
    //         }
    //     ]
    // });

    /////

    let changeMultiplier = 0.2;

    window.setInterval(function() {
        let freeSpacePercentage = parseFloat($('#free-space').text());

        let delta = changeMultiplier * (Math.random() < 0.5 ? -1.0 : 1.0);

        freeSpacePercentage = freeSpacePercentage + freeSpacePercentage * delta;
        freeSpacePercentage = parseInt(freeSpacePercentage);

        $('#free-space').text(freeSpacePercentage + '%');
    }, 2000);

    /////

    // $('#daily-usage .area-chart').highcharts({
    //     title: {
    //         text: '',
    //     },
    //     tooltip: {
    //         pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    //     },
    //     plotOptions: {
    //         pie: {
    //             dataLabels: {
    //                 enabled: true,
    //                 style: {
    //                     fontWeight: '300'
    //                 }
    //             }
    //         }
    //     },
    //     series: [{
    //         type: 'pie',
    //         name: '時間佔比',
    //         data: [
    //             ['前院', 10.38],
    //             ['衣櫥', 26.33],
    //             ['游泳池', 51.03],
    //             ['像老闆一樣', 4.77],
    //             ['吠叫', 3.93]
    //         ]
    //     }]
    // });

    // $('#search-icon').on('click', function(e) {
    //     e.preventDefault();
    //     $('form#search').slideToggle('fast');
    //     $('form#search input:first').focus();
    // });

    // $('form#search input').on('blur', function(e) {
    //     if($('#search-icon').is(':visible')) {
    //         $('form#search').slideUp('fast');
    //     }
    // });
});
