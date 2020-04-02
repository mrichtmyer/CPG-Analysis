// route with data
const url = "http://127.0.0.1:5000/ratings"

d3.json(url).then(function(data){
    //console.log(data)
    // data.forEach(function(data) {
    //     //data.date = parseTime(data.date);
    //     data.avg_monthly_rating = +data.avg_monthly_rating;
    //     data.histogram_values = +data.histogram_values
    //     data.histogram_bins = +data.histogram_bins
    //   });
    //console.log(data)

    // Setting the dimensions for the SVG container
    // var svgHeight = 600;
    // var svgWidth = 400;

    // var svg = d3
    //     .select("#left")
    //     .append("svg")
    //     .attr("height", svgHeight)
    //     .attr("width", svgWidth);

    // var svgGroup = svg.append("g")
    // svgGroup.selectAll("rect")
    //     .data(data.histogram_values)
    //     .enter()
    //     .append("rect")
    //     .attr("width", 50)
    //     .attr("height", function(data) {
    //         return data * 10;
    //     })
    //     .attr("x", function(data, index) {
    //         return index * 60;
    //     })
    //     .attr("y", function(data) {
    //         return 600 - data * 10;
    //     })
    //     .attr("class", "bar");

    var trace = {
        //x: data.histogram_bins,
        y: d=>d.histogram_values,
        type: 'histogram',
        // marker:{
        //     color: ['rgba(204,204,204,1)', 'rgba(222,45,38,0.8)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)']
        //   }
      };

    var d = [trace];
    var layout = {
        title: 'Histogram Chart',
        width: 300,
        height: 300
    }
    Plotly.newPlot('left', d, layout);



})