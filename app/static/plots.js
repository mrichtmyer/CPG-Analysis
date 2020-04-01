// route with data
const url = "http://127.0.0.1:5000/ratings"

// function to recognize datetime
//var parseTime = d3.timeParse("%Y-%m-%d");


d3.json(url).then(function(data){
    console.log(data)
    // data.forEach(function(data) {
    //     //data.date = parseTime(data.date);
    //     data.avg_monthly = +data.avg_monthly;
    //     data.histogram_values = +data.histogram_values
    //     data.histogram_bins = +data.histogram_bins
    //   });

    //console.log(data)

    //console.log(data.avg_monthly)

    // var rating = data.avg_monthly.map(row => row)

    //console.log(rating)
})