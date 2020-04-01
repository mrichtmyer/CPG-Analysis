var sentiment = "http://127.0.0.1:5000/emotions"

d3.json(sentiment).then(function(data){
    console.log(data)
})