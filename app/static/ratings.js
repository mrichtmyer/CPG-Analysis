// route with data
const url = "http://127.0.0.1:5000/ratings"

d3.json(url).then(function(data){

    //console.log(data)
    
    //var timeFormat = 
    
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
        margin: {
            l:50,
            r:50,
            b:50,
            t:50,
            pad:0
        },
        yaxis: { 
            tickcolor: '#000',
            range: [0,6]
        },
        xaxis: {},

    }
    Plotly.newPlot('middle', d, layout);



})

