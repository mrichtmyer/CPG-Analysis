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

    console.log(data)

    var trace = {
        x: data.histogram_rating_bins,
        y: data.histogram_rating_values,
        type: 'bar',
        marker:{
            color: ['rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)','rgba(30,38,204,0.8)']
          }
      };

    var d = [trace];
    var layout = {
        title: 'Product Rating',
        width: 300,
        height: 300
    }
    Plotly.newPlot('left', d, layout);



    var trace = {
        x: data.gb_date,
        y: data.avg_monthly_rating,
        type: 'line',
        // marker:{
        //     color: ['rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)','rgba(30,38,204,0.8)']
        //   }
      };

    var d = [trace];
    var layout = {
        title: 'Average Rating Over Time',
        width: 300,
        height: 300,
        yaxis: { 
            tickcolor: '#000',
            range: [0,6]

        }

    }
    Plotly.newPlot('middle', d, layout);



})