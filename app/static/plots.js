// route with data
const url = "http://127.0.0.1:5000/ratings"

d3.json(url).then(function(data){
    //console.log(data)
    data.forEach(function(data) {
        //data.date = parseTime(data.date);
        data.avg_monthly_rating = +data.avg_monthly_rating;
        data.histogram_values = +data.histogram_values
        data.histogram_bins = +data.histogram_bins
      });
    //console.log(data)

    var trace = {
        x: data.avg_monthly_rating,
        type: 'histogram',
      };
    var d = [trace];
    var layout = {
        title: 'Histogram Chart'
    }
    Plotly.newPlot('left', d, layout);


})