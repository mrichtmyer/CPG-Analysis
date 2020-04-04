// route with data
const url2 = "http://127.0.0.1:5000/max_helpful_review"

d3.json(url2).then(function(data2){

    console.log(data2)
    d3.select("#right")
        .selectAll('p')
        .data(data2)
        .enter()
        .append('p')
        .text(data2)

})