var express = require('express');
var path = require('path');
var fs = require('fs');
var exec = require('child_process').exec
var app = express();

app.use(express.static('public'));

app.all('*', function (req, res, next) {
  console.log(req.method, req.originalUrl, new Date().toLocaleString())
  next()
})
app.get('/', function (req, res) {
  res.sendFile(path.resolve(__dirname, 'public', 'index.html'));
});

app.get('/query', function (req, res) {
  var city = req.query.city;
  exec(`python crawler.py ${city}`, function (err, stdout, stderr) {
    if (err) {
      throw err;
    }
    if (stdout) {
      let time = stdout.split(':');
      fs.readFile('fagns.json', 'utf8', function (err, data) {
        const json = Object.assign(JSON.parse(data), {
          time: `${time[1]}分${time[2]}秒`
        })
        res.send(json)
      })
    }
  }); //exec end
})

var server = app.listen(3000, function () {
  console.log(`app listening at 3000`)
})